import pandas as pd


def oblicz_bmi(waga, wzrost):
    return waga / (wzrost / 100) ** 2


def wczytaj_dane(plik):
    if plik.endswith('.xlsx'):
        return pd.read_excel(plik)
    elif plik.endswith('.txt'):
        return pd.read_csv(plik, sep="\t")
    else:
        raise ValueError("Obsługiwane formaty to .xlsx lub .txt")


def zapisz_wyniki(dane, plik_wyjsciowy):
    dane.to_csv(plik_wyjsciowy, index=False)
    print(f"Wyniki zapisane w {plik_wyjsciowy}")


def main():
    plik_wejsciowy = input("Podaj nazwę pliku wejściowego (.txt lub .xlsx): ")
    plik_wyjsciowy = input("Podaj nazwę pliku wyjściowego (.csv): ")

    try:
        dane = wczytaj_dane(plik_wejsciowy)

        if 'waga' not in dane.columns or 'wzrost' not in dane.columns:
            raise ValueError("Plik musi zawierać kolumny 'waga' i 'wzrost'.")

        dane['BMI'] = dane.apply(lambda row: oblicz_bmi(row['waga'], row['wzrost']), axis=1)

        zapisz_wyniki(dane, plik_wyjsciowy)

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()
