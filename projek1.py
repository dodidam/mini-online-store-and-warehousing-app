data_barang = [
    {'sku':'JCDS01','nama':'Tumbler','stok':20,'harga':10000,'warna':'black'},
    {'sku':'JCDS02','nama':'Jaket','stok':25,'harga':15000,'warna':'black'},
    {'sku':'JCDS03','nama':'Nametag','stok':30,'harga':25000,'warna':'tosca'},
    {'sku':'JCDS04','nama':'Goodiebag','stok':35,'harga':30000,'warna':'cream'},
    {'sku':'JCDS05','nama':'Greeting Card','stok':40,'harga':35000,'warna':'white'}
]

list_admin =[
            {'username':'idamahmadi','password':'idam12'},
            {'username':'purwadhika','password':'pwdhkbtm'}
            ]


# Function
def list_menu(): 

    print(f'''
Selamat Datang di Gudang Rusunawa Kabil

        List Menu :
        1. Menampilkan Daftar Barang
        2. Menambah Barang
        3. Mengubah Barang
        4. Menghapus Barang
        5. Exit Program
''')

def menu1(): 

    while True:
        print('''
Menu Menampilkan Data Barang :

        1. Tampilkan Semua Data
        2. Cari Spesifik
        3. Kembali ke Menu Awal
    ''')
        menu=input('Masukan angka Menu yang ingin dijalankan : ')      
        
        if menu == '1':
            daftar_barang()

        elif menu == '2':
            cari_barang()    

        elif menu == '3':
            main_menu()

        else:
            print('\nHarap masukan angka sesuai menu')
            continue

def menu2(): 

    while True:
        print('''
Menu Menambahkan Barang Gudang :

        1. Tambahkan Barang
        2. Kembali ke Menu Awal
    ''')
        menu=input('Masukan angka Menu yang ingin dijalankan : ')      
        
        if menu == '1':
            tambah_barang()

        elif menu == '2':
            main_menu()    

        else:
            print('\nHarap masukan angka sesuai menu')
            continue

def menu3(): 

    while True:
        print('''
Menu Mengubah Barang Barang :

        1. Ubah Barang Gudang
        2. Kembali ke Menu Awal
    ''')
        menu=input('Masukan angka Menu yang ingin dijalankan : ')      
        
        if menu == '1':
            ubah_barang()

        elif menu == '2':
            main_menu()    

        else:
            print('\nHarap masukan angka sesuai menu')
            continue

def menu4(): 

    while True:
        print('''
Menu Menghapus Barang Barang :

        1. Hapus Barang Gudang
        2. Kembali ke Menu Awal
    ''')
        menu=input('Masukan angka Menu yang ingin dijalankan : ')      
        
        if menu == '1':
            hapus_barang()

        elif menu == '2':
            main_menu()    

        else:
            print('\nHarap masukan angka sesuai menu')
            continue

def daftar_barang():

    if data_barang == []:

        print('\nBelum ada data untuk ditampilkan')
        menu1()
    
    else:

        print('\nDaftar barang')
        print(f'{"No":<3}| {"Nama":<14}| {"Stok":<6}| {"Harga":<7}| {"Warna":<9}| {"SKU":<14}')
        
        for i in range(len(data_barang)):
            
            nama = data_barang[i]['nama']
            stok = data_barang[i]['stok']
            harga = data_barang[i]['harga']
            warna = data_barang[i]['warna']
            sku = data_barang[i]['sku']
            print(f'{i+1:<3}| {nama:<14}| {stok:<6}| {harga:<7}| {warna:<9}| {sku:<14}')
        
def cari_barang():

    barang=input('Masukan nama / sku barang yang ingin dicari : ')
    print('\nHasil pencarian')
    print(f'{"No":<3}| {"Nama":<14}| {"Stok":<6}| {"Harga":<7}| {"Warna":<9}| {"SKU":<14}')
    
    for i in range(len(data_barang)):

        nama = data_barang[i]['nama']
        sku = data_barang[i]['sku']

        if nama == barang or sku == barang: 

            stok = data_barang[i]['stok']
            harga = data_barang[i]['harga']
            warna = data_barang[i]['warna']
            
            print(f'{i+1:<3}| {nama:<14}| {stok:<6}| {harga:<7}| {warna:<9}| {sku:<14}')
        
        else:
            continue

        menu1()
    
    print('Maaf barang yang anda cari belum ditemukan')
    menu1()

