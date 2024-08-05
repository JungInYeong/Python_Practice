#1. 세개 변수 입력받고 가장 큰 변수 반환 함수 (max사용 안됨)

##a,b,c = map(int, input("세 개 변수 입력 : ").split())
##n_list = [a,b,c]
##
##n_max = 0
##
##for num in n_list:
##    if num > n_max:
##        n_max = num
##
##print(n_max)


#2. 피보나치
##
##n = int(input("몇개의 피보나치 수열 : "))
##
##def fibo(n):
##    if n<=2:
##        number = 1
##    else:
##        number = fibo(n-1)+fibo(n-2)
##    return number
##
##print([fibo(n) for n in range(1,n+1)])

# 3. 요소 검색

##num = int(input("숫자 목록 입력 : "))
##
##def find(order_list, element):
##    for ele in order_list:
##        if ele == element:
##            return True
##    return False
##
##list1 = [1,2,3,4,5]
##print(find(list1, 5))
##print(find(list1, 2))
##print(find(list1, 1))
##print(find(list1, 6))

# 4. 요소검색(어려움)

# 5. 소와 황소 게임

# 6. 문자열 팰린드롬(앞으로 읽은 것과, 뒤에서 읽은 것이 같은 문자열, ex)토마토..)
##word = input("검사할 단어 입력 : ")
##reverse = word[::-1]
##
##if word == reverse:
##    print("팰린드롬 문자열 입니다")
##else:
##    print("팰리드롬 문자열이 아닙니다")


# 7. 비밀번호 생성기
import string as st
import random

def pw(size):
    password = st.ascii_letters + st.digits + st.punctuation
    list =[]
    for _ in range(size):
        list.append(random.choice(password))
    return ''.join(list)

length = int(input("몇 글자 비밀번호 작성 : "))
pword = pw(length)
print(pword)

