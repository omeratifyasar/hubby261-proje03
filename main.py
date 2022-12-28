#Most Similar Rafine
import tkinter as tk

window = tk.Tk()
window.title("Basit Pencere")
window.geometry("300x200")

label = tk.Label(window, text="İyi Aramalar :D!")
label.pack()

window.mainloop()


from gensim.models import KeyedVectors

print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

def benzerKelimeler():

    anahtarKelime = input("Anahtar Kelime: ").lower()
    print("Girilen Kelime : "+ str(anahtarKelime))
    oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
    print(oneriler)

    def benzerKelimeler2():

        anahtarKelime2 = input("Anahtar Kelime: ").lower()
        print("Girilen Kelime : " + str(anahtarKelime))
        oneriler = (kelimeVektoru.most_similar(positive=anahtarKelime))
        print(oneriler)

    # Önerileri rafine et
    for oneri in oneriler:
        if anahtarKelime not in oneri[0]:
            print("https://www.google.com.tr/search?q=" + oneri[0])

    benzerKelimeler()

benzerKelimeler()






