print("=" * 50)
print("DEMONSTRASI IMMUTABLE vs MUTABLE")
print("=" * 50)

print("\n1. INTEGER (IMMUTABLE)")
print("-" * 50)
a = 10
print(f"a = 10")
print(f"  id(a) = {id(a)}")
print(f"  type(a) = {type(a)}")

b = a
print(f"\nb = a")
print(f"  id(a) = {id(a)}")
print(f"  id(b) = {id(b)}")
print(f"  id(a) == id(b): {id(a) == id(b)}")

a = 11
print(f"\na = 11  (REASSIGN)")
print(f"  id(a) = {id(a)}  ← BERUBAH!")
print(f"  id(b) = {id(b)}")
print(f"  id(a) == id(b): {id(a) == id(b)}")
print(f"  Nilai a: {a}, Nilai b: {b}")

print("\n" + "=" * 50)
print("2. LIST (MUTABLE)")
print("-" * 50)
x = [1, 2, 3]
print(f"x = [1, 2, 3]")
print(f"  id(x) = {id(x)}")
print(f"  type(x) = {type(x)}")

y = x
print(f"\ny = x")
print(f"  id(x) = {id(x)}")
print(f"  id(y) = {id(y)}")
print(f"  id(x) == id(y): {id(x) == id(y)}")

x[0] = 99
print(f"\nx[0] = 99  (MODIFY)")
print(f"  id(x) = {id(x)}  ← TETAP SAMA!")
print(f"  id(y) = {id(y)}")
print(f"  id(x) == id(y): {id(x) == id(y)}")
print(f"  Nilai x: {x}, Nilai y: {y}")

print("\n" + "=" * 50)
print("KESIMPULAN:")
print("-" * 50)
print("Integer:  Reassign → Object BARU, id BERUBAH")
print("List:     Modify   → Object SAMA, id TETAP")
print("=" * 50)