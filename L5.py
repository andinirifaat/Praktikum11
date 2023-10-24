def volume_kerucut(r,h):
    phi=3.14159
    volume=(1/3) * phi* r**2 * h
    print(volume)

jar_alas=int(input("Masukkan jari-jari alas :"))
tinggi=int(input("Masukkan tinggi kerucut :"))

volume_kerucut(jar_alas,tinggi)