data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')

nama, nim, alamat = data
nim_list = tuple(nim)
nama_list = nama.split()
nama_depan = tuple(nama_list[0])
nama_reversed = tuple(reversed(nama_list))

print("NIM :", nim)
print("NAMA :", nama)
print("ALAMAT :", alamat)
print("NIM: ", nim_list)
print("NAMA DEPAN: ", nama_depan)
print("NAMA TERBALIK :",nama_reversed)