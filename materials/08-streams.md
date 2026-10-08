---
pagetitle: "Strumienie standardowe"
---

# Strumienie standardowe i przekierowania (Standard streams)

::: {.callout-tip}
### Cele szkolenia

- Zdefiniować trzy standardowe strumienie danych (`stdin`, `stdout`, `stderr`) i zrozumieć ich rolę w systemie Unix.
- Rozdzielać i zapisywać standardowe wyjście oraz komunikaty o błędach do odrębnych plików za pomocą operatorów `>` oraz `2>`.
- Łączyć strumienie `stdout` i `stderr` w jeden plik dziennika (`2>&1` lub `&>`).
- Wyciszać niepotrzebne komunikaty ostrzeżeń za pomocą wirtualnego urządzenia `/dev/null`.
:::

## Wejście i wyjście programu

Każdy program uruchamiany w systemie Unix może pobierać dane wejściowe i generować dane wyjściowe.  
Na przykład:

```bash
ls sentinel2_scenes
```

- Ścieżka `sentinel2_scenes` stanowi dane wejściowe dla programu `ls`.
- Zwrócona lista katalogów scen to standardowy wynik działania polecenia.

Jeśli jednak program napotka problem (np. nieistniejący plik lub katalog):

```bash
ls sentinel2_scenes/S2A_nonexistent_scene
```

```output
ls: cannot access 'sentinel2_scenes/S2A_nonexistent_scene': No such file or directory
```

Komunikat o błędzie trafia do oddzielnego kanału.  
W architekturze Unix każdy proces posiada trzy domyślne **strumienie standardowe**:

1. **Standardowe wejście (`stdin`, deskryptor `0`)** – dane przekazywane do programu (np. wpisywane z klawiatury lub przekazywane potokiem `|`).
2. **Standardowe wyjście (`stdout`, deskryptor `1`)** – prawidłowe wyniki działania programu.
3. **Standardowe wyjście błędów (`stderr`, deskryptor `2`)** – komunikaty o błędach, ostrzeżeniach i statusie wykonania.

![Schemat standardowych strumieni wejścia/wyjścia (źródło: Wikimedia Commons)](https://thumb.wikimedia.org/wikipedia/commons/thumb/7/70/Stdstreams-notitle.svg/960px-Stdstreams-notitle.svg.png)

Mimo że w oknie terminala zarówno `stdout`, jak i `stderr` wyświetlają się razem, powłoka traktuje je jako dwa całkowicie odrębne kanały komunikacji.

## Przekierowywanie strumieni wyjściowych

Rozróżnienie między `stdout` a `stderr` możemy zilustrować za pomocą operatorów przekierowania.

Polecenie:

```bash
ls sentinel2_scenes > valid_scenes.txt
```

Zapisuje listę katalogów do pliku `valid_scenes.txt`. Na ekranie nie pojawia się żaden tekst.

Zobaczmy co się stanie, gdy wykonamy polecenie generujące błąd:

```bash
ls sentinel2_scenes/S2A_nonexistent > valid_scenes.txt
```

```output
ls: cannot access 'sentinel2_scenes/S2A_nonexistent': No such file or directory
```

Błąd nadal pojawił się na ekranie, a plik docelowy pozostał pusty!  
Dzieje się tak, ponieważ domyślny operator `>` (równoważny `1>`) przekierowuje **wyłącznie standardowe wyjście (`stdout`)**.

Aby przekierować **strumień błędów (`stderr`)**, używamy operatora `2>`:

```bash
ls sentinel2_scenes/S2A_nonexistent > valid_scenes.txt 2> error_log.txt
```

Teraz w terminalu nie pojawi się żaden komunikat: błąd został bezpiecznie zapisany w pliku `error_log.txt`.

::: {.callout-note}
#### Zastosowanie w inżynierii danych satelitarnych
Rozdzielanie `stdout` i `stderr` jest kluczowe podczas wsadowego przetwarzania danych satelitarnych (np. konwersji tysięcy scen Sentinel przez GDAL, SNAP lub biblioteki Pythona). Dzięki temu czyste dane wyjściowe trafiają do bazy lub pliku wynikowego, a wszystkie ostrzeżenia o brakujących kanałach czy chmurach są zbierane w odrębnym pliku diagnostycznym (`errors.log`).
:::

## Łączenie strumieni `stderr` i `stdout`

Często w skryptach chcemy zapisać pełny przebieg analizy (zarówno komunikaty informacyjne, jak i ewentualne błędy) do jednego wspólnego pliku logu:

```bash
ls sentinel2_scenes sentinel2_scenes/S2A_nonexistent > full_run.log 2>&1
```

Zapis `2>&1` oznacza: „przekieruj strumień błędu (`2>`) do tego samego miejsca, w które wskazuje standardowe wyjście (`&1`)”.

## Wyciszanie komunikatów za pomocą `/dev/null`

W systemach Unix `/dev/null` to specjalne wirtualne urządzenie (tzw. „czarna dziura” lub kosz), które natychmiast bezpowrotnie porzuca wszystkie przesłane do niego dane.

Jeśli narzędzie generuje dużą liczbę zbędnych ostrzeżeń, które chcemy zignorować:

```bash
ls sentinel2_scenes sentinel2_scenes/fake_scene 2> /dev/null
```

Błędy dotyczące nieistniejących plików zostaną wyciszone i pominięte.

## Ćwiczenia

:::{.callout-exercise}
#### Rejestracja błędów przetwarzania
{{< level 2 >}}

Napisz skrypt `process_all_logs.sh`, który próbuje wylistować i sprawdzić logi dla kilku stacji naziemnych: `SVB`, `KIR`, `FAKE_STATION`, `MAS`.

Skrypt powinien:
1. Przekierować nazwy istniejących plików do `available_logs.txt`.
2. Przekierować błędy o braku plików dla nieistniejących stacji do `missing_stations.log`.

::: {.callout-answer collapse=true}

```bash
#!/usr/bin/env bash

ls telemetry_logs/ground_station_SVB_*.log \
   telemetry_logs/ground_station_KIR_*.log \
   telemetry_logs/ground_station_FAKE_STATION_*.log \
   telemetry_logs/ground_station_MAS_*.log \
   > available_logs.txt 2> missing_stations.log

echo "Dostepne pliki zapisano w: available_logs.txt"
echo "Brakujace stacje odnotowano w: missing_stations.log"
```
:::
:::

## Podsumowanie

::: {.callout-tip}
### Główne punkty

- Powłoka obsługuje trzy standardowe strumienie danych dla każdego procesu:
  - `stdin` (deskryptor 0) – dane wejściowe programu.
  - `stdout` (deskryptor 1) – standardowe wyjście (wyniki).
  - `stderr` (deskryptor 2) – wyjście diagnostyczne (ostrzeżenia i błędy).
- Operatory przekierowania:
  - `>` (lub `1>`) – przekierowuje `stdout` do pliku.
  - `2>` – przekierowuje `stderr` do pliku logu.
  - `2>&1` – scala strumień błędów ze standardowym wyjściem.
  - `2> /dev/null` – wycisza i odrzuca strumień błędów.
:::
