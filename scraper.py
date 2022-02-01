from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  # loading the browser
  driver = webdriver.Chrome(options=chrome_options)
  return driver
def get_videos(driver):
  video_div_tag = "ytd-video-renderer"
  video_divs = driver.find_elements(By.TAG_NAME,video_div_tag)
  return video_divs

def parse_video(video):
  title_tag = video.find_element(By.ID, 'video-title')
  title = title_tag.text
  url = title_tag.get_attribute('href')
  thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
  thumbnail_url = thumbnail_tag.get_attribute('src')

  channel_div = video.find_element(By.CLASS_NAME,'ytd-channel-name')
  channel_name = channel_div.text

  description = video.find_element(By.ID, 'description-text').text

  views_and_date_div = video.find_element(By.ID,'metadata-line')
  views_date = views_and_date_div.text

  return {
    'title':title,
    'url':url,
    'thumbnail_url':thumbnail_url,
    'channel_name':channel_name,
    'description':description,
    'views_and_date':views_date
  }
if __name__ == "__main__":
  print("Creating driver....")
  driver = get_driver()
  youtube_trending_url="https://www.youtube.com/feed/trending?bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D"
  # open a tab with this url
  print("Fetching URL.....")
  driver.get(youtube_trending_url)
  # get page title
  # print('Page title',driver.title)
  videos = get_videos(driver)
  print(f"Found {len(videos)} videos")

  print("Parsing top 10 videos")
  # title, url, thumbnail url, channel, views, uploaded date, description is what we need

  videos_data = [parse_video(video) for video in videos[:10]]
  # print(videos_data[1])
  print("Saving to CSV.....")
  videos_df = pd.DataFrame(videos_data)
  videos_df.to_csv('trending.csv', index=None)
  