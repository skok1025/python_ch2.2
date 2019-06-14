# packing : tuple만 가능하다

t = 10,20,30,'python'
print(t,type(t))

# unpacking
a, b, c, d = t
print(a,b,c,d)

# Error
# a,b,c = t
# a, b, c, d, e, f = t

t = (1,2,3,4,5)
a, *b = t
print(b,type(b))

*a, b = t
print(b,type(b))

a,b,*c = t
print(a,b,c)

a,*b,c = t
print(a,b,c)

# cf. 멀티 파라미터


def sum(*num):
    sum = 0
    for n in num:
        sum += n
    return sum


print(sum(1,2))
print(sum(1,2,3))
print(sum(1,2,3,4,5,6))


# c 의 printf() 함수 흉내내기

def printf(format,*args):
    print(format % args)

printf('name: %s, age: %d',"둘리",10)