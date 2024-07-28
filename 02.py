IdNpw=((1001,'DoGoD'),(1037,'CaTaC'),(1263,'GolD'),(2401,'Vicky$'))

print("Availabe Ids Are :")
for i in IdNpw:
    print(i[0])

print("Enter Id,PassWord and New Password ")
id=int(input())
pword=input()
npword=input()

IdNpw=list(IdNpw)
for i in range(len(IdNpw)):
    if IdNpw[i][0]==id and IdNpw[i][1]==pword:
        IdNpw[i]=list(IdNpw[i])
        IdNpw[i][1]=npword
        IdNpw[i]=tuple(IdNpw[i])

print(tuple(IdNpw))