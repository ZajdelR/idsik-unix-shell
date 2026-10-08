#!/usr/bin/env python3
"""
Generator rozszerzonego zestawu danych do ćwiczeń: Inżynieria Danych Satelitarnych i Kosmicznych
Zarządzanie projektem informatycznym - UPWr
"""

import os
import random
import gzip
import zipfile
import shutil
from datetime import datetime, timedelta

random.seed(42)

BASE_DIR = os.path.abspath("dane_do_cwiczen")

def create_readme_and_sources():
    os.makedirs(BASE_DIR, exist_ok=True)
    
    readme_path = os.path.join(BASE_DIR, "README.txt")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("""================================================================================
ROZSZERZONY PAKIET DANYCH: INŻYNIERIA DANYCH SATELITARNYCH I KOSMICZNYCH
Zarządzanie projektem informatycznym (UPWr 2026/2027)
================================================================================

Ten zestaw danych zawiera tysiące plików i struktur katalogowych symulujących
rzeczywiste środowisko pracy inżyniera danych satelitarnych w centrach przetwarzania
danych (np. ESA CDS, USGS, EUMETSAT, Copernicus Data Space Ecosystem).

Struktura katalogów i zawartość:

1. sentinel2_scenes/
   Struktury produktów Sentinel-2 L2A (.SAFE) dla kafelków w Polsce i Europie
   (Wrocław T33UWT, Warszawa T34UCA, Poznań T33UXT, Kraków T34UDE, Gdańsk T34UEC,
   Alpy T32TMS). Zawierają pliki metadanych MTD_MSIL2A.xml, manifest.safe, kanały
   spektralne 10m i 20m oraz raporty jakości QI_DATA.

2. landsat_scenes/
   Struktury produktów Landsat-8/9 Collection 2 Level-2 (L2SP) z plikami metadanych
   MTL.txt, raportami kątowymi ANG.txt oraz rastrami pasm spektralnych (SR_B1..B7, QA_PIXEL).

3. telemetry_logs/
   Setki dobowych dzienników stacji naziemnych (Spitsbergen, Kiruna, Maspalomas,
   Kourou, Troll, Matera, Inuvik, Punta Arenas) z lat 2023-2024 oraz skompresowane
   miesięczne archiwa .log.gz.

4. cloud_cover_reports/
   Tabelaryczne bazy danych CSV z dziesiątkami tysięcy rekordów obserwacji
   satelitarnych (pokrycie chmurami, śniegiem, kąty słoneczne, flagi jakości).

5. orbital_catalog/
   Katalogi parametrów orbitalnych (TLE) ponad 80 aktywnych satelitów obserwacji Ziemi,
   specyfikacje techniczne sensorów (MSI, OLI, TIRS, SAR C-band, OLCI) oraz harmonogramy
   przelotów.

6. gnss_stations/
   Dobowe logi jakości i skompresowane pliki obserwacyjne RINEX dla 15 europejskich
   stacji referencyjnych sieci ASG-EUPOS oraz EPN (m.in. WROC, JOZE, KRAK, GDAN, POZN).

7. raw_telemetry_chunks/
   Tysiące surowych pakietów telemetrycznych (chunk_*.dat / chunk_*.log)
   do testowania wydajności potoków powłoki Bash, poleceń find, xargs, cat i zliczania.

8. scripts_repo/
   Szablony skryptów powłoki Bash do automatyzacji przetwarzania danych i kontroli jakości.
================================================================================
""")

    sources_path = os.path.join(BASE_DIR, "sources.txt")
    with open(sources_path, "w", encoding="utf-8") as f:
        f.write("""Źródła danych i dokumentacja teledetekcyjna:
- Copernicus Data Space Ecosystem (CDSE): https://dataspace.copernicus.eu/
- ESA Sentinel-2 User Handbook: https://sentinels.copernicus.org/web/sentinel/user-guides/sentinel-2-msi
- USGS EarthExplorer (Landsat): https://earthexplorer.usgs.gov/
- ASG-EUPOS Polish Active Geodetic Network: http://www.asgeupos.pl/
- EUREF Permanent GNSS Network (EPN): https://epncb.oma.be/
- CEOS Earth Observation Handbook: http://eohandbook.com/
- GDAL Geospatial Data Abstraction Library: https://gdal.org/
- Spire / Space-Track TLE Orbit Data: https://www.space-track.org/
""")


