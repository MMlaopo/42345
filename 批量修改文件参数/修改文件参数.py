import re

file_name = 'Self_Define_Functions.h'



parameter_1 = "const int Population_Size ="
parameter_2 = "const double mutation_probability"
parameter_3 = "const double crossover_probability"
# parameter_4 = "const double c2"

with open('file_path_GA.txt', 'r') as file:
    for line in file:
        line = line.rstrip()

        # 找出数字
        my_string = line
        result_list = []

        start_index = 0
        while True:
            start_index = my_string.find("=", start_index) + 1
            if start_index == 0:
                break
            end_index = my_string.find("/", start_index)
            if end_index == -1:
                end_index = len(my_string)
            word = my_string[start_index:end_index]
            result_list.append(word)
        print(result_list)
        final_path = line + '/' + file_name
        print(final_path)
        with open(final_path, "r") as file:
            lines = file.readlines()
        line_number = 0

        for code_line in lines:
            if parameter_1 in code_line:
                flag = line_number
                my_string = code_line
                new_string = re.sub(r'\d+', result_list[0], my_string)
                print(new_string)
                lines[flag] = new_string + '\n'

            if parameter_2 in code_line:
                flag = line_number
                my_string = code_line
                new_string = re.sub(r'\d+\.\d+', result_list[1], my_string)
                print(new_string)
                lines[flag] = new_string + '\n'

            if parameter_3 in code_line:
                flag = line_number
                my_string = code_line
                new_string = re.sub(r'\d+\.\d+', result_list[2], my_string)
                print(new_string)
                lines[flag] = new_string + '\n'

            # if parameter_4 in code_line:
            #     flag = line_number
            #     my_string = code_line
            #     new_string = re.sub(r'\d+\.\d+', result_list[3], my_string)
            #     print(new_string)
            #     lines[flag] = new_string + '\n'

            line_number = line_number + 1

        with open(final_path, 'w') as f:
            f.writelines(lines)




