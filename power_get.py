#!/bin/python3
#-*- coding: UTF-8 -*-
import sys
import requests
import traceback
import time
import json
from lxml import etree

api = "http://www.gyruibo2.cn/WxSearch/GetRoomInfo"

header = {
	'User-Agent': 'Mozilla/5.0 (Linux; Android 11; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2691 MMWEBSDK/200901 Mobile Safari/537.36 MMWEBID/419 MicroMessenger/7.0.19.1760(0x27001380) Process/toolsmp WeChat/arm64 NetType/2G Language/zh_CN ABI/arm64'
}

Apartid = {
			"10": "8170",
			"11": "8003",
			"12": "8003",
			"13": "8006",
			"14": "8006",
			"15": "8007",
			"16": "8008",
			"17": "8009",
			"18": "8163",
			"19": "8010",
			"20": "8011",
			"21": "8012",
			"22": "8013",
			"23": "8014",
			"24": "8015",
			"28": "8016",
			"29": "8157",
			"34": "8018",
			"40": "8019",
			"43": "8020",
			"45": "8021",
			"46": "8022",
			"47": "8023",
			"48": "8024",
			"49": "8304"
			}

def GetRoomInfo(Roomname):
	session = requests.session()
	session.headers = header
	try:
		api_get = api + "?SchID=1&Apartid=" + Apartid[Roomname[0:2]] +"&Roomname=" + Roomname
		html_data = session.get(str(api_get))
		#print (html_data.text)
		raw_data = etree.HTML(html_data.text)
		Room_data = {
			'state' : 'ok',
			'name' : raw_data.xpath('//div/div/div/label/text()')[0].replace('\r\n','').strip(),
			'Used' : raw_data.xpath('//div/div/div/label/text()')[1].replace('\r\n','').replace('度','').strip(),
			'Remaining'  : raw_data.xpath('//div/div/div/label/text()')[2].replace('\r\n','').replace('度','').strip(),
			'RecordTime'  : raw_data.xpath('//div/div/div/label/text()')[3].replace('\r\n','').strip(),
			'TimeStamp'  : str(round(time.mktime(time.strptime(raw_data.xpath('//div/div/div/label/text()')[3].replace('\r\n','').strip(), "%Y/%m/%d %H:%M:%S"))))		#转成时间戳
			}
		if Room_data['name'] == '':
			Room_data['state']='null'

	except :
		Room_data = {
			'state' : 'error',
			'info' : traceback.format_exc()
			}
	return(Room_data)

if __name__ == '__main__':
	for i in range(len(sys.argv)-1):
		print (json.dumps(GetRoomInfo(sys.argv[i+1])))