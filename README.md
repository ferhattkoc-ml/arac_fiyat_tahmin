
```markdown
# 🏎️ AudiPredict AI — Enterprise Vehicle Valuation
> **Premium Segment İkinci El Araçlarda Teknik ve Yapısal Özelliklere Göre Fiyat Tahmini: CatBoost Regresyon Yaklaşımı Belgesi ve MLOps Altyapısı**[cite: 1]

An analytical, production-ready vehicle valuation platform developed as part of an undergraduate research project[cite: 1]. This repository focuses on bridging the gap between rigorous statistical modeling and robust **Inference Operations (InferenceOps)**[cite: 1].

---

### 📝 Akademik Özet & Proje Amacı
Bu proje, **Süleyman Demirel Üniversitesi Mühendislik ve Doğa Bilimleri Fakültesi İstatistik Bölümü** lisans araştırma projesi kapsamında geliştirilmiştir[cite: 1]. Çalışmanın amacı, Türkiye ikinci el otomobil piyasasındaki premium segment araçların fiyat dinamiklerini etkileyen teknik ve yapısal faktörleri analiz etmek ve bu faktörlere dayalı yüksek doğruluklu bir fiyat tahmin motoru oluşturmaktır[cite: 1].

Klasik doğrusal regresyon modellerinin aksine, araç fiyatlarındaki doğrusal olmayan (non-linear) karmaşık etkileşimleri ve çoklu bağlantı (multicollinearity) problemlerini adreslemek amacıyla, gradyan artırma (gradient boosting) tabanlı güçlü bir makine öğrenmesi algoritması olan **CatBoost Regresyonu** tercih edilmiştir[cite: 1].

---

### 🛠️ Teknik Mimari ve MLOps Özellikleri

Mevcut repo, modelin eğitim (training) süreçlerinden ziyade doğrudan üretim ortamındaki tahmin operasyonlarına (**Inference Operations**) odaklanır[cite: 1]:

*   **Native CatBoost Inference Engine:** Model, One-Hot Encoding veya Label Encoding gibi veri boyutunu artıran ve seyrekleştiren ara işlemlere gerek duymadan, kategorik verileri yerleşik (native) olarak işleyebilen dondurulmuş `model.cbm` (CatBoost Binary Model) formatında servis edilir[cite: 1]. Bu sayede tahmin gecikme süresi (latency) minimuma indirilmiştir[cite: 1].
*   **Veri Tabanı Tabanlı Telemetri ve Loglama:** Üretim ortamında yapılan her tahmin isteği; girdi parametreleri, üretilen tahmin değeri, sistem zaman damgası ve model versiyon bilgisi ile birlikte **PostgreSQL (SQLAlchemy ORM)** üzerinde analitik olarak saklanır[cite: 1]. Bu altyapı, zaman içinde oluşabilecek **Veri Kayması (Data Drift)** ve **Kavram Kayması (Concept Drift)** analizleri için zemin hazırlar[cite: 1].
*   **Operational UI:** Sistemin anlık sağlık durumunu (system health), geçmiş tahmin loglarını ve hata dağılımlarını izlemek amacıyla Flask tabanlı entegre bir yönetim paneli (dashboard) sunulmaktadır[cite: 1].

---

### 📐 Veri Ön İşleme ve Özellik Mühendisliği (Feature Engineering)
Modelin yanlılığını (bias) azaltmak ve tahmin tutarlılığını en üst düzeyeye çıkarmak adına veri seti üzerinde katı istatistiksel filtreler uygulanmıştır[cite: 1]:

1. **Yapısal Arındırma:** Piyasa fiyatlamasını manipüle eden ağır hasar kayıtlı araçlar ile şase, podye veya airbag işlemi görmüş, yapısal bütünlüğü bozulmuş araçlar veri setinden çıkarılmıştır[cite: 1].
2. **Zaman Filtresi:** Modelin güncel piyasa dinamiklerini yakalaması adına 2010 model yılı öncesi araçlar analiz dışı bırakılmıştır[cite: 1].
3. **Yıllık Kullanım Yoğunluğu (km_per_age):** Toplam kilometre bilgisi, aracın yaşına bölünerek yıllık ortalama yıpranma katsayısı türetilmiş ve modele güçlü bir öngörücü olarak eklenmiştir[cite: 1].

---

### 📊 Model Performansı ve İstatistiksel Metrikler

Optuna çerçevesi kullanılarak gerçekleştirilen Bayesyen hiperparametre optimizasyonu sonucunda test setinde elde edilen performans metrikleri aşağıdadır[cite: 1]:

| Değerlendirme Metriği | Matematiksel Gösterim | Model Çıktısı (Test Seti) |
| :--- | :--- | :--- |
| **R² (Determinasyon Katsayısı)** | R² = 1 - [ ∑(y_i - ŷ_i)² / ∑(y_i - ȳ)² ] | **0.9708**[cite: 1] |
| **MAE (Ortalama Mutlak Hata)** | MAE = (1/n) * ∑ \|y_i - ŷ_i\| | **129,973 TL**[cite: 1] |
| **RMSE (Kök Ortalama Kare Hata)** | RMSE = √ [ (1/n) * ∑(y_i - ŷ_i)² ] | **181,508 TL**[cite: 1] |

> **📊 İstatistiksel Çıkarım:** R² = 0.9708 değeri, premium ikinci el araç fiyatlarında görülen varyansın **%97.08**'inin modelde yer alan bağımsız değişkenler tarafından açıklandığını göstermektedir[cite: 1]. Residual Histogram ve Q-Q Plot analizleri, tahmin hatalarının (e_i = y_i - ŷ_i) sıfır ortalamalı normal dağılım varsayımına büyük ölçüde uyduğunu doğrulamıştır[cite: 1]. SHAP (SHapley Additive exPlanations) analizleri ise fiyatı belirleyen en baskın faktörlerin *Motor Gücü (HP)* ve *Model Prestiji (Segment/Varyant)* olduğunu ortaya koymuştur[cite: 1].

---

### 🏗️ Proje Yapısı

```text
├── app.py                  # API Katmanı, Flask Rotaları ve İstek Yönetimi
├── model.cbm               # Üretim ortamındaki dondurulmuş (serialized) CatBoost modeli
├── database/
│   ├── __init__.py         # Veritabanı bağlantı konfigürasyonu
│   └── models.py           # SQLAlchemy Tahmin Logları Tablo Şeması
├── static/
│   ├── css/                # Dashboard görsel stilleri
│   └── js/                 # Dinamik grafikler ve log filtreleme betikleri
├── templates/
│   ├── index.html          # İnteraktif Fiyat Tahmin Panel Arayüzü
│   └── dashboard.html      # Sistem Analitiği ve MLOps İzleme Ekranı
└── logs/
    └── app.log             # Yapılandırılmış (structured) uygulama günlükleri

