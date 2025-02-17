import datetime

ListPerpus = [{
    'Nomor': 101,
    'Judul': 'Dune',
    'Penulis': 'Frank Herbert',
    'Terbit': 1965,
    'Jenis': 'Novel Sci-Fi'
}, {
    'Nomor': 102,
    'Judul': 'Pokemon Adventures',
    'Penulis': 'Hideori Kusaka',
    'Terbit': 1997,
    'Jenis': 'Komik'
}, {
    'Nomor': 103,
    'Judul': 'The Asian Kitchen',
    'Penulis': 'Kong Foong lin',
    'Terbit': 2014,
    'Jenis': 'Buku Resep'
}, {
    'Nomor': 104,
    'Judul': 'Mr Standfast, A Novel',
    'Penulis': 'John Buchan',
    'Terbit': 2016,
    'Jenis': 'Novel Thriller'
}, {
    'Nomor': 105,
    'Judul': 'The NY Magz Book Of Cartoon',
    'Penulis': 'The W Magazine',
    'Terbit': 2001,
    'Jenis': 'Majalah'
}]

ListPerpusBaru = ListPerpus.copy()
RecycleBin = []
users = {
    'admin': 'admin',
    'user1': 'password123'
}
daftarpeminjam = {}
dendaperhari = 10000

def login():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username in users and users[username] == password:
            print("Login berhasil!")
            return username
        else:
            print("Login gagal. Coba lagi.")

def NomorSebagaiInput():
    while True:
        global Nomor
        Nomor = input(' Masukkan Nomor Buku : ')
        if Nomor.isdigit():
            Nomor = int(Nomor)
            break
        else:
            print('!!!!!! Menu yang Dimasukkan Adalah Angka !!!!!!')

def InputTahun():
    while True:
        global Terbit
        Terbit = input(' Masukkan Tahun Terbit Buku : ')
        if Terbit.isdigit():
            Terbit = int(Terbit)
            break
        else:
            print('!!!!!! Input yang Dimasukkan Adalah Angka !!!!!!')

def InputUmur():
    while True:
        global Umur
        Umur = input(' Masukkan Umur Anda : ')
        if Umur.isdigit():
            Umur = int(Umur)
            break
        else:
            print('!!!!!! Input yang Dimasukkan Adalah Angka !!!!!!')

def TanggalPinjam(datestr):
    try:
        datetime.datetime.strptime(datestr, "%d-%m-%Y")
        return True
    except ValueError:
        return False

