# 文件名：微信通知.py

import requests
import json
import datetime

# 映射星期
week_map = {
'Monday': '周一',
'Tuesday': '周二',
'Wednesday': '周三',
'Thursday': '周四',
'Friday': '周五',
'Saturday': '周六',
'Sunday': '周日'
}

# 当前日期和星期几
now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')
weekday = week_map[now.strftime('%A')]


# 企业微信群机器人 Webhook 地址（请替换为你自己的）测试用：https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=**********aea
webhook_url = '机器人地址'

# 构造消息内容 {today}
message = {
"msgtype": "markdown",
"markdown": {
"content": f"# <font color=\"warning\">信息中心：</font> \n >需在{weekday}下班后进行刻盘、导入、打印、复印的同事，于下班前到信息中心领取并向@吕利芬或@孙阳提交<font color=\"info\">《信息中心使用申请单》</font>，以便安排。\n <font color=\"comment\">节假日请忽略本消息</font>"
}
}

# 发送消息
response = requests.post(webhook_url, headers={'Content-Type': 'application/json'}, data=json.dumps(message))
