import urllib2
import sys
from bs4 import BeautifulSoup

# 対象ページ読み込み（最初のページのみ）
html = urllib2.urlopen("https://qiita.com/g-empr/like")
# エラー吐くのでパーサー通す
soup = BeautifulSoup(html, "html.parser")
# 投稿者取得
author_list = soup.select(".ItemLink__info a")
# 記事取得
article_list = soup.find_all("a", class_="u-link-no-underline")
# 記事の抜き出しと整形
for i in range(len(author_list)):
    print('<li>\n\t<span>{0}\'s entry: < /span >\n\t< a href="https://qiita.com{2}" > {1} < /a >\n < /li >'.format(
        author_list[i].string.encode('utf-8'),
        article_list[i].string.encode('utf-8'),
        article_list[i].get("href")
    ))
# 別ファイルへの書き込み
# f = open('test.txt', 'w')
# f.write(title.encode('utf-8'))
# f.close()
