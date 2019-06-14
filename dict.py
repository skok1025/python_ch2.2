# 생성
d = {'basketball':5, 'baseball':9}
print(d,type(d))

# 접근
print(d['basketball'])

# 변경가능
d['valleyball'] = 6
print(d)

# 반복(*), 연결(+) 지원하지 않는다. (sequence 형이 아니기 떄문에)

#길이
print(len(d))

#in, not in 가능 : 키만 가능
print('soccer' in d)
print('valleyball' in d)

#
# 다양한 dict 객체 생성 방법
#

# 1. literal
d = {}
print(type(d))

s = set()
print(type(s))

# dict() 사용법 1
d = dict()
print(d)


# dict() 사용법 2
d = dict(one=1, two=2,three=3)
print(d)

# dict() 사용법 3
d = dict([('one',1),('two',2),('three',3)])
print(d)

# dict() 사용법 4
keys = ('one','two','three')
values = 1,2,3
d = dict(zip(keys,values))
print(d)

# 다양한 key 타입 (Immutable 타입만)
d = {}
d[True] = 'true'
d['twenty'] = 20
d[(1,2,3)] = 6
# d[[1,2,3]] = 5

print(d)

# key 객체
keys = d.keys()
print(keys,type(keys))
for key in keys :
    print("{0}:{1}".format(key,d[key]))

# values 객체
values = d.values()
print(values,type(values))

# items 객체
# [(key1,val1), (key2,val2) .... ]
items = d.items()
print(items,type(items))

phone ={
    '둘리':'000-0000-0000',
    '마이콜':'111-0000-0000',
    '또치':'222-0000-0000'
}

#get 함수
# get을 사용하는 이유는 해당 키값의 값이 존재하지 않는 경우 None을 받기 위함
# print(phone['도우넛'])
print(phone.get('도우넛'))

# setDefault
# print(phone.setdefault({'도우넛','333-3333-3333'}))
print(phone)

number = phone.pop()
print(number)
print(phone)

# 업데이트
phone.update(
    {
        '도우넛':'333-3333-3333',
        '고피': '444-4444-4444'
    }
)