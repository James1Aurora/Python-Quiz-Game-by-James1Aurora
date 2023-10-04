
import random
import time
import sys

#hi this is  james aurora, if you try this code on VScode, please make sure you press run and debug build to prevent error.
#thx guys

def kuis(pertanyaan, jawaban):
    return {"pertanyaan": pertanyaan, "jawaban": jawaban}

def nilaibenar(poin):
    print("Benar, poin bertambah satu\n")
    return poin + 1

def nilaisalah(poin):
    print("Salah, poin berkurang satu\n")
    return poin

def main():
    poin = 0
    random.seed(time.time())

    questions = [kuis("43+22 sama dengan", "65"),
                 kuis("Berapa Luas Segitiga siku-siku jika diketahui panjang alasnya 6cm dan tingginya 4", "12"),
                 kuis("Berapa volume sebuah tabung dengan jari-jari 7 cm dan tinggi 10 cm?", "1540"),
                 kuis("Disediakan data 1,2,3,4,5 berapa rata-ratanya?", "3"),
                 kuis("Bangun Datar: Tentukan keliling segitiga dengan panjang sisi-sisi 6 cm, 8 cm, dan 10 cm.", "24"),
                 kuis("Berapa banyak simpul (vertex) yang terdapat dalam sebuah graf yang memiliki 7 sisi (edge)?", "6")]
    
    totalpertanyaan = len(questions)
    pertanyaanditanya = [False] * totalpertanyaan
    
    while True:
        if all(pertanyaanditanya):
            break
        
        index = random.randint(0, totalpertanyaan - 1)
        
        if not pertanyaanditanya[index]:
            print("Pertanyaan:", questions[index]["pertanyaan"])
            jawaban = input("Jawabanmu : ")
            if jawaban == questions[index]["jawaban"]:
                poin = nilaibenar(poin)
            else:
                poin = nilaisalah(poin)
            pertanyaanditanya[index] = True
    
    print("\n||============================================================||")
    print("||                      Hasil Akhir Kuis                      ||")
    print("||============================================================||")
    print("|| Poin Akhir:", str(poin), "||")
    print("||============================================================||")

if __name__ == "__main__":
    print("||================== Python Kuis Game Akbar ==================||")
    print("|| Selamat datang di Kuis Akbar... apakah kamu ingin bermain? ||")
    print("||============================================================||")
    print(" ")
    game = input()
    if game.lower() != "yes":
        sys.exit()
    print("oke kita main sekarang!", " ")
    main()
