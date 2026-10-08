---
pagetitle: "Łączenie poleceń i potoki"
---

# Łączenie poleceń i potoki (Combining commands)

::: {.callout-tip}
## Cele szkolenia

- Tworzyć wieloetapowe potoki przetwarzania danych za pomocą operatora potoku (`|`).
- Wykorzystywać polecenia `cut`, `sort`, `uniq` do ekstrakcji, sortowania i deduplikacji danych tabelarycznych (CSV, TSV, logi).
- Projektować potoki do natychmiastowej analizy i podsumowywania danych z plików tekstowych i skompresowanych (`zcat`).

:::

## Operator potoku (`|` - Pipe)

W poprzednim rozdziale filtrowaliśmy i zliczaliśmy błędy w plikach w kilku oddzielnych krokach, zapisując pliki tymczasowe na dysku:

1. Połączenie raportów: `cat cloud_cover_reports/poland_*.csv > all_poland.csv`
2. Przefiltrowanie do nowego pliku: `grep "SENTINEL-2A" all_poland.csv > s2a.csv`
3. Zliczenie wierszy: `wc -l s2a.csv`

Tworzenie plików pośrednich na dysku jest niewygodne, zajmuje miejsce i spowalnia analizę.  
W systemach Unix jednym z najpotężniejszych mechanizmów jest **potok** (*pipe*), oznaczany symbolem pionowej kreski `|`.

Potok przekazuje standardowe wyjście (*stdout*) jednego programu bezpośrednio jako standardowe wejście (*stdin*) kolejnego programu, bez konieczności zapisu danych pośrednich na dysku:

```bash
cat cloud_cover_reports/poland_*.csv | grep "SENTINEL-2A" | wc -l
```

W tym jednolinijkowym potoku wyjście polecenia `cat` trafia do `grep`, a przefiltrowany wynik z `grep` trafia bezpośrednio do `wc -l`.

## Przetwarzanie tabelaryczne: `cut`, `sort`, `uniq`

Połączenie potokami kilku wyspecjalizowanych narzędzi pozwala budować zaawansowane łańcuchy analizy danych tabelarycznych (CSV, TSV, logi telemetryczne).

### Ekstrakcja kolumn (`cut`)

Polecenie `cut` służy do wycinania określonych kolumn/pól z każdego wiersza tekstu:

```bash
cat cloud_cover_reports/poland_sentinel2_2024.csv | cut -d "," -f 4
```

Opcje:
- `-d ","` – określa **separator kolumn** (*delimiter*). W plikach CSV separatorem jest przecinek. Domyślnym separatorem dla polecenia `cut` jest znak tabulacji (`\t`).
- `-f 4` – wskazuje **numer pola/kolumny** (*field*), którą chcemy wyodrębnić (w tym przypadku identyfikator kafelka MGRS `tile_id`).

### Sortowanie danych (`sort`)

Polecenie `sort` sortuje wiersze tekstu:

```bash
cat cloud_cover_reports/poland_sentinel2_2024.csv | cut -d "," -f 4 | sort
```

Domyślnie `sort` porządkuje wiersze **alfabetycznie** (leksykalnie).

::: {.callout-note collapse=true}
#### Sortowanie alfabetyczne a numeryczne (`sort -n`)
Domyślnie ciąg `10` w sortowaniu alfabetycznym znajdzie się przed `2` (ponieważ `1` jest przed `2`).  
Jeśli sortujesz liczby (np. procent zachmurzenia, wysokości orbit, SNR), zawsze dodawaj opcję numeryczną: `sort -n`.  
Aby odwrócić porządek (od największej do najmniejszej wartości), dodaj opcję `-r` (*reverse*): `sort -n -r`.
:::

### Deduplikacja i zliczanie (`uniq`)

Polecenie `uniq` usuwa powtarzające się sąsiednie linie tekstu.  
**Ważne:** `uniq` wykrywa duplikaty tylko wtedy, gdy wiersze znajdują się bezpośrednio obok siebie – dlatego przed użyciem `uniq` dane muszą być posortowane za pomocą `sort`!

```bash
cat cloud_cover_reports/poland_sentinel2_2024.csv | cut -d "," -f 4 | grep -v "tile_id" | sort | uniq
```

Aby nie tylko usunąć duplikaty, ale także **policzyć liczbę wystąpień** każdego kafelka, używamy opcji `-c` (*count*):

```bash
cat cloud_cover_reports/poland_sentinel2_2024.csv | cut -d "," -f 4 | grep -v "tile_id" | sort | uniq -c | sort -n -r
```

