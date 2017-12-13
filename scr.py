# coding: UTF-8
import urllib2
import sys
from bs4 import BeautifulSoup

# 対象ページの読み込み
html = urllib2.urlopen("https://qiita.com/g-empr/like")
# そのままだとエラーを吐くのでパーサーに通す
soup = BeautifulSoup(html, "html.parser")
# 抜き出す要素をリスト化
author_list = soup.select(".ItemLink__info a")
article_list = soup.find_all("a", class_="u-link-no-underline")

# ループで要素を整形しながらファイルに追加
# withを使うことでファイルのopenからcloseまでのまとまりを作ることができる
with open('article.txt', 'w') as f:
    for i in range(len(author_list)):
        item = '<li>\n\t<span>{0}\'s entry: </span>\n\t<a href="https://qiita.com{2}">{1}</a>\n</li>\n'.format(
            # UNICODEエラーを吐くのでencodeする
            author_list[i].string.encode('utf-8'),
            article_list[i].string.encode('utf-8'),
            article_list[i].get("href")
        )
        f.write(str(item))
