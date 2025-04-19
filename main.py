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
              print(f"\nEnter Details for student {i+1}:\n")
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


def main():
    # write()
    read()



if __name__ =="__main__":
    main()
