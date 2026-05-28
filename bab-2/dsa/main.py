number_list = [2 , 9 , 22 ,80 , 99]

left_pointer = number_list[0]

for i in range(1 , len(number_list)):
    right_pointer = number_list[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer


print(left_pointer)