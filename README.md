![Icon](Icon_with_Text.png)
# XTwist Explorer

**XTwist Explorer** ist eine interaktive Python-Anwendung zur Analyse und Visualisierung von Pseudozufallszahlengeneratoren (PRNGs).  
Der Name leitet sich aus den beiden untersuchten Algorithmen – **XOR-Shift** und **Mersenne Twister** – ab und unterstreicht den explorativen Charakter der Software.  

Die Anwendung wurde entwickelt, um die Funktionsweise dieser Generatoren **visuell nachvollziehbar und didaktisch verständlich** zu machen.  
Sie bietet eine intuitive Benutzeroberfläche, in der sich Parameter, Seeds und Visualisierungseinstellungen dynamisch anpassen lassen.


## Hauptfunktionen

- **Drie Analyse-Tabs:**  
  - **Mersenne Twister** – Visualisierung des Seed- und Twisted-Arrays  
  - **XOR-Shift Generator** – Schritt-für-Schritt-Darstellung der Bit-Transformationen  
  - **Linear Congruential Generator**

- **Interaktive Visualisierungen:**  
  - Histogramm zur Prüfung der Gleichverteilung  
  - 2D- und 3D-Streudiagramme zur Erkennung von Korrelationen  
  - Autokorrelationsdiagramm über mehrere Lags  

- **Benutzerdefinierte Steuerung:**  
  - Anpassbare Sample Size, Bins und Seed  
  - Dynamischer Wechsel zwischen 2D und 3D  
  - Parametersteuerung (a, b, c) für den XOR-Shift  

- **Didaktische Visualisierung:**  
  - Farbcodierte Bitveränderungen (Rot, Grün, Blau)  
  - Hervorhebung der Zustandsabhängigkeiten im Mersenne Twister  

---

## ⚙️ Technische Grundlage

- **Sprache:** Python  
- **GUI:** Tkinter & CustomTkinter  
- **Bibliotheken:** NumPy, Matplotlib, SciPy 

## 🚀 Mögliche Erweiterungen

- Exportfunktionen für Daten und Diagramme (CSV, JSON, PNG)  
- Optimierte UI-Performance bei komplexen Visualisierungen  
- Interaktive Zustandsarrays mit Highlighting bei Klick  
- Erweiterte Einstellungsoptionen (Lag, Anzeigegröße, etc.)  
- Animierte Schritt-für-Schritt-Darstellungen  


## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.  
Frei zur Nutzung, Modifikation und Weiterentwicklung – mit Namensnennung.