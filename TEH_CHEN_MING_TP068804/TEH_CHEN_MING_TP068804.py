#Teh Chen Ming
#TP068804


# This function will show three selection for user

def Choose_user():
    print("=============Welcome to FRESHCO Sdn Bhd==============")
    while True:
        print("1. Admin \n2. New Customer\n3. Registered Customer")
        selection = input("Choose your selection(1,2,3):")
        if selection in ["1", "2", "3"]:
            return selection
        else:
            end()
        print("Please only choose option 1,2,3")
        continue


# function to check is digit
def is_int(num):
    try:
        num = int(num)
        return True
    except:
        return False


# function to check is float
def is_flt(num):
    try:
        num = float(num)
        return True
    except:
        return False


# This function will let the admin choose the selection once he pass the login section.
def admin_login():
    print("Please enter the name and password")
    f = open("admin.txt", 'r')
    x = f.read()
    line = x.split('|')
    f.close()
    for i in [1, 2, 3, 4]:
        if i == 4:
            print("You have lost all your attempts")
            main()
        else:
            admin_name = input("name:")
            admin_ps = input("password:")
            if admin_name == line[0] and admin_ps == line[1]:
                print('Welcome!,' + admin_name)
                return
            else:
                print("Try again")
                continue


# This function will let admin choose the function
def admin_UI():
    while True:
        print("==================================================")
        print("1. Upload groceries detail into system.")
        print("2. View all uploaded groceries.")
        print("3. Delete groceries.")
        print("4. Update/modify groceries information.")
        print("5. Delete groceries information.")
        print("6. Search specific groceries detail.")
        print("7. View all order of customers.")
        print("8. Search order of specific customer.")
        print("9. Back to Main page.")
        print("10. Exit")
        admin_selection = input("Choose your selection(1 to 10):")
        if admin_selection in ['1', '2', '3', '4', '5', '6', '7', '8', '9','10']:
            return admin_selection
        else:
            print("Please only choose 1 to 10")
            continue


# This function is for the new user.
def new_user_UI():
    while True:
        print("==================================================")
        print("1. View all groceries detail.")
        print("2. Registration.")
        print("3. Back to main page.")
        print("4. Exit.")
        new_user_selection = input("Choose your selection(1 to 4):")
        if new_user_selection in ['1', '2', '3', '4']:
            return new_user_selection
        else:
            print("Please only choose 1 to 4")
            continue


# This function is for the user.
def user_UI():
    while True:
        print("==================================================")
        print("1. View all groceries detail.")
        print("2. Place order of groceries and do payment.")
        print("3. View own order.")
        print("4. Delete order.")
        print("5. View personal information.")
        print("6. Back to main page.")
        print("7. Exit.")
        user_selection = input("Choose your selection(1 to 7):")
        if user_selection in ['1', '2', '3', '4', '5', '6', '7']:
            return user_selection
        else:
            print("Please only choose(1 to 7)")
            continue


# This function is to upload Groceries detail into system
def upload():
    print("==================================================")
    print("Hi admin, please do not enter any '|' symbol when entering the item info")
    name_list = []
    fhand = open('grocery_list.txt', 'r')
    for lines in fhand:
        item_list = lines.split('|')
        name_list.append(item_list[0])
    while True:
        new_item = input("Please enter the new grocery item you want to add:")
        if new_item not in name_list and '|' not in new_item:
            break
        else:
            print("Item name is existed or you have entered a '|', please enter other item name")
    fhand.close()
    print("Please enter item's expired date")
    expired_date = calendar()
    while True:
        quantity = input("enter the quantity you want to add:")
        if is_int(quantity) and int(quantity) > 0:
            quantity = str(quantity)
            break
        else:
            print("Please only enter an actual number")
            continue
    while True:
        price = input("Enter the price(Only number):")
        if is_flt(price) and float(price) >= 0.10:
            price = float(price)
            price = "{:.2f}".format(price)
            break
        else:
            print("Please only enter an actual price")
            continue

    while True:
        specification = input("Enter the specification for this item:")
        if '|' not in specification:
            break
        else:
            print("You have entered '|'")
            continue

    print("====================================")
    print("Please confirm your item info")
    print("Name:" + new_item)
    print("Expired date:" + expired_date)
    print("Quantity:" + quantity)
    print("Price:RM" + price)
    print("Specification:" + specification)
    print("====================================")

    while True:
        ans = input("Save it?\nEnter y or n(y is yes and n is no):")
        if ans in ['y', 'n']:
            if ans == 'y':
                fhand = open("grocery_list.txt", 'a')
                fhand.write("\n" + new_item + "|" + expired_date + "|" + quantity + "|RM" + price + "|" + specification)
                fhand.close()
                return
            else:
                print("We have deleted the info")
                return
        else:
            print("Please only enter y or n(y is yes and n is no)")


