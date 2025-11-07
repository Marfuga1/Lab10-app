import timeit

toto = '''
x = [1, 7, 1]
sum = 0
for i in range(3):
    x.append(x[i-1] + x[i-3])
for i in range(len(x)):
    c = float(x[i]) / (2**i)
    sum = sum + c
'''

print(timeit.Timer(setup=toto).repeat(8))
