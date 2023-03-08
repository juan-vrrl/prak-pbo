#Juan Verrel Tanuwijaya, 121140072
#Prak 3, no 1

#Inisiasi Class dan Atribut

class AkunBank:
    list_pelanggan=[]
    
    #Konstruktor
    def __init__(self, no, nama, saldo):
        self.__no_pelanggan=no
        self.__nama_pelanggan=nama
        self.__jumlah_saldo=saldo
        self.list_pelanggan.append(self.__no_pelanggan)
      
    #Fungsi untuk menampilkan pilihan menu (diinput user)  
    def lihat_menu(self):
        #Akan diberikan menu pilihan secara looping yang akan berhenti jika user menginputkan "4"
        while True:
            print(f"Selamat datang di Bank Jago\nHalo {self.__nama_pelanggan}, ingin melakukan apa?\n1. Lihat saldo\n2. Tarik tunai\n3. Transfer saldo\n4. Keluar")
            pilih=input("Masukkan Pilihan : ")
            
            #Tergantung inputan user akan dipilih method yang sesuai dengan input, atau jika diinput "4" maka akan keluar dari menu
            if pilih=="1":
                self.lihat_saldo()
            
            elif pilih=="2":
                self.tarik_tunai()
            
            elif pilih=="3":
                self.transfer()
            
            elif pilih=="4":
                print("Terimakasih sudah menggunakan menu!")
                break    
            
            else:
                print("Pilihan tidak sesuai!\n")
     
    #Fungsi untuk menampilkan nama dan jumlah saldo akun           
    def lihat_saldo(self):
            print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}\n")             
    
    #Fungsi untuk menarik tunai dari rekening
    def tarik_tunai(self):
            while True:
                tarik=int(input("Masukkan nominal yang ingin ditrasnfer : "))
                if tarik>self.__jumlah_saldo:
                    print("Nominal saldo yang Anda punya tidak cukup!")
                else:
                    self.__jumlah_saldo-=tarik
                    print("Saldo berhasil ditarik!\n")
                    break
    
    #Fungsi untuk mentransfer uang ke no rekening bank yang dituju berdasarkan variabel class list_pelanggan
    def transfer(self):
            #inisiasi variabel transfer dan rekening inputan
            transfer=int(input("Masukkan nominal yang ingin ditransfer : "))
            rekening=int(input("Masukkan no rekening tujuan : "))
            #Dilakukan pengecekan apakah rekening tujuan yang diinputkan ada didalam data list_pelanggan, jika ada maka akan ditampilkan bahwa transfer ke rekening tujuan berhasil
            #Tergantung kepada akun yang diakses jika pengguna akun mentransfer ke rekening bank miliknya sendiri maka akan diberikan tampilan error akan tetapi jika mentransfer ke rekening akun lain maka nominal saldo akan berkurang sesuai inputan transfer
            for x in range(len(self.list_pelanggan)):
                if rekening==self.list_pelanggan[x]:
                    if x==0:
                        if self.__nama_pelanggan=="Juan":
                            print("Tidak bisa melakukan transfer ke rekening sendiri!\n")  
                            break
                        
                        else:
                            self.__jumlah_saldo-=transfer
                            print(f"Transfer Rp {transfer} ke Juan sukses!\n")  
                            break
                            
                    elif x==1:
                        if self.__nama_pelanggan=="Ukraina":
                            print("Tidak bisa melakukan transfer ke rekening sendiri!\n")  
                            break
                        
                        else:
                            self.__jumlah_saldo-=transfer
                            print(f"Transfer Rp {transfer} ke Ukraina sukses!\n")  
                            break
                        
                    elif x==2:
                        if self.__nama_pelanggan=="Elon Musk":
                            self.__jumlah_saldo+=transfer
                            print("Tidak bisa melakukan transfer ke rekening sendiri!\n")  
                            break
                        
                        else:
                            self.__jumlah_saldo-=transfer
                            print(f"Transfer Rp {transfer} ke Elon Musk sukses!\n")  
                            break
                    
                if x==2:
                    print("No rekening tujuan tidak dikenal! Kembali ke menu utama\n")
 
#main
#Inisiai Objek                        
Akun1 = AkunBank(1234, "Juan", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

#Pemanggilan Method lihat menu melalui Akun1(akun saya)
Akun1.lihat_menu()










.