# This function is to show all customer order
def show_customer():
    print("==================================================")
    print("The current order list:")
    initial_list = []
    final_list = []
    i = 1
    f = open('customer_order.txt', 'r')
    for lines in f:
        initial_list.append(lines)
    for item in initial_list:
        item_info = item.split('|')
        print(str(i) + ') Name:' + item_info[0])
        print('Item:' + item_info[1])
        print('Quantity:' + item_info[2])
        final_list.append(item_info)
        i += 1
    f.close()
    return final_list


# This function is to show all item.
def show_item():
    print("==================================================")
    print("The current list we are selling:")
    initial_list = []
    final_list = []
    i = 1
    f = open('grocery_list.txt', 'r')
    for lines in f:
        initial_list.append(lines)
    for item in initial_list:
        item_info = item.split('|')
        print(str(i) + ') Name:', item_info[0])
        print('Expired Date:', item_info[1])
        print('Quantity:', item_info[2])
        print('Price:', item_info[3])
        print('Specification:', item_info[4])
        final_list.append(item_info)
        i += 1
    f.close()
    return final_list


# This function is to update/modify Groceries information
def modify_info():
    # Display item list
    final_list = show_item()
    # Choose the item wanted to change
    while True:
        print("========================================================")
        selection = input("Please enter the item you want to update:")
        if is_int(selection):
            selection = int(selection) - 1
        else:
            print("Please enter a valid number")
            continue
        if selection < len(final_list) and selection >= 0:
            break
        else:
            print("Try again")
            continue

    # This function is to choose the info wanted to change
    while True:
        info = input("Which info you want to change?\n1.Name\n2.Expired Date\n"
                     "3.Quantity\n4.Price\n5.Specification\nChoice:")
        if is_int(info):
            info = int(info) - 1
        else:
            print("Please enter a valid number")
            continue
        if info <= 4 and info >= 0:
            break
        else:
            print("Invalid input")
            continue

    while True:
        # for change name
        if info == 0:
            change = input("Enter your new item's name:")
            if '|' not in change:
                break
            else:
                print("Do not enter '|' in the item's name")
                continue
        # for change date
        elif info == 1:
            change = calendar()
            break
        # for change quantity
        elif info == 2:
            change = input("Enter your new quantity:")
            if is_int(change):
                change = int(change)
            else:
                print("Please enter a valid number")
                continue
            if change >= 0:
                break
            else:
                print("Please enter a positive number")
                continue
        # for change price
        elif info == 3:
            change = input("Enter your new price:")
            if is_flt(change):
                change = float(change)
            else:
                print("Please enter a valid price")
                continue
            if change > 0:
                change = "{:.2f}".format(change)
                change = 'RM' + str(change)
                break
            else:
                print("Please enter a positive number")
                continue
        elif info == 4:
            change = input("Enter your new specification:")
            if '|' not in change:
                break
            else:
                print("Do not enter '|' in the specification")
                continue

    final_list[selection][info] = str(change)

    print("===========================================")
    print("This is the result after changed")
    print("Name:" + final_list[selection][0])
    print("Expired date:" + final_list[selection][1])
    print("Quantity:" + final_list[selection][2])
    print("Price:" + final_list[selection][3])
    print("Specification:" + final_list[selection][4])
    print("============================================")

    while True:
        ans = input("Save it?\nEnter y or n(y is yes and n is no):")
        if ans in ['y', 'n']:
            if ans == 'y':
                f = open("grocery_list.txt", 'w')
                for i in final_list:
                    f.write(i[0])
                    f.write('|')
                    f.write(i[1])
                    f.write('|')
                    f.write(i[2])
                    f.write('|')
                    f.write(i[3])
                    f.write('|')
                    f.write(i[4])
                f.close()
                break
            else:
                print("We have wiped out the update")
                break
        else:
            print("Please only enter y or n(y is yes and n is no)")


