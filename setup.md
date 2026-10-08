---
pagetitle: "Dane i przygotowanie środowiska"
number-sections: false
---

# Dane i przygotowanie środowiska {.unnumbered}

## Rozszerzony pakiet danych satelitarnych do ćwiczeń (`dane_do_cwiczen`)

Wszystkie ćwiczenia i przykłady w ramach kursu opierają się na dedykowanym pakiecie danych inżynierii satelitarnej `dane_do_cwiczen` (ponad **1600 plików** symulujących rzeczywiste centrum przetwarzania danych teledetekcyjnych i kosmicznych).

Zestaw zawiera m.in.:

- **`sentinel2_scenes/`** – wieloczasowe struktury produktów poziomu L2A misji Sentinel-2 (katalogi `.SAFE` z metadanymi XML i rastrami spektralnymi 10m i 20m dla Wrocławia, Warszawy, Poznania, Krakowa, Gdańska i Alp).
- **`landsat_scenes/`** – produkty Landsat-8 i Landsat-9 Collection 2 Level-2 z plikami metadanych MTL, współczynnikami kątowymi oraz maskami jakości pikseli QA.
- **`telemetry_logs/`** – setki dobowych dzienników stacji naziemnych (Spitsbergen, Kiruna, Maspalomas, Kourou, Troll, Matera, Inuvik, Punta Arenas) oraz archiwa skompresowane `.log.gz`.
- **`cloud_cover_reports/`** – bazy danych CSV z tysiącami rekordów obserwacji satelitarnych dla Polski i Europy.
- **`orbital_catalog/`** – katalogi parametrów orbitalnych (TLE) ponad 80 aktywnych satelitów (ESA, NASA, NOAA, konstelacje komercyjne) oraz specyfikacje kanałów sensorów (MSI, OLI, TIRS).
- **`gnss_stations/`** – dobowe raporty jakości i skompresowane pliki obserwacyjne RINEX dla 15 europejskich stacji geodezyjnych (m.in. `WROC`, `JOZE`, `KRAK`, `GDAN`, `POZN`, `POTS`, `WTZR`, `ONSA`).
- **`raw_telemetry_chunks/`** – setki surowych strumieni pakietów telemetrycznych (`chunk_*.dat`) do testowania wydajności potoków powłoki Bash, poleceń `find`, `xargs` i `grep`.
- **`scripts_repo/`** – wzorce skryptów automatyzujących przetwarzanie i kontrolę jakości (QC) w powłoce Bash.

### Pobieranie i rozpakowanie danych

Pobierz archiwum ZIP i rozpakuj je na Pulpicie (`Desktop`) lub w swoim katalogu roboczym:

Możesz to zrobić bezpośrednio z poziomu terminala:

```bash
cd ~/Desktop
# Jeśli posiadasz plik dane_do_cwiczen.zip lokalnie:
unzip dane_do_cwiczen.zip
cd dane_do_cwiczen
ls
```

## Oprogramowanie

### Terminal Unix

::: {.panel-tabset group="os"}
#### Windows 10/11

Aby przygotować środowisko na systemie Windows, zalecamy skorzystanie z aplikacji **MobaXterm** lub **Windows Subsystem for Linux (WSL2)**:

- **MobaXterm**:
  - Pobierz wersję [**MobaXterm Portable edition**](https://mobaxterm.mobatek.net/download-home-edition.html).
  - Rozpakuj plik ZIP na Pulpicie i uruchom `MobaXterm_Personal_XX.X.exe`.
  - Kliknij **Start local terminal**.
  - Zainstaluj edytor tekstu wpisując: `apt install nano` (potwierdź klawiszem `y`).
- **WSL2 (rekomendowane rozwiązanie zaawansowane)**:
  - Szczegółowy poradnik konfiguracji Ubuntu i VS Code znajdziesz w rozdziale [Unix w systemie Windows (WSL)](materials/a02-wsl.md).

#### macOS

System macOS posiada wbudowany terminal powłoki (zsh/bash).
Naciśnij <kbd><kbd>⌘</kbd> + <kbd>Spacja</kbd></kbd>, aby otworzyć wyszukiwarkę *Spotlight*, i wpisz `terminal`.

Opcjonalnie możesz zainstalować nowoczesny emulator terminala [_iTerm2_](https://iterm2.com).

:::{.callout-warning}
#### Uprawnienia w systemie macOS
Jeśli podczas wykonywania polecenia `ls` w terminalu pojawi się komunikat o braku uprawnień, przejdź do: *Ustawienia systemowe -> Prywatność i ochrona -> Pełny dostęp do dysku* i zaznacz aplikację Terminal.
:::

#### Linux

Dystrybucje Linuksa (np. Ubuntu, Fedora, Debian) mają domyślnie zainstalowany terminal.
W systemie _Ubuntu_ terminal można otworzyć skrótem klawiszowym <kbd><kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd></kbd>.

:::
