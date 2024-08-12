import tkinter as tk
import random


kelimeler = {
    "enable": "etkinleştirmek",
    "expose": "maruz bırakmak",
    "lead to": "yol açmak",
    "major in": "uzmanlaşmak",
    "open up": "açılmak",
    "pretend": "numara yapmak",
    "sufficient": "yeterli",
    "probability": "olasılık",
    "recognition": "tanıma",
    "attain": "ulaşmak",
    "diverse": "çeşitli",
    "establish": "kurmak",
    "extract": "çıkarmak",
    "status": "durum",
    "structure": "yapı",
    "submit": "sunmak",
    "come up with": "bulmak, ortaya atmak",
    "complex": "karmaşık",
    "figure out": "anlamak, çözmek",
    "functional": "işlevsel",
    "layer": "katman",
    "measure": "ölçmek",
    "operate": "işletmek",
    "similarity": "benzerlik",
    "simulation": "simülasyon",
    "three-dimensional": "üç boyutlu",
    "train": "eğitmek",
    "classic": "klasik",
    "element": "öğe, element",
    "environmentally friendly": "çevre dostu",
    "flexible": "esnek",
    "image": "görüntü",
    "industrial": "endüstriyel",
    "measurement": "ölçüm",
    "process": "süreç",
    "alter": "değiştirmek",
    "contrast": "karşılaştırmak",
    "eventually": "sonunda",
    "income": "gelir",
    "interact": "etkileşimde bulunmak",
    "substitute": "yerine geçmek, yedek",
    "affect": "etkilemek",
    "capacity": "kapasite",
    "characteristic": "özellik",
    "claim": "iddia",
    "critical thinking": "eleştirel düşünme",
    "criticism": "eleştiri",
    "dishonest": "dürüst olmayan",
    "efficiently": "verimli bir şekilde",
    "evidence": "kanıt",
    "function": "işlev",
    "interfere": "müdahale etmek",
    "potential": "potansiyel",
    "sample": "örnek",
    "concept": "kavram",
    "focus": "odaklanmak",
    "master": "ustalaşmak",
    "observation": "gözlem",
    "psychologist": "psikolog",
    "contemporary": "çağdaş",
    "context": "bağlam",
    "contradict": "çelişmek",
    "identify": "tanımlamak",
    "intelligence": "zeka",
    "revenue": "gelir",
    "accidentally": "kazara",
    "adapt to": "uyum sağlamak",
    "ancestor": "ata",
    "break out": "patlak vermek",
    "cause": "neden olmak",
    "destruction": "yıkım",
    "expand": "genişletmek",
    "inner": "iç",
    "lower": "alçaltmak",
    "natural disaster": "doğal afet",
    "preserve": "korumak",
    "protection": "koruma",
    "spread": "yayılmak",
    "take something for granted": "bir şeyi hafife almak",
    "thus": "böylece",
    "warmth": "sıcaklık",
    "burn up": "yanmak",
    "fired up": "heyecanlanmak",
    "burned out": "tükenmek",
    "get burned": "yanmak",
    "dramatically": "çarpıcı biçimde",
    "justify": "haklı çıkarmak",
    "maintain": "sürdürmek",
    "option": "seçenek",
    "store": "depolamak",
    "turning point": "dönüm noktası",
    "detect": "tespit etmek",
    "occupy": "işgal etmek",
    "release": "serbest bırakmak",
    "restore": "yenilemek",
    "sequence": "sıra",
    "source": "kaynak",
    "visible": "görünür",
    "barrier": "engel",
    "exhausting": "yorucu",
    "extreme": "aşırı",
    "global": "küresel",
    "layover": "mola",
    "outstanding": "göze çarpan",
    "risk": "risk",
    "decision-making": "karar verme",
    "middle-class": "orta sınıf",
    "part-time": "yarı zamanlı",
    "slow-moving": "yavaş ilerleyen",
    "approximately": "yaklaşık olarak",
    "implement": "uygulamak",
    "commitment": "taahhüt",
    "monitor": "izlemek",
    "rush": "acele etmek",
    "rush hour": "trafik saati",
    "safety": "güvenlik",
    "spirit": "ruh",
    "venue": "mekan",
    "three-bedroom": "üç yatak odalı",
    "twelve-year-old": "on iki yaşında",
    "strategy": "strateji",
    "visual": "görsel",
    "circulate": "dolaşmak",
    "concentration": "konsantrasyon",
    "concern": "endişe",
    "digest": "sindirmek",
    "epidemic": "salgın",
    "extinct": "nesli tükenmiş",
    "harmful": "zararlı",
    "myth": "efsane",
    "peak": "zirve",
    "researcher": "araştırmacı",
    "toxin": "toksin",
    "trace back to": "izini sürmek",
    "transmit": "iletmek",
    "unsafe": "güvensiz",
    "ache": "ağrı",
    "come down with": "hastalanmak",
    "disorder": "bozukluk",
    "infection": "enfeksiyon",
    "life-threatening": "hayati tehlike",
    "treat": "tedavi etmek",
    "check-up": "kontrol",
    "critical": "kritik",
    "valid": "geçerli",
    "assess": "değerlendirmek",
    "clarify": "açıklığa kavuşturmak",
    "eliminate": "ortadan kaldırmak",
    "incidence": "olay",
    "reinforce": "pekiştirmek",
    "vary": "değişmek",
    "bond": "bağ",
    "construct": "inşa etmek",
    "convert into": "dönüştürmek",
    "current": "mevcut",
    "be designed to": "tasarlanmış olmak",
    "desire": "arzu etmek",
    "emphasize": "vurgulamak",
    "ensure": "sağlamak",
    "entire": "tüm",
    "estimate": "tahmin etmek",
    "gather": "toplamak",
    "generosity": "cömertlik",
    "kindness": "naziklik",
    "lay off": "işten çıkarmak",
    "resource": "kaynak",
    "survival": "hayatta kalma",
    "specification": "özellik",
    "survivor": "hayatta kalan",
    "adapt": "uyum sağlamak",
    "cooperate": "işbirliği yapmak",
    "economy": "ekonomi",
    "expand": "genişletmek",
    "respond": "yanıt vermek",
    "transform": "dönüştürmek",
    "acquire": "edinmek",
    "aspect": "bakış açısı",
    "bullying": "zorbalık",
    "case": "durum",
    "content": "içerik",
    "hack": "hacklemek",
    "high-tech": "yüksek teknoloji",
    "intellectual property": "fikri mülkiyet",
    "measure": "ölçü",
    "motive": "güdü",
    "privacy": "mahremiyet",
    "recover": "iyileşmek",
    "against the law": "yasadışı",
    "fine": "ceza",
    "legal": "yasal",
    "theft": "hırsızlık",
    "criminal offense": "suç",
    "penalty": "ceza",
    "appreciate": "takdir etmek",
    "estimate": "tahmin etmek",
    "expose": "maruz bırakmak",
    "compensate": "telafi etmek",
    "exploit": "istismar etmek",
    "odd": "garip",
    "anticipate": "beklemek",
    "distracted": "dikkati dağılmış",
    "initially": "başlangıçta",
    "irritated": "sinirli",
    "make sense of": "anlam vermek",
    "benefit from": "yararlanmak",
    "contribute to": "katkıda bulunmak",
    "due to": "nedeniyle",
    "perceive": "algılamak",
    "prompt": "teşvik etmek",
    "recall": "hatırlamak",
    "repetitive": "tekrarlayan",
    "escape from": "kaçmak",
    "get away with": "yanına kar kalmak",
    "impact on": "etkisi",
    "random": "rastgele",
    "reveal": "açığa çıkarmak",
    "sensitive to": "duyarlı",
    "ties in with": "ile bağlantılı",
    "unpredictable": "tahmin edilemez",
    "variation": "varyasyon",
    "interfere with": "müdahale etmek",
    "quality of life": "yaşam kalitesi",
    "suffer from": "muhtemel",
    "actual": "gerçek",
    "force": "zorlamak",
    "irresponsible": "sorumsuz",
    "leak": "sızdırmak",
    "literally": "kelimenin tam anlamıyla",
    "accessible": "erişilebilir",
    "distribute": "dağıtmak",
    "commercial": "ticari",
    "assure": "temin etmek",
    "equip": "donatmak",
    "justify": "haklı çıkarmak",
    "headquarters": "genel merkez",
    "practical": "pratik",
    "presumably": "muhtemelen",
    "revolutionary": "devrim niteliğinde",
    "smoothly": "düzgün bir şekilde",
    "motor": "motor",
    "network": "ağ",
    "manual": "el kitabı",
    "modify": "değiştirmek",
    "surface": "yüzey",
    "terrifying": "korkutucu",
    "unbearable": "katlanılmaz",
    "vital": "hayati",
    "rapidly": "hızla",
    "steer": "yönlendirmek"
}


