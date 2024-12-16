sifre = "19649"

rakamlar = "0123456789"

flag = 0

for basamak0 in rakamlar: 
    for basamak1 in rakamlar:
        for basamak2 in rakamlar:
            for basamak3 in rakamlar:
                for basamak4 in rakamlar:
                    deneme = (basamak0+basamak1+basamak2+basamak3+basamak4)
                    print(deneme)
                    if deneme == sifre:
                        print ("Parolanız: "+ deneme)
                        flag = True
                        break
                
                if flag == True:
                    break
            if flag == True:
                    break
        if flag == True:
                 break   
    if flag == True:
                 break    