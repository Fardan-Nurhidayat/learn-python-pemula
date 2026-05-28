nilai = -1

if nilai < 0:
    raise ValueError("Nilai tidak boleh negatif")

predikat = "Lulus" if nilai >= 70 else "Tidak Lulus"

print(f"Nilai: {nilai}")
print(f"Predikat: {predikat}")