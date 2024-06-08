'''
Assume a file containing a series of integers is named sum_nums.txt and exists on the computer's disk.
Write a program that calculates the average of all the numbers stored in the file
'''
'''
Modify the program that you wrote for Question 3 so it handles the following exceptions:
    It should handle any IOError exceptions that are raised when the file is opened and data is
    read from it.

    It should handle any ValueError exceptions that are raised when the items that are read
    from the file are converted to a number.
'''


total, line_count = 0, 0
try:
    with open("Tester_Text_Files/sum_nums.txt", "r") as file:
        for line in file:
            try:
                num = int(line)
                total += num
                line_count += 1
            except ValueError:
                print(f"Could not convert data to an integer: {line.strip()}")
    
    if line_count > 0:
        average = total / line_count
        print("Average:", average)
    else:
        print("No valid data to calculate average.")

except IOError:
    print('Error opening or read the file.')

