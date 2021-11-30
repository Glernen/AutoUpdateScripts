# 2345王牌联盟签到

import requests
import time
import json
import os

# ==============  1.2345王牌联盟 cookie 变量 ============== #
WPLM_COOKIE = os.environ["WPLM_COOKIE"]  # 必填！2345王牌联盟 的 cookie


headers = {
	'Host': 'jifen.2345.com',
	'Connection': 'keep-alive',
	'Accept': 'application/json, text/plain, */*',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 10; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36 package/com.shouji2345 versionName/4.5.9 versionCode/459 WangPai,WangPaiBrowser,Android',
	'token': '8c028b154341dda188577f800ed8be8a',
	# 'Referer': 'https://jifen.2345.com/wph5/sign/index?isFullScreen=1',
	'Content-Type': 'application/x-www-form-urlencoded',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'X-Requested-With': 'com.shouji2345',
	'cookies':WPLM_COOKIE,
}


#周任务奖励领取
def TaskWeekList():
	r = requests.get('https://jifen.2345.com/appv4/task/DecennialList',headers=headers)
	TaskWeekdata = r.json()
	# print (TaskWeekdata)
	GoldInfoList = TaskWeekdata['data']['goldInfo']['list']#奖励列表
	TaskList = TaskWeekdata['data']['taskWeekList']
	# print (GoldInfo)
	# print (TaskList)
	for i in TaskList:
		if i["status"] == 2:
			print (f""" 已完成 {i["name"]} 任务 · {i["popText"]} \n""")
		if i["status"] == 3:
			print (f""" 未完成 {i["name"]} 任务""")
		if i["status"] == 7:
			print (f""" {i["statusDesc"]} {i["name"]} 任务""")


	Gold = TaskWeekdata['data']['goldInfo']['info']['gold']#已有金币奖励
	print (f"""\n 已有奖励 · {Gold}""")
	print ("\n"+"##"*30)


#2345APP端签到请求
def CheckIn():
	try:
		r_CheckIn = requests.get('https://jifen.2345.com/appv4/checkIn/index', headers=headers)
		return r_CheckIn.json()
	except Exception as e:
		print (e)


#2345积分统计
def JiFen(month):
	try:
		headers = {
			'Host': 'jifen.2345.com',
			'Connection': 'keep-alive',
			'Accept': 'application/json, text/plain, */*',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 10; COL-AL10 Build/HUAWEICOL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.186 Mobile Safari/537.36 package/com.shouji2345 versionName/4.5.9 versionCode/459 WangPai,WangPaiBrowser,Android',
			'token': '8c028b154341dda188577f800ed8be8a',
			# 'Referer': 'https://jifen.2345.com/wph5/user/jifen-detail',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
			'X-Requested-With': 'com.shouji2345',
			'cookies':WPLM_COOKIE,
		}
		data = {
			'queryMonth':month,
		}
		r_JiFen = requests.get('https://jifen.2345.com/appv4/jifen/entry?type=1', headers=headers, data=data)
		return r_JiFen.json()
	except Exception as e:
		print (e)


def run():

	print ("\n 【每日签到】" )
	print ("=="*30)
	currDate = CheckIn()['data']['currDate']#签到日期
	continueCheckIn = CheckIn()['data']['continueCheckIn']#已签到的值为1
	awardScore = CheckIn()['data']['awardScore']#获得积分
	awardExp = CheckIn()['data']['awardExp']#获得经验值
	print ("\n %s 已签到 积分+%s  经验值+%s \n" %(currDate,awardScore,awardExp))
	print ("##"*30)

####################################################################################
	print ("\n 【检查周任务状态】" )
	print ("=="*30+"\n")
	TaskWeekList()

####################################################################################
	print ("\n 【账户积分统计】" )
	print ("=="*30)
	month = time.strftime('%Y-%m',time.localtime())
	Count = JiFen(month)['data']['userScore']
	deposits_yuan = Count['deposits']['yuan']#已存金额
	uscore_yuan = Count['uscore']['yuan']#可提现金额
	wscore_yuan = Count['wscore']['yuan']#待发金额
	score1_jf =Count['score1']['jifen']#昨日推广积分
	count_je = round((deposits_yuan + uscore_yuan + wscore_yuan),2)
	print ("\n 昨日推广积分为 %s 分，已有总金额 %s 元 \n" %(score1_jf,count_je))
	print ("##"*30)
#####################################################################################
#####################################################################################




if __name__ == "__main__":
	run()

