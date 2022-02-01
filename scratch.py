import requests
from bs4 import BeautifulSoup as bs
youtube_trending_url = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

# does not execute javascript
response = requests.get(youtube_trending_url)

print("Status code", response.status_code)
# if status code was 404 then we would understand that the code is not working
# print("Output", response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = bs(response.text, 'html.parser')
print("Page title:",doc.title.text)

video_divs = doc.find_all('div',class_='ytd-video-renderer')
# we find that there are 0 videos found, this is because the requests lib just pulls the html and does not execute the javascript, the JS is responsible to make netwrok request and get info, this is client server side application or a dynamic website. Thus we will use selenium to make a UI-less browser
print(f"Found {len(video_divs)} videos")