users = []

print ("menu:\n1.tambah nama\n2.hapus nama\n3.cek nama terakhir\n4.cek semua nama\n5.keluar\n")

while True:
  choice = int(input("pilih menu: "))
  if choice == 1:
    add = input("add name: ")
    users.append(add)
    print("berhasil di tambah\n")

  elif choice == 2:
    delete = input("delete name: ")
    if users:
      users.remove(delete)
      print ("berhasil dihapus\n")
    else:
      print ("belum ada list nama\n")

  elif choice == 3:
    if users:
      print (users[-1])
    else:
      print ("belum ada data yang di tambahkan\n")

  elif choice == 4:
    if users:
      print (users)
    else:
      print ("belum ada list\n")
  elif choice == 5:
    print ("anda out")
    break
