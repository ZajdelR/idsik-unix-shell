---
pagetitle: "Zmienne i argumenty w skryptach"
---

# Zmienne i argumenty w Bashu (Variables & arguments)

::: {.callout-tip}
## Cele szkolenia

- Tworzyć uniwersalne skrypty powłoki przyjmujące parametry od użytkownika (argumenty pozycyjne `$1`, `$2`).
- Definiować i odczytywać zmienne w powłoce Bash (`zmienna="wartosc"`, `${zmienna}`).
- Zapisywać wyniki wykonania poleceń do zmiennych (`zmienna=$(polecenie)`).
- Wykorzystywać polecenie `basename` do dynamicznej manipulacji nazwami plików wyjściowych.

:::

## Przekazywanie parametrów do skryptu (Argumenty pozycyjne)

W poprzednim rozdziale napisaliśmy skrypt analizujący błędy ze stacji `SVB`.  
Aby skrypt stał się uniwersalnym narzędziem dla inżyniera danych, powinien przyjmować kod stacji lub ścieżkę do pliku jako parametr przekazany przez użytkownika.

W powłoce Bash służą do tego **zmienne pozycyjne**:
- `$1` – pierwszy argument przekazany po nazwie skryptu,
- `$2` – drugi argument,
- `$3` – trzeci argument, itd.

Napiszmy skrypt `analyze_station.sh`:

```bash
#!/usr/bin/env bash

station="$1"

echo "=== Analiza stacji naziemnej: $station ==="
cat telemetry_logs/ground_station_${station}_*.log | grep "ERROR" | wc -l
```

Teraz możemy uruchomić skrypt dla dowolnej stacji bez edycji kodu:

```bash
bash analyze_station.sh KIR
```

```output
=== Analiza stacji naziemnej: KIR ===
18
```

## Zmienne w powłoce Bash

Zmienne w Bashu pozwalają na przechowywanie tekstu, ścieżek do katalogów ze scenami satelitarnymi czy parametrów filtracji.

Zmienną tworzymy za pomocą znaku równości:

```bash
satellite="SENTINEL-2A"
```

::: {.callout-important}
#### Brak spacji wokół znaku `=`
W powłoce Bash **nie wolno stawiać spacji** przed ani po znaku `=`.  
- Poprawnie: `satellite="SENTINEL-2A"`
- Błędnie: `satellite = "SENTINEL-2A"` (Bash potraktuje `satellite` jako nazwę programu do uruchomienia).
:::

Aby odczytać wartość zmiennej, poprzedzamy jej nazwę symbolem dolara `$`:

```bash
echo "$satellite"
```

```output
SENTINEL-2A
```

::: {.callout-note}
#### Cudzysłów podwójny `"` vs apostrof `'`
- W **cudzysłowie podwójnym (`"..."`)** zmienne są interpretowane i zastępowane ich wartościami:
  ```bash
  echo "Przetwarzanie misji: $satellite"
  # Wynik: Przetwarzanie misji: SENTINEL-2A
  ```
- W **apostrofach pojedynczych (`'...'`)** tekst jest traktowany dosłownie:
  ```bash
  echo 'Przetwarzanie misji: $satellite'
  # Wynik: Przetwarzanie misji: $satellite
  ```
:::

### Łączenie zmiennych z tekstem (`${zmienna}`)

Dobrą praktyką programistyczną w Bashu jest ujmowanie nazwy zmiennej w nawiasy klamrowe `${...}`:

```bash
tile="T33UWT"
echo "scene_${tile}_clean.csv"
```

```output
scene_T33UWT_clean.csv
```

### Zapisywanie wyniku polecenia do zmiennej (`$()`)

Często zachodzi potrzeba zapisania wyniku wykonania polecenia do zmiennej:

```bash
zmienna=$(polecenie)
```

Przykład:

```bash
error_count=$(cat telemetry_logs/ground_station_KIR_*.log | grep "ERROR" | wc -l)
echo "Laczna liczba wykrytych anomalii: $error_count"
```

## Ćwiczenia

:::{.callout-exercise}
#### Zrozumienie zmiennych i podstawień
{{< level 1 >}}

