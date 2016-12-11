# -*- coding: UTF-8 -*-
import requests, json
from bs4 import BeautifulSoup

"""Search software from BaiDu Softwares WebPage.
Get the download link by the software name.
Args:
    keyword: A software name keyword.
Returns:
    Download links for search result.
"""
def baidu_search_currpage(keyword, page=1):
    search_url = "http://rj.baidu.com/search/index/?kw=" + keyword + "&pageNum=" + str(page)
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
        if jsondata["data"]["page"]["totalP"] ==0:
            print("Sorry!No search results!Please change the keyword!")
            return None
        else:
            return jsondata

    else:
        print("The program has a problem. The result status was bad, please make sure your internet access was worked!")
        return None

def baidu_search_allpage(jsondata):
    jsonalldata=[jsondata]
    pagenumber = jsondata["data"]["page"]["totalP"]
    keyword=jsondata["data"]["search"]["kw"]
    for page in range(2, pagenumber+1):
        jsonalldata.append(baidu_search_currpage(keyword, page))
    return jsonalldata

def baidu_search_infolist(jsondata, AllData = False):
    softinfo_list = []
    totalP = jsondata["data"]["page"]["totalP"]
    keyword = jsondata["data"]["search"]["kw"]
    soft_count = jsondata["data"]["searchResultHint"]["soft_count"]
    baseURL = "http://rj.baidu.com" + jsondata["data"]["page"]["baseURL"]
    number = 0
    while (number != -1):
        try:
            softinfo = jsondata["data"]["softList"]["list"][number]
        except:
            number = -1
        else:
            number = number + 1
            softinfo_list.append(softinfo)
    if AllData is True:
        number = 0
        print(totalP+1)
        print("----------------------------------")
        for pagedata in range(2, totalP + 1):
            print(pagedata)
            indexjsondata = baidu_search_currpage(keyword, pagedata)
            print(indexjsondata)
            print("**********************************")

            while (number != -1):
                try:
                    softinfo = indexjsondata["data"]["softList"]["list"][number]
                except:
                    number = -1
                else:
                    number = number + 1
                    softinfo_list.append(softinfo)
                    print(softinfo)
                    return softinfo_list


"""test function"""
result =baidu_search_currpage("360")
test = baidu_search_infolist(result, True)
'''
for teststr in test:
    print(teststr)
'''