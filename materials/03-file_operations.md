---
pagetitle: "Operacje na plikach i katalogach"
---

# Operacje na plikach i katalogach (File operations)

::: {.callout-tip}
## Cele szkolenia

- Rozróżniać kopiowanie (`cp`) i przenoszenie/zmianę nazwy (`mv`) plików oraz katalogów.
- Zrozumieć ryzyko nieodwracalnej utraty danych podczas nadpisywania i usuwania plików w powłoce.
- Tworzyć, przenosić, kopiować i usuwać pliki oraz foldery za pomocą poleceń `mkdir`, `rmdir`, `rm`, `cp` i `mv`.

:::

## Tworzenie katalogów (`mkdir`)

Wiemy już, jak nawigować po systemie plików. Jak jednak tworzyć nowe foldery i organizować przestrzeń roboczą dla projektów satelitarnych?  
Przejdźmy do naszego folderu z danymi i sprawdźmy jego zawartość:

```bash
cd ~/Desktop/dane_do_cwiczen
ls
```

```output
README.txt            cloud_cover_reports   orbital_catalog       sources.txt
sentinel2_scenes      gnss_stations         scripts_repo          telemetry_logs
```

Utwórzmy nowy katalog o nazwie `project_wroclaw` za pomocą polecenia `mkdir` (*make directory*):

```bash
mkdir project_wroclaw
```

Nowy katalog zostanie utworzony w bieżącym katalogu roboczym:

```bash
ls
```

```output
README.txt            cloud_cover_reports   orbital_catalog       project_wroclaw
sentinel2_scenes      gnss_stations         scripts_repo          sources.txt
telemetry_logs
```

Jeśli spróbujemy **utworzyć zagnieżdżoną strukturę katalogów za jednym razem**, polecenie zgłosi błąd, jeśli katalog nadrzędny jeszcze nie istnieje:

```bash
mkdir project_wroclaw/sentinel2/cloud_masks
```

```output
mkdir: cannot create directory 'project_wroclaw/sentinel2/cloud_masks': No such file or directory
```

Mamy dwa rozwiązania tego problemu:

1. Tworzyć katalogi krok po kroku:
   ```bash
   mkdir project_wroclaw/sentinel2
   mkdir project_wroclaw/sentinel2/cloud_masks
   ```
2. Użyć flagi `-p` (*parents*), która automatycznie utworzy brakujące katalogi nadrzędne:
   ```bash
   mkdir -p project_wroclaw/sentinel2/cloud_masks
   ```

Flaga `-p` zapobiega także wyświetlaniu błędu, jeśli wskazany katalog już istnieje.

::: {.callout-note collapse=true}
#### Dobre praktyki nazewnictwa plików w projektach inżynierskich
Nieodpowiednie nazwy plików mogą znacznie utrudnić pracę w wierszu poleceń i automatyzację skryptami:

1. **Unikaj spacji w nazwach.** Spacja w powłoce rozdziela polecenia i argumenty. Zamiast `dane sentinel maj.csv` stosuj `dane_sentinel_maj.csv` lub `dane-sentinel-maj.csv`.
2. **Nie zaczynaj nazwy od myślnika (`-`).** Programy mogą potraktować taki plik jako opcję (flagę).
3. **Używaj tylko bezpiecznych znaków:** liter (bez polskich znaków diakrytycznych w nazwach plików technicznych), cyfr, kropek `.`, myślników `-` i podkreśleń `_`.
4. Jeśli musisz odwołać się do pliku ze spacją w nazwie, ujmij jego nazwę w cudzysłów: `"moje dane.txt"`.
:::

## Przenoszenie i zmiana nazwy (`mv`)

W katalogu `dane_do_cwiczen` znajduje się plik `sources.txt` (zawierający notatki z wykazem serwisów danych satelitarnych).  
Przenieśmy ten plik do nowo utworzonego katalogu `project_wroclaw` za pomocą polecenia `mv` (*move*):

```bash
mv sources.txt project_wroclaw/
```

Pierwszy argument wskazuje plik źródłowy, a drugi – miejsce docelowe. Sprawdźmy:

```bash
ls project_wroclaw
```

```output
sentinel2  sources.txt
```

Zmieńmy teraz nazwę pliku z `sources.txt` na `documentation_links.txt`.  
W systemie Unix do **zmiany nazwy pliku** również służy polecenie `mv`:

```bash
mv project_wroclaw/sources.txt project_wroclaw/documentation_links.txt
```

::: {.callout-warning}
#### Uwaga na nadpisywanie plików
Polecenie `mv` bez ostrzeżenia nadpisze istniejący plik docelowy, jeśli w folderze docelowym istnieje już plik o identycznej nazwie!
:::

## Kopiowanie plików i katalogów (`cp`)

Polecenie `cp` (*copy*) działa podobnie do `mv`, z tą różnicą, że tworzy kopię, pozostawiając plik źródłowy bez zmian:

```bash
cp project_wroclaw/documentation_links.txt links_backup.txt
ls
```

