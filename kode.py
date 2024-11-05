
class Karyawan:
    def __init__(self, nama, umur, gaji):
        self._nama = nama  
        self._umur = umur
        self._gaji = gaji


    def get_nama(self):
        return self._nama


    def set_nama(self, nama):
        self._nama = nama

    
    def get_umur(self):
        return self._umur

    def set_umur(self, umur):
        self._umur = umur

    
    def get_gaji(self):
        return self._gaji

    
    def set_gaji(self, gaji):
        self._gaji = gaji

    def info(self):
        return f"Nama: {self._nama}, Umur: {self._umur}, Gaji: {self._gaji}"



class Jabatan(Karyawan):
    def __init__(self, nama, umur, gaji, posisi):
        super().__init__(nama, umur, gaji)  
        self._posisi = posisi

    def get_posisi(self):
        return self._posisi


    def set_posisi(self, posisi):
        self._posisi = posisi

    def info(self):
        return f"Nama: {self._nama}, Umur: {self._umur}, Gaji: {self._gaji}, Posisi: {self._posisi}"

karyawan1 = Karyawan("Ahmad", 30, 5000000)
print(karyawan1.info())  

karyawan1.set_nama("Ali")
karyawan1.set_gaji(5500000)
print(karyawan1.info())  


jabatan1 = Jabatan("Budi", 28, 7000000, "Manajer")
print(jabatan1.info())  

# test
jabatan1.set_posisi("Direktur")
print(jabatan1.info())  
