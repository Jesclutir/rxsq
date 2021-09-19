# coding:utf-8
import requests
import json
import time
from datetime import date, timedelta
from lxml import etree
import execjs
import os


# 一卡通号、密码、姓名、手机号、身份证号等个人信息
username = os.environ["username"]
password = os.environ["password"]
USER_NAME = os.environ["USER_NAME"]
PHONE_NUMBER = os.environ["PHONE_NUMBER"]
ID_NO = os.environ["ID_NO"]

###################################健康申报##################################

# 登录url
base_addr = 'http://ehall.seu.edu.cn/'
login = "https://newids.seu.edu.cn/authserver/login?service=http%3A%2F%2Fehall.seu.edu.cn%2Fqljfwapp2%2Fsys%2FlwReportEpidemicSeu%2Findex.do%3Ft_s%3D1627267837606%26amp_sec_version_%3D1%26gid_%3DZDFGWVJaaVZtdGpVWHFXSUprc3NtV01zSU9sRGRONC95WUVFaUwvWkI1T2lxQ0VxWHgwWjVXM29GbjVZSjMzQTFMOGNzbWtEU1NCdi9sWTdIZ1VlWGc9PQ%26EMAP_LANG%3Dzh%26THEME%3Dindigo%23%2FdailyReport"


# 新增url
index = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/index.do?t_s=1627267837606&amp_sec_version_=1&gid_=ZDFGWVJaaVZtdGpVWHFXSUprc3NtV01zSU9sRGRONC95WUVFaUwvWkI1T2lxQ0VxWHgwWjVXM29GbjVZSjMzQTFMOGNzbWtEU1NCdi9sWTdIZ1VlWGc9PQ&EMAP_LANG=zh&THEME=indigo'
getCheckinFormTips = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/api/daily/getCheckinFormTips.do'
getUserDetailDB = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/api/base/getUserDetailDB.do'
clm10 = base_addr + 'clm10'
getRouteConfig = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/configSet/noraml/getRouteConfig.do?v=026686544202624285'
iconfont = 'http://res.seu.edu.cn/fe_components/iconfont/iconfont.woff?t=1463659141'
lwReportEpidemicSeu = base_addr + 'qljfwapp2/sys/emappagelog/config/lwReportEpidemicSeu.do'
headPic = base_addr + 'qljfwapp2/sys/itpub/common/headPic.do?id=' + username
getServerTime = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/api/daily/getServerTime.do'
getTwSetting = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/api/ekdz/getTwSetting.do'
getList = base_addr + 'qljfwapp2/sys/emapcomponent/schema/getList.do'
dailyReport = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport.do'
getMyDailyReportDatas = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/getMyDailyReportDatas.do'

# 新增点击
cxwdjbxxcjsl = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/cxwdjbxxcjsl.do'
getTodayHasReported = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/getTodayHasReported.do'
checkMrbpaSfksb = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/api/ekdz/checkMrbpaSfksb.do'
getMyTodayReportWid = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/getMyTodayReportWid.do'
getLatestDailyReportData = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/getLatestDailyReportData.do'

# 保存url
getServerTime = base_addr + 'qljfwapp2/sys/lwReportEpidemicSeu/api/daily/getServerTime.do'
T_REPORT_EPIDEMIC_CHECKIN_SAVE = 'http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/modules/dailyReport/T_REPORT_EPIDEMIC_CHECKIN_SAVE.do'


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
print(login_response)
print('跳转统一身份认证登录')

# 获取Location,向DailyReport客户端发送请求
url = login_response.headers['Location']
s.get(url, allow_redirects=False)
print('登录成功,跳转健康申报')

# 对照浏览器执行相同的请求

# 当前时间生成
date_time = time.strftime("%Y-%m-%d", time.localtime())
today_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
dbrq = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
print('当前时间：',today_time)