def tambah_barang():

    sku_baru=input('Masukan SKU Barang : ')

    for i in range(len(data_barang)):

        sku = data_barang[i]['sku']

        if sku == sku_baru:

            print('\nData sudah ada, masukan yang lain')
            menu2()

        else:
            continue 

    nama=input('Masukan Nama Barang : ')
    stok=int(input('Masukan Stok Barang : '))
    harga=int(input('Masukan Harga Beli Barang : '))
    warna=input('Masukan Warna : ')
    barangbaru = {'sku':sku_baru,'nama':nama,'stok':stok,'harga':harga, 'warna':warna}

    while True:

        konfirmasi=input('\nApakah anda yakin ingin menyimpan data ini? \nketik (Ya/Tidak) : ')
    
        if konfirmasi.lower() == 'ya':

            data_barang.append(barangbaru) 

            print('\nBarang berhasil ditambahkan')
            menu2()

        elif konfirmasi.lower() == 'tidak':
            print('\nPenambahan data telah dibatalkan')
            menu2()

        else :
            print('\nHarap masukan perintah sesuai instruksi')
            continue

def ubah_barang():

    # bisa disederhanakn
    
    sku_barang=input('Masukan SKU Barang : ')

    for i in range(len(data_barang)):

        sku = data_barang[i]['sku']

        if sku == sku_barang:

            nama = data_barang[i]['nama']
            stok = data_barang[i]['stok']
            harga = data_barang[i]['harga']
            warna = data_barang[i]['warna']

            print('\nHasil pencarian')
            print(f'{"No":<3}| {"Nama":<14}| {"Stok":<6}| {"Harga":<7}| {"Warna":<9}| {"SKU":<14}')
            print(f'{i+1:<3}| {nama:<14}| {stok:<6}| {harga:<7}| {warna:<9}| {sku:<14}')
            
            kolom=input('\nMasukan kolom yang ingin diubah : ')
            
            if kolom in data_barang[i].keys():
                
                value_baru = input('Masukan value : ')

                if value_baru.isnumeric() == True:
                
                    value_baru = int(value_baru)
                    print('\nJumlah diubah')
                    
                else:
                    print('\nKeterangan diubah')

                data_barang[i][f'{kolom}'] = value_baru
                print('Update data berhasil')
                menu3()                
                
            else:                 

                print('\nKolom tidak ditemukan')
                menu3()
            
        else:
            continue
            
    print('\nBarang/SKU tidak ditemukan')
    menu3()            
    
def hapus_barang():
    
     # bisa disederhanakn
    
    sku_barang=input('Masukan SKU Barang : ')

    for i in range(len(data_barang)):

        sku = data_barang[i]['sku']

        if sku == sku_barang:

            nama = data_barang[i]['nama']
            stok = data_barang[i]['stok']
            harga = data_barang[i]['harga']
            warna = data_barang[i]['warna']

            print('\nHasil pencarian')
            print(f'{"No":<3}| {"Nama":<14}| {"Stok":<6}| {"Harga":<7}| {"Warna":<9}| {"SKU":<14}')
            print(f'{i+1:<3}| {nama:<14}| {stok:<6}| {harga:<7}| {warna:<9}| {sku:<14}')
            
            while True:

                konfirmasi=input('\nApakah anda yakin ingin menyimpan data ini? \nketik (Ya/Tidak) : ')
        
                if konfirmasi.lower() == 'ya':
                    data_barang.pop(i)
                    print('\nBarang berhasil dihapus')
                    menu4()

                elif konfirmasi.lower() == 'tidak':
                    print('\nBarang tidak jadi dihapus')
                    menu4()

                else:
                    print('\nMasukan perintah sesua instruksi')
                    continue
        
        else:
            continue
                
    print('\nBarang/SKU tidak ditemukan')
    menu4()

