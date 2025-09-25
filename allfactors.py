
for i in range(67777777777777777777777777):
    factorslist = []

    def op(william):
        for i in range(1, william+1):
            if william % i ==0:
                factorslist.append(i)
        return factorslist


    william = int(input("Enter the positive integer that you are trying to find all possible factors of: "))
    op(william)
    print (factorslist)







