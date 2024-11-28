# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar=["Toyota","BMW","Renault","Mercedes"]
# 2- Liste kaç elemanlıdır?
print(len(markalar))
# 3- Listenin ilk ve son elemanı nedir?
print(markalar[0]+" ve "+markalar[-1])
# 4- "Renault" markasını "Togg" ile güncelleyiniz.
markalar[2]="TOGG"
# 5- "Togg" listenin bir elemanı mıdır?
sonuc = "TOGG" in markalar
print(sonuc)
# 6- Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
print(markalar+["Ford","Citroen"])
# 7- Listenin son elemanını siliniz.
del(markalar[-1])
print(markalar)
# 8- Aşağıdaki verileri liste içerisinde saklayınız (Liste içinde liste mümkündür.).

    # öğrenci1: Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2: Ada Bilgi   2011 [70,70,80]
    # öğrenci3: Çınar Turan 2017 [60,60,90]
ogrencı1=["Yiğit","Bilgi",2010,[70,80,90]]
ogrencı2=["Ada","Bilgi",2011,[70,70,80]]
ogrencı3=["Çınar","Turan",2017,[60,60,90]]
# 9- Öğrencilerin yaşlarını hesaplayınız.
Yiğitinyaşı=2024-ogrencı1[2]
Adanınyaşı=2024-ogrencı2[2]
Çınarınyaşı=2024-ogrencı3[2]

# 11- Öğrencilerin not ortalamalarını hesaplayınız.
Yiğitinortalaması=(ogrencı1[3][0]+ogrencı1[3][1]+ogrencı1[3][2])/3
Adanınortalaması=(ogrencı2[3][0]+ogrencı2[3][1]+ogrencı2[3][2])/3
Çınarınortalaması=(ogrencı3[3][0]+ogrencı3[3][1]+ogrencı3[3][2])/3
