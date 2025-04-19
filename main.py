# Read
# Write
#FILENAME
FILENAME ="pyStudentDB\data.txt"
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
            print("\nStudent Records from File:\n")
            i=1
            for line in fr:
              data=line.strip().split()
              sname=data[0]
              sroll=data[1]
              smarks=data[2:8]
              sgrade=data[-1]
              smarks = " ".join(smarks)
              # print(data,type(data))
              print(f"SL:{i} NAME:{sname} ROLL:{sroll} MARKS:{smarks} GRADE:{sgrade}")
              i+=1
    except FileNotFoundError:
        print("File not found!")

def main():
    write()
    read()




if __name__ =="__main__":
    main()
