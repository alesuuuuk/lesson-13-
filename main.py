if __name__ == "__main__":
    ### task 1
    name = input("Введіть своє ім'я")

    flag = True
    # while True:
    #     try:
    #         age = int(input("Введіть свій вік"))
    #         if age < 0:
    #             print("Вік не може бути від'ємним числом, спробуйте ще раз!")
    #         elif age > 130:
    #             print("Люди стільки не живуть, введіть ще раз!")
    #         else:
    #             print(f"Привіт, {name}! Твій вік — {age}")
    #             break
    #     except ValueError as arr:
    #         print("Вводити можна лице цифри, спробуйте ще раз!")

    ### task 2

    # first version

    # def format_name_age_first_version(name_user, age_user):
    #     return f"Привіт, {name_user}! Твій вік — {age_user}"
    #
    #
    # while True:
    #     try:
    #         age = int(input("Введіть свій вік"))
    #         if age < 0:
    #             print("Вік не може бути від'ємним числом, спробуйте ще раз!")
    #         elif age > 130:
    #             print("Люди стільки не живуть, введіть ще раз!")
    #         else:
    #             print(format_name_age_first_version(name, age))
    #             break
    #     except ValueError as arr:
    #         print("Вводити можна лице цифри, спробуйте ще раз!")

    # second version
    # def format_name_age_second_version(name_user, age_user):
    #     if age < 0:
    #         return "Вік не може бути від'ємним числом, спробуйте ще раз!"
    #     elif age > 130:
    #         return "Люди стільки не живуть, введіть ще раз!"
    #     else:
    #         return f"Привіт, {name_user}! Твій вік — {age_user}"
    #
    #
    # while True:
    #     try:
    #         age = int(input("Введіть свій вік: "))
    #         result = format_name_age_second_version(name, age)
    #         print(result)
    #         if f"Привіт, {name}! Твій вік — {age}" in result:
    #             break
    #     except ValueError:
    #         print("Вводити можна лише цифри, спробуйте ще раз!")

    ### task 3
    numbers = [-35, 40, 90, -21, -1, 32]

    while flag:
        try:
            temp_num = int(input("Введіть число"))
            choice = input("Чи бажаєте ви додавати числа далі: n - ні, усі решта відповідей зароховуються як так ")
            if choice == "n":
                numbers.append(temp_num)
                flag = False
                for i, num in enumerate(numbers):
                    if num < 0:
                        numbers[i] = abs(num)
                nums_sum = 0
                for i in numbers:
                    nums_sum += i

                print(nums_sum)
            else:
                numbers.append(temp_num)
        except ValueError:
            print("Вводити можна лише цифри!!!")


    ### task 4

    ### version 1
    # def sum_numbers_first_version(nums_arr):
    #     nums_sum = 0
    #     for i in nums_arr:
    #         nums_sum += i
    #     return nums_sum
    #
    # while flag:
    #     try:
    #         temp_num = int(input("Введіть число"))
    #         choice = input("Чи бажаєте ви додавати числа далі: n - ні, усі решта відповідей зароховуються як так ")
    #         if choice == "n":
    #             numbers.append(temp_num)
    #             flag = False
    #             for i, num in enumerate(numbers):
    #                 if num < 0:
    #                     numbers[i] = abs(num)
    #             print(sum_numbers_first_version(numbers))
    #         else:
    #             numbers.append(temp_num)
    #     except ValueError:
    #         print("Вводити можна лише цифри!!!")
    #
    #
    # # second version
    #
    # def sum_numbers_second_version(nums_arr):
    #     nums_sum = 0
    #     for i in nums_arr:
    #         if i <0:
    #             i *= -1
    #             nums_sum += i
    #         else:
    #             nums_sum += i
    #     return nums_sum
    # print("Введіть додатнє число, а після закінчення ведень усіx чисел - я вам виведу їхню суму"
    #                              "(вводити можна лише додатні числа, у разі якщо буде від'ємне число - я візьму його модуть і заміню його)  ")
    # while flag:
    #     try:
    #         temp_num = int(input("Введіть число"))
    #         choice = input("Чи бажаєте ви додавати числа далі: n - ні, усі решта відповідей зароховуються як так ")
    #         if choice == "n":
    #             numbers.append(temp_num)
    #             flag = False
    #             print(sum_numbers_second_version(numbers))
    #         else:
    #             numbers.append(temp_num)
    #     except ValueError:
    #         print("Вводити можна лише цифри!!!")
