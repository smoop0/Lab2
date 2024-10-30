
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)


def display_main_menu():
    print("display_main_menu")
    print(5, 67, 32)

def calc_average(inputList):
    print("calc_average")
    total = sum(inputList)
    calcAvg = sum / len(inputList)
    print("Average =" + calcAvg)
    return calcAvg

def get_user_input():
    print("get_user_input")
    user_input = input()
    userSplit = user_input.split(",")

    convertedList = []    
    for item in userSplit:
        convertedItem = float(item)
        convertedList.append(convertedItem)
    return convertedList

def find_min_max(inputList):
    print("find_min_max")
    inputList.sort() #affects original list
    resultList = [inputList[0], inputList[-1]] 
    # Use "-1" to select the last element in a list
    print("Min & Max list = " + resultList)
    return resultList

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("calc_median_temperature")





if __name__ == "__main__":
    main()

