# 실습1
import random
#n = random.randint(1,100)
#print(n)

#n_list = []

#for i in range(4):
#    n = random.randint(1,100)
#    n_list.append(n)

#n_list.sort()

#for idx in n_list:
#    print(idx)



# 실습2(숫자 맞추기게임)

#while(True):
#    num = random.randint(1, 10)
#    num2 = int(input("숫자를 맞춰보세요 : "))
#    
#    if num2 == num:
#        print(f"맞았어요! 랜덤 숫자는 {num}입니다")
#        break
#    else:
#        print("땡!")
#        continue


# 실습3(로또 번호 뽑기)

n = 0
n_list = []

while len(n_list) < 6:
    n = random.randint(1,45)
    dupl = False
    for i in n_list:
        if i == n:
            dupl = True
            break
    if dupl == False:
        n_list.append(n)    
        
n_list.sort()
print(n_list)    
