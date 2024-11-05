# Kelas dasar untuk Karyawan
class Karyawan:
    def __init__(self, nama, umur, gaji):
        self._nama = nama   # Menggunakan atribut dengan prefix "_" untuk menunjukkan bahwa ini private
        self._umur = umur
        self._gaji = gaji

    # Getter untuk nama
    def get_nama(self):
        return self._nama

    # Setter untuk nama
    def set_nama(self, nama):
        self._nama = nama

    # Getter untuk umur
    def get_umur(self):
        return self._umur

    # Setter untuk umur
    def set_umur(self, umur):
        self._umur = umur

    # Getter untuk gaji
    def get_gaji(self):
        return self._gaji

    # Setter untuk gaji
    def set_gaji(self, gaji):
        self._gaji = gaji

    def info(self):
        return f"Nama: {self._nama}, Umur: {self._umur}, Gaji: {self._gaji}"


# Kelas turunan untuk Jabatan
class Jabatan(Karyawan):
    def __init__(self, nama, umur, gaji, posisi):
        super().__init__(nama, umur, gaji)  # Memanggil konstruktor kelas dasar
        self._posisi = posisi

    # Getter untuk posisi
    def get_posisi(self):
        return self._posisi

    # Setter untuk posisi
    def set_posisi(self, posisi):
        self._posisi = posisi

    def info(self):
        return f"Nama: {self._nama}, Umur: {self._umur}, Gaji: {self._gaji}, Posisi: {self._posisi}"


# Contoh penggunaan kelas
karyawan1 = Karyawan("Ahmad", 30, 5000000)
print(karyawan1.info())  # Output: Nama: Ahmad, Umur: 30, Gaji: 5000000

# Menggunakan setter
karyawan1.set_nama("Ali")
karyawan1.set_gaji(5500000)
print(karyawan1.info())  # Output: Nama: Ali, Umur: 30, Gaji: 5500000

# Karyawan dengan jabatan
jabatan1 = Jabatan("Budi", 28, 7000000, "Manajer")
print(jabatan1.info())  # Output: Nama: Budi, Umur: 28, Gaji: 7000000, Posisi: Manajer

# Menggunakan setter di kelas turunan
jabatan1.set_posisi("Direktur")
print(jabatan1.info())  # Output: Nama: Budi, Umur: 28, Gaji: 7000000, Posisi: Direktur