def TampilkanDaftarBuku():
    print('''
    Menu Untuk Tampilkan Daftar Buku :
    1. Seluruh Buku yang Tersedia
    2. Mencari Buku Tertentu Berdasarkan Nomor
    3. Kembali Ke Menu Utama
    ''')
    MenuParsial = input(' Pilihlah Sub Menu [1-3]: ')
    if MenuParsial == '1':
        if len(ListPerpusBaru) == 0:
            print('!!!!!! Data Tidak Tersedia !!!!!!')
            TampilkanDaftarBuku()
        else:
            print('\n Daftar Buku :')
            for i, Update in enumerate(ListPerpusBaru):
                print(
                    f"\t{i + 1}. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}")
            TampilkanDaftarBuku()
    elif MenuParsial == '2':
        if len(ListPerpusBaru) == 0:
            print('!!!!!! Data Tidak Tersedia !!!!!!')
            TampilkanDaftarBuku()
        else:
            NomorSebagaiInput()
            for Update in ListPerpusBaru:
                if Update['Nomor'] == Nomor:
                    print(f' Data Buku dengan Nomor {Nomor}')
                    print(
                        f" 1. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}")
                    break
            else:
                print('!!!!!! Data Tidak Tersedia !!!!!!')
                TampilkanDaftarBuku()
    elif MenuParsial == '3':
        return
    else:
        print(
            '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        TampilkanDaftarBuku()

def AddDataBuku():
    print('''
    Menu Untuk Menambah Daftar Buku :
    1. Tambahkan Daftar Buku
    2. Kembali Ke Menu Utama
    ''')
    MenuParsial = input(' Pilihlah Sub Menu [1-2]: ')
    if MenuParsial == '1':
        NomorSebagaiInput()
        for Update in ListPerpusBaru:
            if Update['Nomor'] == Nomor:
                print("<<<<<< Data Anda Sudah Tersimpan>>>>>>")
                return
        Judul = input(' Masukkan Judul Buku : ')
        Penulis = input(' Masukkan Nama Penulis Buku : ')
        InputTahun()
        Jenis = input(' Masukkan Jenis Buku : ')
        simpan = input(' Apakah Data Akan Disimpan? (Y/N) : ').upper()
        if simpan == 'Y':
            ListPerpusBaru.append({
                'Nomor': Nomor,
                'Judul': Judul,
                'Penulis': Penulis,
                'Terbit': Terbit,
                'Jenis': Jenis
            })
            print('<<<<<< Data Anda Sudah Tersimpan>>>>>>')
        AddDataBuku()
    elif MenuParsial == '2':
        return
    else:
        print(
            '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        AddDataBuku()

def DeleteDataBuku():
    print('''
    Menu Untuk Menghapus Daftar Buku :
    1. Hapus Data
    2. Lihat Recycle Bin
    3. Kembalikan Data dari Recycle Bin
    4. Kembali Ke Menu Utama
    ''')
    MenuParsial = input(' Pilihlah Sub Menu [1-4]: ')
    if MenuParsial == '1':
        NomorSebagaiInput()
        for j, Update in enumerate(ListPerpusBaru):
            if Update['Nomor'] == Nomor:
                Delete = input(' Apakah Data Akan Dihapus (Y/N) : ').upper()
                if Delete == 'Y':
                    RecycleBin.append(ListPerpusBaru.pop(j))
                    print('<<<<<< Data Anda Sudah Terhapus dan Dipindahkan ke Recycle Bin >>>>>>')
                    break
        else:
            print('!!!!!! Data Tidak Tersedia !!!!!!')
        DeleteDataBuku()
    elif MenuParsial == '2':
        if not RecycleBin:
            print("Recycle Bin kosong.")
        else:
            print("\nIsi Recycle Bin:")
            for i, buku in enumerate(RecycleBin):
                print(
                    f"\t{i + 1}. Nomor: {buku['Nomor']}, Judul: {buku['Judul']}, Penulis: {buku['Penulis']}, Terbit: {buku['Terbit']}, Jenis: {buku['Jenis']}")
        DeleteDataBuku()
    elif MenuParsial == '3':
        if not RecycleBin:
            print("Recycle Bin kosong.")
        else:
            print("Daftar buku di Recycle Bin:")
            for i, buku in enumerate(RecycleBin):
                print(
                    f"\t{i + 1}. Nomor: {buku['Nomor']}, Judul: {buku['Judul']}, Penulis: {buku['Penulis']}, Terbit: {buku['Terbit']}, Jenis: {buku['Jenis']}")
            try:
                IndexKembalikan = int(input("Masukkan nomor buku yang ingin dikembalikan: ")) - 1
                BukuKembalikan = RecycleBin.pop(IndexKembalikan)
                ListPerpusBaru.append(BukuKembalikan)
                print("Buku berhasil dikembalikan dari Recycle Bin.")
            except IndexError:
                print("Nomor buku tidak valid.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
        DeleteDataBuku()
    elif MenuParsial == '4':
        return
    else:
        print(
            '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        DeleteDataBuku()

def UpdateDataBuku():
    print('''
    Menu Untuk Mengubah Data Buku :
    1. Ubah Data Buku
    2. Kembali Ke Menu Utama
    ''')
    MenuParsial = input(' Pilihlah Sub Menu [1-2]: ')
    if MenuParsial == '1':
        NomorSebagaiInput()
        NomorPertama = Nomor
        Informasi = ''
        for Update in ListPerpusBaru:
            if Update['Nomor'] == NomorPertama:
                print(
                    f" 1. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}")
                ContinueUpdate = input(' Apakah Anda Yakin Akan Mengubah Data Buku (Y/N) : ').upper()
                if ContinueUpdate == 'Y':
                    Informasi = input(
                        ' Pilihlah Kategori yang Akan Anda Ubah [Pilihan : Nomor, Judul, Penulis, Terbit, Jenis]: ')
                    if Informasi in ListPerpusBaru[0].keys():
                        if Informasi == 'Nomor':
                            NomorSebagaiInput()
                            NomorBaru = Nomor
                            ListNomor = [Update['Nomor'] for Update in ListPerpusBaru]
                            while NomorBaru in ListNomor:
                                print("<<<<<< Nomor yang Anda Masukkan Sudah Terpakai >>>>>>")
                                NomorSebagaiInput()
                                NomorBaru = Nomor
                        else:
                            NomorBaru = input(f' Masukkan {Informasi} baru : ')
                        update = input(' Apakah Anda Yakin Akan Data yang Diubah (Y/N) : ').upper()
                        if update == 'Y':
                            Update[Informasi] = NomorBaru
                            print('<<<<<< Data Anda Sudah Terbarui >>>>>>')
                        else:
                            print(
                                '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
                        break
        else:
            print('!!!!!! Data Tidak Tersedia !!!!!!')
        UpdateDataBuku()
    elif MenuParsial == '2':
        return
    else:
        print(
            '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        UpdateDataBuku()

def PinjamBuku():
    print('''
    Menu Untuk Meminjam Buku :
    1. Pinjam Sebuah Buku
    2. Kembali Ke Menu Utama
    ''')
    MenuParsial = input(' Pilihlah Sub Menu [1-2]: ')
    if MenuParsial == '1':
        NomorSebagaiInput()
        for Update in ListPerpusBaru:
            if Update['Nomor'] == Nomor:
                Nama = input(' Masukkan Nama Anda : ')
                InputUmur()
                Instansi = input(' Masukkan Instansi Anda : ')
                while True:
                    Tanggal = str(input(' Tanggal Hari ini : '))
                    if not TanggalPinjam(Tanggal):
                        print(
                            "!!!!!! Input yang Anda Masukkan Salah, Silahkan Input Kembali Tanggal Pinjam Dengan Format 'dd-mm-yyyy' !!!!!!")
                        continue
                    break
                daftarpeminjam[Nomor] = {
                    'Nama': Nama,
                    'Umur': Umur,
                    'Instansi': Instansi,
                    'Tanggal Pinjam': Tanggal
                }
                print(f''' Anda Telah Memilih Untuk Meminjam Buku Nomor {Nomor}
    1. Nomor : {Update['Nomor']}, Judul : {Update['Judul']}, Penulis : {Update['Penulis']}, Terbit : {Update['Terbit']}, Jenis : {Update['Jenis']}
    Biodata Anda Telah Tersimpan Sebagai Peminjam :
    Nama : {Nama}
    Umur : {Umur}
    Instansi : {Instansi}
    Tanggal Hari ini : {Tanggal}
    Terima Kasih Anda Telah Bertransaksi di THE LIBRARY
    Silahkan Kembalikan Buku yang Anda Pinjam Dalam Rentang Waktu 14 Hari Setelah Waktu Pinjam
    ''')
                break
        else:
            print('!!!!!! Data Tidak Tersedia !!!!!!')
            PinjamBuku()
    elif MenuParsial == '2':
        return
    else:
        print(
            '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        PinjamBuku()

def KembalikanBuku():
    print('''
    Menu Untuk Mengembalikan Buku :
    1. Kembalikan Buku
    2. Kembali Ke Menu Utama
    ''')
    MenuParsial = input(' Pilihlah Sub Menu [1-2]: ')
    if MenuParsial == '1':
        NomorSebagaiInput()
        if Nomor in daftarpeminjam:
            tglPinjamstr = daftarpeminjam[Nomor]['Tanggal Pinjam']
            tglPinjam = datetime.datetime.strptime(tglPinjamstr, "%d-%m-%Y").date()
            tglKembali = datetime.date.today()
            SelisihHari = (tglKembali - tglPinjam).days
            keterlambatan = max(0, SelisihHari - 14)
            if keterlambatan > 0:
                denda = keterlambatan * dendaperhari
                print(f"Anda terlambat mengembalikan buku selama {keterlambatan} hari.")
                print(f"Denda yang harus dibayar: Rp {denda:,.2f}")
            else:
                print("Buku dikembalikan tepat waktu. Tidak ada denda.")
            del daftarpeminjam[Nomor]
            print("Buku berhasil dikembalikan.")
        else:
            print("Buku ini tidak terdaftar sebagai buku yang dipinjam.")
        KembalikanBuku()
    elif MenuParsial == '2':
        return
    else:
        print(
            '!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')
        KembalikanBuku()

def MenuAdmin():
    while True:
        print('''
        :::::::::::::::::: Menu Admin ::::::::::::::::::
        1. Daftar Buku Di Perpustakaan
        2. Menambahkan Data Buku
        3. Menghapus Data Buku
        4. Mengubah/Mengupdate Data Buku
        5. Keluar
        ''')
        MenuSelection = input('Pilihlah Sebuah Nomor Dari Daftar Menu : ')
        if MenuSelection == '1':
            TampilkanDaftarBuku()
        elif MenuSelection == '2':
            AddDataBuku()
        elif MenuSelection == '3':
            DeleteDataBuku()
        elif MenuSelection == '4':
            UpdateDataBuku()
        elif MenuSelection == '5':
            break
        else:
            print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')

def MenuUser():
    while True:
        print('''
        :::::::::::::::::: Menu User ::::::::::::::::::
        1. Daftar Buku Di Perpustakaan
        2. Meminjam Buku
        3. Mengembalikan Buku
        4. Keluar
        ''')
        MenuSelection = input('Pilihlah Sebuah Nomor Dari Daftar Menu : ')
        if MenuSelection == '1':
            TampilkanDaftarBuku()
        elif MenuSelection == '2':
            PinjamBuku()
        elif MenuSelection == '3':
            KembalikanBuku()
        elif MenuSelection == '4':
            break
        else:
            print('!!!!!! Menu yang Anda Masukkan Tidak Dapat Dijalankan, Silahkan Input Kembali Nomor Menu !!!!!!')

# Program utama
username = login()
if username:
    if username == 'admin':
        MenuAdmin()
    else:
        MenuUser()
print(' Terima Kasih Anda Telah Bertransaksi di THE LIBRARY')
