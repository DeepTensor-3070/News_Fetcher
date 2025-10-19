import requests
import os


api = os.getenv("NEWS_API_KEY")

if not api:
    raise ValueError("❌ NEWS_API_KEY not found. Please set it in your environment or .env file.")

query = input("What type of news are you interested in today? ")


url = f"https://newsapi.org/v2/everything?q={query}&from=2025-09-19&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)

data = r.json()
articles = data["articles"]

for index,article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n---------------------------------------\n")
    