![Komiks i ściągawka poleceń `sort` i `uniq` autorstwa [Julii Evans](https://wizardzines.com/comics/sort-uniq/)](https://wizardzines.com/comics/sort-uniq/sort-uniq.png)

## Ćwiczenia

:::{.callout-exercise #pipes-exr}
#### Zrozumienie działania potoku
{{< level 1 >}}

*(Zadanie koncepcyjne)*

Mając dwa pliki z rejestrem sesji stacji naziemnych:

`cat telemetry_station1.txt`:
```output
SENTINEL-2A
LANDSAT-8
SENTINEL-1A
LANDSAT-8
```

`cat telemetry_station2.txt`:
```output
SENTINEL-2A
SENTINEL-3A
LANDSAT-8
SENTINEL-2B
```

Jaki wynik zwróci następujące polecenie?

```bash
cat telemetry_station*.txt | head -n 6 | tail -n 1
```

::: {.callout-answer}

Wynikiem będzie `SENTINEL-3A`.

Krok po kroku:
1. `cat telemetry_station*.txt` łączy oba pliki w jeden strumień 8 wierszy.
2. `head -n 6` pobiera pierwsze 6 wierszy połączonego strumienia.
3. `tail -n 1` wybiera ostatni (szósty) wiersz z tego zestawu, którym jest `SENTINEL-3A`.
:::
:::

:::{.callout-exercise #sort-exr}
#### Ranking operatorów satelitarnych w katalogu TLE
{{< level 2 >}}

W katalogu `orbital_catalog` znajduje się plik `satellites_tle_catalog.tsv` (dane rozdzielane tabulatorem).

1. Podejrzyj zawartość za pomocą `head -n 5 satellites_tle_catalog.tsv`.
2. Trzecia kolumna zawiera nazwę operatora satelity (`operator`, np. ESA, USGS/NASA, NOAA, EUMETSAT).
3. Zbuduj potok, który:
   - Wyodrębni 3. kolumnę (`cut -f 3`).
   - Odrzuci wiersz nagłówka (`grep -v "operator"`).
   - Posortuje nazwy operatorów (`sort`).
   - Zliczy liczbę satelitów dla każdego operatora (`uniq -c`).
   - Posortuje wynik malejąco według liczby satelitów (`sort -n -r`).

::: {.callout-answer}

```bash
cd ~/Desktop/dane_do_cwiczen/orbital_catalog
cat satellites_tle_catalog.tsv | cut -f 3 | grep -v "operator" | sort | uniq -c | sort -n -r
```
:::
:::

:::{.callout-exercise #zcat-exr}
#### Praca ze skompresowanymi logami telemetrycznymi (`zcat`)
{{< level 3 >}}

Wiele surowych danych satelitarnych, telemetrycznych i naukowych jest kompresowanych do formatu `.gz` (GZip) w celu zaoszczędzenia pamięci masowej.  
Aby przeglądać i przetwarzać skompresowane pliki tekstowe w locie bez konieczności wcześniejszego ich rozpakowywania na dysku, używamy polecenia `zcat` (w systemie macOS: `gzcat`).

W katalogu `telemetry_logs` znajduje się skompresowany plik archiwalny `ground_station_SVB_2024-04_archive.log.gz`:

1. Podejrzyj jego zawartość strumieniowo za pomocą `zcat telemetry_logs/ground_station_SVB_2024-04_archive.log.gz | head -n 10`.
2. Wyszukaj i zlicz wszystkie wpisy ze statusem `ERROR` w tym archiwalnym logu.
3. Policz ile różnych sesji zrealizowano dla poszczególnych satelitów w kwietniu 2024.

::: {.callout-answer}

**Zadanie 1**
```bash
zcat telemetry_logs/ground_station_SVB_2024-04_archive.log.gz | head -n 10
```

**Zadanie 2**
```bash
zcat telemetry_logs/ground_station_SVB_2024-04_archive.log.gz | grep "ERROR" | wc -l
```

**Zadanie 3**
```bash
zcat telemetry_logs/ground_station_SVB_2024-04_archive.log.gz | grep -v "^#" | cut -d "|" -f 3 | sort | uniq -c | sort -n -r
```
:::
:::

## Podsumowanie

::: {.callout-tip}
#### Główne punkty

- Operator potoku `|` łączy wyjście jednego polecenia z wejściem kolejnego, eliminując potrzebę tworzenia plików tymczasowych.
- `cut -d "separator" -f numer_kolumny` – wycina wybrane kolumny z wierszy tekstu.
- `sort` – sortuje wiersze alfabetycznie, a `sort -n` sortuje numerycznie. Flaga `-r` odwraca porządek sortowania (malejąco).
- `uniq` – usuwa powtarzające się sąsiednie wiersze (wymaga wcześniejszego posortowania danych).
- `uniq -c` – zlicza liczbę powtórzeń każdej unikalnej wartości.
- `zcat` / `gzcat` – umożliwia strumieniowe odczytywanie plików skompresowanych algorytmem gzip bezpośrednio do potoku.
:::
