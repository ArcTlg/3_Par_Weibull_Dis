from xlrd import open_workbook
from random import uniform
import math
dosya = open_workbook("w_5_5_4.xlsx")
sayfa = dosya.sheet_by_index(0)

def komsuluk(a, b, c, index):
    e = round(uniform(0.01, 0.09), 6)
    komsuluklar = [[a, b+e, c+e], [a, b+e, c], [a, b, c+e], [a, b-e, c-e], [a, b-e, c], [a, b, c-e], [a, b+e, c-e],
                   [a, b-e, c+e], [a+e, b, c+e], [a+e, b, c], [a-e, b, c-e], [a-e, b, c], [a-e, b, c+e], [a+e, b, c-e],
                   [a+e, b+e, c], [a-e, b-e, c], [a+e, b-e, c], [a-e, b+e, c], [a+e, b+e, c+e], [a-e, b-e, c-e]]
    return komsuluklar[index]

def kisitlar(kisita, kisitb, kisitc):
    kisitKontrol = True
    if kisita <= 0:
        kisitKontrol = False
    if kisitc >= minveri:
        kisitKontrol = False
    if kisitc < 0:
        kisitKontrol = False
    if kisitb <= 0 or kisitb <= kisitc:
        kisitKontrol = False
    return kisitKontrol

def fonk(para, parb, parc):
    cozum = 0
    for i in range(sayfa.nrows):
        cozum += round(math.log(para/parb, math.e) + (-1*(((veriler[i]-parc)/parb)**para))+((para-1) * math.log((veriler[i]-parc)/parb, math.e)), 6)
    return cozum

def yerelarama(a1, b1, c1):
    u = 1
    while True:
        a3, b3, c3 = 0, 0, 0
        a4, b4, c4 = 0, 0, 0
        d = 0.1
        k, l = -0.5, 0.5
        eps1, eps2 = 0.1, 0.005
        if u == 1:
            tekDeg1 = fonk(a1+eps1, b1, c1)
            tekDeg2 = fonk(a1-eps1, b1, c1)
            if tekDeg1 > tekDeg2:
                yon = True
            else:
                yon = False
            while True:
                x1 = round((k+l)/2 - eps2, 6)
                x2 = round((k+l)/2 + eps2, 6)
                if yon:
                    if kisitlar(a1+x1, b1, c1) and kisitlar(a1+x2, b1, c1):
                        fx1 = fonk(a1+x1, b1, c1)
                        fx2 = fonk(a1+x2, b1, c1)
                        if fx1 < fx2:
                            k = x1
                        else:
                            l = x2
                        if l - k < d:
                            lam = round((k + l) / 2, 6)
                            a2 = a1 + lam
                            kon = kisitlar(a2, b1, c1)
                            if kon:
                                a4 = a1
                                a1 = a2
                            break
                    else:
                        break
                else:
                    if kisitlar(a1-x1, b1, c1) and kisitlar(a1-x2, b1, c1):
                        fx1 = fonk(a1-x1, b1, c1)
                        fx2 = fonk(a1-x2, b1, c1)
                        if fx1 < fx2:
                            k = x1
                        else:
                            l = x2
                        if l - k < d:
                            lam = round((k + l) / 2, 6)
                            a2 = a1 - lam
                            kon = kisitlar(a2, b1, c1)
                            if kon:
                                a4 = a1
                                a1 = a2
                            break
                    else:
                        break
            if eps1 > math.sqrt((a4-a1)**2):
                break
        if u == 2:
            tekDeg1 = fonk(a1, b1+eps1, c1)
            tekDeg2 = fonk(a1, b1-eps2, c1)
            if tekDeg1 > tekDeg2:
                yon = True
            else:
                yon = False
            while True:
                x1 = round((k+l)/2 - eps2, 6)
                x2 = round((k+l)/2 + eps2, 6)
                if yon:
                    if kisitlar(a1, b1+x1, c1) and kisitlar(a1, b1+x2, c1):
                        fx1 = fonk(a1+x1, b1, c1)
                        fx2 = fonk(a1+x2, b1, c1)
                        if fx1 < fx2:
                            k = x1
                        else:
                            l = x2
                        if l - k < d:
                            lam = round((k + l) / 2, 6)
                            b2 = b1 + lam
                            kon = kisitlar(a1, b2, c1)
                            if kon:
                                b4 = b1
                                b1 = b2
                            break
                    else:
                        break
                else:
                    if kisitlar(a1, b1-x1, c1) and kisitlar(a1, b1-x2, c1):
                        fx1 = fonk(a1, b1-x1, c1)
                        fx2 = fonk(a1, b1-x2, c1)
                        if fx1 < fx2:
                            k = x1
                        else:
                            l = x2
                        if l - k < d:
                            lam = round((k + l) / 2, 6)
                            b2 = b1 - lam
                            kon = kisitlar(a1, b2, c1)
                            if kon:
                                b4 = b1
                                b1 = b2
                            break
                    else:
                        break
            if eps1 > math.sqrt((b4-b1)**2):
                break
        if u == 3:
            if kisitlar(a1, b1, c1+eps1) and kisitlar(a1, b1, c1-eps1):
                tekDeg1 = fonk(a1, b1, c1+eps1)
                tekDeg2 = fonk(a1, b1, c1-eps1)
                if tekDeg1 > tekDeg2:
                    yon = True
                else:
                    yon = False
            else:
                break
            while True:
                x1 = round((k+l)/2 - eps2, 6)
                x2 = round((k+l)/2 + eps2, 6)
                if yon:
                    if kisitlar(a1, b1, c1+x1) and kisitlar(a1, b1, c1+x2):
                        fx1 = fonk(a1, b1, c1+x1)
                        fx2 = fonk(a1, b1, c1+x2)
                        if fx1 < fx2:
                            k = x1
                        else:
                            l = x2
                        if l - k < d:
                            lam = round((k + l) / 2, 6)
                            c2 = c1 + lam
                            kon = kisitlar(a1, b1, c2)
                            if kon:
                                c4 = c1
                                c1 = c2
                            break
                    else:
                        break
                else:
                    if kisitlar(a1, b1, c1-x1) and kisitlar(a1, b1, c1-x2):
                        fx1 = fonk(a1, b1, c1-x1)
                        fx2 = fonk(a1, b1, c1-x2)
                        if fx1 < fx2:
                            k = x1
                        else:
                            l = x2
                        if l - k < d:
                            lam = round((k + l) / 2, 6)
                            c2 = c1 - lam
                            kon = kisitlar(a1, b1, c2)
                            if kon:
                                c4 = c1
                                c1 = c2
                            break
                    else:
                        break
            if eps1 > math.sqrt((c4-c1)**2):
                break
            else:
                u = 0
        u += 1
    return [a1, b1, c1]

