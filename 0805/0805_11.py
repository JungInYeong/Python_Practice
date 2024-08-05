import numpy as np

## 차원 확장
a = np.array([[1,2],[3,4]])
expanded = np.expand_dims(a,0)
print(expanded)
print(expanded.shape)


## 차원 축소
np_ones = np.ones((1,2,1,3))
print(np_ones)

squeezed = np.squeeze(np_ones,0)
print(squeezed)
print(squeezed.shape)


## 중복 제거
a = [1,2,2,3,3,4,4]

unique_a, indexes, counts = np.unique(a, return_counts=True, return_index=True)
print(unique_a, counts, indexes)

## 정렬
aa = np.array([1,4,2,3])
b = np.sort(aa)
print(f"a {aa}")
print(f"b {b}")

c=np.argsort(aa)
print(f"c {c}")
print(f"cc {aa[c]}")

aa.sort()
print(f"a {aa}")
print()
print()

# 실습
arr = [1,1,2,3,4,5,5,5,5,7,8,9,10,11,24,100]

# 중복 제거
unique_arr = np.unique(a)
print(f"중복제거 {unique_arr}")

# 1의 결과 최대,최수 평균값 출력
max_arr = np.max(unique_arr)
min_arr = np.min(unique_arr)
mean_arr = np.mean(unique_arr)
print(f"최대 {max_arr}")
print(f"최소 {min_arr}")
print(f"평균 {mean_arr}")

# 1의 모든 합 출력
sum_arr = np.sum(unique_arr)
print(f"합 {sum_arr}")

# 중복 제거하지 않은 배열의 중간값
median_arr = np.median(arr)
print(f"중간값 {median_arr}")
