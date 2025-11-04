#Main Program
from update import tambah,lihat,cari, hapus,edit,keluar
absen = []

while True:
  try:
    print('''
    menu:
    1.tambah nama
    2.lihat semua
    3.cari nama
    4.hapus nama
    5.edit nama
    6.keluar
    ''')
    pilihan = int(input("pilih menu: "))
    if pilihan == 1:
      print(tambah(absen))
    elif pilihan == 2:
      lihat(absen)
    elif pilihan == 3:
      cari(absen)
    elif pilihan == 4:
      hapus(absen)
    elif pilihan == 5:
      edit(absen)
    elif pilihan == 6:
      keluar()
  except ValueError:
    print("masukan angka bukan seainnya")
    

#Side Program update.py
from time import sleep

def tambah(data):
  nama = input("masukan nama anda: ")
  hobi = input("hobi kamu: ")
  umur = input("umur: ")
  data.append({"nama":nama, "hobi":hobi, "umur":umur})
  return "berhasil di tambah"

def lihat(data):
  if data:
    for i,x in enumerate (data, start=1):
      print(f"{i}.", end="")
      for key, value in x.items():
        print(f"{key}:{value}", end=" | ")
      print()
  else:
     print("belum ada siswa")

def cari(data):
  if data:
    cari = input("siswa yang dicari: ")
    found = False
    for index,item in enumerate(data, start=1):
      if item["nama"] == cari:
        print(f"{index}.", end="")
        for key, value in item.items():
          print(f"{key}:{value}",end=" |")
        print()
        found = True
    if not found:
      print("belum ada pendaftar")
  else:
    print("siswa itu belum daftar")

def hapus(data):
  if data:
    hapus = input("siswa yang ingin dihapus: ")
    found = False
    for x in data:
      if x["nama"] == hapus:
        for key, value in x.items():
          print(f"{key}:{value}",end=" |")
        data.remove(x)
        print("berhasil dihapus\n")
        found = True
        break
    if not found:
       print("siswa tersebut baik")
  else:
    print("belum ada siswa")
        
def edit(data):
  if data:
    edit = input("siswa mana yg ingin biodatanya diubah: ")
    found = False
    for i,e in enumerate(data, start=1):
      if e["nama"] == edit:
        print(f"{i}.", end="")
        for key, value in e.items():
          print(f"{key}:{value}",end=" |")
        print()
        for key in e.keys():
          baru = input(f"ubah {key}: ")
          if baru:
            e[key] = baru
        print("berhasil diperbarui")
        found = True
        break
    if not found:
      print("siswa belum ada")
  else:
    print("belum ada pendaftar")
            
def keluar():
  for i in range(3, 0, -1):
    print(f"{i}...")
    sleep(1)
  print("anda keluar")
  exit()

    
