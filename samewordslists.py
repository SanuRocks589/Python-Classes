def input2(v):
    list = []
    counter = 0
    for word in v:
        if len(word)>1 and word[0] == word[-1]:
            counter+=1
            list.append(word)
    print(list)

result = input2(["apple","mom","sees","hello","bye"])
print(result)