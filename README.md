# Studi Kasus 6 - Sistem Manajemen Inventaris Barang

# Isi Repository

- inventaris.py : kode program
- inventaris.json : file penyimpanan data barang
- README.md : penjelasan kode program
- output_program.png dan data_tersimpan.png : screenshot hasil program

# Format Data

Data disimpan dalam bentuk array JSON. Setiap barang adalah satu object yang punya empat key, yaitu id, nama, harga, dan stok. Contoh datanya seperti ini:

```json
[
    {
        "id": 1,
        "nama": "Beras 5 kg",
        "harga": 65000,
        "stok": 20
    }
]
```


# Penjelasan Kode Program

# 1. Membaca Data Awal

```
 import json

with open("inventaris.json", "r", encoding="utf-8") as f:
    data = json.load(f)
```

Program mengimpor json trus di baris awal langsung membuka dan membaca file inventaris.json menggunakan fungsi json.load(f). Fungsi ini mengubah data teks JSON menjadi tipe data list di Python.


# 2. Fungsi tambah_data()
Fungsi ini digunakan untuk menambahkan data barang baru ke dalam variabel data.

- Fungsi menerima input nama, harga, dan stok.
- Data baru disusun menjadi tipe data dictionary. ID barang dibuat secara otomatis dengan menjumlahkan total panjang data saat ini ditambah satu (len(data) + 1).
- Dictionary tersebut lalu dimasukkan ke dalam list utama menggunakan perintah data.append().
- Fungsi mengembalikan teks "Data ditambah" sebagai penanda proses berhasil.


# 4. Fungsi simpan_file()
Fungsi ini bertugas menyimpan pembaruan data secara permanen ke file.

- File inventaris.json dibuka dengan mode "w" (write) untuk menimpa data lama dengan list data yang baru diupdate.

- Fungsi json.dump(data, f, indent=4) digunakan untuk menulis list ke dalam file JSON. Tambahan indent=4 berfungsi agar struktur data di dalam file tersusun rapi dengan indentasi 4 spasi.


# 5. Program Utama (While Loop)
Program menggunakan perulangan while True untuk menampilkan menu secara terus menerus sampei user keluar.

- Pilihan 1 (Lihat semua barang): Program akan langsung mencetak isi variabel data yang berisi list barang ke layar terminal.

- Pilihan 2 (Tambah data barang baru): Program meminta input dari user untuk nama barang (string), serta harga dan stok yang langsung diubah menjadi angka menggunakan int(). Kemudian program memanggil fungsi tambah_data() untuk memasukkan data ke list, dan langsung memanggil simpan_file() agar data baru tersebut tersimpan permanen.

- Pilihan 3 (Keluar): Program menampilkan pesan selesai dan menghentikan perulangan menggunakan perintah break.



# Cara Menjalankan
Pastikan file inventaris.py dan inventaris.json berada di dalam folder yang sama, trus jalankan perintah ini di terminal:

- python inventaris.py



# Screenshot Hasil Program

<img width="1600" height="632" alt="29549" src="https://github.com/user-attachments/assets/a6461adb-6619-4b29-9a18-9a3d29f4d046" />

<img width="922" height="768" alt="29548" src="https://github.com/user-attachments/assets/7417089b-d21f-4484-aa52-a85f3146d67f" />
