import requests
import time
import random
import datetime
import json
starttime =datetime.datetime.now()
h=1   #查询次数
y=1   #字符窜长度
b=1   #验证是否出新成绩
while 1:
    #下面的网址是2019-2020
	url="http://jwgl.ujn.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=&xnm=2019&xqm=12&_search=false&nd=&queryModel.showCount=15&queryModel.currentPage=1&queryModel.sortName=&queryModel.sortOrder=asc&time=0"
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56',
		'Cookie': '你的cookie'
			}
	try:
		r=requests.get(url,headers=headers)
		result=json.loads(r.text)
		endtime =datetime.datetime.now()    #计时
		print ('已经运行时间:',str(endtime - starttime)[:-7])    #输出已经运行时间             
		print('查询的字节数:',len(r.text))                   
		y=int(len(r.text))              #查询到的字符串长度
		print('已经查询次数:',h)
		items=result['items'] #items是list 是一个科目
		items_geshu=int(len(items)) #items里面有几颗
		print('目前查询到:',items_geshu,'科')
		for i in range(items_geshu):
			items1=items[i]
			print(items1['jxbmc'],':',items1['cj'])
		h=h+1
		print()
		if len(r.text)>int(b+1) and len(r.text)<10000:
			requests.get('https://sc.ftqq.com/替换server酱的key.send?text=出成绩了')
			b=y
	except:
		print("爬取失败")
	time.sleep(5)
