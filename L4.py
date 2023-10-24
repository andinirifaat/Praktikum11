def faktorial(n):
    if n==0:
       return n==n*1
    else:
        return n*faktorial(n-1)   
    
bilangan_bulat=int(input("Masukkan bilangan bulat : "))
if bilangan_bulat<0:
    print("Maaf faktorial hanya mengeksekusi bilangan bulat")
else:
    hasil=faktorial(bilangan_bulat)
    print(bilangan_bulat,"! =",hasil)