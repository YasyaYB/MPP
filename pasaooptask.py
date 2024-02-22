class Motor:
    def __init__(self, merk, tahun_produksi, warna):
        self.merk = merk
        self.tahun_produksi = tahun_produksi
        self.warna = warna
        self.kecepatan = 0

    def accelarate(self, increase):
        self.kecepatan += increase

    def brake(self, decrease):
        self.kecepatan -= decrease

    def display_info(self):
        print(f"Merk Motor: {self.merk}")
        print(f"Tahun Produksi: {self.tahun_produksi}")
        print(f"Warna: {self.warna}")
        print(f"Kecepatan: {self.kecepatan} km/jam")

# Membuat objek dari class Motor
motor = Motor("Honda", 2021, "Merah")

# Memanggil method untuk mengakselerasi motor
motor.accelarate(20)

# Memanggil method untuk menampilkan informasi motor
motor.display_info()
