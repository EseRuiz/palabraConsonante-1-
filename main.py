#dada una lista de palabras, contar cuantas vocales y consonantes tiene cada palabra
txt = input("Ingrese un texto: ")
txt = txt.lower()
print(txt)
ln = len(txt)
voc = ['a', 'e', 'i', 'o', 'u']
con = [
  'b', 'c', 'd', 'f', 'g', 'h', 'j'
  'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y'
]
vo = 0
co = 0
for i in range(ln):
  if txt[i] in voc:
    vo += 1
  if txt[i] in con:
    co += 1
print("Numero de vocales: ", vo)
print("Numero de consonantes: ", co)
