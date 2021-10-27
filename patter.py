N = int(input("Masukkan bilangan: "))
print("Pola yang terbentuk:")

for i in range (2*N):
    if i >= N:
        y = i-N
        i -= 2*y+1
        for j in range(2*N):
            if j >= N:
                z = j-N
                j -= 2*z+1
                if j < i:
                    print(j%10, end='')
                else:
                    print(i%10, end='')
            else:
                if j < i:
                    print(j%10, end='')
                else:
                    print(i%10, end='')
    else:
        for j in range(2*N):
            if j >= N:
                z = j-N
                j -= 2*z+1
                if j < i:
                    print(j%10, end='')
                else:
                    print(i%10, end='')
            else:
                if j < i:
                    print(j%10, end='')
                else:
                    print(i%10, end='')
    print('', end='\n')
