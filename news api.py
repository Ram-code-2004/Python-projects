import requests
from newsapi import NewsApiClient
sport_news =requests.get("https://newsapi.org/v2/top-headlines?category=sport&apiKey=a42a556fef4a499ab8beaaf36cb071ed")
business_news =requests.get("https://newsapi.org/v2/top-headlines?category=business&apiKey=a42a556fef4a499ab8beaaf36cb071ed")
entertainment_news =requests.get("https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=a42a556fef4a499ab8beaaf36cb071ed")
technology_news =requests.get("https://newsapi.org/v2/top-headlines?category=technology&apiKey=a42a556fef4a499ab8beaaf36cb071ed")
def main():
    choice = input("Enter the category of news you want to read (sport, business, entertainment, technology): ").lower()
    if choice == "sport":
        print("Sport News:")
        articles = sport_news.json()['articles']
        for i, article in enumerate(articles[:5], 1):
         print(f"{i}. {article['title']}")
         print(f"   {article['description']}")
         print(f"   Read more: {article['url']}\n")

    elif choice == "business":
       print("Business News:")
       articles =business_news.json()['articles']
       for i, article in enumerate(articles[:5], 1):
        print(f"{i}. {article['title']}")
        print(f"   {article['description']}")
        print(f"   Read more: {article['url']}\n")

    elif choice == "entertainment":
        print("Entertainment News:")
        articles = entertainment_news.json()['articles']
        for i, article in enumerate(articles[:5], 1):
         print(f"{i}. {article['title']}")
         print(f"   {article['description']}")
         print(f"   Read more: {article['url']}\n")

    elif choice == "technology":
        print("Technology News:")
        articles = technology_news.json()['articles']
        for i, article in enumerate(articles[:5], 1):
           print(f"{i}. {article['title']}")
           print(f"   {article['description']}")
           print(f"   Read more: {article['url']}\n")

    else:
        print("Invalid category. Please choose from sport, business, entertainment, or technology.")
main()