# from copy import copy

languages = ['python', 'perl', 'c', 'java']

# for lang in languages:
#     if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler" % lang)
#     else:
#         print("should not reach here")wkd


print("=" * 50)
print("I'm studing how to programming python!")
print("=" * 50)

multiline = '''
    Life is too short
    You need python
    '''
print(multiline)
print("Length of multiline : %d" % len(multiline))

# String Manipulation
print("=" * 50)
print(" String Manipulation")
print("=" * 50)

a = "Pithon"
b = a[:1] + 'y' + a[2:]
# a[1] = "y"
print(a, b)
print("0x%x" % id(a))
print("0x%x" % id(b))

# List Manipulation
print("=" * 50)
print(" List Manipulation")
print("=" * 50)

a = []  # 비어 있는 리스트는 a = list()로 생성할 수도 있다.
b = [1, 2, 3, 4, 5, 6, 7]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(type(a))

b = [1, 2, 3]
b.append([4, "123"])
print(b)

i = 0

del b[3]

print("#"*20)
print(d.__getitem__(2))


while i < len(b):
    print(b[i])
    i = i + 1

# 튜플
# 리스트와 같으나 값 수정이 되지 않는다.


# 딕셔너리
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# dict_keys, dict_values, dict_items

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

print(dic)
print(dic['name'])

a = {1: 'a'}
a[2] = 'b'
a['name'] = 'pey'
print(a)
del a['name']
print(a)

specialty = {"김연아": "피겨스케이팅", "류현진": "야구", "박지성": "축구", "귀도": "파이썬"}
print(specialty)

keys = list(specialty.keys())  # list가 없어도 된다.

for k in keys:
    print(k)

print(specialty.values())
print(specialty.items())
print(type(specialty))
# #set (집합)
# 중복을 허용하지 않는다.
# 순서가 없다(Unordered).
# ※ 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.
s2 = set("Hello")
print(s2)

b1 = True
b2 = False
print(type(b1))
print(b1)
print(1 == 1)
print(1 < 1)
print(1 < 2)

# 자료형의 참과 거짓
a = [1, 2, 3, 4]
while a:
    print(a.pop())

# others
i = 0


# for i in [0,2,3]:
def add(i):
    i = i + 1
    return i


while i < 3:
    i = add(i)
#    print(i)

# id 함수: 객체의 주소값 리턴.
a_addr = [2, 3]
b_addr = a_addr.copy();  # 변수 포인터 복사. 주소값 복사.
print("0x%x" % id(a_addr))
print("0x%x" % id(b_addr))

# a = [1,2,3]
a = "Something New"
b = a[1:]  # value만 복사
# b = a

b = (a + '.')[:-1]

print("0x%x" % id(a))
print("0x%x" % id(b))
# b[1] = 0
print(a, b)

c = [a, b] = ['python', 'life']
print(a)
print(b)
print(c)

c, b, a = a, b, c
print(a)
print(b)
print(c)

a = "a:b:c:d"
b = a.replace(":", "#")
print(a)
print(b)
print("0x%x" % id(a))
print("0x%x" % id(b))