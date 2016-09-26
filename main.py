# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import urllib,urllib2
from bs4 import BeautifulSoup
import re



def spider():
    url_wdyw = 'http://news.whu.edu.cn/wdyw.htm'
    url_kydt = 'http://news.whu.edu.cn/kydt.htm'

    responce_wdyw = requests.get(url_wdyw).content
    responce_kydt = requests.get(url_kydt).content
    bs_wdyw = BeautifulSoup(responce_wdyw)
    bs_kydt = BeautifulSoup(responce_kydt)


    for id_wdyw in range(0,25):
        li_id_wdyw = 'lineu5_'+ str(id_wdyw)
        wdyw_item = bs_wdyw.find('li',attrs={'id':li_id_wdyw})
        wdyw_title = wdyw_item.find('a')['title'].strip()
        wdyw_url = 'http://news.whu.edu.cn/' + wdyw_item.find('a')['href']
        #wdyw_clicknum = wdyw_item('span')[0].text  #点击量是动态获取，下次补上
        wdyw_date = wdyw_item.find('div',attrs={'class','infodate'}).text.strip()
        bs_wdyw_content = BeautifulSoup(requests.get(wdyw_url).content)
        wdyw_content = bs_wdyw_content.find_all('div',attrs={'class','news_content'})[1].get_text().strip()
        print wdyw_content
        with open('data/'+str(wdyw_title)+'.md','w') as f:
            f.write(wdyw_title+'\n\n'+wdyw_date+'\n\n'+wdyw_content+'\n\n'+wdyw_url)

    for id_kydt in range(0,1):
        li_id_kydt = 'lineu5_'+ str(id_kydt)
        kydt_item = bs_kydt.find('li',attrs={'id':li_id_kydt})
        kydt_title = kydt_item.find('a')['title']
        kydt_url = kydt_item.find('a')['href']
        #kydt_clicknum = kydt_item('span')[0].text  #点击量是动态获取，下次补上
        kydt_date = kydt_item.find('div',attrs={'class','infodate'}).text.strip()
        bs_kydt_content = BeautifulSoup(requests.get(kydt_url).content)
        kydt_content = bs_kydt_content.find_all('div',attrs={'class','news_content'})[1].get_text().strip()
        print kydt_content

spider()
