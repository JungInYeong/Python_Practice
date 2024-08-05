import numpy as np
import random
##x = np.array([3,1,2])
##print(x)
##type(x)
##
##a = [1, 2, 'a','b']
##b = np.array([1, 2, 'a','b'])
##print(a)
##print(b)
##
##list1 = [1, 3, 5]
##list2 = [2, 4, 6]
##
##li = list1 + list2
##print(li)
##
##ndarray1 = np.array([1, 3, 5])
##ndarray2 = np.array([2, 4, 6])
##
##nd = ndarray1 + ndarray2
##print(nd)


# 실습 모듈 사용

# 1. 10개의 0으로 채워진 array
arr1 = np.zeros((10))
print(arr1)

# 2. 5번째 값 1로 바꾸기
arr1[4] = 1
print(arr1)

# 3. 10부터 30까지 수로 이루어진 array

arr3 = np.arange(10,31)
print(arr3)

# 4. 0~99 난수 2x2 array
arr4 = np.random.randint(100, size=(2,2))
print(arr4)

# 5. 0~1 난수 2x4 array
arr5 = np.random.rand(2,4)
print(arr5)
print()

# 6. 35~74 순차적인 1차원배열 10x4 array
arr6 = np.arange(35,75)
arr6 = arr6.reshape(10,4)
print("6번",arr6)
print()
# 7. 6번 역순
arr7 = arr6[::-1]
print(arr7)

# 8. 6번 두번쨰행부터 마지막직전 행까지, 세번쨰 열부터 마지막열까지 슬라이싱
arr8 = arr6[1:9,2:4]
print(arr8)

# 9. 6번 마지막열 모든값 출력(1차원 배열)
arr9 = arr6[:,3]
print(arr9)

# 9-1 6번 마지막열 모든값 출력(2차원 배열)
arr9_1 = arr6[:,3:]
print(arr9_1)
print()

# 10. 9-1 역순
arr10 = arr9_1[::-1]

# 11. 1~50난수 5x6 배열, 짝수만 출력
arr11 = np.random.randint(1,51, size=(5,6))
arr11 = arr11[arr11%2 == 0]
print(arr11)
print(arr10)
