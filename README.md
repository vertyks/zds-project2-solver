# 📄 ZDS Project 2. Solver

Tento skript slouží jako **Solver** pro automatický výpočet úloh spojených s **Q-formátem (pevnou řádovou čárkou)**. Je navržen specificky pro usnadnění práce na **Projektu č. 2** v předmětu **Zpracování dat a signálů (ZDS)** na **VŠB – Technické univerzitě Ostrava**.

## 🚀 Požadavky

* Python 3.x
* Přístup do LMS (pro zadání hodnot z testu)

## 🎯 Použití

1.  **Spusťte program** v terminálu nebo příkazovém řádku:
    ```bash
    python solver.py
    ```

2.  **Zadejte Q formát** podle zadání v LMS (např. `Q12.16`, `12.16` nebo `12,16`).

3.  **Vložte reálná čísla** z testu, když vás k tomu program vyzve.

## 🛠️ Funkce programu

Skript automaticky provede následující operace:
* ✅ **Převod na Hex:** Převede reálná čísla do hexadecimálního formátu s pevnou řádovou čárkou.
* 🔄 **Logika pro záporná čísla:** Aplikuje specifickou transformaci pro záporné hodnoty (prohození bajtů a inkrementace), která je vyžadována v zadání projektu.
* ➕ **Součet a Rozdíl:** Vypočítá součet a rozdíl čísel přímo v Hex formátu.
* 📊 **Kontrola výsledku:** Zobrazí zpětný převod výsledků na reálná čísla pro ověření správnosti.

## ⚠️ Důležité upozornění

Tento nástroj je pomůcka pro studijní účely v rámci předmětu ZDS na **lms.vsb.cz**. Výpočty jsou přesně přizpůsobeny konkrétní logice vyžadované tímto systémem na specifický typ příkladů v tomto projektu.

---
**Autor:** [github.com/vertyks](https://github.com/vertyks)