def create_sentinel2_scenes():
    scenes_dir = os.path.join(BASE_DIR, "sentinel2_scenes")
    os.makedirs(scenes_dir, exist_ok=True)
    
    tiles_info = [
        ("T33UWT", "Wroclaw / Dolny Slask", "WGS84 / UTM zone 33N", 122),
        ("T34UCA", "Warszawa / Mazowsze", "WGS84 / UTM zone 34N", 79),
        ("T33UXT", "Poznan / Wielkopolska", "WGS84 / UTM zone 33N", 122),
        ("T34UDE", "Krakow / Malopolska", "WGS84 / UTM zone 34N", 36),
        ("T34UEC", "Gdansk / Pomorze", "WGS84 / UTM zone 34N", 79),
        ("T33UWS", "Sudety / Karkonosze", "WGS84 / UTM zone 33N", 122),
        ("T32TMS", "Alpy Szwajcarskie", "WGS84 / UTM zone 32N", 65),
    ]
    
    bands_10m = ["B02_10m.jp2", "B03_10m.jp2", "B04_10m.jp2", "B08_10m.jp2", "TCI_10m.jp2"]
    bands_20m = ["B05_20m.jp2", "B06_20m.jp2", "B07_20m.jp2", "B8A_20m.jp2", "B11_20m.jp2", "B12_20m.jp2", "SCL_20m.jp2"]
    
    dates = [
        ("20240410T100031", "2024-04-10T10:00:31", "S2A", 18.2, 42.1),
        ("20240415T095029", "2024-04-15T09:50:29", "S2B", 5.4, 40.2),
        ("20240420T100031", "2024-04-20T10:00:31", "S2A", 75.0, 38.5),
        ("20240502T100031", "2024-05-02T10:00:31", "S2A", 8.9, 35.1),
        ("20240507T095029", "2024-05-07T09:50:29", "S2B", 2.1, 33.6),
        ("20240510T100031", "2024-05-10T10:00:31", "S2A", 12.4, 34.8),
        ("20240512T095029", "2024-05-12T09:50:29", "S2B", 4.2, 33.5),
        ("20240515T100031", "2024-05-15T10:00:31", "S2A", 48.9, 32.1),
        ("20240517T095029", "2024-05-17T09:50:29", "S2B", 0.8, 30.7),
        ("20240520T100031", "2024-05-20T10:00:31", "S2A", 82.1, 29.4),
        ("20240522T095029", "2024-05-22T09:50:29", "S2B", 15.3, 28.2),
        ("20240525T100031", "2024-05-25T10:00:31", "S2A", 6.7, 27.1),
        ("20240527T095029", "2024-05-27T09:50:29", "S2B", 22.0, 26.0),
        ("20240601T100031", "2024-06-01T10:00:31", "S2A", 3.1, 24.5),
        ("20240605T095029", "2024-06-05T09:50:29", "S2B", 91.5, 23.8),
        ("20240610T100031", "2024-06-10T10:00:31", "S2A", 1.4, 23.1),
        ("20240615T095029", "2024-06-15T09:50:29", "S2B", 14.8, 22.9),
        ("20240620T100031", "2024-06-20T10:00:31", "S2A", 5.2, 22.8),
        ("20240625T095029", "2024-06-25T09:50:29", "S2B", 39.0, 23.0),
        ("20240702T100031", "2024-07-02T10:00:31", "S2A", 0.3, 23.6),
    ]
    
    for tile, region, crs, rel_orbit in tiles_info:
        for tag, dt, sat, cloud, sun_z in dates[:random.randint(3, 5)]:
            safe_name = f"{sat}_MSIL2A_{tag}_N0510_R{rel_orbit:03d}_{tile}_{tag[:8]}T140000.SAFE"
            safe_path = os.path.join(scenes_dir, safe_name)
            
            granule_id = f"L2A_{tile}_A{random.randint(10000,99999)}_{tag}"
            granule_img_10m = os.path.join(safe_path, "GRANULE", granule_id, "IMG_DATA", "R10m")
            granule_img_20m = os.path.join(safe_path, "GRANULE", granule_id, "IMG_DATA", "R20m")
            granule_qi = os.path.join(safe_path, "GRANULE", granule_id, "QI_DATA")
            
            os.makedirs(granule_img_10m, exist_ok=True)
            os.makedirs(granule_img_20m, exist_ok=True)
            os.makedirs(granule_qi, exist_ok=True)
            
            # manifest.safe
            with open(os.path.join(safe_path, "manifest.safe"), "w", encoding="utf-8") as f:
                f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<xfdu:XFDU xmlns:xfdu="urn:ccsds:schema:xfdu:encodings">
  <informationPackageMap>
    <xfdu:packageIdentifier>{safe_name}</xfdu:packageIdentifier>
    <xfdu:satellitePlatform>{sat}</xfdu:satellitePlatform>
    <xfdu:acquisitionTime>{dt}Z</xfdu:acquisitionTime>
    <xfdu:processingLevel>Level-2A</xfdu:processingLevel>
    <xfdu:regionDescription>{region}</xfdu:regionDescription>
  </informationPackageMap>
</xfdu:XFDU>
""")
            
            # MTD_MSIL2A.xml
            with open(os.path.join(safe_path, "MTD_MSIL2A.xml"), "w", encoding="utf-8") as f:
                f.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<n1:Level-2A_User_Product xmlns:n1="https://psd-14.sentinel2.eo.esa.int/PSD/User_Product_Level-2A.xsd">
  <General_Info>
    <PRODUCT_NAME>{safe_name}</PRODUCT_NAME>
    <SPACECRAFT_NAME>{sat}</SPACECRAFT_NAME>
    <DATATAKE_SENSING_START>{dt}Z</DATATAKE_SENSING_START>
    <PROCESSING_BASELINE>05.10</PROCESSING_BASELINE>
    <TILE_ID>{tile}</TILE_ID>
    <HORIZONTAL_CRS>{crs}</HORIZONTAL_CRS>
  </General_Info>
  <Quality_Indicators_Info>
    <Cloud_Coverage_Assessment>{cloud:.2f}</Cloud_Coverage_Assessment>
    <Sun_Zenith_Angle>{sun_z:.2f}</Sun_Zenith_Angle>
    <Snow_Coverage_Assessment>{random.uniform(0.0, 3.0):.2f}</Snow_Coverage_Assessment>
    <Degraded_MSI_Data_Percentage>0.00</Degraded_MSI_Data_Percentage>
    <Geometric_Quality_Status>PASSED</Geometric_Quality_Status>
    <Radiometric_Quality_Status>PASSED</Radiometric_Quality_Status>
  </Quality_Indicators_Info>
</n1:Level-2A_User_Product>
""")
            
            for b in bands_10m:
                with open(os.path.join(granule_img_10m, f"{tile}_{tag[:8]}_{b}"), "w") as f:
                    f.write(f"JPEG2000 raster data mock for {sat} {tile} {b}\nResolution: 10m\nAcquisition: {dt}\n")
            
            for b in bands_20m:
                with open(os.path.join(granule_img_20m, f"{tile}_{tag[:8]}_{b}"), "w") as f:
                    f.write(f"JPEG2000 raster data mock for {sat} {tile} {b}\nResolution: 20m\nAcquisition: {dt}\n")
                    
            with open(os.path.join(granule_qi, "cloud_mask.gml"), "w") as f:
                f.write(f"<!-- Cloud mask polygon GML for {tile} cloud_cov={cloud}% -->\n<gml:FeatureCollection></gml:FeatureCollection>\n")
            with open(os.path.join(granule_qi, "report.xml"), "w") as f:
                f.write(f"<QualityReport scene=\"{safe_name}\" status=\"VALID\" score=\"0.99\"/>\n")


