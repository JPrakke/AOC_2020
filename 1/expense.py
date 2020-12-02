import os

input = os.path.join('input', 'input.txt')
input_list = []

with open(input , 'r') as reader:
    for line in reader.readlines():
        input_list.append(line)

def challenge_1(input_list):
    for i in range(len(input_list)):
        for j in range (len(input_list)):
            if int(input_list[i]) + int(input_list[j]) == 2020:
                print(int(input_list[i]) * int(input_list[j]))

def challenge_2(input_list):
    for i in range(len(input_list)):
        for j in range (len(input_list)):
            for ji in range (len(input_list)):
                if int(input_list[i]) + int(input_list[j]) + int(input_list[ji]) == 2020:
                    print(int(input_list[i]) * int(input_list[j]) * int(input_list[ji]))

challenge_1(input_list)