# 新增按键模拟发包
s.get(index)
s.post(getCheckinFormTips)
s.post(getUserDetailDB,{'userType': 'TEACHER'})
s.get(getRouteConfig)
s.get(iconfont)
s.post(clm10,{"ns":1627267940342,"us":1627267940724,"ue":1627267940724,"fs":1627267940344,"dls":1627267940344,"dle":1627267940344,"cs":1627267940345,"ce":1627267940650,"rqs":1627267940650,"rss":1627267940721,"rse":1627267940722,"dl":1627267940729,"di":1627267940879,"dcls":1627267940879,"dcle":1627267940882,"dc":1627267941653,"ls":1627267941653,"le":1627267941654,"tid":1026943149,"pid":275116665,"ac":"logstream_10.64.16.45"})
s.get(lwReportEpidemicSeu)
s.get(headPic)
s.post(getServerTime)
s.post(getTwSetting)
s.post(dailyReport,{'*json':'1'})
s.post(getMyDailyReportDatas,{'*searchMeta':'1'})
s.post(getList,{'schemaType':'aq','pageFlag':'dailyReport,MyDailyReportDatasParam.custom'})
s.post(dailyReport,{'*json':'1','rysflb':'QTRY'})
s.post(getList,{'schemaType':'col','pageFlag':'dailyReport,MyDailyReportDatasDisplay.custom'})
s.post(getMyDailyReportDatas,{'rysflb':'QTRY','pageSize':'10','pageNumber':'1'})
print('新增')
s.post(cxwdjbxxcjsl,{'pageNumber':'1'})
s.post(getTodayHasReported,{'pageNumber':'1'})
s.post(checkMrbpaSfksb)
s.post(dailyReport,{'*json':'1','rysflb':'QTRY','isEdit':'1'})
s.post(getMyTodayReportWid,{'pageNumber':'1'})
s.post(getLatestDailyReportData,{'pageNumber':'1','pageSize':'10'})
s.post(getServerTime)

