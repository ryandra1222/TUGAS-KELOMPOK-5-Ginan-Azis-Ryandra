def main():
    try:
        banyak_pengulangan = int(input("Masukkan banyak pengulangan: "))
        for i in range(banyak_pengulangan):
            print("number", i)
    except ValueError:
        print("Masukan harus berupa bilangan bulat.")

if __name__ == "__main__":
    main()

#Muhammad Abdul Azis - I.2210374
#Ginan Ardiansah - I.2210124
#Ryandra Putra - I.2210358