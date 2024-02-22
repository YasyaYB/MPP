class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Jurusan: {self.jurusan}")


# Membuat objek dari class Mahasiswa
mahasiswa1 = Mahasiswa("Yoga", "12345", "Teknik Informatika")

# Memanggil method untuk menampilkan informasi mahasiswa
mahasiswa1.display_info()
