sectionone=["Ampong","blanco","cabezas","dalogdog","fuentes","jakutin","manolo","ortiz","romolo","sanchez","taipen","villa","zulieta"]

sectiontwo=["Adajar","Bongosia","Caballero","Diaz","faunillan","Juliet","Mirafuentes","Ompad","Roco","Selgas","Talipan","Volvol","Zuliet"]

sectiontrd=["Apus","Blake","Cabanez","Dela cruz","Ferrer","Jardio","Manego","Opus","Romero","Solis","Tope","Velez","Zuldita"]

sectionfrt=["Alacntara","Bulac","Cuevas","Delvo","Gutang","Joaquin","Mavric","Owen","Rogers","Salo","Thompson","Vazquez","Zamora"]
attendance={}
attendances={}
attendancess={}
attendancesss={}
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username=="teacher" and password=="pass1":
        break
    else:
        print("Invalid Username or Password, Please Try Again.")
        
def fstbsit():
    print("===== Attendance =====")
    for student in sectionone:
        while True: 
            mark = input(f"Mark {student} as (P/A/L): ").upper()

            if mark in ["P", "A", "L"]:
                attendance[student] = mark
                break   
            else:
                print(" Invalid mark. Please enter only P, A, or L.")

    print("\nAttendance Record:")
    for student, mark in attendance.items():
        print(f"{student}: {mark}")
        
def secbsit():
    print("===== Attendance =====")
    for std in sectiontwo:
        while True: 
            mark = input(f"Mark {std} as (P/A/L): ").upper()

            if mark in ["P", "A", "L"]:
                attendance[std] = mark
                break   
            else:
                print(" Invalid mark. Please enter only P, A, or L.")

    print("\nAttendance Record:")
    for std, mark in attendance.items():
        print(f"{std}: {mark}")
    
def trdbsit():
    print("===== Attendance =====")
    for stt in sectiontrd:
        while True: 
            mark = input(f"Mark {stt} as (P/A/L): ").upper()

            if mark in ["P", "A", "L"]:
                attendance[stt] = mark
                break   
            else:
                print(" Invalid mark. Please enter only P, A, or L.")

    print("\nAttendance Record:")
    for stt, mark in attendance.items():
        print(f"{stt}: {mark}")
def frtbsit():
    print("===== Attendance =====")
    for stnt in sectionfrt:
        while True: 
            mark = input(f"Mark {stnt} as (P/A/L): ").upper()

            if mark in ["P", "A", "L"]:
                attendance[stnt] = mark
                break   
            else:
                print(" Invalid else. Please enter only P, A, or L.")

    print("\nAttendance Record:")
    for stnt, mark in attendance.items():
        print(f"{stnt}: {mark}")
def view_all_records():
    temp_sections = {
        "BSIT1-01": sectionone,
        "BSIT1-02": sectiontwo,
        "BSIT1-03": sectiontrd,
        "BSIT1-04": sectionfrt
    }
    attend_sections = {
        "BSIT1-01": attendance,
        "BSIT1-02": attendances,
        "BSIT1-03": attendancess,
        "BSIT1-04": attendancesss
    }
    
    
    print("\n===== View All Attendance Records =====")
    for sec, students in temp_sections.items():
        print(f"\n{sec}:")
        for s in students:
            mark = attend_sections[sec].get(s, "Not marked")
            print(f"{s}: {mark}")

while True:
    print("===== Attendance =====")
    print("1. BSIT1-01")
    print("2. BSIT1-02")
    print("3. BSIT1-03")
    print("4. BSIT1-04")
    print("5. View All Records")
    print("6. Exit")
    
     
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        fstbsit()
    elif choice == "2":
        secbsit()
    elif choice == "3":
        trdbsit()
    elif choice == "4":
        frtbsit()
    elif choice == "5":
        view_all_records()
    elif choice == "6":
        print("\n👋 Thank you for using the Attendance Recording System")
        break

    else:   
        print("\n⚠️ Invalid choice. Try again.\n")