#==================SISTEM PERHITUNGAN SKOR UJIAN====================#

# Inisialisasi dictionary untuk menyimpan nama dan nilai para siswa
nilai_siswa = {}

# Loop utama untuk menjalankan program
while True :
        
        # Menampilkan menu
        print("\n"+"="*11 +"MENU" + "="*11)
        print("1. Tambah nilai siswa")
        print("2. Edit nilai siswa")
        print("3. Rata-rata nilai siswa")
        print("4. Urutan peringkat siswa")
        print("5. Keluar")

        # Mengambil input pilihan pengguna
        pilihan = input("Masukkan pilihan (1-5): ")
        print(""+"="*26)

        # Melakukan perintah berdasarkan pilihan pengguna

        # Perintah menambahkan nilai siswa
        if pilihan == "1":
            nama_siswa = input("\nMasukkan nama siswa: ")
            nilai_siswa[nama_siswa] = float(input("Masukkan nilai siswa: "))
            print(f"Nilai siswa {nama_siswa} berhasil ditambahkan!")
        
        # Perintah mengedit nilai siswa
        elif pilihan == "2":
            nama_siswa = input("\nMasukkan nama siswa: ")
            if nama_siswa in nilai_siswa:
                nilai_baru = float(input("Masukkan nilai baru: "))
                nilai_siswa[nama_siswa] = nilai_baru
                print(f"Nilai siswa {nama_siswa} berhasil diubah!")
            else:
                print("\nSiswa yang anda cari tidak ditemukan!")
            
        # Perintah menghitung rata-rata nilai siswa
        elif pilihan == "3":
            if nilai_siswa:
                rata_rata = sum(nilai_siswa.values()) / len(nilai_siswa)
                print(f"\nRata-rata nilai siswa: {rata_rata}")
            else:
                print("\nTidak ada data nilai siswa!")
            
        # Perintah menampilkan urutan peringkat siswa
        elif pilihan == "4":
            if nilai_siswa:

                peringkat = sorted(nilai_siswa.items(), key=lambda x: x[1], reverse=True)
                print("\n" + "="*5 + "URUTAN PERINGKAT" + "="*5)
                for i, (nama, nilai) in enumerate(peringkat, start=1):
                    print(f"{i}. {nama}     : {nilai}")
                print("="*26)
            else:
                print("\nTidak ada data nilai siswa!")

        # Perintah keluar program
        elif pilihan == "5":
            print("\nProgram selesai.")
            break

        else:
            print("\nPilihan yang anda masukkan salah!")