```output
README.txt            cloud_cover_reports   links_backup.txt      orbital_catalog
project_wroclaw       gnss_stations         scripts_repo          telemetry_logs
sentinel2_scenes
```

Aby **skopiować cały katalog wraz z zawartością**, musimy dodać opcję rekurencyjną `-r` (*recursive*):

```bash
cp -r scripts_repo scripts_backup
```

## Usuwanie plików i katalogów (`rm`, `rmdir`)

Do usuwania plików służy polecenie `rm` (*remove*):

```bash
rm links_backup.txt
```

Co się stanie, gdy spróbujemy usunąć katalog `scripts_backup`?

```bash
rm scripts_backup
```

```output
rm: cannot remove 'scripts_backup': Is a directory
```

Domyślnie `rm` odmawia usuwania katalogów. Aby usunąć katalog wraz ze wszystkimi zawartymi w nim plikami i podfolderami, należy użyć opcji `-r`:

```bash
rm -r scripts_backup
```

::: {.callout-danger}
#### W powłoce Unix usunięcie jest bezpowrotne!
W wierszu poleceń **nie ma Kosza** (*Trash / Recycle Bin*). Usunięte poleceniem `rm` pliki są natychmiast wymazywane z systemu plików.  
Używaj `rm -r` z najwyższą ostrożnością. Aby powłoka pytała o potwierdzenie przed usunięciem każdego pliku, można użyć opcji interaktywnej: `rm -r -i nazwa_katalogu`.
:::

Do bezpiecznego usuwania **wyłącznie pustych katalogów** służy polecenie `rmdir` (*remove directory*).

## Ćwiczenia

:::{.callout-exercise #rename-exr}
#### Zmiana nazwy pliku konfiguracyjnego
{{< level 1 >}}

*(Zadanie koncepcyjne)*

Załóżmy, że w bieżącym katalogu utworzyłeś plik tekstowy z parametrami korekcji atmosferycznej dla sensora Sentinel-2 i omyłkowo nazwałeś go `sen2cor_confg.txt`.  
Chcesz poprawić literówkę i zmienić nazwę na `sen2cor_config.txt`. Którego polecenia należy użyć?

1. `cp sen2cor_confg.txt sen2cor_config.txt`
2. `mv sen2cor_confg.txt sen2cor_config.txt`
3. `mv sen2cor_confg.txt .`
4. `cp sen2cor_confg.txt .`

::: {.callout-answer collapse=true}

1. Nie: polecenie utworzy kopię o poprawnej nazwie, ale błędnie nazwany plik nadal pozostanie na dysku.
2. **Prawidłowa odpowiedź**: `mv` zmieni nazwę pliku na właściwą bez tworzenia duplikatu.
3. Nie: kropka wskazuje bieżący katalog, ale nie podaje nowej nazwy pliku.
4. Nie: brak nowej nazwy pliku docelowego.
:::
:::

:::{.callout-exercise #copy-exr}
#### Tworzenie kopii zapasowej katalogu skryptów
{{< level 1 >}}

Przejdź do katalogu danych: `cd ~/Desktop/dane_do_cwiczen`.  
Utwórz kopię zapasową folderu `scripts_repo` o nazwie `scripts_repo_v1`.  
Sprawdź za pomocą `ls`, czy nowy katalog pojawił się na liście.

::: {.callout-answer collapse=true}

```bash
cp -r scripts_repo scripts_repo_v1
ls
```
:::
:::

:::{.callout-exercise #cp-multiple-exr}
#### Kopiowanie wielu raportów do folderu projektu
{{< level 2 >}}

Utwórz katalog `reports_analysis`:
```bash
mkdir reports_analysis
```
Skopiuj do niego pliki raportów dla Polski za jednym razem:
```bash
cp cloud_cover_reports/poland_sentinel2_2023.csv cloud_cover_reports/poland_sentinel2_2024.csv reports_analysis/
```
Sprawdź zawartość `reports_analysis/` za pomocą `ls`.

::: {.callout-answer collapse=true}

```bash
ls reports_analysis
# Wyświetli: poland_sentinel2_2023.csv  poland_sentinel2_2024.csv
```
Gdy ostatnim argumentem polecenia `cp` jest katalog, wszystkie wymienione wcześniej pliki zostaną do niego skopiowane.
:::
:::

## Podsumowanie

::: {.callout-tip}
#### Główne punkty

- Tworzenie katalogów: `mkdir nazwa_katalogu` (oraz `mkdir -p sciezka/do/podkatalogu` dla struktur zagnieżdżonych).
- Przenoszenie i zmiana nazwy: `mv zrodlo cel`.
- Kopiowanie plików: `cp plik_zrodlowy plik_docelowy`.
- Kopiowanie całych katalogów z zawartością: `cp -r katalog_zrodlowy katalog_docelowy`.
- Usuwanie plików: `rm plik`.
- Usuwanie katalogów z zawartością: `rm -r katalog`.
- Usuwanie pustych katalogów: `rmdir katalog`.
- **Uwaga na utratę danych**: W wierszu poleceń usunięcie plików za pomocą `rm` jest trwałe i natychmiastowe (brak kosza systemowego).
:::
