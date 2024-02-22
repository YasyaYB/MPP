class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = {}

    def input_nilai(self, mata_kuliah, nilai):
        self.nilai[mata_kuliah] = nilai

    def rata_rata_nilai(self):
        total_nilai = sum(self.nilai.values())
        jumlah_mata_kuliah = len(self.nilai)
        return total_nilai / jumlah_mata_kuliah

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Nilai: {self.nilai}")

# Membuat objek dari class Mahasiswa
mahasiswa1 = Mahasiswa("Yoga", "12345", "Teknik Informatika")

# Memanggil method untuk input nilai
mahasiswa1.input_nilai("Matematika", 90)
mahasiswa1.input_nilai("Fisika", 88)
mahasiswa1.input_nilai("Kimia", 92)

# Memanggil method untuk menampilkan rata-rata nilai
rata_rata = mahasiswa1.rata_rata_nilai()
print(f"Rata-rata Nilai: {rata_rata}")

# Memanggil method untuk menampilkan informasi mahasiswa
mahasiswa1.display_info()
