# Inisialisasi variabel max
max_value = float('-inf')

while True:
    # Meminta input bilangan dari pengguna
    number = int(input("Masukkan bilangan (0 untuk berhenti): "))
    
    # Jika bilangan adalah 0, keluar dari loop
    if number == 0:
        break
    
    # Cek apakah bilangan lebih besar dari max_value
    if number > max_value:
        max_value = number

# Memeriksa apakah ada bilangan yang dimasukkan
if max_value == float('-inf'):
    print("Tidak ada bilangan yang dimasukkan.")
else:
    print(f"Bilangan terbesar adalah: {max_value}")
