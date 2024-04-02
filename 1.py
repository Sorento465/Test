s = input()
counter = 0
for word in s.split('$'):
    if len(set('aeiou') & set(word)):
        counter += 1
print(counter)