def create_landsat_scenes():
    landsat_dir = os.path.join(BASE_DIR, "landsat_scenes")
    os.makedirs(landsat_dir, exist_ok=True)
    
    scenes = [
        ("LC08_L2SP_190024_20240505_20240515_02_T1", "LANDSAT_8", "2024-05-05", 190, 24, 6.2),
        ("LC09_L2SP_190024_20240513_20240520_02_T1", "LANDSAT_9", "2024-05-13", 190, 24, 12.8),
        ("LC08_L2SP_191024_20240514_20240522_02_T1", "LANDSAT_8", "2024-05-14", 191, 24, 2.1),
        ("LC09_L2SP_191024_20240522_20240530_02_T1", "LANDSAT_9", "2024-05-22", 191, 24, 45.3),
        ("LC08_L2SP_191025_20240601_20240610_02_T1", "LANDSAT_8", "2024-06-01", 191, 25, 8.7),
        ("LC09_L2SP_189024_20240607_20240615_02_T1", "LANDSAT_9", "2024-06-07", 189, 24, 1.4),
    ]
    
    bands = ["SR_B1.TIF", "SR_B2.TIF", "SR_B3.TIF", "SR_B4.TIF", "SR_B5.TIF", "SR_B6.TIF", "SR_B7.TIF", "QA_PIXEL.TIF", "QA_RADSAT.TIF"]
    
    for sname, sat, dt, path, row, cloud in scenes:
        sdir = os.path.join(landsat_dir, sname)
        os.makedirs(sdir, exist_ok=True)
        
        # MTL metadata
        with open(os.path.join(sdir, f"{sname}_MTL.txt"), "w", encoding="utf-8") as f:
            f.write(f"""GROUP = L1_METADATA_FILE
  GROUP = METADATA_FILE_INFO
    ORIGIN = "Image courtesy of the U.S. Geological Survey"
    SPACECRAFT_ID = "{sat}"
    SENSOR_ID = "OLI_TIRS"
    DATE_ACQUIRED = {dt}
    WRS_PATH = {path}
    WRS_ROW = {row}
    CLOUD_COVER = {cloud:.2f}
    CLOUD_COVER_LAND = {cloud:.2f}
    SUN_AZIMUTH = {random.uniform(130.0, 160.0):.4f}
    SUN_ELEVATION = {random.uniform(45.0, 60.0):.4f}
    DATA_TYPE = "L2SP"
  END_GROUP = METADATA_FILE_INFO
END_GROUP = L1_METADATA_FILE
""")
        # ANG file
        with open(os.path.join(sdir, f"{sname}_ANG.txt"), "w") as f:
            f.write(f"# Landsat Viewing and Illumination Angles for {sname}\nBAND01_ANGLE_COEFFICIENTS = 0.12345 0.6789\n")
            
        # Band TIF mocks
        for b in bands:
            with open(os.path.join(sdir, f"{sname}_{b}"), "w") as f:
                f.write(f"GeoTIFF raster data mock for {sat} {b}\n")