# This function is to delete grocery info
def dlt_info():
    # show the list
    final_list = show_item()
    # for choosing item to dlt
    while True:
        print("========================================================")
        selection = input("Please enter the item you want to delete:")
        if is_int(selection):
            selection = int(selection) - 1
        else:
            print("Please enter a valid number")
            continue
        if selection < len(final_list) and selection >= 0:
            break
        else:
            print("Invalid input")
            continue
    # for choosing info to delete
    while True:
        info = input("Which info you want to delete?\n1.Name\n2.Expired Date\n"
                     "3.Quantity\n4.Price\n5.Specification\nchoice:")
        if is_int(info):
            info = int(info) - 1
        else:
            print("Please enter a valid number")
            continue
        if info <= 4 and info >= 0:
            break
        else:
            print("Invalid input")
            continue
    # for dlt and overwrite the txt
    final_list[selection][info] = 'blank'

    print("================")
    print("This is the result after changed")
    print("Name:" + final_list[selection][0])
    print("Expired date:" + final_list[selection][1])
    print("Quantity:" + final_list[selection][2])
    print("Price:" + final_list[selection][3])
    print("Specification:" + final_list[selection][4])
    print("================")

    while True:
        ans = input("Save it?\nEnter y or n(y is yes and n is no):")
        if ans in ['y', 'n']:
            if ans == 'y':
                f = open('grocery_list.txt', 'w')
                for i in final_list:
                    f.write(i[0])
                    f.write('|')
                    f.write(i[1])
                    f.write('|')
                    f.write(i[2])
                    f.write('|')
                    f.write(i[3])
                    f.write('|')
                    f.write(i[4])
                f.close()
                break
            else:
                print("We have deleted the update")
                break
        else:
            print("Please only enter y or n(y is yes and n is no)")


# This function is to find specific item
def find_specific_item():
    print("====================================================")
    print("The current list:")
    initial_list = []
    final_list = []
    i = 1
    f = open('grocery_list.txt', 'r')
    for lines in f:
        initial_list.append(lines)
    for item in initial_list:
        item_info = item.split('|')
        print(str(i) + ') Name:' + item_info[0])
        final_list.append(item_info)
        i += 1
    f.close()
    while True:
        selection = input("which specific item you want to check\nchoose your number example 1/2/3:")
        if is_int(selection):
            selection = int(selection) - 1
            if selection >= 0 and selection <= len(final_list) - 1:
                item_showing = final_list[selection]
                print("====================================================")
                print('Name:', item_showing[0])
                print('Expired Date:', item_showing[1])
                print('Quantity:', item_showing[2])
                print('Price:', item_showing[3])
                print('Specification:', item_showing[4])
                break
            else:
                print("Please enter a valid number")
                continue
        else:
            print("Please enter a number")
            continue


# This function will end the code
def end():
    print("==================================================")
    while True:
        result = input("Do you want to exit?\n type y if want to exit or n to return:")
        if result in ['y', 'n']:
            if result == 'y':
                print("Please come again!")
                exit()
            if result == 'n':
                return
        else:
            print("Please only enter y or n")


