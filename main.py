FILENAME ="pyStudentDB\\data.txt"
class Student:
    def __init__(self, name, roll, marks, grade,pof):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.grade = grade
        self.pof=pof

def write():
    try:
        with open(FILENAME,'a') as fw:
            WRITE_SIZE= int(input("Please,Enter Number Of Students: "))
            for i in range(WRITE_SIZE):
                print(f"\nEnter Details for student {i+1}:")
                while True:
                    sname=input("Name: ").strip()
                    if not sname:
                        print("Cannot Be Empty!!")
                    elif (len(sname))<4:
                        print("Name is too Short")
                    elif any(char.isdigit() for char in sname):
                        print("Name should not contain numbers.")
                    else:
                        break
                while True:
                    sroll=input("Roll: ")
                    if not sroll:
                        print("Cannot Be Empty!!")             
                    elif not sroll.isalnum:
                        print("Roll should be alphanumeric only")
                    else:
                        break
                smarks=[]
                while True:
                    try:
                        smark = input("Marks [PHY CHEM MATH IT ENG HINDI]: ").strip()
                        smarks = [float(x) for x in smark.split()]
                        if len(smarks) != 6:
                            print("Please enter exactly 6 marks.")
                            continue
                        if not all(0 <= mark <= 100 for mark in smarks):
                            print("Each mark must be between 0 and 100.")
                            continue
                        break 
                    except ValueError:
                            print("Invalid input. Please enter only numbers separated by spaces.")             
                sgrade,spof=grade(smarks)
                s=Student(sname,sroll,smarks,sgrade,spof)
                fw.write(f"{s.name} {s.roll} {' '.join(map(str, s.marks))} {s.grade} {s.pof}\n")
            else:
                print("Written Successfully.")

    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Unexpected Error Occurred {e}")
def read():
    try:
        with open(FILENAME, 'r') as fr:
           lines = fr.readlines()
           display(lines)
    except FileNotFoundError:
        print("File not found!")

def display(lines):
    print("\nStudent Records in Table Format:\n")
    print("+----+------------------------------+--------+-------------------------------------------+--------+----------+")
    print("| SL | NAME                         | ROLL   |  PHY    CHEM   MATH    IT    ENG   HINDI  | GRADE  | P/F      |")
    print("+----+------------------------------+--------+-------------------------------------------+--------+----------+")
    
    sl = 1
    for line in lines:
        data = line.strip().split()
        if len(data) < 10:
            continue
        name = " ".join(data[:-9])
        roll = data[-9]
        marks = data[-8:-2]
        grade = data[-2]
        pof = data[-1] 
        formatted_marks = "  ".join(f"{float(mark):>5.1f}" for mark in marks)
        print(f"| {sl:<2} | {name:<28} | {roll:<6} | {formatted_marks:<10}  | {grade:^6} | {pof:^8} |")
        sl += 1


    print("+----+------------------------------+--------+-------------------------------------------+--------+----------+")

def menu():
  while True:
    EXIT=5
    print("\n1.Read Data")
    print("2.Write Data")
    print("3.Read & Write Data")
    print("4.Sort Data")
    print(f"{EXIT}.Exit")
    choice=int(input("Enter Your Choice: "))
    if choice == 1:
        read()
        check(EXIT)
    elif choice == 2:
        write()
        check(EXIT)

    elif choice ==3:
        write()
        read()
        check(EXIT)
    elif choice ==4:
        sort()
        check(EXIT)

    elif choice ==EXIT :
        print("GoodBye...")
        break
    else:
        print("Invalid Choice")

def grade(marks):
    # print(marks)
    sum=0
    for mark in marks:
        sum+=mark
    avg=sum/6
    if(all(mark>33 for mark in marks)) and avg>=40:
        pof="Pass"
    else:
        pof="Fail"
    if (avg >= 90):
        return 'A',pof
    elif (avg >= 80):
        return 'B',pof
    elif (avg >= 70):
        return 'C',pof
    elif (avg >= 60):
        return 'D',pof
    else:
        return 'F',pof
def sort():
    try:
        with open(FILENAME, 'r') as fr:
           lines = fr.readlines()

        students=[]
        for line in lines:
            data=line.strip().split()
            if len(data) <10:
                continue
            name=" ".join(data[:-9])
            roll = data[-9]
            marks = data[-8:-2]
            try:
                marks = list(map(float, data[-8:-2]))
            except ValueError:
                print(f"Invalid marks data for student {name}. Skipping.")
                continue  
            grade = data[-2]
            pof = data[-1] 
            students.append((name,roll,marks,grade,pof))

        choice= int(input("Sort With [1.Roll/2.Marks]"))
        order=int(input("[1.Asending/2.Desending]"))
        
        reverse = True if order == 2 else False
        if choice ==1:
            students.sort(key=lambda  x :x[1],reverse=reverse)
            filename = "pyStudentDB\\SortedByRoll.txt"
        elif choice==2:
            students.sort(key=lambda x:sum(x[2]),reverse=reverse)
            filename = "pyStudentDB\\SortedByMarks.txt"
        else:
            print("Invalid Sort Choice")

        with open(filename,'w') as fw:
            for s in students:
                fw.write(f"{s[0]} {s[1]} {' '.join(map(str,s[2]))} {s[3]} {s[4]}\n")
            else:
                print(f"Sorted data written to: {filename}")

    except FileNotFoundError:
        print("Data file not found.")
    except ValueError:
        print("Invalid input.")
    except Exception as e:
        print(f"Unexpected error: {e}")

def check(EXIT):
    cs=(input(f"Press Any Key To Continue/{EXIT} To Exit."))
    if cs == str(EXIT):
        print("GoodBye...")
        exit()
def main():
    print("\n\n\tWelcome To StudentDB.")
    menu()


if __name__ =="__main__":
    main()
