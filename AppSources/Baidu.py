# -*- coding: UTF-8 -*-
import requests, json
from bs4 import BeautifulSoup
def baidu_search_app(keyword):
    """Search software from BaiDu Softwares WebPage.
    Get the download link by the software name.
    Args:
        keyword: A software name keyword.
    Returns:
        Download links for search result.
    """

    search_url = "http://rj.baidu.com/search/index/?kw=" + keyword
    search_req = requests.get(search_url)
    search_result = search_req.text
    if search_req.status_code == 200:
        find_startkey = "var configs =  "
        find_stopkey = "var loginUrl"
        i_startkey = search_result.index(find_startkey)
        i_stopkey = search_result.index(find_stopkey)
        split_text = search_result[i_startkey + 15:i_stopkey]
        link_text = split_text[0:split_text.rfind(";")]
        jsondata = json.loads(link_text)
        total = (jsondata["data"]["page"]["totalP"])
        if total == 0:
            print ("Sorry!No search results!Please change the keyword!")
        else:
            soft_count = jsondata["data"]["searchResultHint"]["soft_count"]
    else:
        print("The program has a problem. The result status was bad, please make sure your internet access was worked!")


"""test function"""
baidu_search_app("360")
