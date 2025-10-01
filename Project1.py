name = input ("masukan nama anda: ")
def greet (name):
  print (f"hai {name}, selamat datang di kalkulator sederhana !")

greet (name)

while True: 
  alat_jumlah = input ("pilih alat penjumlahan [+, -, *, /]: ")
  def plus (a, b):
    return a + b  
  def minus (a,b):
    return a - b
  def multiple (a, b):
    return a * b
  def divide (a, b):
    return a / b
  
  angka_1 = int(input("masukan angka 1: "))
  angka_2 = int(input("masukan angka 2: "))

  if alat_jumlah == "+":
     print (plus(angka_1, angka_2))
  elif alat_jumlah == "-":
     print (minus(angka_1, angka_2))
  elif alat_jumlah == "*":
     print (multiple(angka_1, angka_2))
  elif alat_jumlah == "/":
     print (divide(angka_1, angka_2))
