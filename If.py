
es_hombre = input("Ingresa tu genero (M = Mujer, H = Hombre): ")
if es_hombre == "H":
    es_hombre = True
else:
    es_hombre = False

es_alto = input("Eres una persona alta o baja? (A = alta, B = baja): ")
if es_alto == "A":
    es_alto = True
else:
    es_alto = False

if es_hombre and es_alto:
    print("Eres un hombre alto")
elif es_hombre and not(es_alto):
    print("Eres un hombre bajito")
elif not(es_hombre) and es_alto:
    print("No eres un hombre pero eres alta")
else:
    print("No eres un hombre y no eres alto")