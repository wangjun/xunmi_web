import requests
from bs4 import BeautifulSoup
import re

gfsoso_url = "http://www.gfsoso.com"

def get_html(keywords, page):

    q = "+".join(keywords)
    search_url = gfsoso_url + "/?q=" + q + "+site%3Ayun.baidu.com+OR+site%3Apan.baidu.com"\
                 + "&pn=" + str((page - 1) * 10)
    print search_url
    header = {
        "User-Agent": "Mozilla/5.0",
        "Cookie": "_GFTOKEN=61ef339d2d8cda7f00"
    }
    r = requests.get(search_url, headers=header)
    soup = BeautifulSoup(r.content)
    return soup

def get_results(html):
    pattern = "<h3 class=\\\\\"r\\\\\"(?:.+?)>(?:.+?)<a href=\\\\\"(.+?)\\\\\" target=\\\\\"_blank\\\\\">(.+?)<\\\\/a>";
    results = re.findall(pattern, html)
    temps = []
    for i in range(len(results)):
        temp = (results[i][1].replace("\n", "").replace(" ", "")
                .replace("\t", "").replace("<b>", "").replace("<\\/b>", "").decode('utf-8'),
                results[i][0].replace("\\/", "/").replace("&amp;", "&").replace("&amp;", "&").decode('utf-8'))
        temps.append(temp)
    results = temps

    return results




