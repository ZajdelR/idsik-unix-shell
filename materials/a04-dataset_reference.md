---
pagetitle: "Opis pakietu danych do ćwiczeń"
---

# Opis pakietu danych do ćwiczeń (Dataset Reference) {.unnumbered}

Niniejszy dodatek zawiera szczegółową dokumentację techniczną wszystkich katalogów, plików, formatów oraz kolumn danych zawartych w pakiecie [`dane_do_cwiczen/`](file:///C:/Users/UPWr/Documents/DYDAKTYKA/2026/ZARZADZANIE_PROJEKTEM/unix-shell/dane_do_cwiczen).

Zestaw ten symuluje rzeczywiste środowisko pracy inżyniera danych satelitarnych w centrach przetwarzania danych teledetekcyjnych (np. ESA Copernicus Data Space Ecosystem, USGS EarthExplorer, EUMETSAT Data Store, sieci geodezyjne ASG-EUPOS / EPN).

---

## Przegląd struktury katalogów

```output
dane_do_cwiczen/
├── README.txt                    # Informacje ogólne o pakiecie danych
├── sources.txt                   # Wykaz źródeł, serwisów satelitarnych i dokumentacji
├── sentinel2_scenes/             # Produkty misji ESA Sentinel-2 L2A w standardzie .SAFE
├── landsat_scenes/               # Produkty misji USGS/NASA Landsat-8 i Landsat-9 L2SP
├── telemetry_logs/               # Dobowe logi stacji naziemnych oraz archiwa .log.gz
├── cloud_cover_reports/          # Raporty CSV statystyk zachmurzenia i jakości scen
├── orbital_catalog/              # Parametry TLE orbit satelitów oraz specyfikacje sensorów
├── gnss_stations/                # Logi jakości i obserwacje RINEX stacji geodezyjnych
├── raw_telemetry_chunks/         # Setki surowych pakietów binarno-tekstowych strumieni CCSDS
└── scripts_repo/                 # Wzorce skryptów automatyzujących powłoki Bash
```

---

## 1. Produkty satelitarne Sentinel-2 (`sentinel2_scenes/`)

Katalog zawiera produkty poziomu Level-2A (reflektancja powierzchniowa BOA po korekcji atmosferycznej) w standardzie dystrybucyjnym ESA **SAFE** (*Standard Archive Format for Europe*).

### Konwencja nazewnictwa katalogów `.SAFE`
```
MMM_MSIL2A_YYYYMMDDTHHMMSS_Nxxyy_ROOO_Txxxxx_<Product Discriminator>.SAFE
```
- **`MMM`**: Identyfikator satelity (`S2A`, `S2B`, `S2C`).
- **`MSIL2A`**: Sensor MSI (*MultiSpectral Instrument*), poziom Level-2A.
- **`YYYYMMDDTHHMMSS`**: Czas pozyskania sceny w formacie UTC (np. `20240510T100031`).
- **`Nxxyy`**: Numer wersji przetwarzania ESA (*Processing Baseline*, np. `N0510`).
- **`ROOO`**: Względny numer orbity (*Relative Orbit*, np. `R122`, `R079`, `R036`).
- **`Txxxxx`**: Kafelek siatki podziału MGRS (np. `T33UWT` Wrocław, `T34UCA` Warszawa, `T33UXT` Poznań, `T34UDE` Kraków, `T34UEC` Gdańsk, `T33UWS` Sudety, `T32TMS` Alpy).

### Wewnętrzne pliki składowe
- **`manifest.safe`**: Główny plik manifestu w formacie XML opisujący zawartość paczki i identyfikatory sceny.
- **`MTD_MSIL2A.xml`**: Globalne metadane produktu (statystyki zachmurzenia, kąty zenitalne słońca, status jakości geometrycznej i radiometrycznej).
- **`GRANULE/<Granule_ID>/IMG_DATA/R10m/`**: Rastry o rozdzielczości terenowej **10 m** (`B02` Blue, `B03` Green, `B04` Red, `B08` NIR, `TCI` True Color Image).
- **`GRANULE/<Granule_ID>/IMG_DATA/R20m/`**: Rastry o rozdzielczości terenowej **20 m** (`B05`, `B06`, `B07` Red Edge, `B8A` Narrow NIR, `B11`, `B12` SWIR, `SCL` Scene Classification Layer).
- **`GRANULE/<Granule_ID>/QI_DATA/`**: Wskaźniki kontroli jakości oraz poligonowe maski chmur (`cloud_mask.gml`, `report.xml`).

---

## 2. Produkty satelitarne Landsat (`landsat_scenes/`)

Katalog zawiera produkty misji **Landsat-8** oraz **Landsat-9** w standardzie *USGS Collection 2 Level-2 Surface Reflectance (L2SP)*.

### Konwencja nazewnictwa
```
LXSS_LLLL_PPPRRR_YYYYMMDD_yyyymmdd_CC_TX
```
- **`LXSS`**: `LC08` (Landsat-8 OLI/TIRS) lub `LC09` (Landsat-9 OLI-2/TIRS-2).
- **`LLLL`**: Poziom przetwarzania (`L2SP` – *Surface Reflectance Standard Product*).
- **`PPPRRR`**: Ścieżka i rząd w globalnym systemie WRS-2 (*Path/Row*, np. `190024`, `191024` dla Polski).
- **`YYYYMMDD`**: Data pozyskania zobrazowania.
- **`yyyymmdd`**: Data wygenerowania produktu w USGS.
- **`CC` / `TX`**: Numer kolekcji (`02`) i kategoria jakości (`T1` – Tier 1).

### Pliki wewnątrz produktu:
- `*_MTL.txt`: Plik metadanych tekstowych zawierający parametry kalibracyjne, współczynniki nasłonecznienia i procent zachmurzenia.
- `*_ANG.txt`: Kąty oświetlenia i obserwacji sensora.
- `*_SR_B1.TIF` do `*_SR_B7.TIF`: Warstwy rastrowe reflektancji powierzchniowej (pasma spektralne).
- `*_QA_PIXEL.TIF`, `*_QA_RADSAT.TIF`: Rastrowe maski jakości pikseli i nasycenia radiometrycznego.

---

## 3. Dzienniki stacji naziemnych (`telemetry_logs/`)

Katalog zawiera ponad **360 dobowych plików tekstowych** oraz **24 skompresowane archiwa miesięczne** (`.log.gz`), rejestrujące sesje pobierania danych (*downlink telemetry*) dla 8 globalnych stacji naziemnych:

| Kod stacji | Nazwa stacji naziemnej | Współrzędne |
| :--- | :--- | :--- |
| **`SVB`** | Spitsbergen (SvalSat, Norwegia) | 78.23° N, 15.39° E |
| **`KIR`** | Kiruna (Szwecja) | 67.85° N, 20.96° E |
| **`MAS`** | Maspalomas (Wyspy Kanaryjskie, Hiszpania) | 27.76° N, 15.63° W |
| **`KRU`** | Kourou (Gujana Francuska) | 5.25° N, 52.80° W |
| **`TRL`** | Troll (Antarktyda) | 72.01° S, 2.53° E |
| **`MAT`** | Matera (Włochy) | 40.65° N, 16.70° E |
| **`INU`** | Inuvik (Kanada) | 68.36° N, 133.72° W |
| **`PUN`** | Punta Arenas (Chile) | 53.16° S, 70.91° W |

### Format rekordów w logach telemetrycznych:
```
TIMESTAMP_UTC | PASS_ID | SATELLITE_ID | FREQ_GHZ | SNR_DB | BER | PACKETS_RECV | PACKETS_LOST | DOWNLINK_MB | STATUS
```
- `TIMESTAMP_UTC`: Czas rozpoczęcia sesji (ISO 8601).
- `PASS_ID`: Unikalny identyfikator przelotu nad stacją.
- `SATELLITE_ID`: Identyfikator satelity (`SENTINEL-1A`, `SENTINEL-2A`, `LANDSAT-8`, itp.).
- `FREQ_GHZ`: Częstotliwość pasma X (np. 8.150 GHz).
- `SNR_DB`: Stosunek sygnału do szumu w decybelach (*Signal-to-Noise Ratio*).
- `BER`: Bitowa stopa błędów (*Bit Error Rate*).
- `PACKETS_RECV`: Liczba odebranych pakietów telekomunikacyjnych.
- `PACKETS_LOST`: Liczba utraconych pakietów (dla `STATUS=OK` wynosi 0).
- `DOWNLINK_MB`: Łączna objętość odebranych danych w megabajtach.
- `STATUS`: Status sesji: `OK`, `WARNING_PACKET_LOSS`, `WARNING_HIGH_TEMPERATURE`, `ERROR_CHECKSUM_FAILED`, `ERROR_SIGNAL_LOST`, `ERROR_SYNC_FAILED`.

---

## 4. Raporty zachmurzenia i metadanych (`cloud_cover_reports/`)

Pliki tabelaryczne CSV zawierające łącznie ponad **6000 rekordów** z parametrami geometrycznymi i atmosferycznymi scen satelitarnych:

- `poland_sentinel2_2024.csv` – 850 obserwacji nad terytorium Polski z 2024 roku.
- `poland_sentinel2_2023.csv` – 750 obserwacji z 2023 roku.
- `poland_sentinel2_2022.csv` – 680 obserwacji z 2022 roku.
- `central_europe_sentinel2_2024.csv` – 1200 obserwacji dla Europy Środkowej (Polska, Niemcy, Czechy, Słowacja).
- `scandinavia_sentinel2_2024.csv` – 950 obserwacji dla Skandynawii.
- `alps_landsat_sentinel_2024.csv` – 600 obserwacji obszarów alpejskich.
- `mediterranean_sentinel2_2024.csv` – 1100 obserwacji dla basenu Morza Śródziemnego.

### Struktura kolumn w plikach CSV:
1. `scene_id` – Pełny identyfikator sceny satelitarnej.
2. `date` – Data akwizycji (`YYYY-MM-DD`).
3. `satellite` – Nazwa platformy (`SENTINEL-2A`, `SENTINEL-2B`, `LANDSAT-8`, `LANDSAT-9`).
4. `tile_id` – Identyfikator kafelka siatki MGRS.
5. `orbit_relative` – Numer względnej orbity.
6. `cloud_coverage_percent` – Procentowe zachmurzenie sceny (0.00 – 100.00%).
7. `nodata_pixel_percent` – Procent pikseli poza zasięgiem matrycy sensora.
8. `snow_ice_percent` – Pokrycie śniegiem i lodem.
9. `sun_zenith_angle` – Kąt zenitalny słońca w stopniach.
10. `quality_flag` – Flaga jakościowa: `PASSED`, `SUSPECT_HAZE`, `FAILED_CORRUPTION`, `PASSED_HIGH_SUN_GLINT`.

---

## 5. Katalogi orbitalne i sensoryczne (`orbital_catalog/`)

### `satellites_tle_catalog.tsv`
Baza danych (TSV) ponad 80 aktywnych satelitów obserwacji Ziemi (misje naukowe ESA, NASA, NOAA, EUMETSAT oraz konstelacje komercyjne PlanetScope, ICEYE SAR, Spire Lemur).

Kolumny:
- `norad_id`: Numer katalogowy US Space Command / NORAD.
- `satellite_name`: Oficjalna nazwa satelity.
- `operator`: Agencja lub podmiot komercyjny.
- `launch_year`: Rok wystrzelenia na orbitę.
- `inclination_deg`: Inklinacja orbity w stopniach.
- `altitude_km`: Średnia wysokość orbity.
- `apogee_km` / `perigee_km`: Apogeum i perygeum orbity.
- `period_min`: Okres orbitalny w minutach.
- `orbit_type`: Typ orbity (`SSO` – heliosynchroniczna, `NON-SSO`).
- `status`: Status operacyjny (`OPERATIONAL`, `DECOMMISSIONED`, `DEGRADED`, `PLANNED`).

### `sensor_bands_spec.tsv`
Charakterystyki spektralne kanałów sensorów **MSI** (Sentinel-2) oraz **OLI/TIRS** (Landsat-8/9):
- `sensor`: Typ sensora.
- `band_id`: Oznaczenie kanału (`B01`–`B12`, `B8A`, `TCI`).
- `band_name`: Nazwa opisowa pasma (np. Coastal Aerosol, Blue, Red Edge, NIR, SWIR, Thermal).
- `central_wavelength_nm`: Długość fali centralnej w nanometrach.
- `bandwidth_nm`: Szerokość pasma spektralnego w nanometrach.
- `spatial_res_m`: Rozdzielczość przestrzenna w metrach (10m, 20m, 30m, 60m, 100m).
- `spectrum_region`: Zakres widmowy (`VNIR`, `SWIR`, `TIR`).

---

## 6. Stacje sieci geodezyjnych GNSS (`gnss_stations/`)

Struktury danych dla 15 europejskich permanentnych stacji referencyjnych sieci **ASG-EUPOS** oraz **EUREF EPN**:
- `WROC` (Wrocław, UPWr)
- `JOZE` (Józefosław, Politechnika Warszawska)
- `KRAK` (Kraków, AGH)
- `GDAN` (Gdańsk, Politechnika Gdańska)
- `LODZ` (Łódź)
- `POZN` (Poznań, CBK PAN)
- `KATW` (Katowice)
- `BIAY` (Białystok)
- `SZCZ` (Szczecin)
- `ZAKO` (Zakopane)
- `BOR1` (Borowiec, CBK PAN)
- `GOPE` (Ondřejov, Czechy)
- `POTS` (Poczdam, GFZ Niemcy)
- `WTZR` (Wettzell, BKG Niemcy)
- `ONSA` (Onsala, Szwecja)

### Zawartość każdego podkatalogu stacji:
- `station_info.json`: Metadane stacji (współrzędne elipsoidalne WGS84, typ odbiornika, typ anteny, przynależność do sieci).
- `<CODE>_2024_daily_status.log`: Dobowy raport kontroli jakości (liczba epok, ubytki danych, zjawiska *cycle slips*, multipath MP1/MP2, status QC).
- `<CODE>00POL_R_..._MO.rnx.gz`: Skompresowane dobowe pliki obserwacji wielosystemowych w standardzie **RINEX 3.04** (GPS, GLONASS, Galileo, BeiDou).

---

## 7. Surowe strumienie pakietów telemetrycznych (`raw_telemetry_chunks/`)

Katalog zawiera **500 surowych plików binarno-tekstowych** (`telemetry_stream_chunk_0001.dat` do `chunk_0500.dat`) symulujących pakiety protokołu **CCSDS** (*Consultative Committee for Space Data Systems*).

Przykładowy fragment:
```output
# RAW TELEMETRY PACKET STREAM CHUNK #0042
HEADER: CCSDS_SYNC=0x1ACFFC1D STREAM_ID=0042 BITRATE_MBPS=150.0
PKT_0042_001 | V=28.12V | T=24.50C | CRC_OK
PKT_0042_002 | V=28.15V | T=24.62C | CRC_OK
PKT_0042_003 | V=27.90V | T=38.90C | CRC_ERR
```
Zastosowanie: testowanie potęgi poleceń `find`, `xargs`, `cat *.dat | grep` oraz równoległego przetwarzania w skryptach powłoki Bash.

---

## 8. Repozytorium skryptów demonstracyjnych (`scripts_repo/`)

Wzorce gotowych skryptów Bash dla studentów:
- `filter_clouds.sh`: Skrypt filtrujący sceny z raportów CSV według zadanego kafelka i progu zachmurzenia.
- `count_telemetry_errors.sh`: Skrypt zliczający błędy stacji naziemnych z obsługą argumentów pozycyjnych.
- `batch_qc_check.sh`: Skrypt do wsadowego audytu integralności pakietów we wszystkich 500 plikach `raw_telemetry_chunks/`.
