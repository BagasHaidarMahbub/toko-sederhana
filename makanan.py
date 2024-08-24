print( " |===========================================| " )
print( " |          PROGRAM KASIR SEDERHANA          | " )                                   
print( " |===========================================| " )
print( " |            PILIH MENU MAKANAN             | " )                                   
print( " |===========================================| " )
print( " |  Ayam Bakar               Rp.15000        | " )
print( " |  Ayam Geprek              Rp.15000        | " )                                   
print( " |  Nasi Rendang             Rp.20000        | " )
print( " |  Nasi Pecel               Rp.10000        | " )  
print( " |  Soto Ayam                Rp.12000        | " )                                 
print( " |===========================================| " )

nomer_makanan = int(input("pilih (1/2/3/4/5) :"))
jml_porsi = int(input("Berapa porsi :"))

if nomer_makanan == 1:
    total_makanan = jml_porsi * 15000
    print(f"Ayam Bakar {jml_porsi} porsi Rp.{total_makanan}")
    makanan = "Ayam Bakar"
elif nomer_makanan == 2:
    total_makanan = jml_porsi * 15000
    print(f"Ayam Geprek {jml_porsi} porsi Rp.{total_makanan}")
    makanan = "Ayam Geprek"
elif nomer_makanan == 3:
    total_makanan = jml_porsi * 20000
    print(f"Nasi Rendang {jml_porsi} porsi Rp.{total_makanan}")
    makanan = "Nasi Rendang"
elif nomer_makanan == 4:
    total_makanan = jml_porsi * 10000
    print(f"Nasi Pecel {jml_porsi} porsi Rp.{total_makanan}")
    makanan = "Nasi Pecel"
elif nomer_makanan == 5:
    total_makanan = jml_porsi * 12000
    print(f"Soto Ayam {jml_porsi} porsi Rp.{total_makanan}")
    makanan = "Soto Ayam"
else:
    print("Menu Tidak Terdaftar!")

print( " |===========================================| " )
print( " |          PROGRAM KASIR SEDERHANA          | " )                                   
print( " |===========================================| " )
print( " |            PILIH MENU MINUMAN             | " )                                   
print( " |===========================================| " )
print( " |  Teh Tawar                Rp.3000        | " )
print( " |  Kopi Susu                Rp.8000        | " )                                   
print( " |  Es Milo                  Rp.13000        | " )
print( " |  Lemon Tea                Rp.8000        | " )  
print( " |  Es Jeruk                 Rp.5000        | " )                                 
print( " |===========================================| " )

nomer_minuman = int(input("pilih (1/2/3/4/5) :"))
jml_gelas = int(input("Berapa porsi :"))

if nomer_minuman == 1:
    total_minuman = jml_gelas * 3000
    print(f"Teh Tawar {jml_gelas} porsi Rp.{total_minuman}")
    minuman = "Teh Tawar"
elif nomer_minuman == 2:
    total_minuman = jml_gelas * 8000
    print(f"Kopi Susu {jml_gelas} porsi Rp.{total_minuman}")
    minuman = "Kopi Susu"
elif nomer_minuman == 3:
    total_minuman = jml_gelas * 13000
    print(f"Es Milo {jml_gelas} porsi Rp.{total_minuman}")
    minuman = "Es Milo"
elif nomer_minuman == 4:
    total_minuman = jml_gelas * 8000
    print(f"Lemon Tea {jml_gelas} porsi Rp.{total_minuman}")
    minuman = "Lemon Tea"
elif nomer_minuman == 5:
    total_minuman = jml_gelas * 5000
    print(f"Es Jeruk {jml_gelas} porsi Rp.{total_minuman}")
    minuman = "Es Jeruk"
else:
    print("Menu Tidak Terdaftar!")

total_semua = total_makanan + total_minuman
print(f"Total yang harus dibayar Rp.{total_semua}")

bayar = int(input("masukan Pembayaran anda :"))

if bayar > total_semua:
    kembalian = bayar - total_semua
else: 
    uang_kurang = total_semua - bayar
    print("uang yang anda bayar kurang!")
    exit()

print( " |===========================================| " )
print( " |               STRUK PEMBELIAN             | " )                                   
print( " |===========================================| " )
print( " | Makanan               :",makanan,"\t|")
print( " | Jumlah porsi          :",jml_porsi,"\t\t\t|")
print( " | Minuman               :",minuman,"\t\t|")
print( " | Jumlah gelas          :", jml_gelas, "\t\t\t|")
print( " | Total pembayaran      :", total_semua, "\t\t|")
print( " | Bayar                 :", bayar, "\t\t|")
print( " | Kembalian             :", kembalian, "\t\t|")
print( " |===========================================| " )