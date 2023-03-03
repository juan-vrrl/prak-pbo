class Mahasiswa:    
    def __init__(self, nama, nim, kelas_pbo_siakad,jumlah_sks):
        self.nama=nama
        self.nim=nim
        self.kelas=kelas_pbo_siakad
        self.sks=jumlah_sks
    
    def infodiri(self):
        print(f"Nama = {self.nama}\nNim = {self.nim}\nKelas PBO Siakad = {self.kelas}\nJumlah SKS = {self.sks}")
        
    def ubahkelas(self,kelasbaru):
        self.kelas=kelasbaru

manusia=Mahasiswa("Juan", "121140072", "RB", "4 SKS")
manusia.infodiri()
manusia.ubahkelas("RA")
manusia.infodiri()
