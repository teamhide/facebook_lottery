import json
import requests
import time
import random
from sys import stdout

user = {}
post = ""
token = ""
limit = "5000"

print("---------------------------------------------------------------------")
print("[*] 추첨을 위한 댓글 수집을 시작합니다.")
r = requests.get("https://graph.facebook.com/"+post+"/comments/?access_token="+token+"&limit="+limit)
r.encoding = "utf8"

decode_str = json.loads(r.text)
count = str(len(decode_str['data']))

print("[*] 총 "+count+"개의 댓글을 가져왔습니다.")
time.sleep(1)

for i in range(int(count)):
	user[decode_str['data'][i]['from']['name']+decode_str['data'][i]['from']['id']] = decode_str['data'][i]['from']['id']+"|"+decode_str['data'][i]['message']

print("[*] 중복 제거 후 총 댓글 수 : "+str(len(user)))
time.sleep(1)
seed = random.choice(list(user.keys()))
print("[*] 당첨자 추첨을 위한 시드 값을 생성했습니다.")
print("---------------------------------------------------------------------")
time.sleep(1)
info = user[seed].split('|')
url = "https://www.facebook.com/app_scoped_user_id/"+info[0]+"/"
comment = info[1]
time.sleep(1)
print("[*] 5초 후 결과가 발표됩니다.")
time.sleep(1)
for i in range(5, 0, -1):
	stdout.write("%d.. "%i)
	stdout.flush()
	time.sleep(1)
print("\n---------------------------------------------------------------------")
print("[*] 추첨 결과\n")
print("이름 : "+seed)
print("주소 : "+url)
print("댓글 : "+comment)
print("---------------------------------------------------------------------")
