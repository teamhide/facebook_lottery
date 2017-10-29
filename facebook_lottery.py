import json
import requests
from random import *
import time

user = []
post = "241289886074076_781067592096300"
token = "EAACEdEose0cBACiQfp2lHltyC0ArWpdyJvqp8nDl0i4mQCB1QZAYDRRqug3krTmxaFfm1Y30UI0u249ig0xI7cJahS9ytEjVMJYdEN4t91Pq9rSuyOOV8KEegZBsU8ZBLFO3571jGpH048kjwfbD0yYpx4Mm2yZBZBTve3dYxIXQWxI368t7cP7eEU3L5tryGsIUiFF0V6QZDZD"
limit = "5000"

r = requests.get("https://graph.facebook.com/"+post+"/comments/?access_token="+token+"&limit="+limit)
r.encoding = "utf8"

decode_str = json.loads(r.text)
count = str(len(decode_str['data']))

print("[*] 총 "+count+"개의 댓글을 가져왔습니다.")

for i in range(int(count)):
	user.append(decode_str['data'][i]['from']['name']+decode_str['data'][i]['from']['id'])

print("[*] 중복 댓글 제거를 시작합니다.")
remove_dup = list(set(user))
print("[*] 총 댓글 수 : "+str(len(remove_dup)))
seed = randrange(int(count))
print("[*] 당첨자 추첨을 위한 시드 값을 생성했습니다 - > "+str(seed))
print("-------------------------------------------------------")
time.sleep(1)
print("[*] 추첨 결과")
print(remove_dup[seed])
