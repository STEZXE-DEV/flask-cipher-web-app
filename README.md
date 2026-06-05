# OPIS PROJEKTU Flask Cipher Web App

Prosta aplikacja webowa do szyfrowania i deszyfrowania tekstu. Projekt zrealizowany w Pythonie z użyciem Flask.

## Co robi aplikacja

- szyfruje i deszyfruje tekst,
- obsługuje trzy szyfry:
  - przestawieniowy,
  - Vigenère’a,
  - Polibiusza,
- działa na normalnym tekście i plikach `.txt`,
- pozwala pobrać wynik jako plik `.txt`,
- obsługuje polskie znaki.

## Użyte szyfry

### Szyfr przestawieniowy
Zmienia kolejność znaków w tekście na podstawie liczby (klucza).

### Szyfr Vigenère’a
Szyfr, który używa słowa-klucza do przesuwania liter w alfabecie.

### Szyfr Polibiusza
Każda litera jest zamieniana na parę liczb według siatki 6×6.

## Struktura projektu

```text
flask-cipher-web-app/
│
├── app.py
├── ciphers/
│   ├── transposition.py
│   ├── vigenere.py
│   ├── polibius.py
│   └── utility/
│       └── util.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── tests/
│   └── test_ciphers.py
│
└── README.md
```

## Wymagania

- Python 3
- Flask

## Jak uruchomić

1. Zainstaluj Flask:
```bash
pip install flask
```

2. Uruchom projekt:
```bash
python app.py
```

3. Wejdź w przeglądarce na:
```text
http://127.0.0.1:5000
```

## Jak używać

1. Wpisujesz tekst albo wrzucasz plik `.txt`
2. Wybierasz szyfr
3. Podajesz klucz
4. Wybierasz czy szyfrujesz czy deszyfrujesz
5. Klikasz „Wykonaj”
6. Otrzymujesz wynik na stronie albo możesz go pobrać

## Testy

W folderze `tests/` są testy algorytmów.

Uruchamiasz je:

```bash
python tests/test_ciphers.py
```

## Autor
SJ - student AKSiM