# modul_kalkulator.py

def tambah(a, b):
    """Menambahkan dua angka."""
    return a + b

def kurang(a, b):
    """Mengurangi angka b dari angka a."""
    return a - b

def kali(a, b):
    """Mengalikan dua angka."""
    return a * b

def bagi(a, b):
    """Membagi angka a dengan b. Menangani pembagian dengan nol."""
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    return a / b

def pangkat(a, b):
    """Menghitung a pangkat b."""
    return a ** b

def akar(a):
    """Menghitung akar kuadrat dari a."""
    if a < 0:
        return "Error: Tidak dapat menghitung akar kuadrat dari angka negatif."
    return a ** 0.5
