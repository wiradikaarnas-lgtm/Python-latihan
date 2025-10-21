identity = []

while True:
  print ("\nmenu:\n1.add ur identity\n2.see all student\n3.search a student\n4.deleate the identity\n5.out\n")
  choice = int(input("select the menu: "))
  if choice == 1:
    name = input("add ur name: ")
    major = input("what is your major: ")
    age = input("how old are u: ")
    dictionary = {"name": name, "major": major, "age": age}
    identity.append(dictionary)
    print ("succes to adding identity")

  elif choice == 2:
    if identity:
      for i, y in enumerate (identity, start=1):
        print (i,y)
    else:
      print("you haven't added a name")
  
  elif choice == 3:
    search = input("what identity do u want to know: ")
    if identity:
      found = False
      for a in identity:
        if a["name"] == search:
          print (a)
          found = True
          break
      if not found:
        print("the name is not found")
    else:
      print("you haven't added a name")

  elif choice == 4:
    deleate = input("what do u want to deleating: ")
    found = False
    for d in identity:
      if d["name"] == deleate:
        identity.remove(d)
        print ("berhasil di hapus")
        found = True
        break
    if not found:
      print ("the name u want to deleting is not found")
        
  elif choice not in [1,2,3,4,5]:
    print ("the number just 1-5")
  else:
    print ("program is done")
    exit()
