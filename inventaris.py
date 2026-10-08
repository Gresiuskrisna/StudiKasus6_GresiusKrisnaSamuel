import json

with open("inventaris.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def tambah_data(nama, harga, stok):
    data.append({
        "id": len(data) + 1,
        "nama": nama,
        "harga": harga,
        "stok": stok
    })
    return "Data ditambah"

def simpan_file():
    with open("inventaris.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    return "tersimpan barang ke inventaris.json"



while True:
    print("\nMenu Inventaris:")
    print("1. Lihat semua barang")
    print("2. Tambah data barang baru")
    print("3. Keluar")
    
    pilih = input("Pilih menu (1/2/3): ")

    if pilih == "1":
        print("\n===== data barang =====")
        print(data)
                
    elif pilih == "2":
        nama_input = input("Nama barang: ")
        harga_input = int(input("Harga: "))
        stok_input = int(input("Stok: "))
        
        print("\n", tambah_data(nama_input, harga_input, stok_input))
        print("\n", simpan_file())

    elif pilih == "3":
        print("Program selesai.")
        break
        
    else:
        print("Pilihan tidak valid.")