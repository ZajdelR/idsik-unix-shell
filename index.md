---
pagetitle: "Zarządzanie projektem informatycznym"
lang: pl
date: today
number-sections: false
---

# Zarządzanie projektem informatycznym {.unnumbered}

Materiały do przedmiotu **Zarządzanie projektem informatycznym** dla studentów kierunku **Inżynieria Danych Satelitarnych i Kosmicznych** na **Uniwersytecie Przyrodniczym we Wrocławiu**, na rok akademicki **2026/2027**.

## Informacje ogólne

**Powłoka Unix**, obsługiwana z wiersza poleceń, jest ważnym narzędziem pracy badaczy i inżynierów, szczególnie w takich dziedzinach jak inżynieria danych satelitarnych, teledetekcja, bioinformatyka i analiza dużych zbiorów danych. Podczas zajęć poznasz podstawową strukturę systemu Unix oraz sposób korzystania z niego za pomocą poleceń. Nauczysz się poruszać po systemie plików, przetwarzać dane tekstowe, łączyć polecenia za pomocą potoków i przekierowań, aby sprawnie wydobywać informacje z plików, oraz pisać skrypty Bash wykorzystujące zmienne i standardowe strumienie wejścia i wyjścia.

::: {.callout-note}
### Autorzy i materiały źródłowe

Materiały opracowano na podstawie następujących publikacji:
- **Tavares, H., Judge, P., Moitra, I. (2024)**. *Introduction to the Unix command line*. [https://cambiotraining.github.io/unix-shell/](https://cambiotraining.github.io/unix-shell/)
- **Gabriel A. Devenyi (Ed.), Gerard Capes (Ed.), Colin Morris (Ed.), Will Pitchers (Ed.), Greg Wilson, Gerard Capes, Gabriel A. Devenyi, Christina Koch, Raniere Silva, Ashwin Srinath, … Vikram Chhatre. (2019, July)**. *swcarpentry/shell-novice: Software Carpentry: the UNIX shell*, June 2019 (Version v2019.06.1). Zenodo. [http://doi.org/10.5281/zenodo.3266823](http://doi.org/10.5281/zenodo.3266823)
:::

::: {.callout-tip}
### Cele kształcenia

- Poznasz zastosowania wiersza poleceń w pracy z danymi i obliczeniami.
- Nauczysz się korzystać z wiersza poleceń, rozumieć budowę poleceń i sięgać do ich dokumentacji.
- Nauczysz się poruszać po systemie plików oraz określać położenie plików i katalogów za pomocą ścieżek.
- Opanujesz podstawowe operacje na plikach w powłoce _Bash_: łączenie plików, zliczanie wierszy, słów i znaków, wyszukiwanie tekstu pasującego do wzorca oraz zliczanie unikatowych wartości.
- Nauczysz się łączyć polecenia za pomocą potoków i przekierowań, aby rozwiązywać bardziej złożone zadania.
- Nauczysz się pisać skrypty _Bash_, które zapisują kolejne kroki analizy i umożliwiają jej odtworzenie.
- Nauczysz się korzystać ze zmiennych, argumentów oraz standardowych strumieni wejścia i wyjścia w skryptach powłoki.
:::


### Dla kogo są te materiały?

Materiały są przeznaczone dla studentów kierunku **Inżynieria Danych Satelitarnych i Kosmicznych Uniwersytetu Przyrodniczego we Wrocławiu**. Nie wymagają wcześniejszego doświadczenia w pracy z wierszem poleceń.


### Wymagania wstępne

Brak. Zajęcia rozpoczynają się od podstaw.


### Ćwiczenia

Ćwiczenia w materiałach oznaczono według poziomu trudności:

| Poziom | Opis |
| ----: | :---------- |
| {{< fa solid star >}} {{< fa regular star >}} {{< fa regular star >}} | Poziom 1: proste ćwiczenia służące poznaniu pojęć i składni omawianych na zajęciach. |
| {{< fa solid star >}} {{< fa solid star >}} {{< fa regular star >}} | Poziom 2: ćwiczenia wymagające połączenia kilku poznanych zagadnień w celu rozwiązania zadania. |
| {{< fa solid star >}} {{< fa solid star >}} {{< fa solid star >}} | Poziom 3: ćwiczenia wymagające samodzielnego rozszerzenia poznanych pojęć i składni w celu rozwiązania nowych problemów. |


## Konsultacje

| Dzień | Godziny |
|:---|:---|
| Środa | 10:00–11:00 |
| Piątek | 13:45–14:45 |

## Zaliczenie przedmiotu

Ocena końcowa uwzględnia zaliczenie wykładu oraz ćwiczeń laboratoryjnych z następującymi wagami:

| Forma zajęć | Forma zaliczenia | Udział w ocenie końcowej |
|:---|:---|---:|
| Wykład | Zaliczenie pisemne | 30% |
| Ćwiczenia laboratoryjne | Projekt, aktywność na zajęciach, prezentacja oraz wykonanie ćwiczeń | 70% |

## Podziękowania i źródła

Niniejsze materiały stanowią adaptację następujących publikacji:

1. **Tavares, H., Judge, P., Moitra, I. (2024)**. *Introduction to the Unix command line*. Dostępne pod adresem: [https://cambiotraining.github.io/unix-shell/](https://cambiotraining.github.io/unix-shell/)
2. **Gabriel A. Devenyi (red.), Gerard Capes (red.), Colin Morris (red.), Will Pitchers (red.), Greg Wilson, Gerard Capes, Gabriel A. Devenyi, Christina Koch, Raniere Silva, Ashwin Srinath, … Vikram Chhatre. (2019, lipiec)**. *swcarpentry/shell-novice: Software Carpentry: the UNIX shell*, czerwiec 2019 (wersja v2019.06.1). Zenodo. [http://doi.org/10.5281/zenodo.3266823](http://doi.org/10.5281/zenodo.3266823) (licencja CC BY 4.0).

Autorzy i wydawcy oryginalnych materiałów nie udzielili rekomendacji tej adaptacji.

----

Dziękujemy również **Julii Evans** za [ilustracje](https://wizardzines.com/) przedstawiające zagadnienia programowania w powłoce Bash.
