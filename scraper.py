import requests

youtube_trending_url = "https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl"

response = requests.get(youtube_trending_url)

print("Status code", response.status_code)
# if status code was 404 then we would understand that the code is not working
print("Output", response.text[:1000])

with open('trending.html', 'w') as f:
  f.write(response.txt)