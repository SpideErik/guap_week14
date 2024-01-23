from random import shuffle


def my_switch(words):
    for i in range(len(words)):
        new_word = list(words[i])
        shuffle(new_word)
        words[i] = ''.join(new_word)


words = 'У лукоморья дуб зелёный Златая цепь на дубе том'.split()
print(words)
my_switch(words)
print(words)



