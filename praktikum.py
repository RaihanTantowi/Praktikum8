class Mahasiswa():
    def menutabel():
        print("=" * 35)
        print("|  PROGRAM INPUT NILAI MAHASISWA  |")
        print("=" * 35)
        print('| 1. Tambah Data                  |')
        print('| 2. Tampilkan Data               |')
        print('| 3. Ubah Data                    |')
        print('| 4. Hapus Data                   |')
        print('| 5. Exit                         |')
        print("=" * 35)
    
    menutabel()

    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def tambah(self,nim,nama,tugas,uts,uas):
        data.nim.append(nim)
        data.nama.append(nama)
        data.tugas.append(tugas)
        data.uts.append(uts)
        data.uas.append(uas)

    def lihat(self):
        for i in range(len(data.nama)):
            print("|", i+1, "  |", end="")
            print('{0:<25}'.format(self.nama[i]), end="")
            print("|", self.nim[i], end="")
            print(" |", self.tugas[i], end="")
            print("    |", self.uts[i], end="")
            print("  |", self.uas[i], " | ", end="")
            print(f'{((self.tugas[i]*30/100) + (self.uts[i]*35/100) + (self.uas[i]*35/100)) :.2f}', " |")

    def ubah(self,nim,nama,tugas,uts,uas):
        self.nim[no] = nim
        self.nama[no] = nama
        self.tugas[no] = tugas
        self.uts[no] = uts
        self.uas[no] = uas

    def hapus(self):
        del self.nim[no]
        del self.nama[no]
        del self.tugas[no]
        del self.uts[no]
        del self.uas[no]

data = Mahasiswa([],[],[],[],[])

while True:
    menu = input("(1)Tambah data, (2)Tampilkan data, (3)Ubah data, (4)Hapus data, (5)Keluar: ")
    if menu == "1" :
       print("\nTambah Data")
       data.tambah(
           input("Masukkan NIM \t : "), 
           input("Masukkan Nama\t : "), 
           int(input("Nilai Tugas\t : ")), 
           int(input("Nilai UTS\t : ")), 
           int(input("Nilai UAS\t : "))
           )
       print("\nData berhasil ditambahkan")

    elif menu == "2" :
        print()
        print("=" *74)
        print("|" + "\t" * 3 + "DAFTAR NILAI MAHASISWA" + "\t" * 3 +  "         |")
        print("="*74)
        print("| No  |          Nama           |    NIM    | TUGAS | UTS | UAS |  AKHIR |")
        print("="*74)
        if len(data.nama) != 0:
            data.lihat()
        else:
            print("                             TIDAK ADA DATA                           ")
        print("="*74)

    elif menu == "3" :
        print("\nUbah Data")
        print("#Masukkan Nama Yang Telah Diinput")
        ubah = input("Masukkan Nama : ")
        if ubah in data.nama:
           no = data.nama.index(ubah)
           print()
           print("#Masukkan Data Yang Baru")
           data.ubah(
               input("Masukkan NIM \t : "), 
               input("Masukkan Nama\t : "), 
               int(input("Nilai Tugas\t : ")), 
               int(input("Nilai UTS\t : ")), 
               int(input("Nilai UAS\t : "))
               )
        else:
            print(ubah, "tidak ada di dalam data")

    elif menu == "4" :
        print("\nHapus Data")
        print("#Masukkan Nama Yang Telah Diinput")
        hapus = input("Masukkan Nama : ")
        if hapus in data.nama:
            no = data.nama.index(hapus)
            data.hapus()
            print("Data", hapus, "Berhasil dihapus")
        else:
            print(hapus, "tidak ada di dalam data")

    elif menu == "5" :
        print("\nThank You :)\n")
        break

    else:
        print("\nPerintah yang dimasukkan salah!\n")