import requests
from pprint import pprint

URL = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=%2B58fRxySTvs0PfFQUY4WIxmfUdNzO2PRCGrFR%2BwurNXadOEb4nRyU4TfZFft%2FX7IOwZchblSbWUzs2S9mm1q2Q%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EC%84%9C%EC%9A%B8&ver=1.0'
#데이터의 주소를 key로 설정
res = requests.get(URL)

data = res.json()

# pprint(data)

#pprint(data['response']['body']['items'][n]) # 코드를 폴더 들어가듯이 접근함. (위의 데이터는 response->body->items 안에 들어 있음, 마지막은 list)

items = data['response']['body']['items']

for item in items:
    if item['stationName'] == '강남구':
        print(item['pm10Value'])
    