ogrendiklerim = set()
tekrar_sorulacaklar = set()

def rastgele_kelime():
    sorulacak_kelime = [kelime for kelime in kelimeler.keys() if kelime not in ogrendiklerim]  #öğrendiğim kelimeleri sorma
    if sorulacak_kelime:
        return random.choice(sorulacak_kelime)
    return None

def dogru_cevabi_goster():
    dogru_cevap_label.config(text=f"Doğru Cevap: {kelimeler[mevcut_kelime]}")
    dogru_cevap_button.config(state=tk.DISABLED)
    ogren_button.config(state=tk.NORMAL)
    tekrar_sor_button.config(state=tk.NORMAL)

def sonraki_kelime():
    global mevcut_kelime
    mevcut_kelime = rastgele_kelime()
    if mevcut_kelime:
        soru_label.config(text=f"Kelime: {mevcut_kelime}")
        dogru_cevap_label.config(text="")
        dogru_cevap_button.config(state=tk.NORMAL)
        ogren_button.config(state=tk.DISABLED)
        tekrar_sor_button.config(state=tk.DISABLED)
    else:
        soru_label.config(text="Öğrenilecek başka kelime yok!")

def kelimeyi_ogrendim():
    ogrendiklerim.add(mevcut_kelime)
    if mevcut_kelime in tekrar_sorulacaklar:
        tekrar_sorulacaklar.remove(mevcut_kelime)
    sonraki_kelime()

