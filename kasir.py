print( " |===========================================| " )
print( " |               TOKO SEDERHANA              | " )                                   
print( " |===========================================| " )

nama    = input("Masukkan nama barang   :")
harga   = int(input("Masukkan harga barang : "))
jumlah  = int(input("jumlah barang yang dibeli :"))

total = harga * jumlah
print("total pembelian Rp.",total)

pembayaran = int(input("Masukkan pembayaran anda : "))
kembalian = pembayaran - total
print("kembalian anda Rp.",kembalian)
