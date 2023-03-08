#Juan Verrel Tanuwijaya, 121140072
#Prak 2

#Inisiasi CLass Mahasiswa dan Atribut
class Mahasiswa:    
    def __init__(self, nama, nim, kelas_pbo_siakad,jumlah_sks):
        self.nama=nama
        self.nim=nim
        self.kelas=kelas_pbo_siakad
        self.sks=jumlah_sks
    
    #Fungsi untuk menampilakn informasi diri dari objek berupa nama, nim, kelaspbo, dan sks
    def infodiri(self):
        print(f"Nama = {self.nama}\nNim = {self.nim}\nKelas PBO Siakad = {self.kelas}\nJumlah SKS = {self.sks}")
        
    #Fungsi untuk mengubah kelas PBO dari objek (Ditentukan User
    def ubahkelas(self,kelasbaru):
        self.kelas=kelasbaru

#Main
#Pemanggilan class & Pemanggilan Method
manusia=Mahasiswa("Juan", "121140072", "RB", "4 SKS")
manusia.infodiri()
manusia.ubahkelas("RA")
manusia.infodiri()
