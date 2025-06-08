#code for printing different pyramids with their height as per user input

#input for the height of the pyramid
n = int(input("Enter the height of pyramid: "))

t = int(input("1. Lower Pyramid\n2. Upper Pyramid\n3. Pyramid\n4.All\n Enter your pattern: "))

match t:
    case 1: #lower
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end=" ")
            print()
    
    case 2: #upper
        for i in range(n, 0, -1):
            print("* " * i, end=" \n")
    
    case 3: #normal
        for i in range(1, n+1):
            for j in range(n-i):
                print(" ", end=" ")
            for k in range(1, 2*i):
                print("*", end=" ")
            print()
    case 4: #for all
        for i in range(1, n+1): #lower
            for j in range(1, i+1):
                print("*", end=" ")
            print()
        print()
        for i in range(n, 0, -1): #upper
            print("* " * i, end=" \n")
        print()
        for i in range(1, n+1): #normal
            for j in range(n-i):
                print(" ", end=" ")
            for k in range(1, 2*i):
                print("*", end=" ")
            print()
    case _:
        print("This is not a valid selection try again.")