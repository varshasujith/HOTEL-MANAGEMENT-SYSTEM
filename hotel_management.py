rooms = [100, "DELUXE", 350, 'N', 202, "LUXURY", 500, "Y", 310, "SUITE", 700, "Y", 
         501, "LUXURY", 500, "N", 728, "SUITE", 700, "Y", 418, "NORMAL", 150, "Y", 
         109, "DELUXE", 350, "N", 230, "LUXURY", 500, "Y", 605, "SUITE", 700, "N", 
         525, "LUXURY", 500, "Y"]

ch = 0

while ch != 7:
    print("\n** HOTEL MANAGEMENT **")
    print("1 VIEW")
    print("2 ADD")
    print("3 MODIFY")
    print("4 DELETE")
    print("5 CHECK IN")
    print("6 CHECK OUT")
    print("7 EXIT")
    
    ch = int(input("Enter choice: "))

    if ch == 1:
        n = int(input("Enter a room no: "))
        s = len(rooms) // 4
        a = -1
        for i in range(s):
            if rooms[i * 4] == n:
                a = i
                break
        if a != -1:
            print("Room no: ", rooms[a * 4])
            print("Room type: ", rooms[a * 4 + 1])
            print("Charge: ", rooms[a * 4 + 2])
            print("Avail: ", rooms[a * 4 + 3])
        else:
            print("Record Not Found")

    elif ch == 2:
        n = int(input("Enter a room no: "))
        s = len(rooms) // 4
        f = 0
        for i in range(s):
            if rooms[i * 4] == n:
                print("Record already exists")
                f = 1
                break
        if f == 0:
            m = input("Enter Room type: ")
            c = int(input("Enter Charge: "))
            avail = input("Enter Avail: ")
            rooms.extend([n, m, c, avail])
            print("Record Added")

    elif ch == 3:
        n = int(input("Enter a room no: "))
        s = len(rooms) // 4
        f = 0
        for i in range(s):
            if rooms[i * 4] == n:
                f = 1
                print("Room Type: ", rooms[i * 4 + 1])
                a = input("Modify Room Type (y/n)? ")
                if a == "y":
                    mn = input("Enter Room Type: ")
                    rooms[i * 4 + 1] = mn
                print("Charge: ", rooms[i * 4 + 2])
                b = input("Modify Charge (y/n)? ")
                if b == "y":
                    c = int(input("Enter Charge: "))
                    rooms[i * 4 + 2] = c
                print("Avail: ", rooms[i * 4 + 3])
                c = input("Modify Avail (y/n)? ")
                if c == "y":
                    avail = input("Enter Avail: ")
                    rooms[i * 4 + 3] = avail
                print("Record Modified")
                break
        if f == 0:
            print("Record Not Found")

    elif ch == 4:
        n = int(input("Enter a room no: "))
        s = len(rooms) // 4
        f = 0
        for i in range(s):
            if rooms[i * 4] == n:
                f = 1
                print("Room Type: ", rooms[i * 4 + 1])
                print("Charge: ", rooms[i * 4 + 2])
                print("Avail: ", rooms[i * 4 + 3])
                confirm = input("Are you sure (y/n)? ")
                if confirm == "y":
                    del rooms[i * 4:i * 4 + 4]
                    print("Record deleted")
                break
        if f == 0:
            print("Record Not Found")

    elif ch == 5:
        n = int(input("Enter a room no: "))
        s = len(rooms) // 4
        f = 0
        for i in range(s):
            if rooms[i * 4] == n:
                f = 1
                if rooms[i * 4 + 3] == 'N':
                    print("Room Not Available")
                else:
                    print("Room Type: ", rooms[i * 4 + 1])
                    print("Charge: ", rooms[i * 4 + 2])
                    print("Avail: ", rooms[i * 4 + 3])
                    v = input("Are you sure (y/n)? ")
                    if v == "y":
                        if rooms[i * 4 + 3] == "Y":
                            rooms[i * 4 + 3] = "N"
                            print("Avail: ", rooms[i * 4 + 3])
                            print("Successfully checked in")
                break
        if f == 0:
            print("Record Not Found")

    elif ch == 6:
        n = int(input("Enter a room no: "))
        s = len(rooms) // 4
        f = 0
        for i in range(s):
            if rooms[i * 4] == n:
                f = 1
                if rooms[i * 4 + 3] == 'Y':
                    print("Room is Vacant")
                else:
                    print("Charge: ", rooms[i * 4 + 2])
                    print("Avail: ", rooms[i * 4 + 3])
                    v = input("Are you sure (y/n)? ")
                    if v == "y":
                        if rooms[i * 4 + 3] == "N":
                            rooms[i * 4 + 3] = "Y"
                            print("Avail: ", rooms[i * 4 + 3])
                            print("Successfully checked out")
                break
        if f == 0:
            print("Record Not Found")

    elif ch == 7:
        print("Exiting...")
    
    else:
        print("Wrong Option")
