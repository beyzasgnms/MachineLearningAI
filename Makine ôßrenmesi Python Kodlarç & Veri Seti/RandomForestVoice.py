#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:19:21 2020

@author: beyzasgnms
"""
import pandas as pd
df = pd.read_csv('voice.csv')
y = df.label
x = df.drop(['label'], axis = 1)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3) 

from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)

from sklearn import metrics
print("Doğruluk değeri(%cinsinden):")
print((metrics.accuracy_score(y_test, y_pred)*100))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred, y_test)
hata = confusion_matrix(y_test, y_pred)
print("Hata matrisi:")
print(hata)

from sklearn.model_selection import cross_val_score
print("10 katlı çapraz doğrulama ile yöntemin başarısı: ", end="")
print(cross_val_score(clf, df, y, cv=10))

"""Kullanıcıdan alınan verilerin hangi etikete ait olduğunu bulduğumuz kısım"""

print("Test etmek istediğiniz verileri giriniz.")
print("Toplam 20 adet değer vardır. Her veri girişinizden sonra enter tuşu ile diğer veriyi giriniz.")
meanfreq = float(input("Ortalama frekans değerini giriniz(kHz cinsinden): "))
sd = float(input("Frekans değerinin standart sapmasını giriniz: "))
median = float(input("Frekans değerinin medyan değeriniz giriniz(kHz cinsinden): "))
Q25 = float(input("Frekans değerinin ilk çeyrek değeriniz giriniz(kHz cinsinden): "))
Q75 = float(input("Frekans değerinin son çeyrek değeriniz giriniz(kHz cinsinden): "))
IQR = float(input("Frekans değerinin karesel aralık değeriniz giriniz(kHz cinsinden): "))
skew = float(input("Çarpıklık değerini giriniz: "))
kurt = float(input("Basıklık değerini giriniz: "))
spent = float(input("Spektral entropi değerini giriniz: "))
sfm = float(input("Spektral düzlük değerini giriniz: "))
mode = float(input("Frekans değerinin modunu giriniz: "))
centroid = float(input("Frekansın sentroid değerini giriniz: "))
meanfun =float(input("Akustik sinyal üzerinden ölçülen temel frekansın ortalamasını giriniz: "))
minfun = float(input("Akustik sinyal üzerinden ölçülen minimum temel frekansın ortalamasını giriniz: "))
maxfun = float(input("Akustik sinyal üzerinden ölçülen maksimum temel frekansın ortalamasını giriniz: "))
meandom =float(input("Akustik sinyal üzerinden ölçülen baskın temel frekansın ortalamasını giriniz: "))
mindom = float(input("Akustik sinyal üzerinden ölçülen minimum baskın temel frekans değerini giriniz: "))
maxdom = float(input("Akustik sinyal üzerinden ölçülen maksimum baskın temel frekans değerini giriniz: "))
dfrange = float(input("Akustik sinyal üzerinden ölçülen baskın frekans aralığını giriniz: "))
modindx = float(input("Modülasyon indeksi değerini giriniz(Temel frekansların bitişik ölçümleri arasındaki toplam mutlak farkın frekans aralığına bölünmesiyle hesaplanır): "))
Inputs = [[meanfreq, sd, median, Q25, Q75, IQR, skew, kurt, spent,sfm, mode, centroid, meanfun, minfun, maxfun, meandom, mindom, maxdom, dfrange, modindx]]
P_array = pd.Series(data=Inputs)
p_array = P_array.values.reshape(1,-1)
tahminle = clf.predict(Inputs)
# Sonuç 0 ise erkek, 1 ise kadın
print("Verilerini girdiğiniz kişinin cinsiyeti: ", end="")
if tahminle:
    print("Kadın")
else:
    print("Erkek")