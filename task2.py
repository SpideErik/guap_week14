from random import shuffle


def my_sort(x, y):
    for j in range(len(y)-1, 0, -1):
        for i in range(0, j):
            if y[i] > y[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                y[i], y[i+1] = y[i+1], y[i]


x = 'У лукоморья дуб зелёный Златая цепь на дубе том'.split()
y = list(range(len(x)))
shuffle(y)
print(x)
print(y)

my_sort(x, y)
print(x)
