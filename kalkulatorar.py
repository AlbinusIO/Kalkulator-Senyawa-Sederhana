massa_atom = {
    'H': 1.008,
    'O': 16.00,
    'C': 12.01,
    'Na': 22.99,
    'Cl': 35.45,
    'N': 14.0067
}
print("==========Kalkulator Senyawa Sederhana==========")
print("List Senyawa Dan Massanya")

for key,value in massa_atom.items():
    print(f"Senyawa = {key} \tar = {value}")
    

rumus = input("masukkan rumus kimia: ")

i = 0
total_massa = 0

#looping
while i < len(rumus):
    
    simbol = rumus[i]
    
    i += 1
    if i < len(rumus) and rumus[i].islower:
        simbol += rumus[i]
        i += 1
    
    
    jumlah = ''
    while i < len(rumus) and rumus[i].isdigit():
        jumlah += rumus[i]
        i += 1
    if jumlah == '':
        jumlah = 1
    else:
        jumlah = int(jumlah)
    
    
    total_massa += massa_atom[simbol] * jumlah


print("dengan menggunakan rumus M = ∑(ni ​* Ari​)")
print(f"Massa molekul relatif (Mr) dari {rumus} = {total_massa}")
