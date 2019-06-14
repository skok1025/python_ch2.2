# 사칙연산
print(2 * 3)
print(2 / 3)
print(2 + 3)
print(2 - 3)

# 나눗셈은 다 같다
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3)
print(2.0 / 3.0)

# //(몫) **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# 몫, 나머지 동시에 값을 반환
result, last = divmod(2,3)
print(result,last)

t = divmod(2,3)
print(t,type(t))

# 연산자 우선순위
print(2+3*4)
print(-2+3*4)
print(-(2+3)*4)

print(4/2*2)

# 결합순서 주의!!
print((2**3)**4)
print(2**3**4)
print(2**(3**4))

print('abcd' > 'abd')
print((1,2,4)<(1,3,1))
print([1,3,2]<[1,2,0])
print([1,2,4]<list((1,3,1)))

# 동질성 비교: == 동일성 비교: is
a = 10
b = 20
c = a
d = 10

print(a == b)
print(a is b)
print(a is c)
print(a == c)
print(a == d)
print(a is d)

l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2)
print(l1 is l2)

# 논리의 계산 순서
print([] or 'logical')
print('logical' or 'operator')
print('' or 'operator')
print('' and 'operator')
print('ok')

s = 'hello world'

def f(msg=''):
    msg and print(msg)
f(s)
f()

def f():
    print('exec')

# if 1+2<10 :
#     f()

1+2<10 and f()





