def beli_barang():
    
    global list_pesanan
    global list_jumlah
    global total_harga
    
    while True:

        nomor = int(input('\nMasukan Nomor barang yang ingin dibeli : '))
        indexing = nomor - 1
        jumlah = int(input('Masukan Jumlah barang yang ingin dibeli : '))
        
        if indexing in list_pesanan:
            print('\nKamu sudah pesan barang ini, selesaikan/batalkan pembayaran terlebih dahulu')
            beli_lagi()

        elif indexing >= len(data_barang) :
            print(f'\nNomer tidak terdaftar, silahkan coba lagi')
            continue

        else:
        
            nama = data_barang[indexing]['nama']
            stok = data_barang[indexing]['stok']
            harga = data_barang[indexing]['harga']

            if jumlah > stok :
                print(f'\nStok tidak cukup, stok {nama} tinggal {stok}')
                continue

            else :
                
                print(f'\n{"Nama":<9}| {"Jumlah":<9}| {"Harga":<9}')
                
                list_pesanan.append(indexing)
                list_jumlah.append(jumlah)
                
                for i in range(len(list_pesanan)):
                    
                    jumlah = list_jumlah[i]
                    indexing = list_pesanan[i]
                    nama = data_barang[indexing]['nama']
                    harga = data_barang[indexing]['harga']
                    print(f'{nama:<9}| {jumlah:<9}| {jumlah*harga:<9}')

                total_harga += jumlah*harga
                beli_lagi()

def beli_lagi():

    while True:

        beli_lagi = input('\nMau beli yang lain? (ya/tidak) : ')
        
        if beli_lagi == 'ya':
            beli_barang()

        elif beli_lagi == 'tidak':

            print(f'\nTotal Harga yang Harus Dibayar = {total_harga}')
            jum_uang=int(input('Masukan Jumlah Uang Anda : '))

            if jum_uang < total_harga:
                print(f'\nTransaksi anda dibatalkan \nuang kurang sebesar {total_harga-jum_uang}')
                menu_login()


            elif jum_uang == total_harga:
                print(f'\nTerimakasih uang anda pas')
                update_stock()

            else:
                print(f'\nTerimakasih telah berbelanja \nuang kembali anda {jum_uang-total_harga}')
                update_stock()

        else :
            print(f'\nHarap ketik sesuai petunjuk')
            continue

def update_stock() :

    global list_pesanan
    global list_jumlah

    for i in range(len(list_pesanan)):

        indexing = list_pesanan[i]
        jumlah = list_jumlah[i]

        data_barang[indexing]['stok'] -= jumlah

    menu_login()

def main_menu():
    
    while True:

        list_menu()
        menu=input('Masukan angka Menu yang ingin dijalankan : ')      

        if menu == '1':

            menu1()

        elif menu == '2':
            
            menu2()

        elif menu == '3':
            menu3()

        elif menu == '4':
            menu4()

        elif menu == '5':
            menu_login() # <- seleesaikan section ini dan kembali ke section sebelumnya(?)

        else:
            print('Masukan angka sesua intruksi')
            continue

def menu_login():

    while True:

        print('''
        
Selamat datang, apa yang kamu cari?
    
        1. Log in sebagai admin gudang
        2. Membeli merchandise kami
        ''')

        menu=input('Masukan angka Menu yang ingin dijalankan : ')      
        
        if menu == '1':

            username_input = input('\nMasukan username admin kamu : ')
            password_input = input('Masukan password admin kamu : ')

            list_username = [list_admin[i]['username'] for i in range(len(list_admin))]
            list_password = [list_admin[i]['password'] for i in range(len(list_admin))]            

            if username_input in list_username:
                
                index_password = list_username.index(username_input)
                password = list_password[index_password]
                
                if password_input == password:

                    main_menu()

                else :

                    print('\nUsername/password yang anda masukan salah, harap coba kembali')
                    continue

            else :

                print('\nUsername/password yang anda masukan salah, harap coba kembali')
                continue

        elif menu == '2':
            global list_pesanan
            global list_jumlah
            global total_harga
            list_pesanan = []
            list_jumlah = []
            total_harga = 0
            daftar_barang()
            beli_barang()

        else:
            print('\nMasukan angka sesuai instruksi')
            continue


menu_login()