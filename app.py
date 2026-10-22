from flask import Flask, render_template, request
import sqlite3
import os
import re

app = Flask(__name__)

# Verilənlər bazasının fayl yolu
DB_PATH = os.path.join(app.root_path, "numbers.db")


def init_db():
    """Telefon nömrələri üçün verilənlər bazasını yaradır."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS phone_numbers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone TEXT UNIQUE NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)


def normalize_phone(phone):
    """Nömrəni standart formata çevirir."""
    translation = str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789")

    phone = phone.translate(translation)
    phone = re.sub(r"[\s\-()]", "", phone)

    if phone.startswith("+98"):
        phone = "0" + phone[3:]
    elif phone.startswith("0098"):
        phone = "0" + phone[4:]

    return phone


@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    message_type = ""

    if request.method == "POST":
        phone = normalize_phone(request.form.get("phone", ""))

        # İran mobil nömrəsinin formatını yoxlayır
        if not re.fullmatch(r"09\d{9}", phone):
            message = "Daxil etdiyiniz nömrə düzgün deyil."
            message_type = "error"

        else:
            try:
                with sqlite3.connect(DB_PATH) as conn:
                    conn.execute(
                        """
                        INSERT INTO phone_numbers (phone)
                        VALUES (?)
                        """,
                        (phone,),
                    )

                message = "Nömrəniz uğurla qeydiyyata alındı."
                message_type = "success"

            except sqlite3.IntegrityError:
                message = "Bu nömrə artıq qeydiyyatdan keçirilib."
                message_type = "error"

    return render_template("index.html", message=message, message_type=message_type)


# Verilənlər bazasını işə salır
init_db()


if __name__ == "__main__":
    app.run(debug=True)
