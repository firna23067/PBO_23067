# program_kalkulator.py

# Mengimpor fungsi dari modul_kalkulator
from modul_kalkulator import tambah, kurang, kali, bagi, pangkat, akar

def tampilkan_menu():
    """Menampilkan menu kalkulator."""
    print("\nKalkulator Sederhana")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Pangkat")
    print("6. Akar Kuadrat")
    print("7. Keluar")

def main():
    """Fungsi utama untuk menjalankan kalkulator."""
    while True:
        tampilkan_menu()
        
        # Memilih operasi
        pilihan = input("Pilih operasi (1/2/3/4/5/6/7): ")
        
        if pilihan == '7':
            print("Terima kasih telah menggunakan kalkulator!")
            break
        
        # Memasukkan angka
        try:
            if pilihan == '6':  # Untuk akar hanya membutuhkan satu angka
                angka1 = float(input("Masukkan angka: "))
                print(f"Hasil akar kuadrat dari {angka1} adalah: {akar(angka1)}")
            else:  # Untuk operasi lain membutuhkan dua angka
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == '1':
                    print(f"Hasil {angka1} + {angka2} = {tambah(angka1, angka2)}")
                elif pilihan == '2':
                    print(f"Hasil {angka1} - {angka2} = {kurang(angka1, angka2)}")
                elif pilihan == '3':
                    print(f"Hasil {angka1} * {angka2} = {kali(angka1, angka2)}")
                elif pilihan == '4':
                    print(f"Hasil {angka1} / {angka2} = {bagi(angka1, angka2)}")
                elif pilihan == '5':
                    print(f"Hasil {angka1} ^ {angka2} = {pangkat(angka1, angka2)}")
                else:
                    print("Pilihan tidak valid. Silakan pilih angka antara 1 sampai 7.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")

if __name__ == "__main__":
    main()
