print([]) # 비어있는 리스트
print([1,2,3]) # 숫자가 들어있는 리스트
print(['a','b','c']) # 문자가 들어있는 리스트

number = [1,2,3,4,55,6]
print(number[3])

# 슬라이싱
shop = ["반바지","이어폰","키보드","청바지"]
print(shop[0])

print(shop[0:2])
print(shop[-1])

# 수정
shop[0] ="무지 반바지"
print(shop)

# 추가/삭제
li = ["a","b","v","d"]
li.append("e")
print(li)

li.remove("v")
print(li)

li.insert(2,"c")
print(li)

'''
if 조건식1:
    조건식1이 참일 때 실행될 문장
    반드시 탭 이후에 작성되어야 함
elif 조건식2:
    조건식2가 참일 때 실행될 문장
    else if와 같다.
else:
    조건1 and 조건2가 모두 거짓일 때 실행될 문장
'''

# 실습 5
num = input("숫자 여러 개 입력 > ")
stk = num.split()

for i in range(len(stk)):
    stk[i] = int(stk[i])
print(stk)

max_num = max(stk)
min_num = min(stk)

print("가장 큰 값 : ",max_num)
print("가장 작은 값 : ",min_num)

stk.remove(max_num)
stk.remove(min_num)

aver = sum(stk)/ len(stk)
print("나머지 값의 평균 : ",aver)
