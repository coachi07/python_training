# loop the set list number and add them together
# check if the current value of sum is greater than 70 stop
listofnumbers=[2,34,56,67,8,9,23,90,57]

sum=0
finaltotal=0
for i in listofnumbers:
    sum=sum +i
    print(sum)
    if sum >=92:
        finaltotal=sum+5
        print(finaltotal)
        finaltotal=finaltotal-20
        print(finaltotal)
        break


 
