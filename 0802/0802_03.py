'''
def 함수이름(매개변수1, ...):
    함수내용
    함수내용
    return 함수의 반환값 # 생략가능
    #return을 이용하지 않는다면, 반환값 = None
여기는 함수밖
'''

#def add(a,b):
#    return a+b

#sum1 = add(1,2)
#print(sum1)

#def func1(*args):
#    print(args)
#    print("type : ",type(args))
#    for t in args:
#        print(t, end = " ")

#func1(1,2,3,4,5,6)
#print()

# factorial 구현
#def facloop(n):
#    mul = 1
#    for i in range(n):
#        mul = mul * (i+1)
#    return mul

#def factorial(n):
#    if n==0 or n==1:
#        return n
#    else:
#        return n * factorial(n-1)

#n! = n * n = (n-1)

#print(facloop(5))
#print(factorial(5))

# 실습1. 함수 & 스택(리스트)
#정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.







#import sys
#line = int(sys.stdin.readline())

#stack = []

#for i in range(line):
#    command = sys.stdin.readline()
#    stackCommand = command.split()
#    if stackCommand == "push":
#        number = command.split()
#        stack.append(number)
#    elif stackCommand == "pop": # 맨 나중에 들어간 요소 출력 / 아무것도 없으면 -1
#        if len(stack) > 0:
#            print(stack.pop()) # 꺼냄과 동시에 꺼낸 것 리턴
#        else:
#            print(-1)
#    elif stackCommand == "top":
#        if len(stack) > 0:
#            print(stack[-1]) # 꺼냄과 동시에 꺼낸 것 리턴
#        else:
#            print(-1)
#    elif stackCommand == "size":
#        # 스택의 크기 출력
#         print(len(stack))
#    elif stackCommand == "empty": 
#        # 비어있을 때는 1아니면 0 출력
#        if len(stack)==0:
#            print(1)
#        else:
#            print(0)
        

# 실습2. 재귀함수로 피보나치 수 구하기

def fibo_n(n):
    if n == 1 or n == 2:
        number = 1
    else:
        number = fibo_n(n-1) + fibo_n(n-2)
    return number
   
    
print(fibo_n())