# This function is to make the date
def calendar():
    # Year
    while True:
        bhd_year = input("Enter the year\n example: 2008,2018,2022:")
        if is_int(bhd_year):
            if int(bhd_year) in range(1800, 2030):
                break
            else:
                print("Invalid year")
                continue
        else:
            print("Please enter an actual year")
    bhd_year = int(bhd_year)
    # Month
    while True:
        bhd_month = input("Enter the month\n example: 02,09,12:")
        if bhd_month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            break
        else:
            print("Please enter an actual month")
            continue
    # Date
    while True:
        bhd_date = input("Enter the date\n example: 08,18,28:")
        if bhd_date in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:

            if bhd_month == '02' and bhd_year % 4 == 0:
                if bhd_date in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14','15',
                                '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29']:
                    break
                else:
                    print("Please enter an actual date")
                    continue
            elif bhd_month == '02' and bhd_year % 4 != 0:
                if bhd_date in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                                '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28']:
                    break
                else:
                    print("Please enter an actual date")
                    continue

            elif bhd_month in ['01', '03', '05', '07', '08', '10', '12']:
                if bhd_date in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14',
                                '15', '16', '17',
                                '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:
                    break
                else:
                    print("Please enter an actual date")
                    continue
            elif bhd_date in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
                              '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']:
                break
            else:
                print("Please enter an actual date")
                continue

        else:
            print("Please enter an actual date")
            continue

    bhd = str(bhd_date) + '/' + str(bhd_month) + '/' + str(bhd_year)
    return bhd


# This function is fo registration.
def register():
    print("==================================================")
    name_list = []
    print("Hi user, please do not enter any '|' symbol when entering your personal info")
    f = open("user.txt", 'r')
    for lines in f:
        item_list = lines.split('|')
        name_list.append(item_list[0])
    f.close()
    while True:
        user_name = input("Username:")
        if user_name not in name_list and '|' not in user_name and len(user_name) >= 1:
            break
        else:
            print("Username is existed or you have entered a '|', please enter another username")

    while True:
        new_name = input("Your real name:")
        if '|' not in new_name and len(new_name) >= 1:
            break
        else:
            print("Please enter your real name")

    while True:
        address = input("Your address:")
        if '|' not in address and len(address) >= 1:
            break
        else:
            print("Please enter an actual address")

    while True:
        Email_ID = input("Your email ID:")
        if '@' in Email_ID and '.' in Email_ID and "mail" in Email_ID and '|' not in Email_ID:
            break
        else:
            print("Please enter a proper email")

    while True:
        Contact_Number = input("Your Contact Number,Please Only Enter Number:")
        test = Contact_Number
        if is_int(test) and len(Contact_Number) >= 10:
            if int(test) > 0:
                Contact_Number = str(Contact_Number)
                break
            else:
                print("Please enter a valid phone number")
                continue
        else:
            print("Please enter a valid number")

    while True:
        Gender = input("1. Male\n2. Female\n3. Other\nPlease choose the number:")
        if Gender == '1':
            Gender = "Male"
            break
        elif Gender == '2':
            Gender = "Female"
            break
        elif Gender == "3":
            Gender = "Other"
            break
        else:
            print("try again")
            continue
    print("Enter your birthday")
    bhd = calendar()

    while True:
        while True:
            Password = input("Create your password:")
            if '|' not in Password:
                break
            else:
                print("Please ensure '|' not in your password")
        Rewrite_Password = input("Enter the password again:")
        if Password == Rewrite_Password:
            break
        else:
            print("Password and rewrite_password is different")
            continue
    print("====================================")
    print("Please confirm your personal info")
    print("Username:" + user_name)
    print("Name:" + new_name)
    print("Address:" + address)
    print("Email:" + Email_ID)
    print("Phone number:" + Contact_Number)
    print("Gender:" + Gender)
    print("Birthday:" + bhd)
    print("password:" + Password)
    print("====================================")
    while True:
        ans = input("Save it?\nEnter y or n(y is yes and n is no):")
        if ans in ['y', 'n']:
            if ans == 'y':
                fhand = open("user.txt", 'a')
                fhand.write("\n")
                fhand.write(user_name)
                fhand.write("|")
                fhand.write(new_name)
                fhand.write("|")
                fhand.write(address)
                fhand.write("|")
                fhand.write(Email_ID)
                fhand.write("|")
                fhand.write(Contact_Number)
                fhand.write("|")
                fhand.write(Gender)
                fhand.write("|")
                fhand.write(bhd)
                fhand.write("|")
                fhand.write(Password)
                fhand.close()
                return
            else:
                print("We have deleted the info")
                return
        else:
            print("Please only enter y or n(y is yes and n is no)")


