import random

code_list = []
for i in range(6):
    state = random.randint(1, 3)
    if state == 1:
        first_kind = random.randint(65, 90)
        random_uppercase = chr(first_kind)
        code_list.append(random_uppercase)
    elif state == 2:
        second_kinds = random.randint(97, 122)
        random_lowercase = chr(second_kinds)
        code_list.append(random_lowercase)
    elif state == 3:
        third_kinds = random.randint(0, 9)
        code_list.append(str(third_kinds))
verification_code = ''.join(code_list)
print(verification_code)
