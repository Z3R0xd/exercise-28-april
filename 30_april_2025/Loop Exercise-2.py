low_case = "abcdefghijklmnopqrstuvwxyz"
up_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_case_list = list(low_case)
up_case_list = list(up_case)

password = input("Please input your password : ")
password_list = list(password)

count = 0

spec_characters = ["$","#","@"]

if any(x in low_case_list for x in password_list):
    count = count + 1 
    if any(x in up_case_list for x in password_list):
        count = count + 1 
        if any(x in spec_characters for x in password_list):
            count = count+1
            if len(password) >= 6:
                count = count + 1 
                if len(password) <=16:
                    count = count + 1 
else:
    print("Password not strong enough")
    
print(count)