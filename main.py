# Rea
# Write
#FILENAME
FILENAME ="pyStudentDB\\data.txt"
class Student:
    def __init__(self, name, roll, marks, grade):
        self.name = name
        self.roll = roll
        self.marks = marks
        self.grade = grade

def write():
    try:
        with open(FILENAME,'a') as fw:
            WRITE_SIZE= int(input("Please,Enter Number Of Students: "))
            for i in range(WRITE_SIZE):
              print(f"\nEnter Details for student {i+1}:")
              sname=input("Name: ")
              sroll=input("Roll: ")
              smarks=[]
              while(len(smarks)!=6):
                print("Marks[PHY CHEM MATH IT ENG HINDI]: ")             
                smark=input()
                smarks=[float(x) for x in smark.split()]
              sgrade='C'
              s=Student(sname,sroll,smarks,sgrade)
              fw.write(f"{s.name} {s.roll} {' '.join(map(str, s.marks))} {s.grade}\n")

              
            else:
                print("Written Successfully.")

    except FileNotFoundError:
        print("File not found!")
def read():
    try:
        with open(FILENAME, 'r') as fr:
           lines = fr.readlines()
           display(lines)
    except FileNotFoundError:
        print("File not found!")

def display(lines):
    print("\nStudent Records in Table Format:\n")
    print("+----+------------------------------+--------+-------------------------------------------+--------+")
    print("| SL | NAME                         | ROLL   |  PHY    CHEM   MATH    IT    ENG   HINDI  | GRADE  |")
    print("+----+------------------------------+--------+-------------------------------------------+--------+")
    sl = 1
    for line in lines:
        data = line.strip().split()
        if len(data) < 9:
            continue
        name = " ".join(data[:-8])
        roll = data[-8]
        marks = data[-7:-1]
        grade = data[-1]
        formatted_marks = "  ".join(f"{float(mark):>5.1f}" for mark in marks)
        print(f"| {sl:<2} | {name:<28} | {roll:<6} | {formatted_marks:<10}  | {grade:^6} |")
        sl += 1
    print("+----+------------------------------+--------+-------------------------------------------+--------+")

def menu():
  while True:
    EXIT=4
    print("\n1.Read Data")
    print("2.Write Data")
    print("3.Read & Write Data")
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

    elif choice ==EXIT :
        print("GoodBye...")
        break
    else:
        print("Invalid Choice")
    
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
