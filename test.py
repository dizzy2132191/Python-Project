'''
season='겨울'
print('지금은','이 따옴표로 쌓인 글을 지우고 대신 변수 season을 넣어 보세요','입니다.')
#이 프린트 문은 season 변수를 읽어 냅니다.
print('지금은','이 따옴표로 쌓인 글을 지우고 대신 변수', season,'을 넣어 보세요','입니다.')

#'', "" ==> 문자열
# 안둘러 싸져 있음? ==> 변수
#ㅁㄴㅇㅎㅁㄴㅇㅎㅁㅈㄷㅎㅁㅎㄴㅇㅎㅋㅌㅎㅋㄴ
#print('지금은','이 따옴표로 쌓인 글을 지우고 대신 변수', season,'을 넣어 보세요','입니다.')

print('지금은','이 따옴표로 쌓인 글을 지우고 대신 변수', season,'을 넣어 보세요','입니다.')
print('지금은','이 따옴표로 쌓인 글을 지우고 대신 변수', season,'을 넣어 보세요','입니다.')
'''

#///////////////////////////////////////////////////////////////////////////////////////
'''
a = 33
b = 3
summation = a + b
multiply = a * b
divide = a / b
remainder = a % b
power = a ** b

print("summation은 {}입니다.".format(summation))
print("multiply는 {}입니다.".format(multiply))
print("divide는 {}입니다.".format(divide))
print("remainder는 {}입니다.".format(remainder))
print("power는 {}입니다.".format(power))
print("test")
'''
#print("주석은")
#print("이 프린트 문을 주석처리 하세요")
#print("실행되지 않습니다.")

#print("여러줄의 주석은")
"""
여러줄의
주석은
어떻게
처리할까요?
"""
#print("따옴표 3개로 감싸서 처리합니다.")
"""
x = 17
y = x + 1
a = 17 / 17
b = 2 * 10
c = 100 % 8

print("x는 {}입니다.".format(x))
print("y는 {}입니다.".format(y))
print("a는 {}입니다.".format(a))
print("b는 {}입니다.".format(b))
print("c는 {}입니다.".format(c))
"""

#x = '2020'
#text = x + '0418'
#print(text)
'''
birth_year = '2004'
birth_date = '0513'
year_and_date = birth_year + birth_date

print("year_and_date : {}".format(year_and_date))



if apple < people:
    print("사과수가 너무 적어! 몇명은 못 먹겠네.")
'''
'''
#if 3 < 5:
   # print("True.")

if 3 > 5:
    print("False.")

if True:
    print("나는 천재다.")

if False:
    print("나는 바보다.")
'''


hour = 12

if hour < 12:
    print('오전입니다.')
if hour >= 12:
    print('오후입니다.')

#from datetime import datetime  (무슨 뜻?)
#hour = datetime.now().hour     (무슨 뜻?)