# This function is for user to log in with 3 attempts
def user_login():
    print("==================================================")
    login_list = []
    f = open('user.txt', 'r')
    for lines in f:
        final = lines.strip()
        info = final.split('|')
        login_list.append(info[0])
        login_list.append(info[-1])
    f.close()

    for x in ['1', '2', '3', '4']:
        j = 0
        m = 1
        if x == '4':
            print("You lose all your attempts")
            main()
        name = input("Username:")
        password = input("Password:")
        while m <= len(login_list) / 2:
            if name == login_list[j] and password == login_list[j + 1]:
                print("Welcome to our website")
                return name
            else:
                j += 2
                m += 1
        print("Try again")


# This function is to place order customer
def order_and_pay(name):
    status = True
    while status:
        print("==================================================")
        final_list = show_item()
        item_list = []
        quantity_list = []
        first_price_list = []
        noRM_price_list = []
        for item in final_list:
            item_list.append(item[0])
            quantity_list.append(item[2])
            first_price_list.append(item[3])

        for price in first_price_list:
            price = price[2:]
            noRM_price_list.append(price)

        while True:
            order = input("Please enter item number you want to buy:")
            if is_int(order):
                order = int(order)
                if order >= 1 and order <= len(item_list):
                    break
                else:
                    print("Please only enter available item")
                    continue
            else:
                print("Please only enter a number")
                continue
        while True:
            quantity = input("How many you want to buy?:")
            if is_int(quantity):
                quantity = int(quantity)
                if quantity > 0:
                    position = order - 1
                    if int(quantity_list[position]) >= quantity:
                        break
                    else:
                        print("Not enough item")
                        continue
                else:
                    print("Please enter a positive number")
            else:
                print("Please only enter a number")
        price = quantity * float(noRM_price_list[position])
        price = "{:.2f}".format(price)
        append_info = str(name) + '|' + str(item_list[position]) + '|' + str(quantity) + '|RM' + str(price)
        print("This is your goods," + name)
        print("================================")
        print("Name:" + str(item_list[position]))
        print("Quantity:" + str(quantity))
        print("================================\nYour Total Amount is RM" + str(price)
              + "\n================================")
        while True:
            ans = input("Save it?\nEnter y or n(y is yes and n is no):")
            if ans in ['y', 'n']:
                if ans == 'y':
                    fhand = open("customer_order.txt", 'a+')
                    fhand.write('\n')
                    fhand.write(append_info)
                    fhand.close()
                    status = False
                    break
                else:
                    print("We have deleted your order")
                    status = False
                    break
            else:
                print("Please only enter y or n(y is yes and n is no)")


# This function will show the specific customer order list.
def shopping_list(name):
    print("==================================================")
    i = 1
    print("This is the shopping list")
    info_list = []
    name_list = []
    f = open("customer_order.txt", 'r')
    for lines in f:
        info = lines.split('|')
        info_list.append(info)

    for x in info_list:
        if x[0] == name:
            print(str(i) + ")Item:" + x[1])
            print("Quantity:" + x[2])
            print("Price:" + x[3])
            i += 1
            name_list.append(x[0])

    if name not in name_list:
        print("Username is not registered or have not ordered anything")
        f.close()
        return info_list
    else:
        f.close()
        return info_list


# This function will show the specific user's info
def show_user_info(name):
    print("==================================================")
    print("This is your information in this website")
    info_list = []
    f = open("user.txt", 'r')
    for lines in f:
        info = lines.split('|')
        info_list.append(info)
    for x in info_list:
        if x[0] == name:
            print("Name:" + x[1])
            print("Address:" + x[2])
            print("Email:" + x[3])
            print("Phone number:" + x[4])
            print("Gender:" + x[5])
            print("Birthday:" + x[6])
            print("password:" + x[7])
    f.close()


