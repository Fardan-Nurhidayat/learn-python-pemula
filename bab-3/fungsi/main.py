def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

def minimal (a , b) :
    """
    Fungsi ini digunakan untuk mencari nilai minimal dari dua bilangan.

    Args:
        a (int): Bilangan pertama.
        b (int): Bilangan kedua.

    Returns:
        int: Nilai minimal dari a dan b.
    """
    return a if a < b else b

Minimal = minimal(10, 10)
print(Minimal)
