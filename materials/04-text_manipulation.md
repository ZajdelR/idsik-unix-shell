---
pagetitle: "Praca z tekstem i plikami danych"
---

# Praca z plikami tekstowymi (Working with text)

::: {.callout-tip}
## Cele szkolenia

- Przeglądać zawartość raportów, logów telemetrycznych i tabel danych (`head`, `tail`, `cat`, `less`).
- Wykorzystywać symbol wieloznaczny `*` do jednoczesnej pracy z wieloma plikami.
- Przekierowywać wyjście poleceń do plików za pomocą operatorów `>` oraz `>>`.
- Wyszukiwać wzorce tekstowe w plikach i logach za pomocą polecenia `grep`.

:::

## Przeglądanie zawartości plików

W analizie danych satelitarnych i telemetrycznych często zachodzi potrzeba szybkiego sprawdzenia zawartości plików bez konieczności uruchamiania ciężkich edytorów graficznych. Jest to szczególnie istotne przy plikach o dużych rozmiarach (np. raportach dziennych, metadanych scen czy logach przetwarzania).

Przejdźmy do katalogu z danymi i wyświetlmy zawartość pliku specyfikacji pasm sensorów w `orbital_catalog` za pomocą polecenia `cat` (*concatenate* – łączenie/wypisywanie):

```bash
cd ~/Desktop/dane_do_cwiczen
cat orbital_catalog/sensor_bands_spec.tsv
```

```output
sensor	band_id	band_name	central_wavelength_nm	bandwidth_nm	spatial_res_m	spectrum_region
MSI-Sentinel-2	B01	Coastal Aerosol	443	20	60	VNIR
MSI-Sentinel-2	B02	Blue	490	65	10	VNIR
MSI-Sentinel-2	B03	Green	560	35	10	VNIR
MSI-Sentinel-2	B04	Red	665	30	10	VNIR
...
```

Polecenie `cat` wypisuje cały plik na ekranie. Jeśli jednak plik ma tysiące linii, `cat` zaleje terminal tekstem.

Aby sprawdzić tylko **początkowe linie pliku** (np. nagłówek tabeli z nazwami kolumn), używamy polecenia `head`:

```bash
head cloud_cover_reports/poland_sentinel2_2024.csv
```

Domyślnie `head` wyświetla pierwsze 10 linii. Liczbę wyświetlanych wierszy można zmienić opcją `-n`:

```bash
head -n 3 cloud_cover_reports/poland_sentinel2_2024.csv
```

```output
scene_id,date,satellite,tile_id,orbit_relative,cloud_coverage_percent,nodata_pixel_percent,snow_ice_percent,sun_zenith_angle,quality_flag
S2A_MSIL2A_20240510T100031_N0510_R122_T33UWT,2024-05-10,SENTINEL-2A,T33UWT,122,12.40,0.50,0.00,34.80,PASSED
S2B_MSIL2A_20240512T095029_N0510_R079_T33UWT,2024-05-12,SENTINEL-2B,T33UWT,79,4.20,1.20,0.00,33.50,PASSED
```

Analogicznie, do wyświetlenia **końcowych linii pliku** (np. najnowszych wpisów w logu stacji naziemnej) służy polecenie `tail`:

```bash
tail -n 3 telemetry_logs/ground_station_SVB_2024-05-01.log
```

Do interaktywnego, wygodnego przeglądania długich plików strona po stronie służy program `less`:

```bash
less orbital_catalog/satellites_tle_catalog.tsv
```

W przeglądarce `less`:
- Strzałki <kbd>↑</kbd> i <kbd>↓</kbd> przewijają plik linia po linii.
- Klawisze <kbd>Page Up</kbd> i <kbd>Page Down</kbd> (lub <kbd>Spacja</kbd>) przewijają o całą stronę.
- Naciśnięcie klawisza <kbd>/</kbd> pozwala na **wyszukiwanie frazy w tekście** (naciśnięcie <kbd>n</kbd> przechodzi do kolejnego dopasowania, a <kbd>Shift</kbd> + <kbd>n</kbd> do poprzedniego).
- Naciśnięcie klawisza <kbd>Q</kbd> zamyka program i powraca do wiersza poleceń.

## Zliczanie linii, słów i znaków (`wc`)

Do zliczania rekordów i linii w plikach tekstowych służy polecenie `wc` (*word count*):

```bash
wc -l cloud_cover_reports/*.csv
```

```output
  251 cloud_cover_reports/poland_sentinel2_2024.csv
  221 cloud_cover_reports/poland_sentinel2_2023.csv
  301 cloud_cover_reports/central_europe_sentinel2_2024.csv
  281 cloud_cover_reports/scandinavia_sentinel2_2024.csv
  201 cloud_cover_reports/alps_landsat_sentinel_2024.csv
 1255 total
```

Flagi `wc`:
- `-l` – zlicza wyłącznie linie (*lines*).
- `-w` – zlicza słowa (*words*).
- `-c` – zlicza bajty / znaki (*characters/bytes*).

## Łączenie wielu plików (`cat`)

Polecenie `cat` (od *concatenate*) może przyjąć wiele plików jako argumenty i połączyć ich zawartość w jeden ciągły strumień tekstu:

```bash
cat cloud_cover_reports/poland_sentinel2_2023.csv cloud_cover_reports/poland_sentinel2_2024.csv > poland_combined.csv
```

## Przekierowanie wyjścia (`>` oraz `>>`)

Domyślnie polecenia wypisują wyniki w terminalu (tzw. standardowe wyjście – *stdout*). Możemy jednak **przekierować wyjście do pliku** za pomocą operatora `>`:

```bash
wc -l telemetry_logs/*.log > summary_logs.txt
```

::: {.callout-warning}
#### Nadpisywanie a dopisywanie (`>` vs `>>`)
- Operator `>` **nadpisuje** zawartość pliku docelowego.
- Operator `>>` **dopisuje** nowe linie na końcu istniejącego pliku (*append*).
:::

## Wyszukiwanie wzorców tekstowych (`grep`)

Polecenie `grep` (*Global Regular Expression Print*) służy do przeszukiwania plików i wypisywania linii pasujących do wzorca.

Wyszukajmy wszystkie operacje zakończone błędem w logach telemetrycznych stacji Spitsbergen:

```bash
grep "ERROR" telemetry_logs/ground_station_SVB_2024-05-01.log
```

Najważniejsze opcje polecenia `grep`:
- `-i` – ignoruje wielkość liter (*case-insensitive*), np. `grep -i "sentinel" catalog.tsv`.
- `-v` – odwraca dopasowanie (*invert match*), wypisując linie, które **nie zawierają** podanego wzorca (np. `grep -v "^#" plik.log` pomija linie komentarzy zaczynające się od `#`).
- `-n` – wyświetla numery wierszy w pliku.
- `-c` – zwraca liczbę pasujących wierszy.
- `-r` (lub `-R`) – rekurencyjne przeszukiwanie wszystkich plików w katalogu.

![Komiks i ściągawka polecenia `grep` autorstwa [Julii Evans](https://wizardzines.com/comics/grep/)](https://wizardzines.com/comics/grep/grep.png)

## Ćwiczenia

:::{.callout-exercise}
#### Przekierowanie strumieni (`>` oraz `>>`)
{{< level 1 >}}

Przejdź do katalogu `dane_do_cwiczen` i wykonaj zadania:

1. Wyszukaj wszystkie wpisy ze statusem `ERROR` w logach stacji Kiruna (`telemetry_logs/ground_station_KIR_*.log`) i zapisz je do nowego pliku `kiruna_errors.txt`.
2. Sprawdź liczbę znalezionych błędów za pomocą `wc -l kiruna_errors.txt`.
3. Używając operatora `>>`, dopisz do tego samego pliku błędy ze stacji Spitsbergen (`telemetry_logs/ground_station_SVB_*.log`).
4. Sprawdź ponownie liczbę wierszy w `kiruna_errors.txt`.

::: {.callout-answer collapse=true}

**Zadanie 1**
```bash
grep "ERROR" telemetry_logs/ground_station_KIR_*.log > kiruna_errors.txt
```

**Zadanie 2**
```bash
wc -l kiruna_errors.txt
```

**Zadanie 3**
```bash
grep "ERROR" telemetry_logs/ground_station_SVB_*.log >> kiruna_errors.txt
```

**Zadanie 4**
```bash
wc -l kiruna_errors.txt
```
Liczba wierszy wzrosła o liczbę błędów dopisanych ze stacji SVB.
:::
:::

:::{.callout-exercise}
#### Zliczanie i filtrowanie scen satelitarnych
{{< level 1 >}}

W pliku `cloud_cover_reports/poland_sentinel2_2024.csv`:

1. Podejrzyj nagłówek i pierwsze 4 wiersze danych za pomocą `head`.
2. Ile łącznie scen zarejestrowano w tym raporcie? (`wc -l`)
3. Użyj `grep`, aby wyodrębnić tylko sceny pozyskane przez satelitę `SENTINEL-2A` i zapisać je do pliku `s2a_poland.csv`.
4. Ile scen pozyskał satelita Sentinel-2A?

::: {.callout-answer}

```bash
head -n 5 cloud_cover_reports/poland_sentinel2_2024.csv
wc -l cloud_cover_reports/poland_sentinel2_2024.csv
grep "SENTINEL-2A" cloud_cover_reports/poland_sentinel2_2024.csv > s2a_poland.csv
wc -l s2a_poland.csv
```
:::
:::

:::{.callout-exercise}
#### Wyszukiwanie pasm termalnych i radarowych
{{< level 2 >}}

W pliku `orbital_catalog/sensor_bands_spec.tsv`:

1. Wyszukaj pasma rejestrujące promieniowanie podczerwone (zawierające słowo "Infrared" lub "SWIR").
2. Użyj opcji `-i`, aby wyszukiwanie nie zależało od wielkości liter.
3. Policz ile takich pasm znajduje się w katalogu.

::: {.callout-answer collapse=true}

```bash
grep -i "infrared" orbital_catalog/sensor_bands_spec.tsv
grep -i "infrared" orbital_catalog/sensor_bands_spec.tsv | wc -l
```
:::
:::

## Podsumowanie

::: {.callout-tip}
#### Główne punkty

- Polecenia `head` i `tail` pozwalają podejrzeć odpowiednio początek lub koniec raportu lub logu.
- Program `less` umożliwia interaktywne przewijanie i przeszukiwanie plików o dowolnym rozmiarze (<kbd>Q</kbd> kończy pracę).
- Polecenie `wc -l` zlicza liczbę wierszy w plikach.
- Operator `>` przekierowuje wyjście programu do pliku (tworzy nowy lub **nadpisuje** istniejący).
- Operator `>>` **dopisuje** wyjście programu na końcu istniejącego pliku.
- Polecenie `grep` wyszukuje linie tekstu pasujące do podanego wzorca (np. `grep -i "ERROR" telemetry_logs/*.log`).
:::