# 注意获取当日期
# data
formData = {
    'WID': 'C8AAD280FAFC039FE0531182410A4F85',
    'NEED_CHECKIN_DATE': date_time,
    'DEPT_CODE': '243015',
    'CZR': '',
    'CZZXM': '' ,
    'CZRQ':date_time+ ' 00:03:10',
    'CLASS_CODE': '',
    'CLASS': '',
    'DZ_DQWZ_JD': '',
    'DZ_DQWZ_WD': '' ,
    'DZ_DQWZ_SF': '',
    'DZ_DQWZ_CS': '',
    'DZ_DQWZ_QX': '',
    'USER_NAME_EN': '',
    'DZ_XYYYPJG_DISPLAY': '',
    'DZ_XYYYPJG': '2',
    'USER_ID': username,
    'USER_NAME': USER_NAME,
    'DEPT_NAME': '网络与信息中心',
    'GENDER_CODE_DISPLAY': '男',
    'GENDER_CODE': '1',
    'PHONE_NUMBER': PHONE_NUMBER,
    'IDCARD_NO': ID_NO,
    'LOCATION_DETAIL': '',
    'EMERGENCY_CONTACT_PERSON': '',
    'EMERGENCY_CONTACT_PHONE': '',
    'EMERGENCY_CONTACT_NATIVE': '',
    'EMERGENCY_CONTACT_HOME': '',
    'HEALTH_STATUS_CODE_DISPLAY': '正常',
    'HEALTH_STATUS_CODE': '001',
    'HEALTH_UNSUAL_CODE': '',
    'IS_SEE_DOCTOR_DISPLAY': '',
    'IS_SEE_DOCTOR': '',
    'SAW_DOCTOR_DESC': '',
    'MEMBER_HEALTH_STATUS_CODE_DISPLAY': '',
    'MEMBER_HEALTH_STATUS_CODE': '',
    'MEMBER_HEALTH_UNSUAL_CODE': '',
    'MENTAL_STATE': '',
    'RYSFLB': 'QTRY',
    'DZ_JSDTCJTW': '36.5',
    'DZ_DTWJTW': '',
    'DZ_DTWSJCTW': '',
    'DZ_SZWZLX_DISPLAY': '在校外(在南京)',
    'DZ_SZWZLX': '004',
    'DZ_SZWZ_GJ_DISPLAY': '',
    'DZ_SZWZ_GJ': '',
    'DZ_SZWZXX': '',
    'DZ_MQZNJWZ': '江宁',
    'DZ_SZXQ_DISPLAY': '',
    'DZ_SZXQ': '',
    'LOCATION_PROVINCE_CODE_DISPLAY': '',
    'LOCATION_PROVINCE_CODE': '',
    'LOCATION_CITY_CODE_DISPLAY': '',
    'LOCATION_CITY_CODE': '',
    'LOCATION_COUNTY_CODE_DISPLAY': '',
    'LOCATION_COUNTY_CODE': '',
    'DZ_SFGL_DISPLAY': '否',
    'DZ_SFGL': '001',
    'DZ_WD': '',
    'DZ_GLKSSJ': '',
    'DZ_GLJSSJ': '',
    'DZ_GLDQ_DISPLAY': '',
    'DZ_GLDQ': '',
    'DZ_GLDSF_DISPLAY': '',
    'DZ_GLDSF': '',
    'DZ_GLDCS_DISPLAY': '',
    'DZ_GLDCS': '',
    'DZ_GLSZDQ': '',
    'DZ_MQSFWYSBL_DISPLAY': '否',
    'DZ_MQSFWYSBL': '0',
    'DZ_YSGLJZSJ': '',
    'DZ_YS_GLJZDSF_DISPLAY': '',
    'DZ_YS_GLJZDSF': '',
    'DZ_YS_GLJZDCS_DISPLAY': '',
    'DZ_YS_GLJZDCS': '',
    'DZ_MQSFWQRBL_DISPLAY': '否',
    'DZ_MQSFWQRBL': '0',
    'DZ_QZGLJZSJ': '',
    'DZ_QZ_GLJZDSF_DISPLAY': '',
    'DZ_QZ_GLJZDSF': '',
    'DZ_QZ_GLJZDCS_DISPLAY': '',
    'DZ_QZ_GLJZDCS': '',
    'DZ_SFYJCS1_DISPLAY': '无',
    'DZ_SFYJCS1': '0',
    'DZ_ZHLKRQ': '',
    'DZ_SFYJCS2_DISPLAY': '无',
    'DZ_SFYJCS2': '0',
    'DZ_GRYGLSJ1': '',
    'DZ_ZHJCGRYSJ1': '',
    'DZ_SFYJCS3_DISPLAY': '无',
    'DZ_SFYJCS3': '0',
    'DZ_ZHJCGRYSJ2': '',
    'DZ_SFYJCS4_DISPLAY': '无',
    'DZ_SFYJCS4': '0',
    'DZ_JJXFBSJ': '',
    'DZ_JJXFBD_SF_DISPLAY': '',
    'DZ_JJXFBD_SF': '',
    'DZ_JJXFBD_CS_DISPLAY': '',
    'DZ_JJXFBD_CS':'', 
    'DZ_BRYWYXFH_DISPLAY': '',
    'DZ_BRYWYXFH': '',
    'DZ_JCQKSM': '',
    'DZ_JRSFFS_DISPLAY': '无',
    'DZ_JRSFFS': '0',
    'DZ_TWDS': '',
    'DZ_JRSTZK_DISPLAY': '无',
    'DZ_JRSTZK': '001',
    'DZ_SMJTQK': '',
    'DZ_SFYJCS5_DISPLAY': '无',
    'DZ_SFYJCS5': '0',
    'DZ_YJZCDDGNRQ': '',
    'DZ_SFYJCS7_DISPLAY': '无',
    'DZ_SFYJCS7': '0',
    'DZ_ZHJCGGRYSJ': '',
    'DZ_SFYJCS8_DISPLAY': '无',
    'DZ_SFYJCS8': '0',
    'DZ_JTQY_DISPLAY': '',
    'DZ_JTQY': '',
    'DZ_SFYJCS9_DISPLAY': '无',
    'DZ_SFYJCS9': '0',
    'DZ_SFYJCS10_DISPLAY': '无',
    'DZ_SFYJCS10': '0',
    'DZ_YWQTXGQK_DISPLAY': '无',
    'DZ_YWQTXGQK': '0',
    'DZ_QKSM':'', 
    'DZ_JRSFYXC_DISPLAY': '无',
    'DZ_JRSFYXC': '0',
    'DZ_MDDSZSF_DISPLAY': '',
    'DZ_MDDSZSF': '',
    'DZ_MDDSZCS_DISPLAY': '',
    'DZ_MDDSZCS': '',
    'DZ_JTFS_DISPLAY': '',
    'DZ_JTFS': '',
    'DZ_CCBC': '',
    'DZ_SFDXBG_DISPLAY': '是',
    'DZ_SFDXBG': '1',
    'DZ_SYJTGJ_DISPLAY': '步行，骑行',
    'DZ_SYJTGJ': '007,006',
    'DZ_SDXQ_DISPLAY': '九龙湖',
    'DZ_SDXQ': '002',
    'DZ_YMJZRQ1': '2021-04-09',
    'DZ_YMJZD1': '九龙湖校区体育馆',
    'DZ_YMJZRQ2': '2021-05-28',
    'DZ_YMJZD2': '九龙湖校区体育馆',
    'DZ_WJZYMYY_DISPLAY': '',
    'DZ_WJZYMYY': '',
    'DZ_WJZYMQTYY': '',
    'REMARK': '',
    'CREATED_AT': today_time,
    'DZ_DBRQ': dbrq,
    'DZ_SFYBH': '0',
    'DZ_SFLXBXS': '',
    'DZ_ZDYPJG': ''
    }

