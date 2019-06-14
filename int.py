a = 23
print(a,type(a))
print(isinstance(a, int))
print(isinstance(a, float))

# 2진수, 10진수, 16진수, 8진 상수 (literal)
b = 0b1101
c = 0o23
d = 0x23
print(b,c,d)

# 3.x int가 long이 합쳐졌음 (무한대)
e = 2 ** 1024
print(e)
print(type(e))

# 변환함수
print(oct(38))
print(hex(38))
print(bin(38))










