keberadaan_balon= 3
print('''
==== practic ====
''')
nama= input ("masukan nama kamu!.. ")

pernyataan = '''coba kamu perhatikan kotak ini
'''

kotak_kosong = ["[_]"]
bentuk = kotak_kosong * 5 
bentuk_join = " " .join(bentuk)

balon = bentuk.copy()
balon [2] = "[O]"
balon_join = ", " .join(balon)

print (f"{pernyataan} {bentuk_join}")

while True:
  try:
    kotak = int(input ("dikotak manakah balon berada? 1/2/3/4/5 ? "))
    if kotak < 1 or kotak > 5:
      print ("masukan angka 1-5")
      continue
    break
  except ValueError:
    print ("masukan angka dan bukan huruf!")

keyakinan = input("apakah kamu yakin? y/n  ")
  
if keyakinan == "y":
  if kotak == keberadaan_balon:
    print (f"kamu benar, balon berada di kotak \n {balon_join}")
  else:
    print ("kamu salah")
else:
  print ("program dihentikan")
  exit()
