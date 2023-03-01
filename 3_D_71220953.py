input_kalimat = input('Masukkan sebuah kalimat: ')
pisah = input_kalimat.split()
kata_terpanjang = max(pisah, key=len)
print(f'Kata terpanjang dalam kalimat tersebut: {kata_terpanjang}')
