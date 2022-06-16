# if 조건문:
#     수행할 문장1
#     수행할 문장2
# else:
#     수행할 문장A
#     수행할 문장B
# and, or, not
# x in s, x not in s
# x or y    x와 y 둘중에 하나만 참이어도 참이다
# x and y   x와 y 모두 참이어야 참이다
# not x x가 거짓이면 참이다

print("=" * 50)
print("조건문")
print("=" * 50)

money = a = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라2")
else:
    print("걸어가라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라3")
elif card:
    print("택시를 타고 가라4")
else:
    print("걸어가라")

# while <조건문>:
#     <수행할 문장1>
#     <수행할 문장2>
#     <수행할 문장3>
# and, or, not
# x in s, x not in s
# x or y    x와 y 둘중에 하나만 참이어도 참이다
# x and y   x와 y 모두 참이어야 참이다
# not x x가 거짓이면 참이다

print("=" * 50)
print("조건문")
print("=" * 50)

treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")

# break
# continue

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break  # break#break#break#break
    else:
        continue  # 없어도 되지만 키워드 익히기 위해 써봄.

# for
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# for문과 함께 자주 사용하는 range 함수
marks = [90, 25, 67, 45, 80]
print(len(marks))
print(range(len(marks)))

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))

for i in range(2, 10):  # 1번 for문
    for j in range(1, 10):  # 2번 for문
        # print(i*j, " ")
        print(i * j, end="  ")  # end
    print('')

# 리스트 안에 for문을 포함하는 리스트 내포(List comprehension)를 사용
# [표현식 for 항목 in 반복가능객체 if 조건문]  -- 조건문 생략가능.

# [1,2,3,4] 중에서 짝수에만 3을 곱하여 담고 싶다면 다음과 같이 리스트 내포 안에 "if 조건"을 사용할 수 있다.
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# for문을 2개 이상 사용하는 것도 가능
# [표현식 for 항목1 in 반복가능객체1 if 조건문1
#         for 항목2 in 반복가능객체2 if 조건문2
#         ...
#         for 항목n in 반복가능객체n if 조건문n]
result = [x * y for x in range(2, 10)
          for y in range(1, 10)]  # if y%2 ==0  조건 넣을 때 의도했던 대로 안나옴.
print(result)