# This function will delete the item
def dlt_item():
    final_list = show_item()
    while True:
        dlt = input("Enter the item number you want to delete:")
        if is_int(dlt):
            dlt = int(dlt) - 1
            if dlt >= 0 and dlt <= len(final_list) - 1:
                break
            else:
                print("Please only enter existed item number")
                continue
        else:
            print("Please enter an actual number")
            continue
    confirm = int(dlt) + 1
    while True:
        reply = input("Do you sure you want to delete " + str(confirm) + ")item?\nEnter y or n(y is yes and n is no):")
        if reply in ["y", "n"]:
            if reply == 'n':
                return
            else:
                break
        else:
            print("Please only enter y or n(y is yes and n is no)")

    del final_list[dlt]
    f = open("grocery_list.txt", 'w')
    for item in final_list:
        f.write(item[0])
        f.write('|')
        f.write(item[1])
        f.write('|')
        f.write(item[2])
        f.write('|')
        f.write(item[3])
        f.write('|')
        f.write(item[4])
    f.close()


# This function will delete the order
def dlt_order(name):
    other_order = []
    user_order = []
    final_list = []
    noRM_price_list = []
    price_list = []
    info_list = shopping_list(name)
    for x in info_list:
        if x[0] == name:
            user_order.append(x)
            price_list.append(x[-1])
        else:
            other_order.append(x)

    if len(user_order) == 0:
        return

    for price in price_list:
        price = price[2:]
        noRM_price_list.append(price)
    while True:
        dlt = input("Enter the item number you want to delete:")
        if is_int(dlt):
            dlt = int(dlt) - 1
            if dlt >= 0 and dlt <= len(user_order) - 1:
                break
            else:
                print("Please only enter existed item number")
                continue
        else:
            print("Please enter an actual number")
            continue
    confirm = int(dlt) + 1
    while True:
        reply = input("Do you sure you want to delete " + str(confirm) + ")item?\nEnter y or n(y is yes and n is no):")
        if reply in ["y", "n"]:
            if reply == 'n':
                return
            else:
                break
        else:
            print("Please only enter y or n(y is yes and n is no)")
            continue

    price = float(noRM_price_list[dlt])
    price = "{:.2f}".format(price)
    print("RM" + price + " have return to you.")
    del user_order[dlt]
    for i in other_order:
        if len(i) == 4:
            final_list.append(i)
    for j in user_order:
        if len(j) == 4:
            final_list.append(j)
    f = open("customer_order.txt", 'w')
    for item in final_list:
        f.write(item[0])
        f.write('|')
        f.write(item[1])
        f.write('|')
        f.write(item[2])
        f.write('|')
        f.write(item[3])
    f.close()


# It will allocate the selection of the admin
def admin_function():
    admin_login()
    while True:
        result = admin_UI()
        if result == '1':
            upload()
        elif result == '2':
            show_item()
        elif result == '3':
            dlt_item()
        elif result == '4':
            modify_info()
        elif result == '5':
            dlt_info()
        elif result == '6':
            find_specific_item()
        elif result == '7':
            show_customer()
        elif result == '8':
            name = input("What is the customer name?")
            shopping_list(name)
        elif result == '9':
            main()
        elif result == '10':
            end()


# It will allocate the selection of the new user
def new_user_function():
    while True:
        result = new_user_UI()
        if result == '1':
            show_item()
        elif result == '2':
            register()
        elif result == '3':
            main()
        elif result == '4':
            end()


# It will allocate the selection of the user
def user_function():
    name = user_login()
    while True:
        result = user_UI()
        if result == '1':
            show_item()
        elif result == '2':
            order_and_pay(name)
        elif result == '3':
            shopping_list(name)
        elif result == '4':
            dlt_order(name)
        elif result == '5':
            show_user_info(name)
        elif result == '6':
            main()
        elif result == '7':
            end()


# Main code starts on here
def main():
    selection = Choose_user()
    # For admin
    if selection == '1':
        admin_function()
    # For new user
    elif selection == '2':
        new_user_function()
    # For user
    elif selection == '3':
        user_function()


main()
