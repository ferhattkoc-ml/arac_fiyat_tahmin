🚗 AudiPredict AI

Premium Segment İkinci El Araçlar İçin Yapay Zekâ Destekli Fiyat Tahmin Sistemi

🏆 Süleyman Demirel Üniversitesi İstatistik Bölümü Lisans Araştırma Projeleri kapsamında geliştirilmiş ve bölüm birincisi seçilmiş araştırma projesi.

⸻

📖 Proje Hakkında

AudiPredict AI, premium segment ikinci el araçların teknik, yapısal ve kullanım özelliklerine göre piyasa değerlerini tahmin etmek amacıyla geliştirilmiş makine öğrenmesi tabanlı bir fiyat tahmin sistemidir.

Proje, Süleyman Demirel Üniversitesi İstatistik Bölümü lisans araştırma projesi kapsamında gerçekleştirilmiş olup istatistiksel modelleme, veri madenciliği, makine öğrenmesi ve uygulamalı yapay zekâ tekniklerini bir araya getirmektedir.

Araştırmanın temel amacı, ikinci el araç fiyatlarını etkileyen değişkenleri ortaya çıkarmak ve bu değişkenleri kullanarak yüksek doğruluklu bir tahmin modeli geliştirmektir.

Geleneksel regresyon yaklaşımlarının aksine, araç piyasasında bulunan karmaşık ve doğrusal olmayan ilişkileri modelleyebilmek amacıyla CatBoost algoritması tercih edilmiştir.

⸻

🏆 Akademik Başarı

Bu çalışma, Süleyman Demirel Üniversitesi İstatistik Bölümü tarafından gerçekleştirilen lisans araştırma projeleri değerlendirmesinde bölüm birincisi seçilmiştir.

Değerlendirme sürecinde aşağıdaki kriterler dikkate alınmıştır:

* Bilimsel araştırma yöntemi
* Veri toplama ve veri kalitesi
* İstatistiksel analiz yaklaşımı
* Makine öğrenmesi performansı
* Sonuçların yorumlanabilirliği
* Gerçek dünya uygulama potansiyeli
* Yazılım geliştirme kalitesi

Proje, akademik ve teknik açıdan en yüksek başarı derecesini elde ederek bölüm birinciliği kazanmıştır.

⸻

🎯 Araştırma Problemi

Türkiye ikinci el otomobil piyasasında araç fiyatları birçok faktörden etkilenmektedir:

* Model yılı
* Kilometre
* Motor gücü
* Yakıt tipi
* Şanzıman tipi
* Kasa tipi
* Donanım paketi
* Hasar geçmişi
* Marka ve model prestiji

Bu faktörler arasındaki karmaşık ilişkiler nedeniyle araç değerleme süreci çoğu zaman uzman görüşüne dayanmaktadır.

Bu proje ile birlikte bu sürecin veri odaklı ve nesnel hale getirilmesi amaçlanmıştır.

⸻

📊 Veri Seti

Araştırma kapsamında oluşturulan veri seti premium segment araçlardan meydana gelmektedir.

Kullanılan temel değişkenler:

Değişken	Açıklama
Model	Araç modeli
Kasa Tipi	Sedan, SUV vb.
Yakıt Tipi	Dizel, Benzin, Hibrit
Vites	Manuel, Otomatik
Kilometre	Toplam kullanım
Motor Gücü	HP
Renk	Araç rengi
Yaş	Araç yaşı
Hasar Kaydı	Hasar bilgisi
Kimden	Sahibinden / Galeriden
Fiyat	Hedef değişken

⸻

🔍 Veri Ön İşleme Süreci

Model performansını artırmak amacıyla veri üzerinde kapsamlı ön işleme çalışmaları gerçekleştirilmiştir.

Yapısal Filtreleme

Aşağıdaki araçlar veri setinden çıkarılmıştır:

* Ağır hasar kayıtlı araçlar
* Şase işlemli araçlar
* Airbag açmış araçlar
* Podye işlemli araçlar

Zaman Filtreleme

2010 yılı öncesi araçlar analiz dışında bırakılmıştır.

Eksik Veri Analizi

Eksik gözlemler detaylı olarak incelenmiş ve uygun yöntemlerle işlenmiştir.

Aykırı Değer Analizi

İstatistiksel aykırı değer tespiti uygulanmıştır.

⸻

⚙️ Özellik Mühendisliği

