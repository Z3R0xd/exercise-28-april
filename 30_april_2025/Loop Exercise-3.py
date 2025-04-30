instruction = 0

while instruction != 3 :
    instruction = int(input("Menu : "))
    if instruction == 1 :
        # gunakan code berikut untuk melengkapi proses di menu 1
        n = 10
        num1 = 0
        num2 = 1
        next_number = num2  
        count = 1
        result = [num1, num2]
        while count <= n:
            count += 1
            num1, num2 = num2, next_number
            result.append(next_number)
          
            next_number = num1 + num2
        print (result)
    
    elif instruction == 2 :
        # gunakan code berikut untuk melengkapi proses di menu 2
        currentDate = 30 # ganti dengan tanggal hari ini
    
        if currentDate % 2 == 0:
            print("tanggal genap")
        else:
            print("tanggal ganjil")
    
    elif instruction == 3:
        print("exit")
    
    else:
        print("menu tidak dikenal")    