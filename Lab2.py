from statistics import median

def main():
    print("ET0735 - (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    my_list = get_user_input()
    calc_average_temperature(my_list)
    calc_min_max_temperature(my_list)
    calc_median_temperature(my_list)

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32): ")

def calc_average_temperature(list):
    sum = 0
    for i in list:
        sum += i
    avg = sum/len(list)
    print("The average temperature is: " + str(avg))

def get_user_input():
    list = input().split(",")
    for i in range(0, len(list)):
        list[i] = float(list[i])
        print(i)
    print(list)
    return list

def calc_min_max_temperature(list):
    max = list[0]
    min = list[0]
    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i
    max_min_list = []
    max_min_list.append(max)
    max_min_list.append(min)
    print("The max and min temperatures are: " + str(max_min_list))
    return max_min_list
def sort_temperature():
    print("hi")
def calc_median_temperature(list):
    print("The median of the temparatures is: " + str(median(list)))

if __name__ == "__main__":
    main()