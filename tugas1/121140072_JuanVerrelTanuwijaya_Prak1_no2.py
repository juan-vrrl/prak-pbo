#Juan Verrel Tanuwijaya, 121140072
#Prak 1, no 2

coba=1
while coba<=3:
    user=input("Username anda : ")
    pw=input("Password anda : ")
    
    if user=="informatika" and pw=="12345678":
        print("Berhasil login!")
        break
    
    else:
        coba+=1
        if coba==4:
            print("Akun anda diblokir!")
        else:
            print("Username atau password salah coba lagi")
            
