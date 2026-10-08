---
pagetitle: "Ściągawka z poleceń Unix"
---

# Ściągawka z poleceń Unix (Cheat sheet) {.unnumbered}

Niniejszy dokument zawiera podsumowanie najważniejszych poleceń powłoki Unix.  
Wartości w nawiasach klamrowych `{...}` oznaczają parametry podawane przez użytkownika (samych nawiasów klamrowych nie wpisujemy w poleceniu).

## Pomoc i dokumentacja

|||
| :---- | :---- |
| `man {polecenie}` | Strona podręcznika systemowego dla danego programu |
| `whatis {polecenie}` | Krótki, jednozdaniowy opis programu |
| `{polecenie} --help` | Wyświetlenie pomocy i listy dostępnych opcji/flag |

## Wyświetlanie zawartości katalogów (`ls`)

|||
| :---- | :---- |
| `ls` | Wypisanie plików i folderów w bieżącym katalogu |
| `ls {sciezka}` | Wypisanie zawartości wskazanego katalogu |
| `ls -l {sciezka}` | Wyświetlenie szczegółowych informacji (uprawnienia, rozmiar, data modyfikacji) |
| `ls -a {sciezka}` | Wyświetlenie wszystkich plików (w tym plików ukrytych zaczynających się od kropki `.`) |
| `ls -lh {sciezka}` | Wyświetlenie rozmiarów w czytelnym formacie (*human-readable*, np. KB, MB, GB) |

## Nawigacja po systemie plików (`cd`, `pwd`)

|||
| :---- | :---- |
| `cd {sciezka}` | Przejście do wskazanego katalogu |
| `cd` lub `cd ~` | Powrót do katalogu domowego użytkownika |
| `cd ..` | Przejście o jeden poziom wyżej (do katalogu nadrzędnego) |
| `pwd` | Wypisanie pełnej ścieżki bieżącego katalogu roboczego (*print working directory*) |

## Tworzenie i usuwanie katalogów

|||
| :---- | :---- |
| `mkdir {katalog}` | Utworzenie nowego katalogu |
| `mkdir -p {sciezka/zagniezdzona}` | Utworzenie zagnieżdżonej struktury katalogów wraz z brakującymi folderami nadrzędnymi |
| `rmdir {katalog}` | Usunięcie pustego katalogu |
| `rm -r {katalog}` | Rekurencyjne usunięcie katalogu wraz z całą jego zawartością (**uwaga: operacja nieodwracalna**) |

## Kopiowanie, przenoszenie i usuwanie plików

|||
| :---- | :---- |
| `cp {zrodlo} {katalog_docelowy/}` | Skopiowanie pliku do wskazanego katalogu z zachowaniem nazwy |
| `cp {zrodlo} {nowy_plik}` | Skopiowanie pliku pod nową nazwą |
| `cp -r {katalog_zrodlowy} {katalog_docelowy}` | Skopiowanie całego katalogu rekurencyjnie |
| `mv {zrodlo} {katalog_docelowy/}` | Przeniesienie pliku do wskazanego katalogu |
| `mv {stara_nazwa} {nowa_nazwa}` | Zmiana nazwy pliku lub katalogu |
| `rm {plik}` | Trwałe usunięcie pliku |

## Przeglądanie i analiza plików tekstowych

|||
| :---- | :---- |
| `less {plik}` | Interaktywne przeglądanie pliku strona po stronie (<kbd>Q</kbd> wyjście, <kbd>/</kbd> szukanie) |
| `head {plik}` | Wyświetlenie pierwszych 10 linii pliku |
| `head -n {N} {plik}` | Wyświetlenie pierwszych N linii pliku |
| `tail {plik}` | Wyświetlenie ostatnich 10 linii pliku |
| `tail -n {N} {plik}` | Wyświetlenie ostatnich N linii pliku |
| `cat {plik}` | Wypisanie całej zawartości pliku do terminala |
| `cat {plik1} {plik2} > {scalony}` | Połączenie zawartości kilku plików w jeden |
| `wc -l {plik}` | Zliczenie liczby wierszy w pliku |
| `zcat {plik.gz}` | Strumieniowe odczytanie pliku skompresowanego (w macOS: `gzcat`) |

## Wyszukiwanie wzorców (`grep`)

|||
| :---- | :---- |
| `grep "{wzorzec}" {plik}` | Wyświetlenie wierszy zawierających podany wzorzec tekstowy |
| `grep -i "{wzorzec}" {plik}` | Wyszukiwanie bez rozróżniania wielkości liter (*case-insensitive*) |
| `grep -v "{wzorzec}" {plik}` | Odwrócenie dopasowania (wyświetlenie wierszy **niezawierających** wzorca) |
| `grep -r "{wzorzec}" {katalog}` | Rekurencyjne przeszukanie wszystkich plików w katalogu |

## Symbole wieloznaczne (Wildcards)

|||
| :---- | :---- |
| `*` | Dopasowanie dowolnego ciągu znaków (zero lub więcej) |
| `?` | Dopasowanie dokładnie jednego znaku |
| `ls *.tif` | Wylistowanie wszystkich plików rastrowych `.tif` |
| `ls S2A_*.nc` | Wylistowanie plików netCDF misji Sentinel-2A |

## Przekierowania i potoki

|||
| :---- | :---- |
| `{polecenie} > {plik}` | Przekierowanie standardowego wyjścia (`stdout`) do pliku (nadpisanie) |
| `{polecenie} >> {plik}` | Dopisywanie standardowego wyjścia na końcu pliku (*append*) |
| `{polecenie} 2> {plik}` | Przekierowanie strumienia błędów (`stderr`) do pliku |
| `{polecenie} > {plik} 2>&1` | Przekierowanie zarówno `stdout`, jak i `stderr` do jednego pliku |
| `{polecenie1} \| {polecenie2}` | Przekazanie wyjścia `polecenie1` jako wejścia do `polecenie2` |
| `cat *.csv \| cut -d "," -f 2 \| sort \| uniq -c` | Ekstrakcja kolumny, posortowanie i zliczenie unikalnych wartości |