def create_telemetry_logs():
    telemetry_dir = os.path.join(BASE_DIR, "telemetry_logs")
    os.makedirs(telemetry_dir, exist_ok=True)
    
    stations = [
        ("SVB", "Spitsbergen_Svalbard", 78.23, 15.39),
        ("KIR", "Kiruna_Sweden", 67.85, 20.96),
        ("MAS", "Maspalomas_Spain", 27.76, -15.63),
        ("KRU", "Kourou_FrenchGuiana", 5.25, -52.80),
        ("TRL", "Troll_Antarctica", -72.01, 2.53),
        ("MAT", "Matera_Italy", 40.65, 16.70),
        ("INU", "Inuvik_Canada", 68.36, -133.72),
        ("PUN", "Punta_Arenas_Chile", -53.16, -70.91)
    ]
    
    satellites = ["SENTINEL-1A", "SENTINEL-1B", "SENTINEL-1C", "SENTINEL-2A", "SENTINEL-2B", "SENTINEL-3A", "SENTINEL-3B", "LANDSAT-8", "LANDSAT-9"]
    statuses = ["OK", "OK", "OK", "OK", "OK", "OK", "OK", "OK", "WARNING_PACKET_LOSS", "WARNING_HIGH_TEMPERATURE", "ERROR_CHECKSUM_FAILED", "ERROR_SIGNAL_LOST", "ERROR_SYNC_FAILED"]
    
    start_date = datetime(2024, 4, 1)
    
    # 45 daily logs for each station = 360 daily log files!
    for day_offset in range(45):
        current_day = start_date + timedelta(days=day_offset)
        day_str = current_day.strftime("%Y-%m-%d")
        
        for code, name, lat, lon in stations:
            log_filename = f"ground_station_{code}_{day_str}.log"
            log_path = os.path.join(telemetry_dir, log_filename)
            
            num_passes = random.randint(14, 30)
            with open(log_path, "w", encoding="utf-8") as f:
                f.write(f"# Telemetry Ground Station Log: {name} (Code: {code})\n")
                f.write(f"# Station Coordinates: Lat {lat:.2f}, Lon {lon:.2f}\n")
                f.write(f"# Log Date: {day_str}\n")
                f.write("# Format: TIMESTAMP_UTC | PASS_ID | SATELLITE_ID | FREQ_GHZ | SNR_DB | BER | PACKETS_RECV | PACKETS_LOST | DOWNLINK_MB | STATUS\n")
                f.write("# ------------------------------------------------------------------------------------------------------------------------\n")
                
                for p in range(1, num_passes + 1):
                    hour = random.randint(0, 23)
                    minute = random.randint(0, 59)
                    second = random.randint(0, 59)
                    ts = f"{day_str}T{hour:02d}:{minute:02d}:{second:02d}Z"
                    pass_id = f"PASS_{code}_{day_str.replace('-','')}_{p:03d}"
                    sat = random.choice(satellites)
                    freq = 8.025 + random.uniform(0.01, 0.45)
                    snr = round(random.uniform(8.5, 24.5), 2)
                    ber = f"1.{random.randint(1,9)}e-{random.randint(5, 9)}"
                    pkts = random.randint(20000, 180000)
                    status = random.choice(statuses)
                    if status == "OK":
                        lost = 0
                    elif "WARNING" in status:
                        lost = random.randint(1, 60)
                    else:
                        lost = random.randint(65, 3500)
                    
                    downlink_mb = round(pkts * 0.00185, 2)
                    
                    f.write(f"{ts} | {pass_id} | {sat:12s} | {freq:.3f} | {snr:5.2f} | {ber:8s} | {pkts:6d} | {lost:4d} | {downlink_mb:7.2f} | {status}\n")

    # Compressed historical monthly archives (.log.gz)
    months = [("2024-01", "January 2024"), ("2024-02", "February 2024"), ("2024-03", "March 2024")]
    for code, name, lat, lon in stations:
        for m_tag, m_name in months:
            gz_filename = f"ground_station_{code}_{m_tag}_archive.log.gz"
            gz_path = os.path.join(telemetry_dir, gz_filename)
            with gzip.open(gz_path, "wt", encoding="utf-8") as f:
                f.write(f"# Monthly Archived Ground Station Log: {name} (Code: {code})\n")
                f.write(f"# Acquisition Month: {m_name} (Historical Archive)\n")
                f.write("# TIMESTAMP_UTC | PASS_ID | SATELLITE_ID | FREQ_GHZ | SNR_DB | BER | PACKETS_RECV | PACKETS_LOST | DOWNLINK_MB | STATUS\n")
                for day in range(1, 29):
                    d_str = f"{m_tag}-{day:02d}"
                    for p in range(1, random.randint(8, 16)):
                        ts = f"{d_str}T{random.randint(0,23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}Z"
                        pass_id = f"PASS_{code}_{d_str.replace('-','')}_{p:03d}"
                        sat = random.choice(satellites)
                        status = random.choice(statuses)
                        pkts = random.randint(15000, 140000)
                        lost = 0 if status == "OK" else random.randint(5, 500)
                        downlink_mb = round(pkts * 0.00185, 2)
                        f.write(f"{ts} | {pass_id} | {sat:12s} | 8.150 | 18.50 | 1.0e-7 | {pkts:6d} | {lost:4d} | {downlink_mb:7.2f} | {status}\n")


