def add(a, b):
    result = a + b
    return result



a = add(3, 4)
print(a)



# def 함수이름(*매개변수):
#     <수행할 문장>
#     ...

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result


result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

# 키워드 파라미터 kwargs
# 이번에는 키워드 파라미터에 대해 알아보자. 키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙인다.

def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(a=1,b="2323")



def add_and_mul(a,b):
    return a+b, a*b

result1,result2 = add_and_mul(3,4)
result = add_and_mul(3,4)
print (result1, result2)
print (result)


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("ted kim",30)


# vartest.py
a = 1

def vartest(a):
    a = a +1
    print("vartest() print %d" % a)


vartest(a)
print(a)


# lambda
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.
# 우리말로는 "람다"라고 읽고 def를 사용해야 할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
# 사용법은 다음과 같다.
#
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
#
# ※ lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

add = lambda a, b: a+b
result = add(3, 4)
print(result)



# input의 사용
a = input()

print("output : %s" % a)

number = input("숫자를 입력하세요: ")

print("output : %d" % int(number))



f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

f2 = open("foo.txt", 'w')
f2.write("Life is too short, you need python")
f2.close()



