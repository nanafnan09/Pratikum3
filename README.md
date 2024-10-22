# Pratikum 3 - Tipe Data, Variable, dan Operator

Nama: Afnan Dika Ramadhan

Kelas: TI.24.5

NIM 312410510 

Mata Kuliah : Bahasa Pemograman


## Mencari bilangan terbesar dari bilangan yang di inputkan
Program ini menentukan bilangan terbesar dari serangkaian bilangan yang di inputkan hingga input 0. Program ini mengunakan loop `while` dan kondisi `if` untuk memperbarui nilai terbesar  yang ditemukan.

## Flowchart Program
![Foto](https://github.com/nanafnan09/FLOWCHART/blob/04aa09acb19d1b0177ff78185162af8aa4b56d68/WhatsApp%20Image%202024-10-21%20at%2020.57.07.jpeg)

## Kode Program
```python
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

else:
    print(f"Bilangan terbesar adalah: {max_value}")
```
## Penjelasan Kode Program

```python

