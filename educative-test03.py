def num_steps(str):
    bitList = list(str[::-1])
    steps = 0
    carryFwdOne = False
    for idx, bit in enumerate(bitList):

        if carryFwdOne and bit == '0':
            bit = '1'
            carryFwdOne = False
        if carryFwdOne and bit == '1':
            bit = '0'
            carryFwdOne = True
        if idx==(len(bitList)-1) and bit == '1':
            continue

        if bit == '1':
            carryFwdOne = True
            steps = steps + 2
        else:
            steps = steps + 1

    return steps

print(num_steps("1011"))
print(num_steps("100"))
print(num_steps("111"))
print(num_steps("1"))

def EdSOL_num_steps(str):
    length = len(str)

    steps = 0
    c = 0
    for i in range(length - 1, 0, -1):
        digit = int(str[i]) + c
        if digit % 2 == 1:
            steps += 2
            c = 1
        else:
            steps += 1

    return steps + c