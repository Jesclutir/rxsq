# coding:utf-8
import requests
import json
import time
from datetime import date, timedelta
from lxml import etree
import execjs
import os


def kutui_post(Subject, Message, Kutui_key):
    url = 'https://push.xuthus.cc/send/' + Kutui_key + '?c=' + Subject + '\n\n' + Message
    r = requests.post(url)





# 一卡通号、密码、姓名、手机号、身份证号等个人信息
username = os.environ["username"]
password = os.environ["password"]
USER_NAME = os.environ["USER_NAME"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
ID_NO = os.environ["ID_NO"]
KU = os.environ["KU"]

# 行程卡信息
scope = '162043657002556'
filetoken = scope+'1'

# 登录url
base_addr = 'http://ehall.seu.edu.cn/'
login = "https://newids.seu.edu.cn/authserver/login?service=http%3A%2F%2Fehall.seu.edu.cn%2Fqljfwapp3%2Fsys%2FlwWiseduElectronicPass%2Findex.do%3Ft_s%3D1620696987722%26amp_sec_version_%3D1%26gid_%3Dc0s4TVVNdUQ5UXplVVZFa3VMT3RlMW0yeHpMN2tCa0VhbEZjSlpIMHNaVkdBckYvd2VlWGorWFhDNzhRSWdnV1g4bEN0cVp5S1dzaDVrOGoraWRlM1E9PQ%26EMAP_LANG%3Dzh%26THEME%3Dindigo%23%2Fapplication"
ticket = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/index.do?t_s=1620696987722&amp_sec_version_=1&gid_=c0s4TVVNdUQ5UXplVVZFa3VMT3RlMW0yeHpMN2tCa0VhbEZjSlpIMHNaVkdBckYvd2VlWGorWFhDNzhRSWdnV1g4bEN0cVp5S1dzaDVrOGoraWRlM1E9PQ&EMAP_LANG=zh&THEME=indigo&ticket=ST-50277-o9qnvbyafruHMyy3On4N1620698052838-nNHH-cas'
index = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/index.do?t_s=1620696987722&amp_sec_version_=1&gid_=c0s4TVVNdUQ5UXplVVZFa3VMT3RlMW0yeHpMN2tCa0VhbEZjSlpIMHNaVkdBckYvd2VlWGorWFhDNzhRSWdnV1g4bEN0cVp5S1dzaDVrOGoraWRlM1E9PQ&EMAP_LANG=zh&THEME=indigo'
lwWiseduElectronicPass = base_addr + 'qljfwapp3/sys/emappagelog/config/lwWiseduElectronicPass.do'
application = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application.do'
getApplicationData = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/getApplicationData.do'
CAMPUS_CODE = base_addr + 'qljfwapp3/code/2d7772bc-4fb3-4e2c-a224-6df948cce897/CAMPUS_CODE.do?_=1620698056185'
getList = base_addr + 'qljfwapp3/sys/emapcomponent/schema/getList.do'
queryUserTask = base_addr + 'qljfwapp3/sys/emapflow/*default/index/queryUserTasks.do'
hqsqjzsj = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/hqsqjzsj.do'
# 申请url
T_APPLY_LIMITE_QUERY = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/T_APPLY_LIMITE_QUERY.do'
applicationSave = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/applicationSave.html?av=30000'
undefined = base_addr + 'qljfwapp3/sys/emapcomponent/file/getUploadedAttachment/undefined.do'
hqdqryyqsbxx = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/hqdqryyqsbxx.do'
SEX = base_addr + 'qljfwapp3/code/2d7772bc-4fb3-4e2c-a224-6df948cce897/SEX.do'
ID_TYPE = base_addr + 'qljfwapp3/code/2d7772bc-4fb3-4e2c-a224-6df948cce897/ID_TYPE.do'
STATUS = base_addr + 'qljfwapp3/code/2d7772bc-4fb3-4e2c-a224-6df948cce897/STATUS.do'
hqsqjzsj = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/hqsqjzsj.do'
queryFirstUserTaskToolbar = base_addr + 'qljfwapp3/sys/emapflow/definition/queryFirstUserTaskToolbar.do?defKey=lwWiseduElectronicPass.MainFlow'
# 填写url
COMMON_STATE = base_addr + 'qljfwapp3/code/2d7772bc-4fb3-4e2c-a224-6df948cce897/COMMON_STATE.do'
pass_campus = base_addr + 'qljfwapp3/code/038e533b-1c26-4572-9320-b8f2efa3f2d1.do' 
SQLY = base_addr + 'qljfwapp3/code/2d7772bc-4fb3-4e2c-a224-6df948cce897/SQLY.do'
uploadTempFile = base_addr + 'qljfwapp3/sys/emapcomponent/file/uploadTempFile.do'
# 提交url
submit1 = base_addr + 'qljfwapp3/sys/emapcomponent/file/saveAttachment/'+str(scope)+'/'+str(filetoken)+'.do'
submit2 = base_addr + 'qljfwapp3/sys/emapcomponent/file/getUploadedAttachment/'+str(filetoken)+'.do'
queryNextDayInschoolCount = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/modules/application/queryNextDayInschoolCount.do'
validateApply = base_addr + 'qljfwapp3/sys/lwWiseduElectronicPass/api/validateApply.do'
# startFlow
startFlow = base_addr + 'qljfwapp3/sys/emapflow/tasks/startFlow.do'

# 使用会话保持cookie
s = requests.Session()

# 首次请求，获取隐藏参数
start_response = s.get(login)
start_html = etree.HTML(start_response.text,parser=etree.HTMLParser())
lt = start_html.xpath('//*[@id="casLoginForm"]/input[1]/@value')[0]
dllt = start_html.xpath('//*[@id="casLoginForm"]/input[2]/@value')[0]
execution = start_html.xpath('//*[@id="casLoginForm"]/input[3]/@value')[0]
_eventId = start_html.xpath('//*[@id="casLoginForm"]/input[4]/@value')[0]
rmShown = start_html.xpath('//*[@id="casLoginForm"]/input[5]/@value')[0]
pwdDefaultEncryptSalt = start_html.xpath('//*[@id="casLoginForm"]/input[6]/@value')[0]
print('首次请求,获取隐藏参数')

# 调用JavaScript对密码进行加密
with open('encrypt.js', 'r') as f:
    js = f.read()
ctx = execjs.compile(js)
password = ctx.call('encryptAES', password, pwdDefaultEncryptSalt)
print('调用JavaScript进行AES加密')

# 登录
data = {
    'username': username,
    'password': password,
    'lt': lt,
    'dllt': dllt,
    'execution': execution,
    '_eventId': _eventId,
    'rmShown': rmShown
    }
login_response = s.post(login, data=data, allow_redirects=False)
print('跳转统一身份认证登录')

# 获取Location,向DailyReport客户端发送请求
url = login_response.headers['Location']
s.get(url, allow_redirects=False)
print('登录成功,跳转入校申请')

# 对照浏览器执行相同的请求
s.get(ticket)
s.get(index)
s.get(lwWiseduElectronicPass)
s.post(application,{'*json':'1'})
s.post(getApplicationData,{'*searchMeta':'1'})
s.get(CAMPUS_CODE)
s.post(getList,{'schemaType':'aq','pageFlag':'application%2CApplicationDataParam'})
s.post(application,{'*json':'1','pageNumber':'1'})
s.post(getList,{'schemaType':'col','pageFlag':'application%2CApplicationDataDisplay'})
_response = s.post(queryUserTask,{'taskType': 'ALL_TASK','nodeId': 'usertask1','appName': 'lwWiseduElectronicPass','module': 'modules','page': 'application','action': 'getApplicationData','*order': '-CREATED_AT','pageSize': '10','pageNumber': '1'})
s.post(hqsqjzsj)

# 当前时间生成
today_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print('当前时间：',today_time)

# 通行时间生成
tomorrow_year = (date.today() + timedelta(days=1)).strftime("%Y")
tomorrow_month = (date.today() + timedelta(days=1)).strftime("%m")
tomorrow_day = (date.today() + timedelta(days=1)).strftime("%d")
tomorrow = str(tomorrow_year)+"-"+str(tomorrow_month)+"-"+str(tomorrow_day)
tomorrow_begin_time = str(tomorrow_year)+"-"+str(tomorrow_month)+"-"+str(tomorrow_day)+" 00:00:01"
tomorrow_end_time = str(tomorrow_year)+"-"+str(tomorrow_month)+"-"+str(tomorrow_day)+" 23:59:59"
print('明天日期：',tomorrow)
print('通行开始时间：',tomorrow_begin_time)
print('通行结束时间：',tomorrow_end_time)

# 申请按键模拟发包
s.post(T_APPLY_LIMITE_QUERY,{'USER_ID':username})
s.get(applicationSave)
s.post(application,{'*json':'1'})
s.post(undefined)
s.post(hqdqryyqsbxx,{'USERID':username})
s.post(SEX)
s.post(ID_TYPE)
s.post(STATUS)
s.post(hqsqjzsj)
s.get(queryFirstUserTaskToolbar)
print('申请')

# 填写过程模拟发包
s.post(COMMON_STATE)
s.post(pass_campus)
s.post(SQLY)
s.post(uploadTempFile,{'scope': scope,'fileToken': filetoken,'size': '0','type': 'jpg,jpeg,png','storeId': 'image','isSingle': '0','fileName': '','files[]': '行程卡.PNG'})
s.post(submit1,{'attachmentParam': str({"storeId":"image","scope":scope,"fileToken":filetoken})})
submit_response = s.post(submit2)
# print(submit_response.text)
s.post(queryNextDayInschoolCount,{'DEPT_CODE':'243015','PERSON_TYPE':'YJS'})
s.post(validateApply,{'userid': username,'campus': '1,2,3','beginTime': tomorrow})
print('提交')

# 注意获取当日期
# data
formData = {
    "WID":"",
    "USER_ID":username,
    "USER_NAME":USER_NAME,
    "GENDER_CODE_DISPLAY":"男",
    "GENDER_CODE":"1",
    "PHONE_NUMBER":PHONE_NUMBER,
    "DEPT_CODE":"243015",
    "DEPT_NAME":"网络与信息中心",
    "ID_TYPE_DISPLAY":"居民身份证",
    "ID_TYPE":"1","ID_NO":ID_NO,
    "PERSON_TYPE_DISPLAY":"QTRY",
    "PERSON_TYPE":"QTRY",
    "JTBG_ADDRESS":"金智楼",
    "SFFHFHYQ_DISPLAY":"是",
    "SFFHFHYQ":"1",
    "NFZHGRFH_DISPLAY":"是",
    "NFZHGRFH":"1",
    "DZ_SFYJCS4":"无",
    "DZ_SFYJCS1":"否",
    "DZ_SFYJCS2":"否",
    "DZ_SFYJCS3":"否",
    "DZ_JRSTZK_DISPLAY":"是",
    "DZ_JRSTZK":"1",
    "SFYZNJJJGL_DISPLAY":"是",
    "SFYZNJJJGL":"1",
    "SFJBZJHBXLXTJ_DISPLAY":"是",
    "SFJBZJHBXLXTJ":"1",
    "YL6":filetoken,   #############################################filetoken
    "YL7":"",
    "CAMPUS_DISPLAY":"九龙湖校区,四牌楼校区,丁家桥校区",
    "CAMPUS":"1,2,3",
    "IN_SCHOOL_TIME":tomorrow_begin_time,
    "OFF_SCHOOL_TIME":tomorrow_end_time,
    "RESSON_DISPLAY":"其他工作",
    "RESSON":"qtgz",
    "QTGZ":"",
    "REMARK":"",
    "TIMES":"",
    "STATUS_DISPLAY":"审核中",
    "STATUS":"2",
    "CREATED_AT":today_time,
    "CZR":"",
    "CZZXM":"",
    "CZRQ":"",
    "IS_FLOW":"1",
    "LXFS_DISPLAY":"",
    "LXFS":"",
    "SQ_REASON_DISPLAY":"",
    "SQ_REASON":"",
    "YL1":"",
    "YL2_DISPLAY":"",
    "YL3_DISPLAY":"",
    "YL3":"",
    "userType":'true',
    }
startFlow_data = {
    'formData':str(formData),
    'sendMessage': 'true',
    'id': 'start',
    'commandType': 'start',
    'execute': 'do_start',
    'name': '提交',
    'url': '/sys/emapflow/tasks/startFlow.do',
    'buttonType': 'success',
    'taskId':'', 
    'defKey': 'lwWiseduElectronicPass.MainFlow'
    }
# startFlow
startFlow_response = s.post(startFlow,startFlow_data)
print('提交确认,startFlow.do')

print(startFlow_response.text)
subject = str(tomorrow)
subject = subject+'入校申请\t成功'
msg = str(tomorrow)+'入校申请成功'
kutui_post(msg,msg,KU)