```

---

### 🚀 Hızlı Başlangıç

#### 1. Depoyu Klonlayın

```bash
git clone [https://github.com/ferhattkoc-ml/arac_fiyat_tahmin.git](https://github.com/ferhattkoc-ml/arac_fiyat_tahmin.git)
cd arac_fiyat_tahmin

```

#### 2. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt

```

#### 3. Uygulamayı Başlatın

```bash
python app.py

```

*Arayüz Erişimi: `http://localhost:5000*`

---

### 📡 Kurumsal API Dokümantasyonu (POST `/predict`)

Sistem, harici kurumsal yazılımların (CRM, ERP, Galeri Yönetim Sistemleri) entegrasyonu için RESTful bir API ucu sunar.

#### İstek Gövdesi (Payload):

```json
{
  "model_variant": "Audi A6",
  "year": 2021,
  "mileage": 38000,
  "fuel_type": "Diesel",
  "transmission": "Automatic"
}

```

#### Başarılı Yanıt (Response 200 OK):

```json
{
  "status": "success",
  "data": {
    "predicted_price": 2450000.00,
    "currency": "TRY",
    "lower_bound": 2320027.00,
    "upper_bound": 2579973.00,
    "confidence_interval": "95%"
  },
  "metadata": {
    "model_version": "v1.0.0",
    "inference_latency_ms": 12.4,
    "timestamp": "2026-05-26T12:26:00Z"
  }
}

```

Not: Alt ve üst sınırlar, modelin MAE (±129,973 TL) sapma payı ve donanım paket farklılıkları göz önünde bulundurularak dinamik olarak hesaplanır.

---

### 🎓 Proje Künyesi ve Teşekkür

* **Araştırmacı:** Ferhat Koç (2211317016)


* **Akademik Danışman:** Prof. Dr. Ulaş YAMANCI


* **Kurum:** Süleyman Demirel Üniversitesi, Mühendislik ve Doğa Bilimleri Fakültesi, İstatistik Bölümü


* **Lisans:** MIT License



```

```
