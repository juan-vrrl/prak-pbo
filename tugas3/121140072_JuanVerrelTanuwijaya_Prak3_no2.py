#Juan Verrel Tanuwijaya, 121140072
#Prak 3, no 2

#Inisiasi Class dan Atribut
class Mobil:
    #Inisiasi atribut kelas yang merupakan variabel konstan yang dimiliki oleh semua objek yang dibuat.
    tipekendaraan="berat"
    def __init__(self,nama,pabrik,tahun):
        #Inisiasi atribut Public, atribut publik dapat diakses didalam maupun diluar kelas itu sendiri, cara mendaklarasikannya adalah dengan menulis nama variabel biasa secara default.
        self.nama = nama
        #Inisiasi atribut Private, atribut Private hanya dapat diakses didalam kelas itu sendiri sehingga tidak dapat diakses diluar kelas tersebut, cara mendeklarasikannya adalah dengan menambahkan "__" didepan variabel atribut.
        self.__pabrik = pabrik
        #Inisiasi atribut Protected, atribut Protected hanya dapat diakses oleh kelas turunannya sendiri, cara mendeklarasikannya adalah dengan menambahkan "_" didepan nama variabel atribut, akan tetapi dalam python atribut protected tetap dapat diakses diluar kelasnya sendiri seperti atribut public.
        self._tahun = tahun
    
    def printprivate(self):
        print(self.__pabrik)
        
mobil1=Mobil("Zenix", "Toyota", 2014)
mobil2=Mobil("Camaro", "Chevrolet", 2017)

#Dikarenakan atribut nama merupakan atribut publik, maka dapat diakses tanpa menggunakan fungsi dari dalam kelas tersebut dan langsung dapat di print dari luar kelas tersebut.
print(mobil1.nama)
#Sedangkan untuk atribut pabrik hanya dapat diakses menggunakan fungsi dari dalam kelas tersebut dikarenakan tidak dapat diakses dari luar kelasnya sendiri.
mobil1.printprivate()
#Dan atribut Protected tetap dapat diakses diluar kelasnya sendiri pada Python
print(mobil1._tahun)

#Print atribut kelas yang memiliki nilai konstan oleh semua objek kelas tersebut
print("Mobil 1 :", mobil1.tipekendaraan)
print("Mobil 2 :", mobil2.tipekendaraan)
