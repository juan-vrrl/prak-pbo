#Juan Verrel Tanuwijaya, 121140072
#Prak 4, no 1

#Inisiasi Class Komputer dan Atributnya
class Komputer:
    def __init__(self,nama,jenis,harga,merk):
        self.nama=nama
        self.jenis=jenis
        self.harga=harga
        self.merk=merk

#Inisiasi Class Turunan dan Atribut tambahannya
class Processor(Komputer):
    def __init__(self,nama,jenis,harga,merk,jumlah,kecepatan):
        super().__init__(nama,jenis,harga,merk)
        self.jumlah_core=jumlah
        self.kecepatan_core=kecepatan
        
    def tampil(self):
        print(f"Processor {self.nama} produksi {self.merk}")
        
class RAM(Komputer):
    def __init__(self,nama,jenis,harga,merk,kapasitas):
        super().__init__(nama,jenis,harga,merk)
        self.kapasitas=kapasitas
        
    def tampil(self):
        print(f"RAM {self.nama} produksi {self.merk}")
        
class HDD(Komputer):
    def __init__(self,nama,jenis,harga,merk,kapasitas,rpm):
        super().__init__(nama,jenis,harga,merk)
        self.kapasitas=kapasitas
        self.rpm=rpm
    
    def tampil(self):
        print(f"SATA {self.nama} produksi {self.merk}")
           
class VGA(Komputer):
    def __init__(self,nama,jenis,harga,merk,kapasitas):
        super().__init__(nama,jenis,harga,merk)
        self.kapasitas=kapasitas
    
    def tampil(self):
        print(f"VGA {self.nama} produksi {self.merk}")
        
class PSU(Komputer):
    def __init__(self,nama,jenis,harga,merk,daya):
        super().__init__(nama,jenis,harga,merk)
        self.daya=daya
    
    def tampil(self):
        print(f"PSU {self.nama} produksi {self.merk}")

#Pembuatan list rakit untuk menyimpan objek
rakit=[]

#Pembuatan Objek
p1 = Processor('Core i7 7740X',"Baru",4350000,'Intel',4,'4.3GHz')
p2 = Processor('Ryzen 5 3600',"Second",250000,'AMD', 4,'4.3GHz')
ram1 = RAM('DDR4 SODimm PC19200/2400MHz',"Baru",328000,'V-Gen','4GB')
ram2 = RAM('DDR4 2400MHz',"Second ",328000,'G.SKILL', '4GB')
hdd1 = HDD('HDD 2.5 inch',"Baru", 295000,'Seagate','500GB',7200)
hdd2 = HDD('HDD 2.5 inch',"Second", 295000,'Seagate', '1000GB',7200)
vga1 = VGA('VGA GTX 1050',"Baru",'Asus',250000,'2GB')
vga2 = VGA('1060Ti', "Second", 250000,'Asus','8GB')
psu1 = PSU('Corsair V550', "Baru", 250000,'Corsair','500W')
psu2 = PSU('Corsair V550', "Second", 250000,'Corsair','500W')

#memasukkan kumpulan objek ke dalam list rakit sebagai 2 list berbeda
rakit.extend([[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]])

#Pemanggilan Fungsi tampil dalam list rakit menggunakan nested loop for
for x in range(len(rakit)):
    print("Komputer", x+1, ":")
    for y in range(len(rakit[x])):
        rakit[x][y].tampil()
    print()
