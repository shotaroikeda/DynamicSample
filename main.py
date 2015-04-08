##################################################################################
#
# CS 196 Dynamic Programming Example
# 
# Given the Following Denominations:
# Dollar = 100 cents
# Quarter = 25 cents
# Dime = 10 cents
# Nickel = 5 cents
# Penny = 1 cent
#
# Find the number of ways to make changes for n cents using dynamic programming.
##################################################################################
dollar = 100
quarter = 25
dime = 10
nickel = 5
penny = 1

# Dummy hack to make sure file is created
dummy = open('saved.txt', 'w')
dummy.close()

# Main starts here
# Creates a file to save our data in. It is read at runtime
saved_file = open('saved.txt' , 'w+b')
saved_data = saved_file.readline()
# Create the list, or read the data
if saved_data == "":
    saved_data = [0]*100
else:
    saved_data = eval(saved_data)

def money_possibility(money):
    # Make the list bigger to account for more numbers
    if money > len(saved_data):
        saved_data.extend([0]*100)

    # Return 0 if the money = 0.
    if money == 0:
        return 0
    elif money < 0:
        raise ValueError('You can\'t get change for negative amounts!')
    elif saved_data[money] > 0:
        return saved_data[money]
    # Calculations for when data does not exist...
    else:
        if (money // dollar) > 0:
            money_new = money % dollar
            saved_data[money] += 1 + money_possibility(money_new)
        if (money // quarter) > 0:
            money_new = money % quarter 
            saved_data[money] += 1 + money_possibility(money_new)
        if (money // dime) > 0:
            money_new = money % dime
            saved_data[money] += 1 + money_possibility(money_new)
        if (money // nickel) > 0:
            money_new = money % nickel 
            saved_data[money] += 1 + money_possibility(money_new)
        if (money // penny) > 0:
            money_new = money % penny
            saved_data[money] += 1 + money_possibility(money_new)

        return saved_data[money]

def write_to_save():
    # Written separately to be able to calculate more amounts of money
    saved_file.write(str(saved_data))
    saved_file.close()


if __name__ == '__main__':
    money_possibility(1)
    money_possibility(5)
    money_possibility(25)
    write_to_save()
