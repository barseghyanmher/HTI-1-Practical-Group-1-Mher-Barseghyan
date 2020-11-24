list1 = [input("Enter numbers with spaces and push 'Enter' :")]
intlst = [int(n) for n in list1[0].split()]
avg=[0]*len(intlst)
for i in range(len(intlst) - 1):
    avg[i]=(intlst[i] * intlst[i + 1])
maximum = max(avg)
print(maximum)