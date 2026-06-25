<div align="center">

# 🚗 AudiPredict AI

**Premium Segment İkinci El Araçlar İçin Yapay Zekâ Destekli Fiyat Tahmin Sistemi**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![CatBoost](https://img.shields.io/badge/CatBoost-FF8C00?style=for-the-badge&logo=python&logoColor=white)](https://catboost.ai)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://postgresql.org)
[![Optuna](https://img.shields.io/badge/Optuna-3C873A?style=for-the-badge&logo=python&logoColor=white)](https://optuna.org)
[![SHAP](https://img.shields.io/badge/SHAP-2B5B84?style=for-the-badge&logo=python&logoColor=white)](https://shap.readthedocs.io)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**🏆 SDÜ İstatistik Bölümü — Lisans Araştırma Projeleri Bölüm Birincisi**

[![R²](https://img.shields.io/badge/R%C2%B2-0.9708-brightgreen?style=flat-square)]()

</div>

---

## 📌 Proje Hakkında

**AudiPredict AI**, premium segment ikinci el araçların teknik, yapısal ve kullanım özelliklerine göre piyasa değerlerini tahmin etmek amacıyla geliştirilmiş **makine öğrenmesi** tabanlı bir fiyat tahmin sistemidir.

Proje, **Süleyman Demirel Üniversitesi İstatistik Bölümü** lisans araştırma projesi kapsamında gerçekleştirilmiş olup istatistiksel modelleme, veri madenciliği, makine öğrenmesi ve uygulamalı yapay zekâ tekniklerini bir araya getirmektedir.

> **Akademik Danışman:** Prof. Dr. Ulaş Yamancı · SDÜ İstatistik Bölümü

---

## 🏆 Akademik Başarı

Bu çalışma, SDÜ İstatistik Bölümü lisans araştırma projeleri değerlendirmesinde **Bölüm Birincisi** seçilmiştir.

| Değerlendirme Kriteri | Açıklama |
|-----------------------|----------|
| 🔬 Bilimsel Araştırma Yöntemi | Hipotez-test odaklı, tekrarlanabilir metodoloji |
| 📊 Veri Kalitesi | Kapsamlı ön işleme, aykırı değer analizi, eksik veri yönetimi |
| 📈 Model Performansı | R² = 0.9708 ile yüksek tahmin başarısı |
| 🔍 Yorumlanabilirlik | SHAP analizi ile model kararlarının açıklanabilirliği |
| 🌍 Gerçek Dünya Uygulaması | Flask API + admin paneli ile production-ready sistem |
| 🧪 Yazılım Kalitesi | Modüler yapı, logging, hata yönetimi |

---

## 🎯 Araştırma Problemi

Türkiye ikinci el otomobil piyasasında araç fiyatları birçok faktörden etkilenmektedir. Bu faktörler arasındaki karmaşık ilişkiler nedeniyle araç değerleme süreci çoğunlukla uzman görüşüne dayanmaktadır. Bu proje ile sürecin **veri odaklı ve nesnel** hale getirilmesi amaçlanmıştır.

| Değişken | Açıklama |
|----------|----------|
| **Model** | Araç modeli (Audi A6, BMW 5 Serisi vb.) |
| **Kasa Tipi** | Sedan, SUV, Hatchback, Coupe |
| **Yakıt Tipi** | Dizel, Benzin, Hibrit |
| **Vites** | Manuel, Otomatik |
| **Kilometre** | Toplam kullanım (km) |
| **Motor Gücü** | HP cinsinden |
| **Renk** | Araç rengi |
| **Yaş** | Araç yaşı (yıl) |
| **Hasar Kaydı** | Hasar geçmişi bilgisi |
| **Kimden** | Sahibinden / Galeriden |
| **Fiyat** | 🎯 Hedef değişken |

---

## 🔧 Veri Ön İşleme

### Yapısal Filtreleme

Aşağıdaki araçlar veri setinden çıkarılmıştır:
- ⛔ Ağır hasar kayıtlı araçlar
- ⛔ Şase işlemli araçlar
- ⛔ Airbag açmış araçlar
- ⛔ Podye işlemli araçlar

### Zaman Filtreleme

📅 2010 yılı öncesi araçlar analiz dışında bırakılmıştır.

### Eksik Veri & Aykırı Değer

Detaylı eksik veri analizi ve istatistiksel aykırı değer tespiti uygulanmıştır.

---

## ⚙️ Özellik Mühendisliği

### km_per_age

Araçların kullanım yoğunluğunu ölçmek için türetilmiş öznitelik:

```
km_per_age = kilometre / yaş
```

Bu değişken modelin **en güçlü tahminleyicilerinden biri** olmuştur.

---

## 🤖 Model Mimarisi

```
┌─────────────┐    ┌──────────────┐    ┌──────────┐    ┌─────────┐
│  Ham Veri   │ →  │ Ön İşleme &  │ →  │ CatBoost │ →  │ Flask   │
│  (CSV/DB)   │    │ Feature Eng. │    │ Model    │    │ API     │
└─────────────┘    └──────────────┘    └──────────┘    └─────────┘
                        │                    │               │
                        ↓                    ↓               ↓
                 Filtreleme           Optuna HP       POST /predict
                 Eksik Veri           Optimizasyon    Admin Panel
                 Aykırı Değer         SHAP Analizi    Logging
```

### CatBoost Regressor

| Özellik | Avantaj |
|---------|---------|
| 🏗️ Kategorik Değişken Desteği | One-hot encoding gerektirmez, doğal işler |
| 🛡️ Overfitting Koruması | Düzenli ağaç yapısı ile güçlü regularization |
| ⚡ Performans | Yüksek doğruluk, hızlı eğitim |
| 🔍 Açıklanabilirlik | SHAP ile uyumlu |

---

## 🎯 Hiperparametre Optimizasyonu

**Optuna** framework'ü ile optimize edilmiştir:

| Parametre | Arama Aralığı |
|-----------|---------------|
| **Learning Rate** | 0.01 – 0.3 |
| **Tree Depth** | 4 – 10 |
| **Iteration Count** | 500 – 5000 |
| **L2 Regularization** | 1 – 10 |
| **Bagging Temperature** | 0.5 – 1.5 |

---

## 📈 Model Performansı

| Metrik | Değer |
|--------|-------|
| **R² Score** | **0.9708** |
| **MAE** | 129,973 ₺ |
| **RMSE** | 181,508 ₺ |

> **Yorum:** Model araç fiyatlarındaki toplam varyansın ~%97'sini açıklayabilmektedir — ikinci el araç piyasasında oldukça yüksek bir başarı.

---

## 🔬 Model Açıklanabilirliği (SHAP)

SHAP analizi ile fiyat üzerinde en etkili değişkenler:

```
Motor Gücü  ████████████████████████
Model       ████████████████████
Araç Yaşı   ██████████████
Kilometre   ██████████
Yakıt Tipi  ██████
```

---

## 🌐 API & Sistem Mimarisi

### Backend

| Katman | Teknoloji |
|--------|-----------|
| **API** | Flask (Python) |
| **Model** | CatBoost (`.cbm` dosyası) |
| **Veritabanı** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Frontend** | HTML + CSS + JavaScript |

### API Kullanımı

```bash
POST /predict
Content-Type: application/json

{
  "model_variant": "Audi A6",
  "year": 2021,
  "mileage": 38000,
  "fuel_type": "Diesel",
  "transmission": "Automatic"
}
```

**Yanıt:**

```json
{
  "predicted_price": 2450000
}
```

---

## 🚀 Kurulum

```bash
# 1. Depoyu klonla
git clone https://github.com/ferhattkoc-ml/arac_fiyat_tahmin.git
cd arac_fiyat_tahmin

# 2. Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Bağımlılıkları yükle
pip install -r requirements.txt

# 4. Uygulamayı başlat
python app.py
```

---

## 🛠️ Tech Stack

| Kategori | Teknolojiler |
|----------|-------------|
| **Dil** | Python 3.9+ |
| **Web Framework** | Flask |
| **ML Model** | CatBoost Regressor |
| **HP Optimizasyon** | Optuna |
| **Model Açıklama** | SHAP |
| **Veri İşleme** | Pandas, NumPy, Scikit-learn |
| **Veritabanı** | PostgreSQL + SQLAlchemy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Deployment** | Flask (Gunicorn uyumlu) |

---

## 📂 Proje Yapısı

```
arac_fiyat_tahmin/
├── app.py                          # Flask uygulaması (API + routes)
├── model.cbm                       # Eğitilmiş CatBoost modeli
├── requirements.txt                # Bağımlılıklar
├── runtime.txt                     # Python runtime (Heroku)
├── templates/
│   ├── index.html                  # Ana sayfa / tahmin arayüzü
│   ├── admin.html                  # Admin paneli
│   └── admin_login.html            # Admin giriş sayfası
└── README.md                       # Bu dosya
```

---

## 📜 Lisans

Bu proje **MIT License** ile lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

---

## 👤 Araştırmacı

**Ferhat Koç** · İstatistik Lisans Mezunu · SDÜ

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/ferhattkoc-ml)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/ferhattkocc/)

## 👨‍🏫 Akademik Danışman

**Prof. Dr. Ulaş Yamancı** · SDÜ İstatistik Bölümü

---

<div align="center">
  <sub>Built with ❤️ by Ferhat Koç · SDÜ İstatistik Bölüm Birincisi 🏆</sub>
</div>
