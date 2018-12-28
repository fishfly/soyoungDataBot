# -*- coding: utf-8 -*-

import httplib
from lxml import etree

def getInfo(page):
	# res
	res = []

	# get all the hospitals in urumuqi
	conn = httplib.HTTPConnection("y.soyoung.com")
	conn.request("GET", "/hospital/0_0_0_0_0_0_475_0_0_2/" + str(page))
	r = conn.getresponse()
	c = r.read()

	# html
	selector = etree.HTML(c)
	div_filter_list = selector.xpath('//html/body/div')[3][1]

	# main
	selector = etree.HTML(etree.tostring(div_filter_list))
	ul_list = selector.xpath('//div/ul')[1]

	# hospital, title, score, pro,
	for i in ul_list:
		res_item = []
		content = i[1]
		#print content.attrib
		score = content[0][0][1]
		name = content[1][0]
		# title = etree.tostring(content[2])
		pro_count = len(content[4]) - 1
		pro = []
		for i in range(pro_count):
			item = content[4][i+1].text.replace(u'\xa0', u'').replace(' ','').replace('\n','')
			pro.append(item)

		res_item.append(name.text)
		res_item.append(score.text)
		for i in pro:
			res_item.append(i)

		res.append(res_item)
	return res

def main():
	index = 0
	for i in range(3):
		info_list = getInfo(i+1)
		for i in info_list:
			index += 1
			print index,
			for j in i:
				print j,
			print

main()