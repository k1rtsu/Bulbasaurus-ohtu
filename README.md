# Bulbasaurus ohtu

Ohjelmistotuotanto 2024 miniprojekti

[![example workflow](https://github.com/k1rtsu/Bulbasaurus-ohtu/workflows/CI/badge.svg)](https://github.com/k1rtsu/Bulbasaurus-ohtu/actions)

[![codecov](https://codecov.io/gh/k1rtsu/Bulbasaurus-ohtu/graph/badge.svg?token=zzkb53ZKhP)](https://codecov.io/gh/k1rtsu/Bulbasaurus-ohtu)

[Product backlog ja sprint backlogit](https://docs.google.com/spreadsheets/d/1RMMjKq7OOiBKllxChY3m_eDCr9RuxWiq2uwkZbb58no/edit?gid=0#gid=0)

## Asennusohje

Kloona repositorio:

```bash
git clone git@github.com:k1rtsu/Bulbasaurus-ohtu.git
```

Luo tiedosto .env, jonne määritetään

```bash
DATABASE_URL=postgresql://xxx
TEST_ENV=true
SECRET_KEY=""
```

Lataa riippuvuudet

```bash
poetry install
```

Avaa virtuaaliympäristö

```bash
poetry shell
```

Luo sovelluksen tarvitsemat tietokantataulut ennen kuin käynnistät sovelluksen ensimmäistä kertaa

```bash
python3 src/db_helper.py
```

Käynnistä sovellus

```bash
python3 src/index.py
```

## Testausohje

Suorita yksikkötestit

```bash
pytest src/tests
```

Suorita Robot-testit

_Käynnistä sovellus virtuaaliympäristössä_

```bash
python3 src/index.py
```

_Suorita Robot-testit sovelluksen ollessa käynnissä_

```bash
robot src/story_tests
```

## Definition of Done

Sprintiin otettu tehtävä voidaan merkitä valmiiksi, kun seuraavat kriteerit täyttyvät.

1. User story ja sen hyväksymiskriteerit on toteutettu.
2. Yksikkötestit ovat valmiit ja menevät läpi.
3. E2E testit ovat valmiit ja menevät läpi.
4. Koodi läpäisee CI prosessin.
5. Koodin katselmointi on valmis.
6. Sprintin tehtävälista ja tuotteen backlogi on päivitetty.