Ham değişkenlerin yanı sıra yeni öznitelikler üretilmiştir.

km_per_age

Araçların kullanım yoğunluğunu ölçmek amacıyla:

km_per_age = kilometre / yaş

değişkeni oluşturulmuştur.

Bu değişken modelin en güçlü tahminleyicilerinden biri olmuştur.

⸻

🤖 Kullanılan Makine Öğrenmesi Algoritması

CatBoost Regressor

Proje kapsamında CatBoost tercih edilmiştir.

Başlıca avantajları:

* Kategorik değişkenleri doğal olarak işleyebilmesi
* Overfitting’e karşı dayanıklılık
* Yüksek doğruluk
* Hızlı eğitim süreci
* Açıklanabilir yapıya uygun olması

⸻

🎯 Hiperparametre Optimizasyonu

Model parametreleri Optuna kullanılarak optimize edilmiştir.

Optimizasyon kapsamında:

* Learning Rate
* Tree Depth
* Iteration Count
* L2 Regularization
* Bagging Temperature

parametreleri araştırılmıştır.

⸻

📈 Model Performansı

Test verisi üzerinde elde edilen sonuçlar:

Metrik	Sonuç
R²	0.9708
MAE	129,973 TL
RMSE	181,508 TL

Sonuçların Yorumu

Model araç fiyatlarındaki toplam varyansın yaklaşık %97’sini açıklayabilmektedir.

Bu sonuç ikinci el araç piyasasında oldukça yüksek bir tahmin başarısına işaret etmektedir.

⸻

🔬 Model Açıklanabilirliği

Model kararlarını yorumlayabilmek amacıyla SHAP analizi uygulanmıştır.

Analiz sonuçlarına göre fiyat üzerinde en etkili değişkenler:

* Motor Gücü
* Model Prestiji
* Araç Yaşı
* Kilometre
* Yakıt Tipi

olarak belirlenmiştir.

⸻

🏗️ Sistem Mimarisi

Proje yalnızca bir makine öğrenmesi modeli değil aynı zamanda üretim ortamına hazır bir uygulama olarak tasarlanmıştır.

Backend

* Python
* Flask
* CatBoost
* SQLAlchemy

Database

* PostgreSQL

Frontend

* HTML
* CSS
* JavaScript

Monitoring

* Prediction Logging
* Error Tracking
* Dashboard Analytics

⸻

📁 Proje Yapısı

.
├── app.py
├── model.cbm
├── database
│   ├── __init__.py
│   └── models.py
├── templates
│   ├── index.html
│   └── dashboard.html
├── static
│   ├── css
│   └── js
└── logs

⸻

🚀 Kurulum

Repository’yi klonlayın

git clone https://github.com/ferhattkoc-ml/arac_fiyat_tahmin.git

Dizine geçin

cd arac_fiyat_tahmin

Bağımlılıkları yükleyin

pip install -r requirements.txt

Uygulamayı başlatın

python app.py

⸻

🌐 API Kullanımı

POST /predict

Örnek istek:

{
  "model_variant":"Audi A6",
  "year":2021,
  "mileage":38000,
  "fuel_type":"Diesel",
  "transmission":"Automatic"
}

Örnek yanıt:

{
  "predicted_price":2450000
}

⸻

📚 Kullanılan Teknolojiler

* Python
* Pandas
* NumPy
* Scikit-Learn
* CatBoost
* Optuna
* SHAP
* Flask
* PostgreSQL
* SQLAlchemy
* HTML/CSS/JavaScript

⸻

👨‍🎓 Araştırmacı

Ferhat Koç

İstatistik Lisans Mezunu

Süleyman Demirel Üniversitesi

⸻

👨‍🏫 Akademik Danışman

Prof. Dr. Ulaş Yamancı

Süleyman Demirel Üniversitesi

İstatistik Bölümü

⸻

📜 Lisans

MIT License

⸻

⭐ Sonuç

AudiPredict AI, istatistiksel araştırma metodolojisi ile modern makine öğrenmesi tekniklerini bir araya getirerek premium segment ikinci el araç fiyatlarının yüksek doğrulukla tahmin edilmesini sağlamaktadır.

Proje hem akademik araştırma başarısı hem de gerçek dünya uygulama potansiyeli açısından güçlü bir örnek oluşturmakta ve bölüm birinciliği ile ödüllendirilmiştir.
