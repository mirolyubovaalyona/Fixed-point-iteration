import numpy as np


n = int(input('Количество неизвестных: '))
k = int(input('Количество итераций: '))

a = np.zeros((n,n))
b = np.zeros(n)

a= [[20, 2, 3, 7],
[1, 12, -2, -5],
[5, -3, 13, 0],
[0, 0, -3, 15]]

b=[5, 4, -3, 7]

#for i in range(n):
#   for j in range(n):
#        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
#
#for i in range(n):
#        b[i] = float(input( 'b['+str(i)+']='))


def f(n, a, b, k):
    x = np.zeros(n)
    xx=x

    for i in range(k):
        for j in range(n):
            xx[j]=b[j]
            for l in range(j):
                xx[j]-=x[l]*a[j][l]
            for l in range(j+1, n):
                xx[j]-=x[l]*a[j][l]
            xx[j]=xx[j]/a[j][j]
            x=xx
        print(x)
    
        
    return x

x=f(n, np.array(a), np.array(b), k)

# Displaying solution
print('Теперь известные элементы: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
print('\n')
print(np.linalg.solve(a, b))

