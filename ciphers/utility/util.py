
# Funkcja służąca do normalizacji (podmiany) polskich znaków diakrytycznych
def normalize(text):
    polish_dict = {
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ź': 'z',
    'ż': 'z'
}
    normalized_text = ''
    for i in text:
        if i in polish_dict:
            normalized_text += polish_dict[i]
        else:
            normalized_text += i

    return normalized_text
