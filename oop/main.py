class Mobil:
    def __init__(self , warna , kecepatan):
        self.warna = warna
        self.kecepatan = kecepatan

    def tambah_kecepatan(self , kecepatan):
        self.kecepatan += kecepatan
    @staticmethod
    def print_mobil():
        print("Mobil Gantengggg")


    def change_color(self , color):
        self.warna = color

    @classmethod
    def get_mobil(cls , name , color):
        return name , color
mobil_1 = Mobil("Merah" , 150)
mobil_1.tambah_kecepatan(100)
mobil_1.name = "Mobil 1"
mobil_1.print_mobil()
print(f"Kecepatan mobil sekarang: {mobil_1.kecepatan}")
print(mobil_1.warna)

print("======================")
mobil_1.change_color("Putih")
print(mobil_1.warna)

print("======================")
print(Mobil.get_mobil("Mobil 1" , "Merah"))

