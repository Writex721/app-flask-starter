# Vyhodnocení splnění úkolů 1-7

Datum: 7. května 2026

---

## Úkol 1: Spuštění aplikace lokálně

**Požadavky:**
- [ ] Instalace závislostí
- [ ] Spuštění příkazem `python app.py`
- [ ] Otevření v prohlížeči na `http://127.0.0.1:5000`
- [ ] Stránka se zobrazí bez chyby
- [ ] Funguje formulář se jménem a pozdravem

**Aktuální stav kódu:**
✅ `requirements.txt` obsahuje `Flask` a `gunicorn`
✅ `app.py` je správně strukturován s Flask aplikací
✅ Route `/` existuje a vrací šablonu
✅ Formulář v `templates/page.html` existuje a má vstupní pole

**Výsledek: ✅ SPLNĚNO**

---

## Úkol 2: Git a veřejný repozitář

**Požadavky:**
- [ ] Inicializace Gitu
- [ ] Vytvoření prvního commitu
- [ ] Veřejný repozitář na GitHubu
- [ ] Propojení a push změn

**Aktuální stav:**
⚠️ **NELZE OVĚŘIT Z KÓDU** – Jedná se o Git operace mimo zdrojový kód. Vyžaduje ověření v GitHub repozitáři.

**Výsledek: ⚠️ NELZE OVĚŘIT (Vyžaduje ověření v Git historii a GitHub)**

---

## Úkol 3: Nasazení na Render.com

**Požadavky:**
- [ ] Vytvoření webové služby na Render
- [ ] Správné nastavení Root directory, Build a Start commands
- [ ] Aplikace běží na veřejné URL
- [ ] Formulář funguje stejně

**Aktuální stav kódu:**
✅ `README.md` obsahuje správné instrukce pro Render
✅ `requirements.txt` je připraven pro instalaci
✅ Build command: `pip install -r requirements.txt` – ✅ správně
✅ Start command: `gunicorn app:app` – ✅ správně

**Výsledek: ⚠️ PŘIPRAVENO, ALE NELZE OVĚŘIT (Vyžaduje test nasazení na Render)**

---

## Úkol 4: Rozšíření formuláře o příjmení (GET)

**Požadavky:**
- [ ] Druhé pole formuláře pro příjmení
- [ ] Načtení obou parametrů přes `request.args.get(...)`
- [ ] Pozdrav ve tvaru: "Jméno Příjmení, rád tě vidím!"
- [ ] Jméno a příjmení se zobrazují v URL

**Aktuální stav kódu:**
✅ `page.html` má pole pro `name` a `surname`
✅ Formulář používá `method="GET"`
✅ `app.py` čte oba parametry: `request.args.get("name")` a `request.args.get("surname")`
✅ Pozdrav má správný formát: `{{ name }} {{ surname }}, rád tě vidím!`
✅ Data se v GET metodě automaticky zobrazují v URL

**Výsledek: ✅ SPLNĚNO**

---

## Úkol 5: Přechod z GET na POST

**Požadavky:**
- [ ] Nová route `/pozdrav-post`
- [ ] Nová šablona `templates/pozdrav_post.html`
- [ ] Formulář s `method="POST"`
- [ ] Route povoluje GET i POST
- [ ] Data se čtou přes `request.form`
- [ ] Data nejsou vidět v URL

**Aktuální stav kódu:**
✅ Route `/pozdrav-post` existuje
✅ Šablona `templates/pozdrav_post.html` existuje
✅ Formulář má `method="POST"`
✅ Route má `methods=["POST", "GET"]`
✅ Data se čtou: `request.form.get("name")`, `request.form.get("surname")`, `request.form.get("password")`
✅ POST metodou se data nezobrazují v URL

**Výsledek: ✅ SPLNĚNO**

---

## Úkol 6: Zadání hesla a tajná informace

**Požadavky:**
- [ ] Pole pro heslo (`type="password"`)
- [ ] Porovnání hesla s hodnotou v proměnné
- [ ] Zobrazení tajné informace při správném hesle
- [ ] Zobrazení chybové hlášky při špatném hesle

**Aktuální stav kódu:**
✅ Formulář má `<input type="password" name="password">`
✅ Heslo se porovnává: `if password == "tajneheslo"`
✅ Správné heslo → `zprava="Uhodl jsi heslo!"`
✅ Špatné heslo → `zprava="Error - špatné heslo"`

✅ **LOGIKA JE SPRÁVNÁ:**
```python
if check:  # Heslo se kontroluje POUZE když je check == True (jméno OK)
    if password == "tajneheslo" and check==True:
        zprava="Uhodl jsi heslo!"
    else:
        zprava="Error - špatné heslo"
```

→ Když jméno není validní, heslo se vůbec nekontroluje, `zprava` zůstane na " " (skrytá)

**Výsledek: ✅ SPLNĚNO**

---

## Úkol 7: Validace vstupů

**Požadavky:**
- [ ] Ošetření prázdného jména
- [ ] Omezení délky jména na 50 znaků
- [ ] Srozumitelné chybové zprávy

**Aktuální stav kódu (OPRAVENO):**
✅ Kontrola prázdného jména: `if not name:`
✅ Omezení délky: `elif len(name) > 50:`
✅ Chybové zprávy: "Error - nelze nezadat jméno" a "Error - jméno je příliš dlouhé"
✅ Inicializace `zprava_jmeno=" "` – správně (prázdný/skrytý obsah)
✅ Inicializace `zprava=" "` – správně (prázdný/skrytý obsah)
✅ **Logika je správná** – heslo se kontroluje jen když je `check == True` (jméno je OK)

**Tok aplikace:**
1. Uživatel nezadá jméno → Vidí: "Error - nelze nezadat jméno" (bez chyby hesla)
2. Uživatel zadá jméno delší než 50 znaků → Vidí: "Error - jméno je příliš dlouhé" (bez chyby hesla)
3. Uživatel zadá jméno OK, heslo OK → Vidí: "Uhodl jsi heslo!"
4. Uživatel zadá jméno OK, heslo špatně → Vidí: "Error - špatné heslo"

**Výsledek: ✅ SPLNĚNO**

---

## Souhrn

| Úkol | Stav | Poznámka |
|------|------|----------|
| 1 | ✅ SPLNĚNO | Aplikace je připravena k spuštění |
| 2 | ⚠️ NELZE OVĚŘIT | Vyžaduje kontrolu v Git historii |
| 3 | ⚠️ PŘIPRAVENO | Vyžaduje test na Render |
| 4 | ✅ SPLNĚNO | GET formulář s příjmením funguje |
| 5 | ✅ SPLNĚNO | POST formulář je funkční |
| 6 | ✅ SPLNĚNO | Heslo funguje správně s logickou kontrolou |
| 7 | ✅ SPLNĚNO | Validace vstupů je správně implementována |

---

## Finální posouzení

**Všechny klíčové funkce jsou implementovány správně:**
- ✅ Jméno se validuje (prázdné/délka)
- ✅ Heslo se kontroluje jen když je jméno OK
- ✅ Chybové zprávy jsou srozumitelné
- ✅ Uživatel vidí pouze relevantní chyby

**Aplikace je připravena pro Úkol 8!**
