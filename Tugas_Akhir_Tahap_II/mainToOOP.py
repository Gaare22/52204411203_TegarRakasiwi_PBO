import os
from random import randint
from prettytable import from_db_cursor
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "5220411203"
)

mycursor = mydb.cursor()

class User:
    def __init__(self):
        self.self = self
        
    def pemesanan(self, kode_pemesanan, id_user, kode_bandara, kode_jadwal, kode_kelas, jk, berangkat):
        sql = "INSERT INTO tb_pemesanan(kode_pemesanan, id_user1, kode_bandara, kode_jadwal, kode_kelas, jenis_kelamin1, berangkat) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (kode_pemesanan, id_user, kode_bandara, kode_jadwal, kode_kelas, jk, berangkat)
        mycursor.execute(sql, val)
        mydb.commit()

    def nama_pemesan(self, booking):
        sql = "SELECT id_user1 FROM tb_pemesanan WHERE kode_pemesanan = %s"
        val = (booking)
        mycursor.execute(sql,(val,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Nama                  = ",x[0])

    def jenis_kelamin(self, booking):
        sql = "SELECT jenis_kelamin1 FROM tb_pemesanan WHERE kode_pemesanan = %s"
        val = (booking)
        mycursor.execute(sql,(val,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Jenis Kelamin         = ",x[0])

    def tanggal_berangkat(self, booking):
        sql = "SELECT berangkat FROM tb_pemesanan WHERE kode_pemesanan = %s"
        val = (booking)
        mycursor.execute(sql,(val,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Tanggal Berangkat     = ",x[0])

    def relasi_kota_tujuan(self, booking):
        sql = "SELECT kota_tujuan FROM tb_pemesanan \
            INNER JOIN tb_tiket ON tb_pemesanan.kode_bandara = tb_tiket.kode_bandara WHERE kode_pemesanan = %s"
        val4 = (booking)
        mycursor.execute(sql,(val4,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Kota Tujuan           = ",x[0])

    def relasi_kelas(self, booking):
        sql5 = "SELECT kelas FROM tb_pemesanan \
            INNER JOIN tb_kelas ON tb_pemesanan.kode_kelas = tb_kelas.kode_kelas WHERE kode_pemesanan = %s"
        val5 = (booking)
        mycursor.execute(sql5,(val5,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Kelas                 = ",x[0])

    def relasi_jadwal(self, booking):
        sql6 = "SELECT jadwal FROM tb_pemesanan \
            INNER JOIN tb_jadwal ON tb_pemesanan.kode_jadwal = tb_jadwal.kode_jadwal WHERE kode_pemesanan = %s"
        val6 = (booking)
        mycursor.execute(sql6,(val6,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Jadwal                = ",x[0])

    def relasi_pukul(self, booking):
        sql = "SELECT pukul FROM tb_pemesanan \
            INNER JOIN tb_jadwal ON tb_pemesanan.kode_jadwal = tb_jadwal.kode_jadwal WHERE kode_pemesanan = %s"
        val6 = (booking)
        mycursor.execute(sql,(val6,))
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Pukul                 = ",x[0])

    def cetak_tiket(self):
        os.system('cls')
        print("Anda Memilih Menu Cetak Tiket Pesawat")
        print("-------------------------------------------------")
        booking = int(input("Masukkan Kode Booking Anda   : "))
        os.system('pause')
        os.system('cls')
        print("-------------------------------------")
        print("--------------- TIKET ---------------")
        print("-------------------------------------")            
        self.nama_pemesan(booking)
        self.jenis_kelamin(booking)
        self.tanggal_berangkat(booking)
        self.relasi_kota_tujuan(booking)
        self.relasi_kelas(booking)
        self.relasi_jadwal(booking)
        self.relasi_pukul(booking)
        print("-------------------------------------")
        print("-------------------------------------")
        os.system('pause')

    def batal_tiket(self):
        os.system('cls')
        print("Anda memilih menu Batalkan Tiket")
        print("-------------------------------------------------")
        batal_tiket = input("Masukkan kode booking Anda : ")
        os.system('pause')
        os.system('cls')
        batal=input("Lanjutkan Pembatalan [Y/T]    : ")
        if batal == 'Y' or batal == 'y':
            msql = "DELETE FROM tb_pemesanan WHERE kode_pemesanan = %s"
            myval = (batal_tiket,)
            mycursor.execute(msql,myval)
            mydb.commit()

            print("TIKET SUDAH DIBATALKAN")
            os.system('pause')

        elif batal == 'T' or batal == 't':
            print("CANCEL TIKET DI BATALKAN")
            os.system('pause')

class Databases:
    def __init__(self):
        self.self = self

    def tambah_user(self, nama, jk, brngkt):
        sql = "INSERT INTO tb_user (nama, jenis_kelamin, tanggal_keberangkatan) VALUES (%s,%s,%s)"
        val = (nama,jk,brngkt)
        mycursor.execute(sql,val)
        mydb.commit()

    def kota_tujuan(self):
        sql4 = "SELECT kota_tujuan FROM tb_tiket WHERE kode_bandara = %s"
        val4 = (kode_bandara,)
        mycursor.execute(sql4,val4)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Kota Tujuan           = ",x[0])
            break   

    def kelas(self):
        sql5 = "SELECT kelas FROM tb_kelas WHERE kode_kelas = %s"
        val5 = (kelas,)
        mycursor.execute(sql5,val5)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Kelas                 = ",x[0])

    def jadwal(self): #jadwal
        sql6 = "SELECT jadwal FROM tb_jadwal WHERE kode_jadwal = %s"
        val6 = (kode_jadwal,)
        mycursor.execute(sql6,val6)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Jadwal                = ",x[0])

    def harga(self): #harga
        sql = "SELECT harga FROM tb_kelas WHERE kode_kelas = %s"
        val = (kelas,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Harga                 =  Rp.",x[0])

    def pukul(self): #pukul
        sql = "SELECT pukul FROM tb_jadwal WHERE kode_jadwal = %s"
        val6 = (kode_jadwal,)
        mycursor.execute(sql,val6)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Pukul                 = ",x[0])

    def rupiah(self):
        sql = "SELECT harga FROM tb_kelas WHERE kode_kelas = %s"
        val = (kelas,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Rp. ",x[0])
        return x

    def ambil_nama(self):
        sql = "SELECT nama FROM tb_user WHERE nama = %s"
        val = (nama,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Nama Sebelumnya      = ", x[0])

    def ambil_jk(self):
        sql = "SELECT jenis_kelamin FROM tb_user WHERE jenis_kelamin = %s"
        val = (jk,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Jenis Kelamin Sebelumnya      = ", x[0])

    def ambil_tanggal(self):
        sql = "SELECT tanggal_keberangkatan FROM tb_user WHERE nama = %s"
        val = (nama,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Tanggal Keberangkatan Sebelumnya         = ", x[0])
            return x

    def ambil_kota(self):
        sql = "SELECT kota_tujuan FROM tb_tiket WHERE kode_bandara = %s"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Kota Tujuan Sebelumnya         = ", x[0])

    def ambil_kelas(self):
        sql = "SELECT kelas FROM tb_kelas WHERE kode_kelas = %s"
        val = (kelas,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Kelas Tujuan Sebelumnya         = ", x[0])

    def ambil_jadwal(self):
        sql = "SELECT pukul FROM tb_jadwal WHERE kode_jadwal = %s"
        val = (kode_jadwal,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Pukul Keberangkatan Sebelumnya         = ", x[0])

    def ubah_nama_user(self, namabaru, nama):
        sql = "UPDATE tb_user SET nama = %s WHERE nama = %s "
        val = (namabaru, nama)
        mycursor.execute(sql,val,)
        mydb.commit()

    def ubah_jk_user(self, jkbaru, jk):
        sql = "UPDATE tb_user SET jenis_kelamin = %s WHERE jenis_kelamin = %s "
        val = (jkbaru, jk)
        mycursor.execute(sql,val,)
        mydb.commit()

    def ubah_tanggal_user(self, brngktbaru, brngkt):
        sql = "UPDATE tb_user SET tanggal_keberangkatan = %s WHERE tanggal_keberangkatan = %s "
        val = (brngktbaru, brngkt)
        mycursor.execute(sql,val,)
        mydb.commit()

    def ubah_nama_tiket(self, noboking):
        namabaru = input('Masukkan Nama baru    : ')
        sql = "UPDATE tb_pemesanan SET id_user1 = %s WHERE kode_pemesanan = %s "
        val = (namabaru, noboking)
        mycursor.execute(sql,val,)
        mydb.commit()

    def ubah_jk_tiket(self, noboking):
        jkbaru = input('Masukkan Jenis Kelamin baru    : ')
        sql = "UPDATE tb_pemesanan SET jenis_kelamin1 = %s WHERE kode_pemesanan = %s "
        val = (jkbaru, noboking)
        mycursor.execute(sql,val,)
        mydb.commit()

    def ubah_tanggal_tiket(self, noboking):
        brngktbaru = input('Masukkan Tanggal Keberangkatan Baru : ')
        sql = "UPDATE tb_pemesanan SET berangkat = %s WHERE kode_pemesanan = %s "
        val = (brngktbaru, noboking)
        mycursor.execute(sql,val,)
        mydb.commit()

    def ubah_tujuan(self, noboking):
        print("\nDaftar Tujuan Pesawat")
        mycursor.execute("SELECT kode_bandara, kota_tujuan FROM tb_tiket")
        x = from_db_cursor(mycursor)
        print(x)        
        kode_bandara=input("\nMasukkan Kode Bandara Tujuan Anda           : ")

        os.system("pause")
        os.system("cls")

        print("\nDaftar Kelas Pesawat")
        sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        y = from_db_cursor(mycursor)
        print(y)        
        kelas=input("\nMasukkan Kode Kelas Pilihan Anda                 : ")
        
        os.system('pause')
        os.system("cls")

        print("\nJadwal Keberangkatan Pesawat")
        sql = "SELECT * FROM tb_jadwal WHERE kode_bandara = %s ORDER BY pukul"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        z = from_db_cursor(mycursor)
        print(z)        
        kode_jadwal = input("\nMasukkan Kode Jadwal Pilihan Anda           : ")

        sql = "UPDATE tb_pemesanan SET kode_bandara = %s, kode_jadwal = %s, kode_kelas = %s WHERE kode_pemesanan = %s"
        val = (kode_bandara, kode_jadwal, kelas, noboking)
        mycursor.execute(sql, val,)
        mydb.commit()

    def ubah_kelas(self, noboking):
        print('Ubah Kelas')
        print('-'*30)
        kode_bandara = input('Masukkan Kode Bandara Anda    : ')
        os.system('cls')
        print("Daftar Kelas Pesawat")
        sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        y = from_db_cursor(mycursor)
        print(y)        
        kelas=input("\nMasukkan Kode Kelas Pilihan Anda                 : ")
        
        os.system('pause')
        os.system("cls")

        print("\nJadwal Keberangkatan Pesawat")
        sql = "SELECT * FROM tb_jadwal WHERE kode_bandara = %s ORDER BY pukul"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        z = from_db_cursor(mycursor)
        print(z)        
        kode_jadwal = input("\nMasukkan Kode Jadwal Pilihan Anda           : ")

        sql = "UPDATE tb_pemesanan SET kode_jadwal = %s, kode_kelas = %s WHERE kode_pemesanan = %s"
        val = (kode_jadwal, kelas, noboking)
        mycursor.execute(sql, val,)
        mydb.commit()

    def ubah_jadwal(self, noboking):
        print('Ubah Jadwal')
        print('-'*30)
        kode_bandara = input('Masukkan Kode Bandara Anda    : ')
        os.system('cls')
        print("Jadwal Keberangkatan Pesawat")
        sql = "SELECT * FROM tb_jadwal WHERE kode_bandara = %s ORDER BY pukul"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        z = from_db_cursor(mycursor)
        print(z)        
        kode_jadwal = input("\nMasukkan Kode Jadwal Pilihan Anda           : ")

        sql = "UPDATE tb_pemesanan SET kode_jadwal = %s WHERE kode_pemesanan = %s"
        val = (kode_jadwal, noboking)
        mycursor.execute(sql, val,)
        mydb.commit()


def menu():
    os.system('cls')
    print("======================================")
    print("|           SELAMAT DATANG           |")
    print("|    LOKET PENJUALAN TIKET PESAWAT   |")
    print("|       PT. PESAWAT KITA SEMUA       |")
    print("|  BANDARA INTERNASIONAL YOGYAKARTA  |")
    print("======================================")
    print("\nMenu :")
    print("--------------------")
    print("1. Pesan Tiket")
    print("2. Cetak Tiket")
    print("3. Update Data Tiket")
    print("4. Batalkan Tiket")
    print("0. Keluar")

control_database = Databases()
while True:
    menu()
    pilih = int(input("Pilih menu yang diinginkan   : "))

    if pilih == 1:
        os.system('cls')
        print("Anda Memilih Menu Beli Tiket Pesawat")
        print("--------------------------------------")
        nama = input("Masukkan Nama Anda                            : ")
        untuk_jk = True
        while untuk_jk:
            jk = input("Masukkan Jenis Kelamin [L/P]                  : ")
            if jk == 'L' or jk == 'l':
                jk = "Laki-laki"
                break
            elif jk == 'P' or jk == 'p':
                jk = "Perempuan"
                break
            else:
                print("Kode yang Anda Masukkan Salah")
        brngkt = input("Masukkan Tanggal Keberangkatan [yyyy/mm/dd]   : ")
        
        control_database.tambah_user(nama, jk, brngkt)

        os.system("pause")
        os.system("cls")

        print("\nDaftar Tujuan Pesawat")
        mycursor.execute("SELECT kode_bandara, kota_tujuan FROM tb_tiket")
        x = from_db_cursor(mycursor)
        print(x)        
        kode_bandara=input("\nMasukkan Kode Bandara Tujuan Anda           : ")

        os.system("pause")
        os.system("cls")

        print("\nDaftar Kelas Pesawat")
        sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        y = from_db_cursor(mycursor)
        print(y)        
        kelas=input("\nMasukkan Kode Kelas Pilihan Anda                 : ")
        
        os.system('pause')
        os.system("cls")

        print("\nJadwal Keberangkatan Pesawat")
        sql = "SELECT * FROM tb_jadwal WHERE kode_bandara = %s ORDER BY pukul"
        val = (kode_bandara,)
        mycursor.execute(sql,val)
        z = from_db_cursor(mycursor)
        print(z)        
        kode_jadwal = input("\nMasukkan Kode Jadwal Pilihan Anda           : ")

        os.system('pause')
        os.system("cls")

        oke=True
        while oke :
            os.system('cls')
            print("----------------------------------------")
            print("             DATA PEMESANAN             ")
            print("----------------------------------------")
            print("Nama                  = ",nama)
            print("Jenis Kelamin         = ",jk)
            print("Tanggal Keberangkatan = ",brngkt)
            control_database.kota_tujuan()
            control_database.kelas()
            control_database.jadwal()
            control_database.pukul()
            control_database.harga()

            print("---------------------------")
            pilih2=input("\nApakah Data Sudah Benar? [Y/T]     : ")
            if pilih2 == 'Y' or pilih2 == 'y':
                os.system("pause")
                oke=False
            elif pilih2 == 'T' or pilih2 == 't':
                os.system('pause')
                os.system("cls")
                print("Ubah Data :")
                print("--------------")
                print("1. Nama")
                print("2. Jenis Kelamin")
                print("3. Tanggal Keberangkatan")
                print("4. Kota Tujuan")
                print("5. Kelas")
                print("6. Jadwal Keberangkatan")
                print("0. Kembali")
                print("--------------")
                pilih3=int(input("Masukkan Data yang ingin di ubah : "))
                if pilih3 == 1:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Nama ")
                    print("-------------")
                    control_database.ambil_nama()
                    print("-------------")
                    namabaru=input("Nama Baru            : ")

                    control_database.ubah_nama_user(namabaru, nama)

                    nama = namabaru

                elif pilih3 == 2:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Jenis Kelamin ")
                    print("-------------")
                    control_database.ambil_jk()
                    print("-------------")
                    jkbaru=input("Jenis Kelamin Baru            : ")

                    control_database.ubah_jk_user(jkbaru, jk)

                    jk = jkbaru

                elif pilih3 == 3:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Tanggal Keberangkatan ")
                    print("-------------")
                    control_database.ambil_tanggal()
                    print("-------------")
                    brngktbaru=input("Tanggal Keberangkatan Baru               : ")

                    control_database.ubah_tanggal_user(brngktbaru, brngkt)

                    brngkt = brngktbaru

                elif pilih3 == 4:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Kota Tujuan ")
                    print("-------------")
                    control_database.ambil_kota()
                    print("-------------")
                    mycursor.execute("SELECT kode_bandara, kota_tujuan FROM tb_tiket")
                    x = from_db_cursor(mycursor)
                    print(x)        
                    kode_bandara_baru=input("\nMasukkan Kode Bandara Tujuan Anda           : ")
                    kode_bandara = kode_bandara_baru

                    os.system('pause')
                    os.system("cls")

                    print("\nDaftar Kelas Pesawat")
                    sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    y = from_db_cursor(mycursor)
                    print(y)        
                    kelas_baru=input("Masukkan Kode Kelas Pilihan Anda                 : ")
                    kelas = kelas_baru
                    
                    os.system('pause')
                    os.system("cls")

                    print("\nJadwal Keberangkatan Pesawat")
                    sql = "SELECT * FROM tb_jadwal WHERE kode_bandara = %s ORDER BY pukul"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    z = from_db_cursor(mycursor)
                    print(z)        
                    kode_jadwal_baru = input("\nMasukkan Kode Jadwal Pilihan Anda           : ")
                    kode_jadwal = kode_jadwal_baru

                elif pilih3 == 5:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Kelas ")
                    print("-------------")
                    control_database.ambil_kelas()
                    print("-------------")
                    sql = "SELECT kode_kelas, kelas, harga FROM tb_kelas WHERE kode_bandara = %s"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    y = from_db_cursor(mycursor)
                    print(y)        
                    kelasbaru = input("Masukkan Kode Kelas Pilihan Anda                 : ")
                    kelas = kelasbaru
                elif pilih3 == 6:
                    os.system('pause')
                    os.system("cls")
                    print("Ubah Jadwal ")
                    print("-------------")
                    control_database.ambil_jadwal()
                    print("-------------")
                    sql = "SELECT * FROM tb_jadwal WHERE kode_bandara = %s ORDER BY pukul"
                    val = (kode_bandara,)
                    mycursor.execute(sql,val)
                    z = from_db_cursor(mycursor)
                    print(z)        
                    kode_jadwal_baru = input("\nMasukkan Kode Jadwal Pilihan Anda           : ")
                    kode_jadwal = kode_jadwal_baru
                elif pilih3 == 0:
                    oke
                else:
                    print("OK")
                    break
            else:
                print("KODE SALAH")

        os.system('cls')
        beli=input("Lanjutkan Pembelian [Y/T]    : ")
        print("----------------------------------------")
        
        if beli == 'Y' or beli == 'y':
            os.system("cls")
            print("Menu Pembayaran")
            print("-----------------")
            print("\nTagihan Anda     ")
            print("-----------------")
            harga = control_database.rupiah()
            print("-----------------")
            # print(type(harga)) #tuple
            values = ','.join(str(v) for v in harga)
            # print(type(values)) #str
            h = int(values)
            # print(type(h)) #int

            kurang = True
            while kurang:
                uang=int(input("\nMasukkan Nominal Uang            = Rp. "))
                if uang < h:
                    print("Maaf Uang Anda Kurang") 
                elif uang == h:
                    print("-------------------------------------------------")
                    print("Uang Anda                        = Rp. ", uang)
                    print("Jumlah yang harus di bayar       = Rp. ", h)
                    print("-------------------------------------------------")
                    print("Uang Pas, Tidak ada Kembalian")
                    os.system('pause')
                    break
                else:
                    kembali = uang - h
                    print("-------------------------------------------------")
                    print("Uang Anda                        = Rp. ", uang)
                    print("Jumlah yang harus di bayar       = Rp. ", h)
                    print("-------------------------------------------------")
                    print("Kembalian                        = ",kembali)
                    os.system('pause')
                    break
        elif beli == 'T' or beli =='t':
            break
        else:
            print("Kode Salah, Silahkan pilih Y/T")

        os.system('cls')
        bil = randint(0,1000)
        print("-------------------------------")
        print("Pembelian Anda Telah Berhasil")
        print("-------------------------------")
        os.system('pause')
        os.system('cls')
        print("-------------------------------------")
        print("--------------- TIKET ---------------")
        print("-------------------------------------")
        print("Nama                  = ",nama)
        print("Jenis Kelamin         = ",jk)
        print("Tanggal Keberangkatan = ",brngkt)
        control_database.kota_tujuan()
        control_database.kelas()
        control_database.jadwal()
        control_database.pukul()
        control_database.harga()
        print("KODE BOOKING          = ",bil)
        print("-------------------------------------")
        print("-------------------------------------")
        os.system('pause')
        
        input_pemesanan = User()
        input_pemesanan.pemesanan(bil,nama,kode_bandara,kode_jadwal,kelas,jk,brngkt)

    elif pilih == 2:
        User().cetak_tiket()

    elif pilih == 3:
        os.system('cls')
        print("Anda Memilih Menu Ubah Data Tiket Pesawat")
        print("-------------------------------------------------")
        booking = int(input("Masukkan Kode Booking Anda   : "))
        os.system('pause')
        os.system('cls')
        print("Pilih Data yang akan diubah")
        print("--------------")
        print("1. Nama")
        print("2. Jenis Kelamin")
        print("3. Tanggal Keberangkatan")
        print("4. Kota Tujuan")
        print("5. Kelas")
        print("6. Jadwal Keberangkatan")
        print("0. Kembali")
        print("--------------")
        pilih=int(input("Masukkan Data yang ingin di ubah : "))
        if pilih == 1:
            control_database.ubah_nama_tiket(booking)
        elif pilih == 2:
            control_database.ubah_jk_tiket(booking)
        elif pilih == 3:
            control_database.ubah_tanggal_tiket(booking)
        elif pilih == 4:
            control_database.ubah_tujuan(booking)
        elif pilih == 5:
            control_database.ubah_kelas(booking)
        elif pilih == 6:
            control_database.ubah_jadwal(booking)
        elif pilih == 0:
            break
        else:
            print('Kode Error')
            os.system('pause')

    elif pilih == 4:
        User().batal_tiket()

    elif pilih == 0:
        print("Terimakasih Telah Menggunakan Program Ini")
        break

    else:
        print("MAAF, KODE SALAH")