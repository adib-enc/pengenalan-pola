# Pengenalan Pola - P3
# Naive bayes classifier

Dataset: Fake news

Percobaan klasifikasi menggunakan sklearn.GaussianNB, apakah sebuah berita termasuk berita palsu atau bukan.
- Skenario 1 : berdasarkan panjang text

## Hasil
### skenario 1
```
              precision    recall  f1-score   support

           0       0.43      0.23      0.30        13
           1       0.23      0.43      0.30         7

    accuracy                           0.30        20
   macro avg       0.33      0.33      0.30        20
weighted avg       0.36      0.30      0.30        20
```