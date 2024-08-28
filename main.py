modern_sozluk = {
                "CRINGE": "garip ya da utandirici bir sey",
                "LOL": "komik bir seye verilen cevap",
                "BOOMER": "yasli eski jenarasyon",
                "AGGRO": "agresiflesmek",
                "SHEESH": "onaylamak",
                "TOKSIK": "kendi başarısızlıklarını ve kendi mutsuzluklarını karşısındaki kişiyi ayna olarak görüp yansıtan kişidir",
                "CILGIN": "aşırı heyecanlı, deli, akıl almaz",
                "KOKOFONI": "Uyduruk, hoş olmayan seslerin karışımı",
                "kakofoni": "Uyduruk, hoş olmayan seslerin karışımı",
                "çılgın": "Aşırı heyecanlı, deli, akıl almaz",
                "toksik": "kendi başarısızlıklarını ve kendi mutsuzluklarını karşısındaki kişiyi ayna olarak görüp yansıtan kişidir",
                "aggro": "agresiflesmek",
                "boomer": "yasli eski jenarasyon",
                "lol": "komik bir seye verilen cevap",
                "cringe": "garip ya da utandirici bir sey",
}
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in modern_sozluk.keys():
       print(modern_sozluk[word])
