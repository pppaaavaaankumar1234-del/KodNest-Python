n=1345678
while n!=0:
    digit=n%10
    count=0
    for i in range(1,digit+1):
        if digit%i==0:
            count+=1
    if count==2:
        print(digit)
    n=n//10



