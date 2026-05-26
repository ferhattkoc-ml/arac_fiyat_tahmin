```markdown
# 🏎️ AudiPredict AI — Enterprise Vehicle Valuation
> **Premium Segment İkinci El Araçlarda Teknik ve Yapısal Özelliklere Göre Fiyat Tahmini: CatBoost Regresyon Yaklaşımı ve MLOps Altyapısı**

An analytical, production-ready vehicle valuation platform developed as part of an undergraduate research project. This repository focuses on bridging the gap between rigorous statistical modeling and robust **Inference Operations (InferenceOps)**.

---

### 📝 Akademik Özet & Proje Amacı
Bu proje, **Süleyman Demirel Üniversitesi Mühendislik ve Doğa Bilimleri Fakültesi İstatistik Bölümü** lisans araştırma projesi kapsamında geliştirilmiştir. Çalışmanın amacı, Türkiye ikinci el otomobil piyasasındaki premium segment araçların fiyat dinamiklerini etkileyen teknik ve yapısal faktörleri analiz etmek ve bu faktörlere dayalı yüksek doğruluklu bir fiyat tahmin motoru oluşturmaktır.

Klasik doğrusal regresyon modellerinin aksine, araç fiyatlarındaki doğrusal olmayan (non-linear) karmaşık etkileşimleri ve çoklu bağlantı (multicollinearity) problemlerini adreslemek amacıyla, gradyan artırma (gradient boosting) tabanlı güçlü bir makine öğrenmesi algoritması olan **CatBoost Regresyonu** tercih edilmiştir.

---

### 🛠️ Teknik Mimari ve MLOps Özellikleri

Mevcut repo, modelin eğitim (training) süreçlerinden ziyade doğrudan üretim ortamındaki tahmin operasyonlarına (**Inference Operations**) odaklanır:

* **Native CatBoost Inference Engine:** Model, One-Hot Encoding veya Label Encoding gibi veri boyutunu artıran ve seyrekleştiren ara işlemlere gerek duymadan, kategorik verileri yerleşik (native) olarak işleyebilen dondurulmuş `model.cbm` (CatBoost Binary Model) formatında servis edilir. Bu sayede tahmin gecikme süresi (latency) minimuma indirilmiştir.
* **Veri Tabanı Tabanlı Telemetri ve Loglama:** Üretim ortamında yapılan her tahmin isteği; girdi parametreleri, üretilen tahmin değeri, sistem zaman damgası ve model versiyon bilgisi ile birlikte **PostgreSQL (SQLAlchemy ORM)** üzerinde analitik olarak saklanır. Bu altyapı, zaman içinde oluşabilecek **Veri Kayması (Data Drift)** ve **Kavram Kayması (Concept Drift)** analizleri için zemin hazırlar.
* **Operational UI:** Sistemin anlık sağlık durumunu (system health), geçmiş tahmin loglarını ve hata dağılımlarını izlemek amacıyla Flask tabanlı entegre bir yönetim paneli (dashboard) sunulmaktadır.

---

### 📐 Veri Ön İşleme ve Özellik Mühendisliği (Feature Engineering)
Modelin yanlılığını (bias) azaltmak ve tahmin tutarlılığını en üst düzeneye çıkarmak adına veri seti üzerinde katı istatistiksel filtreler uygulanmıştır:
1.  **Yapısal Arındırma:** Piyasa fiyatlamasını manipüle eden ağır hasar kayıtlı araçlar ile şase, podye veya airbag işlemi görmüş, yapısal bütünlüğü bozulmuş araçlar veri setinden çıkarılmıştır.
2.  **Zaman Filtresi:** Modelin güncel piyasa dinamiklerini yakalaması adına 2010 model yılı öncesi araçlar analiz dışı bırakılmıştır.
3.  **Yıllık Kullanım Yoğunluğu ($km\_per\_age$):** Toplam kilometre bilgisi, aracın yaşına bölünerek yıllık ortalama yıpranma katsayısı türetilmiş ve modele güçlü bir öngörücü olarak eklenmiştir.

---

### 📊 Model Performansı ve İstatistiksel Metrikler

Optuna çerçevesi kullanılarak gerçekleştirilen Bayesyen hiperparametre optimizasyonu sonucunda test setinde elde edilen performans metrikleri aşağıdadır:

| Değerlendirme Metriği | Matematiksel Formül | Model Çıktısı (Test Seti) |
| :--- | :--- | :--- |
| **$R^2$ (Determinasyon Katsayısı)** | $$R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$ | **0.9708** |
| **MAE (Ortalama Mutlak Hata)** | $$MAE = \frac{1}{n}\sum_{i=1}^{n}\lvert y_i - \hat{y}_i \rvert$$ | **129,973 TL** |
| **RMSE (Kök Ortalama Kare Hata)** | $$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$ | **181,508 TL** |

> **İstatistiksel Çıkarım:** $R^2 = 0.9708$ değeri, premium ikinci el araç fiyatlarında görülen varyansın **%97.08**'inin modelde yer alan bağımsız değişkenler tarafından açıklandığını göstermektedir. Residual Histogram ve Q-Q Plot analizleri, tahmin hatalarının ($\epsilon_i = y_i - \hat{y}_i$) sıfır ortalamalı normal dağılum varsayımına büyük ölçüde uyduğunu doğrulamıştır. SHAP (SHapley Additive exPlanations) analizleri ise fiyatı belirleyen en baskın faktörlerin *Motor Gücü (HP)* ve *Model Prestiji (Segment/Varyant)* olduğunu ortaya koymuştur.

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

*Not: Alt ve üst sınırlar, modelin MAE (±129,973 TL) sapma payı ve donanım paket farklılıkları göz önünde bulundurularak dinamik olarak hesaplanır.*

---

### 🎓 Proje Künyesi ve Teşekkür

* **Araştırmacı:** Ferhat Koç (2211317016)
* **Akademik Danışman:** Prof. Dr. Ulaş YAMANCI
* **Kurum:** Süleyman Demirel Üniversitesi, Mühendislik ve Doğa Bilimleri Fakültesi, İstatistik Bölümü
* **Lisans:** MIT License

```

```