def tekrar_sor():
    tekrar_sorulacaklar.add(mevcut_kelime)
    sonraki_kelime()

def kalan_kelime_sayisi_guncelle():    #(bir problem var)
    kalan_sayi = len([kelime for kelime in kelimeler.keys() if kelime not in ogrendiklerim and kelime not in tekrar_sorulacaklar])
    kalan_label.config(text=f"Kalan kelime sayısı: {kalan_sayi}")
    kalan_pencere_label.config(text=f"Kalan kelime sayısı: {kalan_sayi}")

def kalan_pencere_ac():
    kalan_pencere = tk.Toplevel(root)
    kalan_pencere.title("Kalan Kelime Sayısı")
    global kalan_pencere_label
    kalan_pencere_label = tk.Label(kalan_pencere, text="", font=("Helvetica", 14))
    kalan_pencere_label.pack(pady=20)
    kalan_kelime_sayisi_guncelle()




root = tk.Tk()
root.title("Kelime Öğrenme Uygulaması")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

soru_label = tk.Label(root, text="", font=("Helvetica", 16), fg="#333333", bg="#f0f0f0")
soru_label.pack(pady=20)

dogru_cevap_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#ff0000", bg="#f0f0f0")
dogru_cevap_label.pack(pady=10)

dogru_cevap_button = tk.Button(root, text="Doğru Cevabı Göster", command=dogru_cevabi_goster, font=("Helvetica", 14), bg="#4CAF50", fg="white")
dogru_cevap_button.pack(pady=5)

ogren_button = tk.Button(root, text="Bu Kelimeyi Öğrendim", command=kelimeyi_ogrendim, font=("Helvetica", 14), bg="#2196F3", fg="white")
ogren_button.pack(pady=5)

tekrar_sor_button = tk.Button(root, text="Bu Kelimeyi Tekrar Sor", command=tekrar_sor, font=("Helvetica", 14), bg="#f44336", fg="white")
tekrar_sor_button.pack(pady=5)

sonraki_button = tk.Button(root, text="Sonraki Kelime", command=sonraki_kelime, font=("Helvetica", 14), bg="#FFC107", fg="white")
sonraki_button.pack(pady=20)

kalan_button = tk.Button(root, text="Kalan Kelime Sayısı", command=kalan_pencere_ac, font=("Helvetica", 14), bg="#795548", fg="white")
kalan_button.pack(pady=10)

kalan_label = tk.Label(root, text="", font=("Helvetica", 14), fg="#333333", bg="#f0f0f0")
kalan_label.pack(pady=10)



mevcut_kelime = None
sonraki_kelime()

root.mainloop()
