#main program code
from json import add_student,show,search, delete,out

data_save = []
while True:
  try:
    print("menu:\n1.add identity\n2.show all\n3.search\n4.delete\n5.out")
    
    choice = int(input("\nselected menu: "))
    if choice == 1:
      print(add_student(data_save))
    elif choice == 2:
      show(data_save)
    elif choice == 3:
      search(data_save)
    elif choice == 4:
      delete(data_save)
    elif choice == 5:
      out()
      break
      
  except ValueError:
    print("just input a number not character")


#side program code

from time import sleep

def add_student(profil):
  name = input("what ur name: ")
  major = input("what ur majority: ")
  age = input("how old are u: ")
  profil.append({"name":name, "major":major, "age":age})
  return "adding succeses\n"

def show(profil):
  if profil:
    for i,p in enumerate(profil, start=1):
      print(f"{i}:", end="")
      for key, value in p.items:
        print(f"{key.capitalize()}:{value.capitalize()}", end=" , ")
        print()
  else:
    print ("no profil is added\n")

def search(profil):
  cari = input("what are u looking for: ")
  found = False
  if profil:
    for s in profil:
      if s["name"] == cari:
        print (f"this what u looking for\n{s}\n")
        found = True
        break
    if not found:
      print ("not adding\n")
  else:
    print ("no profil is added\n")

def delete(profil):
  if profil:
    hapus = input("delete a name: ")
    found = False
    for d in profil:
      if d["name"] == hapus:
        profil.remove(d)
        print (f"{d}\nsucces to delete it\n")
        found = True
        break
    if not found:
      print ("not yet\n")
  else:
    print ("not adding\n")
      
def out():
  print("anda akan keluar dalam hitungan")
  for i in range(3,0,-1):
    print (i)
    sleep(1)
  print ("anda keluar")
  
  
