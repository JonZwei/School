1print("Data 51100 - Fall 2022")
print("Jon Zweiacher")
print("Programming Assignment #1")

def user_input():
    num = input("Enter a positive number: ")
    num = int(num)
    return num

active = True
numbers = []
mean = variance = 0

while active:
    num = int(input("Enter a positive number: "))
    
    if num >= 0:
        numbers.append(num)
        sum_num = sum(numbers)
        len_num = len(numbers)
        
        if len_num > 1:    
            variance = (((len_num-2)/(len_num-1))*variance) + (pow((num - mean),2)/len_num)
        
        mean = mean + ((num-mean)/len_num)
        
        print("The mean is: " + str(mean))
        print("The variance is: " + str(variance))
    else:
        active = False

    