

action = input('>> ').split()

words = []
num = 0

for word in action:
    words += word
    num += 1

print(action, words, num)
