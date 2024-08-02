# 실습1
rainbow =['red','orange','yellow','green','blue','indigo','purple']

print(rainbow[2])

rainbow.sort()
print(rainbow)

rainbow.append('skyblue')
print(rainbow)

del rainbow[3:7]
print(rainbow)

## tuple

t1 = (1,2,3)
t2 = (1,2,3,'가','나')

print(t1+t2)
print(t1 * 3)
print(t1[0])
print(t2[0:~3])


## set
s1 = {1,2,3}
s2 = set([1,3,5,7,9])
s3 = set('hello')

print(s1)
print(s2)
print(s3)

s3.remove('e')
print(s3)


s3.clear()
print(s3) # set() 출력, 빈셋

s3.update(["h","i"])
s3.update("bye")
s3.update(["bye"])
print(s3)

## dictionary
dict1 = {1:'a',2:'b',3:'c',4:'d'}
dict2 = {
    'name' : 'in',
    'age' : 20,
    'todo' : ['헬스장'],
    'hate' : ('조개'),
    () : "빈튜플",
    }

print(type(dict1))
print(dict1)
print(dict2)


print(dict1[1])
print(dict2["todo"])


print(dict1.get(1))
print(dict2.get('todo'))
print(dict1.get(5))

print(dict2.keys())
print(dict2.values())

for key in dict2.keys():
    print(key, end = ": ")
    print(dict2[key])

del dict1[1]
print(dict1)
dict1.clear()
print(dict1)

def capitalize(str):
    return str.upper()

print(capitalize('apple'))

list1 =['apple','banana', 'coconut']
set1 = set('banana')
tuple1 = ('a','b')

list2 = map(capitalize, list1)
set2 = map(capitalize, set1)
tuple2 = map(capitalize, tuple1)

print(list(list2))
print(set(set2))
print(tuple(tuple2))


# 실습 1. set 사용
#print("====실습 1 set 사용====")
#import sys
#input = sys.stdin.readline
#n,m = map(int,input().split())
#s1 = set()

#for i in range(n):
#    s1.add(input())

#count = 0
#for i in range(m):
#    word = input()
#    if word in s1:
#        count = count + 1

#print("s1에 포함되는 단어 개수 : ", count)
#print()


# 실습 2. 딕셔너리 사용
diction1 = {'Alice': 85, 'Bob' : 90, 'Charlie' : 95}
print(diction1)

# 학생 추가
diction1["David"] = 80
print(diction1)

# 학생 삭제
diction1.pop("Bob")
print(diction1)

# 학생 전체 출력
for student in diction1.keys():
    print(f"{student}의 점수는 {diction1.get(student)}")

