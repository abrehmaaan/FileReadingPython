import os
while True:
    print("Marksheet Management Program")
    print("1. Read Records")
    print("2. Add Records")
    print("3. Update Record")
    print("4. Search Record")
    print("5. Delete Record")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        lines = []
        with open('records.txt') as f:
            [lines.append(line.strip()) for line in f.readlines()]
        for line in lines:
            record = line.split(',')
            print("Name: "+record[0])
            print("Course\tMarks")
            for i in range(1,len(record)):
                sub = record[i].split(':')
                print(sub[0]+"\t"+sub[1])
    elif choice == 2:
        num = int(input("How many records do you want to enter?: "))
        f = open("records.txt", "a")
        for i in range(num):
            name = input("Enter Student Name: ")
            f.write(name+",")
            for j in range(4):
                course = input("Enter Course Name: ")
                marks = float(input("Enter Marks: "))
                f.write(course+":"+str(marks))
                if j != 3:
                    f.write(",")
                else:
                    f.write("\n")
        f.close()
    elif choice == 3:
        name = input("Enter student name you want to update: ")
        found = False
        lines = []
        with open('records.txt') as f:
            [lines.append(line.strip()) for line in f.readlines()]
        f_new = open("newrecords.txt", "w")
        for line in lines:
            record = line.split(',')
            if (record[0] == name):
                f_new.write(name+",")
                for j in range(4):
                    course = input("Enter Course Name: ")
                    marks = float(input("Enter Marks: "))
                    f_new.write(course+":"+str(marks))
                    if j != 3:
                        f_new.write(",")
                    else:
                        f_new.write("\n")
                print("Record Updated!")
                found = True
            else:
                f_new.write(line+"\n")
        f_new.close()
        os.remove("records.txt")
        os.rename("newrecords.txt", "records.txt")
        if not found:
            print("No Such Record Found!")
    elif choice == 4:
        name = input("Enter student name you want to search: ")
        found = False
        lines = []
        with open('records.txt') as f:
            [lines.append(line.strip()) for line in f.readlines()]
        for line in lines:
            record = line.split(',')
            if (record[0] == name):
                print("Record Found!")
                print("Name: "+record[0])
                print("Course\tMarks")
                for i in range(1,len(record)):
                    sub = record[i].split(':')
                    print(sub[0]+"\t"+sub[1])
                found = True
                break
        if not found:
            print("No Such Record Found!")
    elif choice == 5:
        name = input("Enter student name you want to delete: ")
        found = False
        lines = []
        with open('records.txt') as f:
            [lines.append(line.strip()) for line in f.readlines()]
        f_new = open("newrecords.txt", "w")
        for line in lines:
            record = line.split(',')
            if (record[0] == name):
                print("Record Deleted!")
                found = True
            else:
                f_new.write(line+"\n")
        f_new.close()
        os.remove("records.txt")
        os.rename("newrecords.txt", "records.txt")
        if not found:
            print("No Such Record Found!")
    elif choice == 6:
        break
    else:
        print("Wrong Choice")
    repeat = input("Do you want to continue? (y/n) ")
    if repeat == 'n' or repeat == 'N':
        break