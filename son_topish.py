import random as r


eng_katta_ishora = True
qiymat_uzunligi = []
qiymat_uzunligi2 = []
while eng_katta_ishora:

    ishora = True
    print("Keling o'ylagan sonni topish oyinini oynaymiz")
    taxminiy_variant = int(input("1 dan 10 gacha son o'yladim. Topa olasizmi ? \n>> "))
    # print(taxminiy_variant)
    sonlar = list(range(1,11))
    # print(sonlar)
    oylagan_son = r.choice(sonlar)
    # print(oylagan_son)

    while ishora :
        qiymat = taxminiy_variant
        if qiymat > oylagan_son:
            taxminiy_variant = int(input("Xato,o'ylangan son bundan kichikroq. Yana harakat qilib koring: \n>>"))
            qiymat_uzunligi.append(qiymat)
        elif qiymat < oylagan_son:
            taxminiy_variant = int(input("Xato, o'ylangan son bundan kattaroq. Yana harakat qilib koring \n>>"))
            qiymat_uzunligi.append(qiymat)
        elif qiymat == oylagan_son:
            qiymat_uzunligi.append(qiymat)
            print(f"TOPDINGIZ!!! {oylagan_son} sonini o'ylagan edim. {len(qiymat_uzunligi)} ta taxmin bilan topdingiz.  Tabriklayman !!! ")
            ishora = False
            eng_katta_ishora = False
        else:
            print("Togri qiymat kiriting")
            
        
    
    eng_katta_ishora2 = True

    while eng_katta_ishora2:
        print("1 dan 10 gacha son oylang. Men topishga harakat qilaman.")
        qiymat = input("Son O'ylagan bo'lsangiz enter tugmasini bosing.")
        qiymat_uzunligi = []
        sonlar = list(range(1,11))
        # print(sonlar)
        oylagan_sonim = r.choice(sonlar)

        savol_sonning_qiyamti = str(input(f"Siz {oylagan_sonim} sonini o'yladingiz: to'g'rimi (T), men o'ylagan son     bundan kattaroq (+), yoki kichikroq (-) \n>> "))

        ishora2 = True
        while ishora2:
            qiymat = savol_sonning_qiyamti
            if qiymat  == '+':
                oylagan_sonim += 1
                qiymat_uzunligi2.append(qiymat)
                savol_sonning_qiyamti = str(input(f"Siz {oylagan_sonim + 1} sonini o'yladingiz: to'g'rimi (T), men  o'ylagan son bundan kattaroq (+), yoki kichikroq (-) \n>> "))
            elif qiymat == '-':
                oylagan_sonim -= 1
                qiymat_uzunligi2.append(qiymat)
                savol_sonning_qiyamti = str(input(f"Siz {oylagan_sonim - 1} sonini o'yladingiz: to'g'rimi (T), men  o'ylagan son bundan kattaroq (+), yoki kichikroq (-) \n>> "))
            elif qiymat == 't' or qiymat == 'T':
                qiymat_uzunligi2.append(qiymat)
                print(f"Soningizni {len(qiymat_uzunligi2)} ta taxmin bilan topdik")
                ishora2 = False
                eng_katta_ishora2 = False
            else:
                print("Togri qiymat kiriting")




    if qiymat_uzunligi > qiymat_uzunligi2:
        print(f"Siz {len(qiymat_uzunligi2)} ta taxmin bilan topdingiz va yutqazdingiz ")
    elif qiymat_uzunligi2 > qiymat_uzunligi:
        print(f"Siz {len(qiymat_uzunligi2)} ta taxmin bilan topdingiz va yutdingiz ")
    elif qiymat_uzunligi2 == qiymat_uzunligi:
        print(f"Siz {len(qiymat_uzunligi2)} ta taxmin bilan topdingiz va durrang! ")

    savol = str(input("Yana o'ynashni hohlaysizmi ? ha(h)  /  yo'q(y) \n>> "))
    if savol == 'h':
        eng_katta_ishora = True
        eng_katta_ishora2 = True
        ishora = True
        ishora2= True
    else :
        print("O'yinni yakunladingiz")
        
   
    
    
