import os

# Class Induk
class Lingkungan:
    def __init__(self, location, pollution_level):
        self.location = location
        self._pollution_level = pollution_level

    def measure_pollution(self):
        # Implementasi pengukuran polusi
        pass

    def display_info(self):
        print('-'*30)
        print("Lokasi                      : ", self.location)
        print("Persentase Polusi           : ", self._pollution_level)


# Anak class pertama
class Kualitas_Udara(Lingkungan):
    def __init__(self, location, pollution_level, air_quality):
        super().__init__(location, pollution_level)
        self.air_quality = air_quality

    def display_info(self):
        super().display_info()
        print("Persentase Kualitas Udara   : ", self.air_quality)
        

# Anak class kedua
class Kualitas_Air(Lingkungan):
    def __init__(self, location, pollution_level, water_turbidity):
        super().__init__(location, pollution_level)
        self.water_turbidity = water_turbidity

    def display_info(self):
        super().display_info()
        print("Persentase Kekeruhan Air    : ", self.water_turbidity)
        


# Anak class dari Kualitas_Air
class Pemurnian_Air(Kualitas_Air):
    def __init__(self, location, pollution_level, water_turbidity, water_purity):
        super().__init__(location, pollution_level, water_turbidity)
        self.water_purity = water_purity


    # Overloading display_info method with an additional parameter
    def display_info(self, include_purity=True):
        super().display_info()
        if include_purity:
            print("Persentase Pemurnian Air    : ", self.water_purity)


# Fungsi untuk membuat objek Kualitas_Udara dari input pengguna
def create_air_quality():
    location = input("Masukkan Lokasi                     : ")
    pollution_level = int(input("Masukkan Persentase Polusi          : "))
    air_quality = int(input("Masukkan Persentase Kualitas Udara  : "))
    return Kualitas_Udara(location, pollution_level, air_quality)


# Fungsi untuk membuat objek Kualitas_Air dari input pengguna
def create_water_quality():
    location = input("Masukkan Lokasi                     : ")
    pollution_level = int(input("Masukkan Persentase Polusi          : "))
    water_turbidity = int(input("Masukkan Persentase Kekeruhan Air   : "))
    return Kualitas_Air(location, pollution_level, water_turbidity)


# Fungsi untuk membuat objek Pemurnian_Air dari input pengguna
def create_water_purity():
    location = input("Masukkan Lokasi                     : ")
    pollution_level = int(input("Masukkan Persentase Polusi          : "))
    water_turbidity = int(input("Masukkan Persentase Kekeruhan Air   : "))
    water_purity = int(input("Masukkan Persentase Pemurnian Air   : "))
    return Pemurnian_Air(location, pollution_level, water_turbidity, water_purity)


# Fungsi untuk menampilkan menu CRUD
def display_menu():
    os.system('cls')
    print("\nMENU:")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")


# Fungsi utama
def main():
    environmental_objects = []

    while True:
        display_menu()
        choice = input("Masukkan Pilihan Anda : ")

        if choice == '1':  # Create
            while True:
                print("\nTipe yang ingin Dibuat : ")
                print("1. Kualitas Udara")
                print("2. Kualitas Air")
                print("3. Pemurnian Air")
                print('0. Kembali')
                type_choice = input("Masukkan Pilihan Anda : ")

                if type_choice == '1':
                    air_quality = create_air_quality()
                    environmental_objects.append(air_quality)
                elif type_choice == '2':
                    water_quality = create_water_quality()
                    environmental_objects.append(water_quality)
                elif type_choice == '3':
                    water_purity = create_water_purity()
                    environmental_objects.append(water_purity)
                elif type_choice == '0':
                    break
                else:
                    print("Kode Error")
                    os.system('pause')

        elif choice == '2':  # Read
            os.system('cls')
            print("\nData Objek Lingkungan:")
            for obj in environmental_objects:
                obj.display_info()

            os.system('pause')

        elif choice == '3':  # Update
            os.system('cls')
            print("\nPilih Data Baru:")
            print("1. Kualitas_Udara")
            print("2. Kualitas_Air")
            print("3. Pemurnian_Air")
            type_choice = input("Masukkan Pilihan Anda : ")

            if type_choice in ['1', '2', '3']:
                print("\nMengubah Data Kesehatan Lingkungan : ")
                index = int(input("Pilih Objek Lingkungan yang akan diperbaharui : "))
                index = index - 1
                if 0 <= index < len(environmental_objects):
                    if type_choice == '1':
                        air_quality = create_air_quality()
                        environmental_objects[index] = air_quality
                        print('Berhasil Diubah')
                        os.system('pause')
                    elif type_choice == '2':
                        water_quality = create_water_quality()
                        environmental_objects[index] = water_quality
                        print('Berhasil Diubah')
                        os.system('pause')
                    elif type_choice == '3':
                        water_purity = create_water_purity()
                        environmental_objects[index] = water_purity
                        print('Berhasil Diubah')
                        os.system('pause')
                else:
                    print("Kode Error")
                    os.system('pause')
            else:
                print("Kode error")
                os.system('pause')

        elif choice == '4':  # Delete
            os.system('cls')
            print("\nMenghapus Objek Lingkungan")
            index = int(input("Masukkan Objek yang ingin di Hapus : "))
            index = index - 1
            if 0 <= index < len(environmental_objects):
                del environmental_objects[index]
                print("Objek Berhasil di hapus")
                os.system('pause')
            else:
                print("Kode Error")
                os.system('pause')
        elif choice == '5':  # Exit
            print("Exiting program. Goodbye!")
            break

        else:
            print("Kode Error.")
            os.system('pause')


if __name__ == "__main__":
    main()
