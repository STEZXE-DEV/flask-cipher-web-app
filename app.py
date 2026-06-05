from flask import Flask, render_template, request, session, send_file
from io import BytesIO

from ciphers.transposition import encrypt as t_encrypt, decrypt as t_decrypt
from ciphers.polibius import encrypt as p_encrypt, decrypt as p_decrypt
from ciphers.vigenere import encrypt as v_encrypt, decrypt as v_decrypt

app = Flask(__name__)
app.secret_key = "top_secret"


# =========================
# STRONA GŁÓWNA
# =========================
@app.route("/")
def home():
    return render_template("index.html", title="Strona główna")


# =========================
# OBSŁUGA FORMULARZA
# =========================
@app.route("/process", methods=["POST"])
def process():

    # pobranie danych z formularza
    text = request.form.get("text", "").strip()
    cipher = request.form.get("cipher")
    key = request.form.get("key", "").strip()
    mode = request.form.get("mode")
    file = request.files.get("file")

    # jeśli użytkownik wrzucił plik, to nadpisujemy tekst
    if file and file.filename:
        text = file.read().decode("utf-8").replace("\r", "")

    result = ""
    error = ""

    # =========================
    # WALIDACJA DANYCH
    # =========================
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
            # POLIBIUSZ
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

        # błąd konwersji klucza (np. litery zamiast liczby)
        except ValueError:
            error = "Klucz musi być liczbą."

        # inne nieprzewidziane błędy
        except Exception as e:
            error = f"Błąd: {e}"

    # zapis wyniku w sesji (do pobierania pliku)
    session["result"] = result

    return render_template(
        "index.html", title="Strona główna", result=result, error=error
    )


# =========================
# POBIERANIE WYNIKU
# =========================
@app.route("/download")
def download():

    result = session.get("result")

    # jeśli brak wyniku
    if not result:
        return "Brak wyniku do pobrania."

    # tworzenie pliku w pamięci (bez zapisu na dysk)
    buffer = BytesIO()
    buffer.write(result.encode("utf-8"))
    buffer.seek(0)

    # wysłanie pliku do pobrania
    return send_file(
        buffer, as_attachment=True, download_name="wynik.txt", mimetype="text/plain"
    )


# uruchomienie aplikacji
if __name__ == "__main__":
    app.run(debug=True)
