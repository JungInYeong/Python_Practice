# 실습1(회원 명부 작성)
##f = open("./member.txt","w")
##
##n_list = []
##
##for i in range(3):
##    id, pw = input("이름 비밀번호 입력 : ").split()
##    n_list.append([id, pw])
##
##print(n_list[1])

# 실습2(회원 명부를 이용한 로그인 기능)

##name = input("이름을 입력하세요 : ")
##pw = input("비밀번호를 입력하세요 : ")
##
##format = f"id:{name}/ pw:{pw}\n"
##
##fRead = open("./member.txt","r")
##fRead.seek(0)
##
##userList = fRead.readlines()
###print(userList)
###print(format)
##
##if format not in userList:
##    print("로그인 실패")
##else:
##    print("로그인 성공")
