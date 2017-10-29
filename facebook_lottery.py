import json
import requests
import time
import random

user = {}
post = "" # 페이지번호_포스트번호 형태
token = "" # access_token
limit = "5000" # 가져올 댓글의 수

print("[*] 추첨을 위한 댓글 수집을 시작합니다.")
r = requests.get("https://graph.facebook.com/"+post+"/comments/?access_token="+token+"&limit="+limit)
r.encoding = "utf8"

decode_str = json.loads(r.text)
count = str(len(decode_str['data']))

print("[*] 총 "+count+"개의 댓글을 가져왔습니다.")

for i in range(int(count)):
	user[decode_str['data'][i]['from']['name']+decode_str['data'][i]['from']['id']] = decode_str['data'][i]['from']['id']+"|"+decode_str['data'][i]['message']

print("[*] 중복 제거 후 총 댓글 수 : "+str(len(user)))
seed = random.choice(list(user.keys()))
print("[*] 당첨자 추첨을 위한 시드 값을 생성했습니다.")
print("-------------------------------------------------------")
info = user[seed].split('|')
url = "https://www.facebook.com/app_scoped_user_id/"+info[0]+"/"
comment = info[1]
time.sleep(3)
print("[*] 추첨 결과")
print("이름 : "+seed)
print("주소 : "+url)
print("댓글 : "+comment)
