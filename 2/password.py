import os

input_file = os.path.join('input', 'input.txt')
passwords = []
rules = []

def input_parser(input_file):
    input_list = []
    with open(input_file, 'r') as reader:
        for line in reader.readlines():
            input_list.append(line)
    for i in input_list:
        input_split = i.split(': ')
        pwd_parse = input_split[1].replace('\n', '')
        passwords.append(pwd_parse)
        rule_split = input_split[0].split('-')
        rule_split_2 = rule_split[1].split(' ')
        min_rule = rule_split[0]
        max_rule = rule_split_2[0]
        letter_rule = rule_split_2[1]    
        rules.append([min_rule, max_rule, letter_rule])

def challenge_1(passwords, rules):
    correct_passwords = 0
    incorrect_passwords = 0
    input_parser(input_file)
    for i in range(len(passwords)):
        letter_ct = 0
        for letter in passwords[i]:
            if letter == rules[i][2]:
                letter_ct += 1
        if letter_ct >= int(rules[i][0]) and letter_ct <= int(rules[i][1]):
            correct_passwords += 1
        else:
            incorrect_passwords += 1
    print(f''' 
        correct: {correct_passwords}
        incorrect: {incorrect_passwords}    
    ''')

challenge_1(passwords, rules)