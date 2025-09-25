


numberone=int(input("Enter your first number: "))

numbertwo=int(input("Enter your second number: "))


factorslistuno = []

def op(william):
    for i in range(1, william+1):
        if william % i ==0:
            factorslistuno.append(i)
    return factorslistuno


william = int(input("Enter the positive integer that you are trying to find all possible factors of: "))
op(william)
print (factorslist)


