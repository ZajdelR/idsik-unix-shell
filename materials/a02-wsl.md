---
pagetitle: "Unix w systemie Windows (WSL)"
---

# Unix w systemie Windows (WSL) {.unnumbered}

W rozdziale [Dane i przygotowanie środowiska](../../setup.md) rekomendowaliśmy instalację programu _MobaXterm_ jako prostego sposobu na uruchomienie powłoki w systemie Windows.  
Choć *MobaXterm* jest wygodny w konfiguracji, nie stanowi pełnego środowiska Linux. Jeśli w pracy inżynierskiej chcesz korzystać ze specjalistycznego oprogramowania natywnie linuksowego (narzędzia teledetekcyjne, GDAL, biblioteki przetwarzania danych satelitarnych i uczenia maszynowego), idealnym rozwiązaniem jest **Windows Subsystem for Linux (WSL2)**.

WSL2 to oficjalna technologia firmy Microsoft dla Windows 10 i 11, pozwalająca uruchamiać prawdziwe jądro Linuksa (*Ubuntu*) bezpośrednio obok systemu Windows, z bezpośrednim dostępem do plików na dyskach Windows.

## Instalacja WSL2

Szczegółowy podręcznik znajduje się na [stronie dokumentacji Microsoft](https://learn.microsoft.com/pl-pl/windows/wsl/install).  
Krótka instrukcja:

1. Wyszukaj w menu Start aplikację **PowerShell**, kliknij prawym przyciskiem myszy i wybierz **Uruchom jako administrator**.
2. W oknie PowerShell wpisz polecenie:
   ```powershell
   wsl --install
   ```
3. Po zakończeniu pobierania i instalacji uruchom ponownie komputer (*Restart*).
4. Po ponownym uruchomieniu otworzy się okno terminala Ubuntu z prośbą o utworzenie nazwy użytkownika (*username*) i hasła (*password*).
   - *Uwaga:* Podczas wpisywania hasła w terminalu znaki nie pojawiają się na ekranie (jest to standardowe zabezpieczenie w Linuksie). Wpisz hasło i naciśnij <kbd>Enter</kbd>.

## Dostęp do dysków Windows z poziomu WSL2

Główny dysk systemowy Windows `C:\` jest dostępny w WSL pod ścieżką `/mnt/c/`.  
Aby ułatwić sobie nawigację, możesz utworzyć dowiązania symboliczne (*symlinks*) do swoich folderów Pulpitu i Dokumentów:

```bash
ln -s $(wslpath $(powershell.exe '[environment]::getfolderpath("MyDocuments")' | tr -d '\r')) ~/Documents
ln -s $(wslpath $(powershell.exe '[environment]::getfolderpath("Desktop")' | tr -d '\r')) ~/Desktop
```

## Integracja z Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com/) doskonale integruje się z WSL2.

1. Pobierz i zainstaluj VS Code w systemie Windows.
2. Zainstaluj w VS Code rozszerzenie **WSL** (od Microsoftu).
3. Będąc w terminalu WSL w wybranym katalogu projektu, wpisz:
   ```bash
   code .
   ```
   VS Code otworzy się w środowisku Windows, ale będzie bezpośrednio edytować pliki i uruchamiać procesy wewnątrz Linuksa WSL.
