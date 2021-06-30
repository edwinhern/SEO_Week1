import requests
import json
url = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"

r = requests.get(url)
# Retreive the story number
story = r.json()[0]
# Open story number url
story_url = "https://hacker-news.firebaseio.com/v0/item/"+str(story)+".json?print=pretty"
# Request 
r = requests.get(story_url).json()
# Print JSON file

print("Title" + r["title"])
print("Author" + r["by"])
print("Link" + r["url"])

