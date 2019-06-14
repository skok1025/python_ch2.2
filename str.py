# 한줄 문자열 정의

s = ''
str = 'Hello world'
print(type(s), type(str))

# 여러줄
str2 = '''
print(str2)
'''

'''
여기는 주석

'''

#
# 문자열 연산
#

# 1. 인덱싱
str1 = 'First String'
str2 = 'Second String'

print(str1[0])
print(str1[-1],str1[-2])

# 2. Slicing
# s[start:stop:step]
str3 = str2[2:5]
print(str3)
# print(str2[2:len(str2):1])
print(str2[2:])

s = "Python"
print(s[-1]) # 마지막 문자
print(s[-2:]) # 마지막 2개 문자
print(s[:-2]) # 마지막 2개 문자 제외

print(s[::-1])
print(s[1::-1])
print(s[:-3:-1]) # 마지막 두개 문자 역순
print(s[-3::-1])

# 연결 (+)
print(str1+' '+str2)
# 리터럴 연결시
str3 = '1st' '' '2nd'

# 문자열 객체 연결은 문자열 끼리만 가능하다.
name = '둘리'
age = 10
# print(name + age)

# 반복 (*)
print(str1 * 3)

# len() 함수
print(len(str1))

# in , not in 연산
print("F" in str1)
print('S' not in str1)

# str 객체는 Immutable
# str1[0] = 'f'

# 서식 = format 함수
print("name:" +name)

# 서식
f = "name: %s, age=%d"
print(f %(name,age))

# 서식
f = "name: %(n)s, age: %(a)d"
print(f % {'n':'둘리', 'a':10})

#
# 객체 함수
#

# 1. 대소문자 관련
s = 'i Like Java'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 검색
s = 'I Like Java, I Don\'t Like Python'
print(s.count('Like'))
print(s.find('Like'))
print(s.find('Like',5))
print(s.find('javaScript'))
print(s.rfind('Like'))

# 발견 못하면 예외 발생
# print(s.index("JavaScript"))

print(s.startswith("I Like"))
print(s.startswith("Like",2))
print(s.endswith("Java",0,11))

# 편집과 치환
s = '    spam and ham  '
print(s.strip())

s = '<><abc><><defg><><>'
print('------'+s.strip('<>')+'-----')
print('------'+s.strip('><')+'-----')

s = 'Hello Java'
print(s.replace('Java','Python'))

# 분리 & 결합
s = 'spam and ham'
t = s.split(' and ')
print(t,type(t))

s2 = ':'.join(t)
print(s2)

s3 = 'one:two:three:four:five'
print(s3.split(':',2))
print(s3.rsplit(':',2))

lines ='''1st line
2nd line 

3rd line 
4th line 
'''
print(lines.split('\n'))
print(lines.splitlines())

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())

print('abcd'.islower())
print('abcd'.isupper())

print('     '.isspace())
print('\r\n'.isspace())
print('\t'.isspace())

# '0' 채우기
print('20'.zfill(5))
print('1234'.zfill(5))

# 서식: 객체함수
print('name:{}, age:{}'.format('둘리',10))
print('name:{1}, age:{0}'.format(10,'마이콜'))
print('{:3}의 제곱근은 {:.7}'.format(2,2**0.5))
print('name:{n}, age:{a}'.format_map({'a':20,'n':'둘리'}))















