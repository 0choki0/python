numbers = [1, 2, 3, 4, 5]

# max[(1, 2, 3, 4, 5)]
max_num = max(numbers)
#print(max_num)
min_num = min(numbers)
#print(min_num)

import random # random을 공구라고 생각하면 된다.

random_number = random.randint(1, 100) # random에서 randint를 꺼내옴 / randint(a,b)는 a <= N <= B 에서의 N값을 나타냄
#print(random_number)


########

menus = ['김밥', '라면', '만두']
random_number = random.randint(0,2)
#print(menus[random_number])

menu = random.choice(menus) # choice(seq)는 list에서 한가지를 가져온다.
#print(menu)


########

numbers = range(1, 46) # range(a,b)는 a <= N < b 에서의 N값의 리스트 나타냄
lucky_number = random.sample(numbers, 6) #sample(a, n)은 a리스트에서 n개를 뽑음.
#print(sorted(lucky_number)) # sorted()는 데이터를 정렬된 형태로 바꾸어줌.

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086'

import requests

res = requests.get(URL)

#print(res.text) #res에서 text 값만 출력 해달라는 문구
#print(res.json) #text와 표기가 살짝 다름(파이썬 표준 표기)

data = res.json() #제이슨이라는 데이터를 key(data)로 저장

drwtNo1 = data['drwtNo1']
drwtNo2 = data['drwtNo2']
drwtNo3 = data['drwtNo3']
drwtNo4 = data['drwtNo4']
drwtNo5 = data['drwtNo5']
drwtNo6 = data['drwtNo6']

#print(drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6)

lotto_number = [drwtNo1, drwtNo2, drwtNo3, drwtNo4, drwtNo5, drwtNo6]

print(lucky_number)
print(lotto_number)

print(set(lucky_number) & set(lotto_number)) #set(a) & set(b) 은 a의 list와 b의 list에서 교집합을 나타냄



