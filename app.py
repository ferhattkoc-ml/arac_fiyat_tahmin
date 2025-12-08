from flask import Flask, request, jsonify, render_template, redirect, session, url_for
from flask_cors import CORS
import pandas as pd
from catboost import CatBoostRegressor
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

# 🔐 Admin login için secret key
app.secret_key = "ferhat-super-secret-key-123"

# ---------------------------------------------------
# 🔥 VERİTABANI AYARLARI
# ---------------------------------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///requests.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# ---------------------------------------------------
# 🔥 SQL TABLOSU
# ---------------------------------------------------
class RequestLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    Model = db.Column(db.String(50))
    Kasa_tipi = db.Column(db.String(50))
    Yakit_tipi = db.Column(db.String(50))
    Vites = db.Column(db.String(50))
    Renk = db.Column(db.String(50))
    Kimden = db.Column(db.String(20))

    kilometre = db.Column(db.Float)
    Motor_gucu = db.Column(db.Float)
    Yas = db.Column(db.Float)
    Hasar_Kaydi = db.Column(db.Float)

    km_per_age = db.Column(db.Float)
    model_yili = db.Column(db.Float)

    tahmin = db.Column(db.Float)

    ad = db.Column(db.String(100))
    email = db.Column(db.String(100))
    tel = db.Column(db.String(50))
    not_text = db.Column(db.String(200))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# ---------------------------------------------------
# 🔥 MODELİ YÜKLE
# ---------------------------------------------------
try:
    model = CatBoostRegressor()
    model.load_model("model.cbm")
    print("🔥 MODEL BAŞARIYLA YÜKLENDİ")
except Exception as e:
    print("❌ Model yüklenemedi:", e)


# ---------------------------------------------------
# 🔥 MODELİN BEKLEDİĞİ KOLONLAR
# ---------------------------------------------------
expected_columns = [
    "kilometre", "Motor_gucu", "Yas", "Hasar_Kaydi",
    "km_per_age", "model_yili",
    "Model", "Kasa_tipi", "Yakit_tipi", "Vites", "Renk", "Kimden"
]


# ---------------------------------------------------
# 🔥 ROOT → Tahmin Paneline yönlendir
# ---------------------------------------------------
@app.get("/")
def redirect_to_panel():
    return redirect("/tahmin-paneli")


# ---------------------------------------------------
# 🔥 Tahmin Paneli
# ---------------------------------------------------
@app.get("/tahmin-paneli")
def tahmin_page():
    return render_template("index.html")   # templates/index.html


# ---------------------------------------------------
# 🔥 ADMIN LOGIN
# ---------------------------------------------------
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "ferhat123":
            session["admin_logged"] = True
            return redirect("/admin")

        return render_template("admin_login.html", error=True)

    return render_template("admin_login.html")


# ---------------------------------------------------
# 🔥 ADMIN PANELİ (KORUMALI)
# ---------------------------------------------------
@app.get("/admin")
def admin_page():
    if not session.get("admin_logged"):
        return redirect("/admin-login")
    return render_template("admin.html")


# ---------------------------------------------------
# 🔥 /predict — Tahmin + SQL kayıt
# ---------------------------------------------------
@app.post("/predict")
def predict():
    try:
        data = request.get_json()

        # Ek kolonlar
        data["km_per_age"] = data["kilometre"] / (data["Yas"] + 0.1)
        data["model_yili"] = 2025 - data["Yas"]

        df = pd.DataFrame([data])
        df = df[expected_columns]

        tahmin = float(model.predict(df)[0])

        # SQL KAYDI
        log = RequestLog(
            Model=data["Model"],
            Kasa_tipi=data["Kasa_tipi"],
            Yakit_tipi=data["Yakit_tipi"],
            Vites=data["Vites"],
            Renk=data["Renk"],
            Kimden=data["Kimden"],
            kilometre=data["kilometre"],
            Motor_gucu=data["Motor_gucu"],
            Yas=data["Yas"],
            Hasar_Kaydi=data["Hasar_Kaydi"],
            km_per_age=data["km_per_age"],
            model_yili=data["model_yili"],
            tahmin=tahmin,
            ad=data.get("ad", ""),
            email=data.get("email", ""),
            tel=data.get("tel", ""),
            not_text=data.get("not", "")
        )

        db.session.add(log)
        db.session.commit()

        return jsonify({"tahmin": tahmin})

    except Exception as e:
        print("❌ Tahmin hatası:", e)
        return jsonify({"error": str(e)}), 400


# ---------------------------------------------------
# 🔥 ADMIN — KAYIT LİSTELE
# ---------------------------------------------------
@app.get("/admin/records")
def admin_records():
    if not session.get("admin_logged"):
        return jsonify({"error": "Yetkisiz erişim"}), 401

    logs = RequestLog.query.order_by(RequestLog.id.desc()).all()

    result = []
    for r in logs:
        result.append({
            "id": r.id,
            "submittedAt": r.created_at.strftime("%d.%m.%Y %H:%M"),
            "tahmin": r.tahmin,
            "features": {
                "Model": r.Model,
                "Kasa_tipi": r.Kasa_tipi,
                "Yakit_tipi": r.Yakit_tipi,
                "Vites": r.Vites,
                "Renk": r.Renk,
                "Kimden": r.Kimden,
                "kilometre": r.kilometre,
                "Motor_gucu": r.Motor_gucu,
                "Yas": r.Yas,
                "Hasar_Kaydi": r.Hasar_Kaydi,
            },
            "contact": {
                "ad": r.ad,
                "email": r.email,
                "tel": r.tel,
                "not": r.not_text
            }
        })

    return jsonify(result)


# ---------------------------------------------------
# 🔥 ADMIN — KAYIT SİL
# ---------------------------------------------------
@app.delete("/admin/delete/<int:id>")
def admin_delete(id):
    if not session.get("admin_logged"):
        return jsonify({"error": "Yetkisiz erişim"}), 401

    rec = RequestLog.query.get(id)
    if not rec:
        return jsonify({"error": "Kayıt bulunamadı"}), 404

    db.session.delete(rec)
    db.session.commit()
    return jsonify({"ok": True})


# ---------------------------------------------------
# 🔥 UYGULAMA BAŞLAT
# ---------------------------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
