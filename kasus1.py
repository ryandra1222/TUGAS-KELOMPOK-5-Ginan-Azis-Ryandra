
import math

def main_menu():
    print("=== Aplikasi Perhitungan Bangun Ruang ===")
    print("1. Bola")
    print("2. Kubus")
    print("3. Balok")
    print("4. Keluar")

def bola_menu():
    print("\n=== Pilihan Bola ===")
    print("1. Keliling")
    print("2. Luas Permukaan")
    print("3. Volume")

def kubus_menu():
    print("\n=== Pilihan Kubus ===")
    print("1. Keliling")
    print("2. Luas Permukaan")
    print("3. Volume")

def balok_menu():
    print("\n=== Pilihan Balok ===")
    print("1. Keliling")
    print("2. Luas Permukaan")
    print("3. Volume")

def hitung_keliling_bola(jari_jari):
    return 2 * math.pi * jari_jari

def hitung_luas_permukaan_bola(jari_jari):
    return 4 * math.pi * jari_jari ** 2

def hitung_volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3

def hitung_keliling_kubus(sisi):
    return 12 * sisi

def hitung_luas_permukaan_kubus(sisi):
    return 6 * sisi ** 2

def hitung_volume_kubus(sisi):
    return sisi ** 3

def hitung_keliling_balok(panjang, lebar, tinggi):
    return 4 * (panjang + lebar + tinggi)

def hitung_luas_permukaan_balok(panjang, lebar, tinggi):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def main():
    while True:
        main_menu()
        choice_main = input("Pilih bangun ruang (1/2/3/4): ")
        
        if choice_main == '1':
            bola_menu()
            choice_bola = input("Pilih jenis perhitungan (1/2/3): ")
            if choice_bola == '1':
                jari_jari = float(input("Masukkan jari-jari bola: "))
                print("Keliling bola adalah:", hitung_keliling_bola(jari_jari))
            elif choice_bola == '2':
                jari_jari = float(input("Masukkan jari-jari bola: "))
                print("Luas permukaan bola adalah:", hitung_luas_permukaan_bola(jari_jari))
            elif choice_bola == '3':
                jari_jari = float(input("Masukkan jari-jari bola: "))
                print("Volume bola adalah:", hitung_volume_bola(jari_jari))
            else:
                print("Pilihan tidak valid.")
        
        elif choice_main == '2':
            kubus_menu()
            choice_kubus = input("Pilih jenis perhitungan (1/2/3): ")
            if choice_kubus == '1':
                sisi = float(input("Masukkan panjang sisi kubus: "))
                print("Keliling kubus adalah:", hitung_keliling_kubus(sisi))
            elif choice_kubus == '2':
                sisi = float(input("Masukkan panjang sisi kubus: "))
                print("Luas permukaan kubus adalah:", hitung_luas_permukaan_kubus(sisi))
            elif choice_kubus == '3':
                sisi = float(input("Masukkan panjang sisi kubus: "))
                print("Volume kubus adalah:", hitung_volume_kubus(sisi))
            else:
                print("Pilihan tidak valid.")
        
        elif choice_main == '3':
            balok_menu()
            choice_balok = input("Pilih jenis perhitungan (1/2/3): ")
            if choice_balok == '1':
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                print("Keliling balok adalah:", hitung_keliling_balok(panjang, lebar, tinggi))
            elif choice_balok == '2':
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                print("Luas permukaan balok adalah:", hitung_luas_permukaan_balok(panjang, lebar, tinggi))
            elif choice_balok == '3':
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                print("Volume balok adalah:", hitung_volume_balok(panjang, lebar, tinggi))
            else:
                print("Pilihan tidak valid.")
        
        elif choice_main == '4':
            print("Terima kasih telah menggunakan aplikasi.")
            break
        
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()

#Muhammad Abdul Azis - I.2210374
#Ginan Ardiansah - I.2210124
#Ryandra Putra - I.2210358