def create_cloud_cover_reports():
    reports_dir = os.path.join(BASE_DIR, "cloud_cover_reports")
    os.makedirs(reports_dir, exist_ok=True)
    
    datasets = [
        ("poland_sentinel2_2024.csv", ["T33UWT", "T33UWS", "T34UCA", "T33UXT", "T34UEC", "T34UDE", "T33UVR", "T33UXS"], 2024, 850),
        ("poland_sentinel2_2023.csv", ["T33UWT", "T33UWS", "T34UCA", "T33UXT", "T34UEC", "T34UDE", "T33UVR", "T33UXS"], 2023, 750),
        ("poland_sentinel2_2022.csv", ["T33UWT", "T33UWS", "T34UCA", "T33UXT", "T34UEC", "T34UDE", "T33UVR", "T33UXS"], 2022, 680),
        ("central_europe_sentinel2_2024.csv", ["T33UWT", "T32UNT", "T33UXP", "T34UED", "T32UPU", "T33UVR", "T31TFJ", "T33UXS", "T32UNG"], 2024, 1200),
        ("scandinavia_sentinel2_2024.csv", ["T34VEM", "T33WXS", "T35VNJ", "T34WCD", "T32VNH", "T33WVR", "T34VFN"], 2024, 950),
        ("alps_landsat_sentinel_2024.csv", ["T32TMS", "T32TMR", "T32TLR", "T32TLS", "T32TNS", "T32TMQ"], 2024, 600),
        ("mediterranean_sentinel2_2024.csv", ["T33SUC", "T32SLJ", "T31TEG", "T34SGH", "T33TVN", "T32SKB"], 2024, 1100),
    ]
    
    satellites = ["SENTINEL-2A", "SENTINEL-2B", "LANDSAT-8", "LANDSAT-9"]
    quality_flags = ["PASSED", "PASSED", "PASSED", "PASSED", "PASSED", "PASSED", "SUSPECT_HAZE", "FAILED_CORRUPTION", "PASSED_HIGH_SUN_GLINT"]
    
    for fname, tiles, year, n_records in datasets:
        fpath = os.path.join(reports_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("scene_id,date,satellite,tile_id,orbit_relative,cloud_coverage_percent,nodata_pixel_percent,snow_ice_percent,sun_zenith_angle,quality_flag\n")
            
            for idx in range(1, n_records + 1):
                month = random.randint(1, 12)
                day = random.randint(1, 28)
                hour = random.randint(9, 11)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                d_str = f"{year}-{month:02d}-{day:02d}"
                sat = random.choice(satellites)
                sat_prefix = "S2A" if sat == "SENTINEL-2A" else ("S2B" if sat == "SENTINEL-2B" else ("LC08" if sat == "LANDSAT-8" else "LC09"))
                tile = random.choice(tiles)
                orbit = random.choice([22, 36, 65, 79, 108, 122, 151])
                
                cloud = round(random.betavariate(1.8, 3.5) * 100, 2)
                nodata = round(random.uniform(0.0, 8.5), 2)
                snow = round(random.uniform(0.0, 15.0) if month in [1, 2, 3, 11, 12] else random.uniform(0.0, 0.5), 2)
                sun_zenith = round(20.0 + abs(month - 6.5) * 6.5 + random.uniform(-2.0, 2.0), 2)
                qflag = random.choice(quality_flags)
                
                scene_id = f"{sat_prefix}_MSIL2A_{d_str.replace('-','')}T{hour:02d}{minute:02d}{second:02d}_N0510_R{orbit:03d}_{tile}"
                f.write(f"{scene_id},{d_str},{sat},{tile},{orbit},{cloud},{nodata},{snow},{sun_zenith},{qflag}\n")


def create_orbital_catalog():
    orbit_dir = os.path.join(BASE_DIR, "orbital_catalog")
    os.makedirs(orbit_dir, exist_ok=True)
    
    # satellites_tle_catalog.tsv (80+ satellites)
    tle_path = os.path.join(orbit_dir, "satellites_tle_catalog.tsv")
    with open(tle_path, "w", encoding="utf-8") as f:
        f.write("norad_id\tsatellite_name\toperator\tlaunch_year\tinclination_deg\taltitude_km\tapogee_km\tperigee_km\tperiod_min\torbit_type\tstatus\n")
        satellites_data = [
            (39084, "LANDSAT-8", "USGS/NASA", 2013, 98.22, 705.0, 705.8, 704.2, 98.8, "SSO", "OPERATIONAL"),
            (49260, "LANDSAT-9", "USGS/NASA", 2021, 98.20, 705.0, 705.6, 704.4, 98.8, "SSO", "OPERATIONAL"),
            (39634, "SENTINEL-1A", "ESA", 2014, 98.18, 693.0, 693.5, 692.5, 98.6, "SSO", "OPERATIONAL"),
            (41456, "SENTINEL-1B", "ESA", 2016, 98.18, 693.0, 693.6, 692.4, 98.6, "SSO", "DECOMMISSIONED"),
            (56789, "SENTINEL-1C", "ESA", 2024, 98.18, 693.0, 693.4, 692.6, 98.6, "SSO", "OPERATIONAL"),
            (40697, "SENTINEL-2A", "ESA", 2015, 98.62, 786.0, 786.5, 785.5, 100.6, "SSO", "OPERATIONAL"),
            (42063, "SENTINEL-2B", "ESA", 2017, 98.62, 786.0, 786.7, 785.3, 100.6, "SSO", "OPERATIONAL"),
            (61001, "SENTINEL-2C", "ESA", 2024, 98.62, 786.0, 786.4, 785.6, 100.6, "SSO", "OPERATIONAL"),
            (41335, "SENTINEL-3A", "ESA/EUMETSAT", 2016, 98.65, 814.5, 815.0, 814.0, 101.0, "SSO", "OPERATIONAL"),
            (43437, "SENTINEL-3B", "ESA/EUMETSAT", 2018, 98.65, 814.5, 815.2, 813.8, 101.0, "SSO", "OPERATIONAL"),
            (46826, "SENTINEL-6-MICHAEL-FREILICH", "ESA/NASA/NOAA", 2020, 66.04, 1336.0, 1336.8, 1335.2, 112.4, "NON-SSO", "OPERATIONAL"),
            (25994, "TERRA", "NASA", 1999, 98.20, 705.0, 708.2, 701.8, 98.9, "SSO", "DEGRADED"),
            (27424, "AQUA", "NASA", 2002, 98.20, 705.0, 707.9, 702.1, 98.9, "SSO", "OPERATIONAL"),
            (28485, "AURA", "NASA", 2004, 98.20, 705.0, 708.1, 701.9, 98.9, "SSO", "OPERATIONAL"),
            (37849, "SUOMI-NPP", "NOAA/NASA", 2011, 98.74, 824.0, 824.7, 823.3, 101.4, "SSO", "OPERATIONAL"),
            (43013, "NOAA-20", "NOAA", 2017, 98.74, 824.0, 824.8, 823.2, 101.4, "SSO", "OPERATIONAL"),
            (54234, "NOAA-21", "NOAA", 2022, 98.74, 824.0, 824.6, 823.4, 101.4, "SSO", "OPERATIONAL"),
            (29522, "METOP-A", "EUMETSAT", 2006, 98.70, 817.0, 818.1, 815.9, 101.2, "SSO", "DECOMMISSIONED"),
            (38771, "METOP-B", "EUMETSAT", 2012, 98.70, 817.0, 817.8, 816.2, 101.2, "SSO", "OPERATIONAL"),
            (43689, "METOP-C", "EUMETSAT", 2018, 98.70, 817.0, 817.9, 816.1, 101.2, "SSO", "OPERATIONAL"),
            (53807, "SWOT", "NASA/CNES", 2022, 77.60, 890.0, 891.2, 888.8, 102.8, "NON-SSO", "OPERATIONAL"),
            (44431, "COSMO-SKYMED-2ND-GEN-1", "ASI", 2019, 97.86, 619.0, 620.1, 617.9, 97.2, "SSO", "OPERATIONAL"),
            (51444, "ENMAP", "DLR", 2022, 97.96, 653.0, 654.2, 651.8, 97.8, "SSO", "OPERATIONAL"),
            (44387, "PRISMA", "ASI", 2019, 97.88, 615.0, 616.0, 614.0, 97.0, "SSO", "OPERATIONAL"),
            (49008, "RADARSAT-CONSTELLATION-1", "CSA", 2019, 97.74, 593.0, 593.8, 592.2, 96.5, "SSO", "OPERATIONAL"),
            (49009, "RADARSAT-CONSTELLATION-2", "CSA", 2019, 97.74, 593.0, 593.7, 592.3, 96.5, "SSO", "OPERATIONAL"),
            (49010, "RADARSAT-CONSTELLATION-3", "CSA", 2019, 97.74, 593.0, 593.9, 592.1, 96.5, "SSO", "OPERATIONAL"),
            (39265, "ALOS-2", "JAXA", 2014, 97.90, 628.0, 628.6, 627.4, 97.4, "SSO", "OPERATIONAL"),
            (59899, "ALOS-4", "JAXA", 2024, 97.90, 628.0, 628.5, 627.5, 97.4, "SSO", "OPERATIONAL"),
            (43054, "FLEX", "ESA", 2025, 98.62, 814.0, 814.6, 813.4, 101.1, "SSO", "PLANNED"),
            (47345, "BIOMASS", "ESA", 2025, 98.00, 666.0, 666.5, 665.5, 98.1, "SSO", "PLANNED")
        ]
        
        # Add commercial Earth Observation constellations (Planet, ICEYE, Spire)
        for i in range(1, 26):
            satellites_data.append((70000 + i, f"PLANETSCOPE-FLOCK-{i:02d}", "PLANET", 2023, 97.45, 475.0, 476.2, 473.8, 94.1, "SSO", "OPERATIONAL"))
        for i in range(1, 16):
            satellites_data.append((80000 + i, f"ICEYE-SAR-X{i:02d}", "ICEYE", 2023, 97.68, 560.0, 561.0, 559.0, 95.8, "SSO", "OPERATIONAL"))
        for i in range(1, 16):
            satellites_data.append((90000 + i, f"SPIRE-LEMUR-2-{i:02d}", "SPIRE", 2024, 97.50, 500.0, 501.2, 498.8, 94.6, "SSO", "OPERATIONAL"))
            
        for row in satellites_data:
            f.write("\t".join(str(x) for x in row) + "\n")

    # sensor_bands_spec.tsv
    bands_path = os.path.join(orbit_dir, "sensor_bands_spec.tsv")
    with open(bands_path, "w", encoding="utf-8") as f:
        f.write("sensor\tband_id\tband_name\tcentral_wavelength_nm\tbandwidth_nm\tspatial_res_m\tspectrum_region\n")
        bands_data = [
            ("MSI-Sentinel-2", "B01", "Coastal Aerosol", 443, 20, 60, "VNIR"),
            ("MSI-Sentinel-2", "B02", "Blue", 490, 65, 10, "VNIR"),
            ("MSI-Sentinel-2", "B03", "Green", 560, 35, 10, "VNIR"),
            ("MSI-Sentinel-2", "B04", "Red", 665, 30, 10, "VNIR"),
            ("MSI-Sentinel-2", "B05", "Vegetation Red Edge 1", 705, 15, 20, "VNIR"),
            ("MSI-Sentinel-2", "B06", "Vegetation Red Edge 2", 740, 15, 20, "VNIR"),
            ("MSI-Sentinel-2", "B07", "Vegetation Red Edge 3", 783, 20, 20, "VNIR"),
            ("MSI-Sentinel-2", "B08", "NIR Broad", 842, 115, 10, "VNIR"),
            ("MSI-Sentinel-2", "B8A", "NIR Narrow", 865, 20, 20, "VNIR"),
            ("MSI-Sentinel-2", "B09", "Water Vapour", 945, 20, 60, "SWIR"),
            ("MSI-Sentinel-2", "B10", "SWIR Cirrus", 1375, 30, 60, "SWIR"),
            ("MSI-Sentinel-2", "B11", "SWIR 1", 1610, 90, 20, "SWIR"),
            ("MSI-Sentinel-2", "B12", "SWIR 2", 2190, 180, 20, "SWIR"),
            ("OLI-Landsat-8/9", "B1", "Coastal Aerosol", 443, 16, 30, "VNIR"),
            ("OLI-Landsat-8/9", "B2", "Blue", 482, 60, 30, "VNIR"),
            ("OLI-Landsat-8/9", "B3", "Green", 561, 57, 30, "VNIR"),
            ("OLI-Landsat-8/9", "B4", "Red", 655, 37, 30, "VNIR"),
            ("OLI-Landsat-8/9", "B5", "Near Infrared", 865, 28, 30, "VNIR"),
            ("OLI-Landsat-8/9", "B6", "SWIR 1", 1609, 85, 30, "SWIR"),
            ("OLI-Landsat-8/9", "B7", "SWIR 2", 2201, 187, 30, "SWIR"),
            ("OLI-Landsat-8/9", "B8", "Panchromatic", 590, 172, 15, "VNIR"),
            ("OLI-Landsat-8/9", "B9", "Cirrus", 1373, 20, 30, "SWIR"),
            ("TIRS-Landsat-8/9", "B10", "Thermal Infrared 1", 10895, 590, 100, "TIR"),
            ("TIRS-Landsat-8/9", "B11", "Thermal Infrared 2", 12005, 1010, 100, "TIR")
        ]
        for row in bands_data:
            f.write("\t".join(str(x) for x in row) + "\n")


def create_gnss_stations():
    gnss_dir = os.path.join(BASE_DIR, "gnss_stations")
    os.makedirs(gnss_dir, exist_ok=True)
    
    stations = [
        ("WROC", "Wroclaw_University_of_Environmental_and_Life_Sciences", 51.113, 17.062, 145.2),
        ("JOZE", "Jozefoslaw_Astrogeodynamical_Observatory", 52.097, 21.031, 140.5),
        ("KRAK", "Krakow_AGH", 50.066, 19.920, 260.8),
        ("GDAN", "Gdansk_Technical_University", 54.371, 18.618, 48.0),
        ("LODZ", "Lodz_Technical_University", 51.753, 19.453, 230.1),
        ("POZN", "Poznan_Space_Research_Centre_PAS", 52.395, 16.925, 85.4),
        ("KATW", "Katowice_Silesia_Observatory", 50.259, 19.021, 290.3),
        ("BIAY", "Bialystok_Technical_University", 53.118, 23.149, 160.2),
        ("SZCZ", "Szczecin_West_Pomeranian_University", 53.447, 14.538, 55.6),
        ("ZAKO", "Zakopane_Tatra_Station", 49.299, 19.951, 850.4),
        ("BOR1", "Borowiec_Astrogeodynamic_Observatory", 52.277, 17.073, 122.3),
        ("GOPE", "Ondrejov_Geodetic_Observatory_Czechia", 49.914, 14.786, 592.6),
        ("POTS", "Potsdam_GFZ_Germany", 52.381, 13.068, 97.1),
        ("WTZR", "Wettzell_Geodetic_Observatory_Germany", 49.144, 12.878, 665.8),
        ("ONSA", "Onsala_Space_Observatory_Sweden", 57.395, 11.926, 45.3)
    ]
    
    for code, full_name, lat, lon, height in stations:
        st_dir = os.path.join(gnss_dir, code)
        os.makedirs(st_dir, exist_ok=True)
        
        # station_info.json
        with open(os.path.join(st_dir, "station_info.json"), "w", encoding="utf-8") as f:
            f.write(f"""{{
  "marker_name": "{code}",
  "description": "{full_name}",
  "network": "ASG-EUPOS / EPN",
  "coordinates": {{
    "latitude_deg": {lat},
    "longitude_deg": {lon},
    "ellipsoidal_height_m": {height}
  }},
  "receiver_type": "TRIMBLE ALLOY",
  "antenna_type": "TRM59800.00 NONE",
  "status": "OPERATIONAL"
}}
""")
        # Daily observation log
        log_path = os.path.join(st_dir, f"{code}_2024_daily_status.log")
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"# Daily Station QC Log for {code} ({full_name})\n")
            f.write("DATE\tEPOCHS_EXPECTED\tEPOCHS_RECORDED\tDATA_COMPLETENESS_PCT\tCYCLE_SLIPS\tMP1_CM\tMP2_CM\tQC_STATUS\n")
            for day in range(1, 31):
                d_str = f"2024-05-{day:02d}"
                exp = 2880
                rec = random.randint(2840, 2880)
                comp = round((rec / exp) * 100, 2)
                slips = random.randint(0, 18)
                mp1 = round(random.uniform(12.0, 32.0), 1)
                mp2 = round(random.uniform(15.0, 38.0), 1)
                qc = "GOOD" if comp > 98.5 and mp1 < 28.0 else ("FAIR" if comp > 95.0 else "POOR")
                f.write(f"{d_str}\t{exp}\t{rec}\t{comp}\t{slips}\t{mp1}\t{mp2}\t{qc}\n")
                
        # Compressed RINEX mock
        for d in [130, 135, 140]:
            rnx_path = os.path.join(st_dir, f"{code}00POL_R_2024{d}0000_01D_30S_MO.rnx.gz")
            with gzip.open(rnx_path, "wt", encoding="utf-8") as f:
                f.write(f"     3.04           OBSERVATION DATA    M (Mixed)           RINEX VERSION / TYPE\n")
                f.write(f"sbf2rin-v13.6.0     UPWr GNSS Group     20240515 000500 UTC PGM / RUN BY / DATE\n")
                f.write(f"{code}                                                        MARKER NAME\n")
                f.write(f"GPS + GLONASS + GALILEO + BEIDOU tracking records mock data DOY {d}\n")
                for i in range(50):
                    f.write(f"> 2024 05 15 00 00 {i*30:02d}.0000000  0 32\n")
                    f.write(f"G01  22345678.123 4  -12345.678 8   45.200\n")
                    f.write(f"E02  24567890.456 8  -23456.789 7   48.500\n")


