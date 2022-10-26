from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://news.ycombinator.com/"

soup = BeautifulSoup(requests.get(url).text, "lxml")

articles_span = soup.find_all("span", class_="titleline")
articles_anchors = [span.find("a") for span in articles_span]
articles_text = [a.text for a in articles_anchors]
articles_links = [link.get("href") for link in articles_anchors]

articles_score = soup.find_all("span", class_="score")
articles_upvotes = [int(score.text.split()[0]) for score in articles_score]

# top = max(articles_upvotes)
# ind = articles_upvotes.index(top)

# df = pd.DataFrame(
#     {"title": articles_text, "link": articles_links, "upvote": articles_upvotes})
# df.to_csv("hackersNews.csv", index=False)
print((articles_upvotes))
