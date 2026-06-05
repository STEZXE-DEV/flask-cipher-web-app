from flask import Flask, render_template, request, session, send_file
from io import BytesIO

from ciphers.transposition import encrypt as t_encrypt, decrypt as t_decrypt
from ciphers.polibius import encrypt as p_encrypt, decrypt as p_decrypt
from ciphers.vigenere import encrypt as v_encrypt, decrypt as v_decrypt

app = Flask(__name__)
app.secret_key = "top_secret"


@app.route("/")
def home():
    return render_template("index.html", title="Strona główna")


@app.route("/process", methods=["POST"])
def process():

    text = request.form.get("text", "").strip()
    cipher = request.form.get("cipher")
    key = request.form.get("key", "").strip()
    mode = request.form.get("mode")
    file = request.files.get("file")

    if file and file.filename:
        text = file.read().decode("utf-8")

    result = ""
    error = ""

    # WALIDACJA
    if not text:
        error = "Pole tekstowe nie może być puste."

    elif not key:
        error = "Klucz nie może być pusty."

    else:
        try:

            # =========================
            # TRANSPOSITION
            # =========================
            if cipher == "transposition":

                key = int(key)

                if mode == "encrypt":
                    result = t_encrypt(text, key)

                else:
                    result = t_decrypt(text, key)

            # =========================
            # POLIBIUS
            # =========================
            elif cipher == "polibius":

                key = int(key)

                if mode == "encrypt":
                    result = p_encrypt(text, key)

                else:
                    result = p_decrypt(text, key)

            # =========================
            # VIGENERE
            # =========================
            elif cipher == "vigenere":

                if mode == "encrypt":
                    result = v_encrypt(text, key)

                else:
                    result = v_decrypt(text, key)

            else:
                error = "Nieznany szyfr."

        except ValueError:
            error = "Klucz musi być liczbą."

        except Exception as e:
            error = f"Błąd: {e}"

    session["result"] = result

    return render_template(
        "index.html", title="Strona główna", result=result, error=error
    )


@app.route("/download")
def download():

    result = session.get("result")

    if not result:
        return "Brak wyniku do pobrania."

    buffer = BytesIO()
    buffer.write(result.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer, as_attachment=True, download_name="wynik.txt", mimetype="text/plain"
    )


if __name__ == "__main__":
    app.run(debug=True)