def create_raw_telemetry_chunks():
    chunks_dir = os.path.join(BASE_DIR, "raw_telemetry_chunks")
    os.makedirs(chunks_dir, exist_ok=True)
    
    # Generate 500 telemetry chunk files to demonstrate powers of find, xargs, wc, grep over thousands of files
    for chunk_id in range(1, 501):
        cname = f"telemetry_stream_chunk_{chunk_id:04d}.dat"
        cpath = os.path.join(chunks_dir, cname)
        with open(cpath, "w", encoding="utf-8") as f:
            f.write(f"# RAW TELEMETRY PACKET STREAM CHUNK #{chunk_id:04d}\n")
            f.write(f"HEADER: CCSDS_SYNC=0x1ACFFC1D STREAM_ID={chunk_id:04d} BITRATE_MBPS=150.0\n")
            n_packets = random.randint(20, 60)
            for p in range(1, n_packets + 1):
                crc_status = "CRC_OK" if random.random() > 0.05 else "CRC_ERR"
                temp = round(random.uniform(15.0, 38.0), 2)
                volt = round(random.uniform(27.8, 28.6), 2)
                f.write(f"PKT_{chunk_id:04d}_{p:03d} | V={volt}V | T={temp}C | {crc_status}\n")


def create_scripts_repo():
    scripts_dir = os.path.join(BASE_DIR, "scripts_repo")
    os.makedirs(scripts_dir, exist_ok=True)
    
    with open(os.path.join(scripts_dir, "filter_clouds.sh"), "w", encoding="utf-8") as f:
        f.write("""#!/usr/bin/env bash

# Skrypt: filter_clouds.sh
# Opis: Filtruje raport zachmurzenia według zadanego kafelka MGRS i maksymalnego dopuszczalnego zachmurzenia.
# Użycie: bash filter_clouds.sh <plik_raportu.csv> <kafelek_MGRS> <max_cloud_percent>

REPORT="$1"
TILE="$2"
MAX_CLOUD="$3"

echo "Filtrowanie scen dla kafelka: $TILE w pliku $REPORT (Max zachmurzenie: ${MAX_CLOUD}%)"
grep "$TILE" "$REPORT" | awk -F',' -v max="$MAX_CLOUD" '$6 <= max {print $1, "Data:", $2, "Zachmurzenie:", $6"%"}'
""")

    with open(os.path.join(scripts_dir, "count_telemetry_errors.sh"), "w", encoding="utf-8") as f:
        f.write("""#!/usr/bin/env bash

# Skrypt: count_telemetry_errors.sh
# Opis: Zlicza błędy w logach wybranej stacji naziemnej.
# Użycie: bash count_telemetry_errors.sh <kod_stacji_np_SVB>

STATION="$1"
echo "Analiza błędów telemetrycznych dla stacji: $STATION"

grep "ERROR" telemetry_logs/ground_station_${STATION}_*.log 2>/dev/null | wc -l
""")

    with open(os.path.join(scripts_dir, "batch_qc_check.sh"), "w", encoding="utf-8") as f:
        f.write("""#!/usr/bin/env bash

# Skrypt: batch_qc_check.sh
# Opis: Wyszukuje wszystkie uszkodzone pakiety w surowych strumieniach danych telemetrycznych.
# Użycie: bash batch_qc_check.sh

echo "=== Rozpoczecie kontroli jakosci (QC) strumieni telemetrycznych ==="
total_chunks=$(ls raw_telemetry_chunks/*.dat | wc -l)
total_errors=$(grep -c "CRC_ERR" raw_telemetry_chunks/*.dat 2>/dev/null | grep -v ":0$" | wc -l)

echo "Przeanalizowano plikow chunk: $total_chunks"
echo "Liczba plikow zawierajacych bledy CRC: $total_errors"
""")


def package_zip():
    zip_output = os.path.join(os.path.dirname(BASE_DIR), "dane_do_cwiczen.zip")
    with zipfile.ZipFile(zip_output, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(BASE_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, os.path.dirname(BASE_DIR))
                zipf.write(file_path, rel_path)
    print(f"Utworzono archiwum: {zip_output}")


if __name__ == "__main__":
    print("Generowanie rozszerzonego zestawu danych satelitarnych w 'dane_do_cwiczen'...")
    create_readme_and_sources()
    create_sentinel2_scenes()
    create_landsat_scenes()
    create_telemetry_logs()
    create_cloud_cover_reports()
    create_orbital_catalog()
    create_gnss_stations()
    create_raw_telemetry_chunks()
    create_scripts_repo()
    package_zip()
    print("Gotowe! Wszystkie pliki zostały pomyślnie wygenerowane.")
