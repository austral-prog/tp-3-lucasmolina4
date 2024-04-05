def check_vowels():
   nombre=input("ingrese su nombre: ")
    print(nombre)
    FinD1= "a" in nombre.lower()
    FinD2= "e" in nombre.lower()
    FinD3= "i" in nombre.lower()
    FinD4= "o" in nombre.lower()
    FinD5= "u" in nombre.lower()

    print(f"Contiene a:   {FinD1}")
    print(f"Contiene e:   {FinD2}")
    print(f"Contiene i:   {FinD3}")
    print(f"Contiene o:   {FinD4}")
    print(f"Contiene u:   {FinD5}")