parametreler = []
cozumler = []
sayac = 0
for sutun_no in range(sayfa.ncols):
    a1, a2, b1, b2, c1, c2 = 0.1, 10, 0, 10, 0, 0
    veriler = sayfa.col_values(sutun_no)
    minveri = min(veriler)
    while sayac < 10:
        c2 = minveri
        basA = round(uniform(a1, a2), 6)
        basC = round(uniform(c1, c2), 6)
        b1 = basC + 0.5
        basB = round(uniform(b1, b2), 6)
        basCozum = 0
        veriler = []
        eps = 1
        for satir_no in range(sayfa.nrows):
            veriler.append(sayfa.cell_value(satir_no, sutun_no))
            basCozum += math.log(basA/basB, math.e) + (-1*(((veriler[satir_no]-basC)/basB)**basA))+((basA-1) *
                                                                                         math.log((veriler[satir_no]-basC)/basB, math.e))
        cozumler.append([basA, basB, basC, basCozum])
        sayac += 1
    aort = 0
    bort = 0
    cort = 0
    for i in range(10):
        aort += cozumler[i][0]
        bort += cozumler[i][1]
        cort += cozumler[i][2]
    a1 = (aort/10) - 1
    a2 = (aort/10) + 2
    c1 = (cort/10) + 0.1
    basA = round(uniform(a1, a2), 6)
    basC = round(uniform(c1, c2), 6)
    b1 = basC + 0.1
    b2 = (bort/10) - 0.1
    basB = round(uniform(b1, b2), 6)
    basCozum = 0
    for satir_no in range(sayfa.nrows):
        basCozum += math.log(basA/basB, math.e) + (-1*(((veriler[satir_no]-basC)/basB)**basA))+((basA-1) *
                                                                                     math.log((veriler[satir_no]-basC)/basB, math.e))
    say = 0
    while say < 20:
        par = komsuluk(basA, basB, basC, say)
        kontrol = kisitlar(par[0], par[1], par[2])
        if kontrol == False:
            say += 1
        else:
            yerpar = yerelarama(par[0], par[1], par[2])
            degCozum = fonk(yerpar[0], yerpar[1], yerpar[2])
            if degCozum > basCozum:
                basCozum = degCozum
                basA = yerpar[0]
                basB = yerpar[1]
                basC = yerpar[2]
                say = 0
            else:
                say += 1
    parametreler.append([basA, basB, basC, basCozum])
    print(parametreler[sutun_no])

atop = 0
btop = 0
ctop = 0

for j in range(sayfa.ncols):
    atop += parametreler[j][0]
    btop += parametreler[j][1]
    ctop += parametreler[j][2]
print(atop/100, btop/100, ctop/100)