*(Zadanie koncepcyjne)*

Jaki wynik zwróci poniższy fragment kodu?

```bash
datadir="/home/participant/Desktop/dane_do_cwiczen"
catalog_files=$(ls "$datadir/orbital_catalog")
echo "${catalog_files}"
```

1. `/home/participant/Desktop/dane_do_cwiczen`
2. `/home/participant/Desktop/dane_do_cwiczen/orbital_catalog`
3. Nazwy plików w katalogu `orbital_catalog` (`satellites_tle_catalog.tsv`, `sensor_bands_spec.tsv`, itd.)
4. Błąd wykonania

::: {.callout-answer collapse=true}

**Prawidłowa odpowiedź: 3.** Polecenie `ls "$datadir/orbital_catalog"` zwraca listę nazw plików wewnątrz tego katalogu, która następnie zostaje zapisana w zmiennej `catalog_files` i wyświetlona.
:::
:::

:::{.callout-exercise}
#### Skrypt filtrujący sceny według kafelka MGRS i satelity
{{< level 2 >}}

Napisz skrypt `filter_scenes.sh`, który przyjmuje 3 parametry:
- `$1` – plik raportu CSV (np. `cloud_cover_reports/poland_sentinel2_2024.csv`)
- `$2` – kod kafelka (np. `T33UWT`)
- `$3` – nazwę satelity (np. `SENTINEL-2A`)

Skrypt powinien:
1. Wypisać informację: `Wyszukiwanie scen kafelka $2 dla satelity $3 w pliku $1`
2. Przefiltrować raport i wypisać liczbę znalezionych scen.

::: {.callout-answer collapse=true}

W pliku `filter_scenes.sh`:

```bash
#!/usr/bin/env bash

report="$1"
tile="$2"
sat="$3"

echo "Wyszukiwanie scen kafelka $tile dla satelity $sat w pliku $report"
grep "$tile" "$report" | grep "$sat" | wc -l
```

Uruchomienie:
```bash
bash filter_scenes.sh cloud_cover_reports/poland_sentinel2_2024.csv T33UWT SENTINEL-2A
```
:::
:::

:::{.callout-exercise}
#### Automatyczne tworzenie raportów wyjściowych (`basename`)
{{< level 3 >}}

Polecenie `basename` wyodrębnia samą nazwę pliku ze ścieżki oraz pozwala odciąć rozszerzenie:
```bash
basename telemetry_logs/ground_station_SVB_2024-05-01.log .log
# Wynik: ground_station_SVB_2024-05-01
```

Napisz skrypt `extract_station_errors.sh`, który przyjmuje ścieżkę do pliku logu jako `$1`, wyciąga nazwę bazową i zapisuje wszystkie linie z błędem `ERROR` do nowego pliku `${base}_errors.txt`.

::: {.callout-answer collapse=true}

```bash
#!/usr/bin/env bash

input_file="$1"
base_name=$(basename "$input_file" ".log")

echo "Przetwarzanie logu: $input_file"
grep "ERROR" "$input_file" > "${base_name}_errors.txt"
echo "Bledy zapisano w pliku: ${base_name}_errors.txt"
```

Uruchomienie:
```bash
bash extract_station_errors.sh telemetry_logs/ground_station_SVB_2024-05-01.log
```
:::
:::

## Podsumowanie

![Komiks i ściągawka o zmiennych w powłoce Bash autorstwa [Julii Evans](https://wizardzines.com/comics/variables/)](https://wizardzines.com/comics/variables/variables.png)

::: {.callout-tip}
#### Główne punkty

- Zmienne w Bashu definiujemy bez spacji: `nazwa="wartosc"`.
- Wartość zmiennej odczytujemy za pomocą `$nazwa` lub bezpieczniej `"${nazwa}"`.
- W cudzysłowie `""` zmienne są rozwijane, w apostrofach `''` zachowują formę dosłowną.
- Zmienne pozycyjne `$1`, `$2`, `$3` przechowują argumenty przekazane do skryptu z wiersza poleceń.
- Podstawienie polecenia: `wynik=$(polecenie)` wykonuje polecenie i przypisuje jego wynik tekstowy do zmiennej.
:::
