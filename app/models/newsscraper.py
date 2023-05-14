import requests
from bs4 import BeautifulSoup

search_term = "$aapl"
url = f"https://www.reuters.com/search/news?sortBy=date&dateRange=all&blob={search_term}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("div", class_="search-result-content")

for article in articles:
    if search_term.upper() in article.find("h3", class_="search-result-title").get_text().upper():
        title = article.find("h3", class_="search-result-title").get_text().strip()
        author = article.find("span", class_="search-result-author").get_text().strip()
        url = article.find("a", href=True)["href"]
        print(f"{title}\nAuthor: {author}\nURL: {url}\n-----------------------")