# 保存按键模拟发包
s.post(getServerTime)
s.post(dailyReport,{'*json':'1'})
T_REPORT_EPIDEMIC_CHECKIN_SAVE_response = s.post(T_REPORT_EPIDEMIC_CHECKIN_SAVE,formData)
print('保存确认,T_REPORT_EPIDEMIC_CHECKIN_SAVE')
print(T_REPORT_EPIDEMIC_CHECKIN_SAVE_response.text)


###################################入校申请##################################
# 苏康码信息
scope = '163081005208572'
filetoken = scope+'1'

# 登录url
base_addr = 'http://ehall.seu.edu.cn/'
#login = "https://newids.seu.edu.cn/authserver/login?service=http%3A%2F%2Fehall.seu.edu.cn%2Fqljfwapp3%2Fsys%2FlwWiseduElectronicPass%2Findex.do%3Ft_s%3D1620696987722%26amp_sec_version_%3D1%26gid_%3Dc0s4TVVNdUQ5UXplVVZFa3VMT3RlMW0yeHpMN2tCa0VhbEZjSlpIMHNaVkdBckYvd2VlWGorWFhDNzhRSWdnV1g4bEN0cVp5S1dzaDVrOGoraWRlM1E9PQ%26EMAP_LANG%3Dzh%26THEME%3Dindigo%23%2Fapplication"
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


# 获取Location,向DailyReport客户端发送请求
url = 'http://ehall.seu.edu.cn/qljfwapp3/sys/lwWiseduElectronicPass/index.do?t_s=1628043795009&amp_sec_version_=1&gid_=c0s4TVVNdUQ5UXplVVZFa3VMT3RlMW0yeHpMN2tCa0VhbEZjSlpIMHNaVkdBckYvd2VlWGorWFhDNzhRSWdnV1g4bEN0cVp5S1dzaDVrOGoraWRlM1E9PQ&EMAP_LANG=zh&THEME=indigo#/application'
s.get(url)
print('转到入校申请')

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
s.post(uploadTempFile,{'scope': scope,'fileToken': filetoken,'size': '0','type': 'jpg,jpeg,png','storeId': 'image','isSingle': '0','fileName': '','files[]': '行程卡.jpg'})
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
    "SFYZNJJJGL":"1、8月11日九龙湖体育馆结果阴性2、8月8日九龙湖体育馆结果阴性3、8月5日九龙湖体育馆结果阴性",
    "SFJBZJHBXLXTJ_DISPLAY":"是",
    "SFJBZJHBXLXTJ":"1",
    "YL6":filetoken,
    "YL7":"",
    "CAMPUS_DISPLAY":"九龙湖校区,四牌楼校区,丁家桥校区",
    "CAMPUS":"1,2,3",
    "IN_SCHOOL_TIME":tomorrow_begin_time,
    "OFF_SCHOOL_TIME":tomorrow_end_time,
    "RESSON_DISPLAY":"其他工作",
    "RESSON":"qtgz",
    "QTGZ":"",
    "REMARK":"燕湖路201号龙湖冠寓",
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
