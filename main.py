# Loops - while loop

# print nos 1 to 6

i = 1
while i < 7:
    print(i)  # 1, 2, 3,   6
    i = i + 1


# break
i = 1
while i < 7:
    if i == 3:
        break
    print(i)  # 1, 2, 3,   6
    i = i + 1

# continue
i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)

# else
i = 1
while i < 7:
    # if i == 3:
    #     break
    print(i)
    i = i + 1
else:
    print('while completed successfully.')
