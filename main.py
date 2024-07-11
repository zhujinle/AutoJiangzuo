import requests, json
import time
import warnings
warnings.filterwarnings("ignore")
#定义接口地址
url = "https://api.jingjia6.com/bm/bm"
#构造参数
data = {'field.0':'xxx','field.1':'xxxxx','field.2':'xxxxxx','bm_id':'xxxxx'}
#指定参数类型
header={'Content-Type': 'application/json',
        'appid': 'wx2b732132f727acb0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9105',
        'token': 'xxxxxx',
        'Referer': 'https://servicewechat.com/wx2b732132f727acb0/196/page-frame.html'
        }
#发送请求
datajson = json.dumps(data)
response = requests.post(url, datajson, headers=header, verify=False)
#查看结果
jsonresponse = json.loads(response.content)
print(jsonresponse)
print(jsonresponse['status'])
time.sleep(0.84)
while(1):
    if jsonresponse['status'] != 200:
        print(jsonresponse)
        response = requests.post(url, datajson, headers=header, verify=False)
        jsonresponse = json.loads(response.content)
        time.sleep(0.84)
    else:
        print(jsonresponse)
        print("抢到")
        break