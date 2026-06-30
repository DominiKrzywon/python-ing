# ing.pl cookie consent — Playwright (Python)

Przykład testu który pokrywa przepływ zgody na cookies na stronie banku ing.pl:

- Wejście na stronę
- Klik **Dostosuj**
- Włączenie cookies analitycznych
- Klik **Zaakceptuj wybrane**
- Weryfikacja, że zgoda zapisała się w przeglądarce (`context.cookies()`)

## Struktura

```
python-ing/
├── .github/workflows/playwright.yml  # Pipeline CI/CD (matrix: 3 przeglądarki)
├── pages/cookie_policy_page.py       # Page Object (wszystkie selektory bannera)
├── tests/test_cookie_consent.py      # Test (kroki + asercje)
├── fixtures/ing-mock.html            # Mock bannera cookies (używany na CI)
├── conftest.py                       # Konfiguracja pytest + mockowanie
├── pytest.ini                        # Ustawienia pytest
└── requirements.txt                  # Zależności Python
```

## Uruchomienie lokalne

Wymagania wstępne: **Python 3.12 lub nowszy**.

```bash
git clone https://github.com/DominiKrzywon/python-ing.git
cd python-ing
pip install -r requirements.txt
playwright install --with-deps chromium
pytest --browser chromium
```

## Obsługa captchy

ING.pl chroni stronę przez Captchę, która blokuje ruch z adresów IP datacenter (np. GitHub Actions). Aby testy działały na CI/CD bez prób obchodzenia zabezpieczeń, requesty do ing.pl są przechwytywane i zastępowane lokalnym fixture'm (`fixtures/ing-mock.html`). Mock odwzorowuje baner cookies z identycznymi selektorami, dzięki czemu Page Object i asercje działają tak samo jak na prawdziwej stronie.

Lokalnie (bez zmiennej `CI`) test trafia na prawdziwy ing.pl.

## CI (GitHub Actions)

Workflow `.github/workflows/playwright.yml` uruchamia test równolegle w **chromium**, **firefox** i **webkit** (matrix). Wynik (HTML report) ląduje jako artefakt osobno dla każdej przeglądarki.
