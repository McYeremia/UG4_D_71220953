print('========== BARIS ARITMATIKA ==========')

def deret(a, b, n):
    total = n/2 * (2*a + (n-1)*b)
    return total

a = int(input('Masukkan bilangan awal: '))
b = int(input('Masukkan selisih bilangan: '))
n = int(input('Masukkan banyaknya suku: '))
print('Total dari deret aritmatika tersebut adalah: ', deret(a,b,n))
