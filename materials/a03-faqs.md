---
pagetitle: "Często zadawane pytania (FAQ)"
---

# Często zadawane pytania (FAQ) {.unnumbered}

::: {.callout-tip}
#### Wprowadzenie
W tym dokumencie zebrano odpowiedzi na najczęstsze pytania i wątpliwości pojawiające się podczas nauki wiersza poleceń powłoki Unix.
:::

## Podstawy powłoki

### Czym różni się jądro systemu (kernel) od powłoki (shell)?
**Jądro (kernel)** to centralny komponent systemu operacyjnego zarządzający sprzętem (procesorem, pamięcią, dyskami, kartami sieciowymi).  
**Powłoka (shell)** to interpreter wiersza poleceń stanowiący interfejs pośredniczący między użytkownikiem a jądrem systemu.

### Jakie są najpopularniejsze powłoki Unix?
- **Bash** (*Bourne Again SHell*) – domyślny standard w większości dystrybucji Linuksa.
- **Zsh** (*Z Shell*) – domyślna powłoka w nowszych wersjach systemu macOS, w pełni kompatybilna z większością składni Basha.
- **Sh** (*Bourne Shell*) – pierwotna, minimalistyczna powłoka uniksowa.

## Składnia, skróty klawiszowe i rozwiązywanie problemów

### Co zrobić, gdy polecenie „zawiesiło się” lub trwa zbyt długo?
Naciśnij kombinację klawiszy <kbd>Ctrl</kbd> + <kbd>C</kbd>. Spowoduje to natychmiastowe przerwanie bieżącego procesu (wysłanie sygnału `SIGINT`) i powrót do znaku zachęty powłoki.

### Jak wyczyścić ekran terminala?
Naciśnij skrót <kbd>Ctrl</kbd> + <kbd>L</kbd> lub wpisz polecenie `clear`.

### Jak działa autouzupełnianie nazw plików i katalogów?
Wpisz pierwsze litery nazwy i naciśnij klawisz <kbd>Tab ⇥</kbd>. Dwukrotne naciśnięcie <kbd>Tab ⇥</kbd> wyświetli wszystkie pasujące nazwy. Pamiętaj, że w systemie Unix wielkość liter ma znaczenie (*case-sensitive*).

### Jak przywołać wcześniej wpisywane polecenia?
Naciskaj strzałkę w górę <kbd>↑</kbd> na klawiaturze. Możesz także przeszukiwać historię poleceń za pomocą skrótu <kbd>Ctrl</kbd> + <kbd>R</kbd>.

### Dlaczego w projektach informatycznych zaleca się stosowanie ścieżek względnych?
Stosowanie ścieżek względnych (*relative paths*) wewnątrz katalogu projektu sprawia, że cały projekt staje się **przenośny (portable)**:
- Jeśli cały folder projektu zostanie skopiowany na inny dysk, inny serwer obliczeniowy lub pobrany przez współpracownika z repozytorium Git, wszystkie skrypty i potoki przetwarzania będą działać bez konieczności poprawiania zakodowanych na sztywno ścieżek (np. `/home/jan/...`).

## Operacje na plikach i danych

### Czy pliki usunięte poleceniem `rm` trafiają do kosza?
Nie. Polecenie `rm` bezpowrotnie usuwa wskaźniki do plików w systemie plików. W wierszu poleceń nie ma kosza systemowego (*Trash / Recycle Bin*). Dlatego operacji `rm` (a w szczególności `rm -r`) należy używać z dużą rozwagą.

### Jaka jest różnica między operatorami `>` a `>>`?
- Operator `>` **nadpisuje** plik docelowy (tworzy nowy lub usuwa dotychczasową zawartość).
- Operator `>>` **dopisuje** nowe wiersze na końcu istniejącego pliku (*append*).

### Czym różni się sortowanie `sort -n` od domyślnego `sort`?
Domyślne polecenie `sort` sortuje ciągi alfabetycznie (leksykograficznie), przez co wartość `100` znajdzie się przed `2`. Flaga `-n` wymusza interpretację i porządkowanie wartości jako liczb (*numeric sort*).
