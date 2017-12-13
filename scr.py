import urllib2
import sys
from bs4 import BeautifulSoup

html = urllib2.urlopen("https://qiita.com/g-empr/like")

soup = BeautifulSoup(html, "html.parser")

author_list = soup.select(".ItemLink__info a")
article_list = soup.find_all("a", class_="u-link-no-underline")

for i in range(len(author_list)):
    print('<li>\n\t<span>{0}\'s entry: < /span >\n\t< a href="https://qiita.com{2}" > {1} < /a >\n < /li >'.format(
        author_list[i].string.encode('utf-8'),
        article_list[i].string.encode('utf-8'),
        article_list[i].get("href")
    ))

# f = open('test.txt', 'w')
# f.write(title.encode('utf-8'))
# f.close()
