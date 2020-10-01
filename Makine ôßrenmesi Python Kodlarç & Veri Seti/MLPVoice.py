#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:18:02 2020
@author: beyzasgnms
"""
import pandas as pd
df = pd.read_csv('voice.csv')
y = df.label
x = df.drop(['label'], axis = 1)

from sklearn.model_selection import train_test_split
training_set, validation_set = train_test_split(df, test_size = 0.2, random_state = 21)
X_train = training_set.iloc[:,0:-1].values
Y_train = training_set.iloc[:,-1].values
X_val = validation_set.iloc[:,0:-1].values
y_val = validation_set.iloc[:,-1].values

from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(hidden_layer_sizes=(150,100,50), max_iter=300,activation = 'relu',random_state=1)
classifier.fit(X_train, Y_train)
y_pred = classifier.predict(X_val)
y_tahmin = classifier.predict(x)

from sklearn.metrics import accuracy_score 
basari = accuracy_score(y, y_tahmin, normalize=True, sample_weight=None)
print("Doğruluk değeri(%cinsinden):")
print(basari*100)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_pred, y_val)
hata = confusion_matrix(y_val, y_pred)
print("Hata matrisi:")
print(hata)

from sklearn.model_selection import cross_val_score
print("10 katlı çapraz doğrulama ile yöntemin başarısı:")
print(cross_val_score(classifier, df, y, cv=10))

"""Kullanıcıdan alınan verilerin hangi etikete ait olduğunu bulduğumuz kısım"""

print("Test etmek istediğiniz verileri giriniz")
print("Toplam 20 adet değer vardır. Her veri girişinizden sonra enter tuşu ile diğer veriyi giriniz.")
meanfreq = int(input("Ortalama frekans değerini giriniz(kHz cinsinden):"))
sd = int(input("Frekans değerinin standart sapmasını giriniz:"))
median = int(input("Frekans değerinin medyan değeriniz giriniz(kHz cinsinden):"))
Q25 = int(input("Frekans değerinin ilk çeyrek değeriniz giriniz(kHz cinsinden):"))
Q75 = int(input("Frekans değerinin son çeyrek değeriniz giriniz(kHz cinsinden):"))
IQR = int(input("Frekans değerinin karesel aralık değeriniz giriniz(kHz cinsinden):"))
skew = int(input("Çarpıklık değerini giriniz:"))
kurt = int(input("Basıklık değerini giriniz:"))
spent = int(input("Spektral entropi değerini giriniz:"))
sfm = int(input("Spektral düzlük değerini giriniz:"))
mode = int(input("Frekans değerinin modunu giriniz:"))
centroid = int(input("Frekansın sentroid değerini giriniz:"))
meanfun =int(input("Akustik sinyal üzerinden ölçülen temel frekansın ortalamasını giriniz:"))
minfun = int(input("Akustik sinyal üzerinden ölçülen minimum temel frekansın ortalamasını giriniz:"))
maxfun = int(input("Akustik sinyal üzerinden ölçülen maksimum temel frekansın ortalamasını giriniz:"))
meandom =int(input("Akustik sinyal üzerinden ölçülen baskın temel frekansın ortalamasını giriniz:"))
mindom = int(input("Akustik sinyal üzerinden ölçülen minimum baskın temel frekans değerini giriniz:"))
maxdom = int(input("Akustik sinyal üzerinden ölçülen maksimum baskın temel frekans değerini giriniz:"))
dfrange = int(input("Akustik sinyal üzerinden ölçülen baskın frekans aralığını giriniz:"))
modindx = int(input("Modülasyon indeksi değerini giriniz(Temel frekansların bitişik ölçümleri arasındaki toplam mutlak farkın frekans aralığına bölünmesiyle hesaplanır):"))
Inputs = [[meanfreq, sd, median, Q25, Q75, IQR, skew, kurt, spent,sfm, mode, centroid, meanfun, minfun, maxfun, meandom, mindom, maxdom, dfrange, modindx]]
P_array = pd.Series(data=Inputs)
p_array = P_array.values.reshape(1,-1)
tahminle = classifier.predict(Inputs)
# Sonuç 0 ise erkek, 1 ise kadın
print("Verilerini girdiğiniz kişinin cinsiyeti: ", end="")
if tahminle:
    print("Kadın")
else:
    print("Erkek")