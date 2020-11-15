import os

#function untuk menentukan suatu bilangan prima atau bukan
def prime_num (num) :
    count=0
    for i in range(1,num+1) :
        if num%i==0 :
            count+=1
    if count==2 : return True
    return False

while True :
    os.system("cls")
    while True :
        try :
            n = int(input("Masukkan sebuah angka : "))
            if n<1 : raise Exception("Angka harus >=1")
            break
        except ValueError:
            print(">>>ERROR: Input harus berupa integer")
        except Exception as e :
            print(">>>ERROR:",e)

    #output
    if prime_num(n) :
        print(f"{n} adalah bilangan prima")
    else :
        print(f"{n} bukan bilangan prima")
    
    #ulang?
    while True :
        ul = input("Ulang? (y/n) ").lower()
        if ul in ["yes","y","no","n"]:
            break
    if ul in ["no","n"]:
        break

