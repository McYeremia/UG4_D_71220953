input_bil = input('Masukkan sekumpulan bilangan(pisahkan dengan koma): ')
a = list[input_bil]
pisah = input_bil.split(', ')

print('Bilangan terbesar dari kumpulan bilangan yang di input:', max(pisah))
print('Bilangan terkecil dari kumpulan bilangan yang di input:', min(pisah))