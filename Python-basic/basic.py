
# 아래의 3가지 경우는 양쪽의 의미가 다르다 
 # 1. apple / Apple (대문자와 소문자의 구분)
 # 2. git add. / git add . (공백의 구분)
 # 3. mesaage / massage (문자의 구분)

# 주석, 단축키 : ctrl+/

# 1. 저장 - 변수, variable 

 # 1. 숫자(int)
dust = 10
 # 2. 글자(string)
dust = '5'
 # 3. 참/거짓(boolean)
dust = True # False
#print(dust)

dust_list = [10, 20, 0, 50, 100]
#print(dust_list[3])

# dictionary 앞에 부분을 key, 뒷부분을 value
dust_dict = {
    '서울': 100,
    '대전': 10,
    '부산': 50,
}
#print(dust_dict['부산'])


# 2. 조건

age = 10

if age > 20:
    print('성인입니다.')
elif age > 8:
    print('청소년입니다.')
else:
    print('어린이입니다.')

dust = 20
# dust가 150보다 크다면 => 매우나쁨
# 80~149 => 나쁨
# 30~79 => 보통
# 0~29 => 좋음
if dust > 150:
    print('매우나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
# 이상/이하는 <=/>= 로 표현한다. and 구문으로 두개의 조건을 걸 수 있다.


# 3. 반복

menus = ['김밥', '라면', '김치찜', '불고기']

n = 0
while n < 4:
    print(menus[n])
    n = n + 1
# while은 조건이 True인 경우 반복하고 False인 경우 반복을 멈춘다.

for menu in menus:
    print(menu)