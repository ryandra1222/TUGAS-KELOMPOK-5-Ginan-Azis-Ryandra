def main():
    try:
        max_tingkat = int(input("Masukkan tingkat maksimum: "))
        for i in range(1, max_tingkat + 1):
            print("#" * i)
    except ValueError:
        print("Masukan harus berupa bilangan bulat.")

if __name__ == "__main__":
    main()
    
#Muhammad Abdul Azis - I.2210374
#Ginan Ardiansah - I.2210124
#Ryandra Putra - I.2210358