# Daftar unsur dan massa atomnya (dua list sejajar)
unsur = ['H', 'O', 'C', 'Na', 'Cl']
massa_atom = [1.008, 16.00, 12.01, 22.99, 35.45]

rumus = input("Masukkan rumus senyawa (contoh: H2O): ")

i = 0
total_massa = 0

while i < len(rumus):
    simbol = rumus[i]
    i += 1

    # Cek apakah huruf berikutnya huruf kecil
    if i < len(rumus) and rumus[i].islower():
        simbol += rumus[i]
        i += 1

    # Ambil jumlah atom (jika ada angka)
    jumlah = ''
    while i < len(rumus) and rumus[i].isdigit():
        jumlah += rumus[i]
        i += 1

    if jumlah == '':
        jumlah = 1
    else:
        jumlah = int(jumlah)

    # Cari indeks simbol di list unsur
    if simbol in unsur:
        indeks = unsur.index(simbol)
        massa = massa_atom[indeks] * jumlah
        total_massa += massa
    else:
        print(f"Unsur {simbol} tidak dikenal.")

print(f"Massa total senyawa {rumus} = {total_massa:.3f}")
