# Bulbasaurus ohtu
Ohjelmistotuotanto 2024 miniprojekti

[![example workflow](https://github.com/k1rtsu/Bulbasaurus-ohtu/workflows/CI/badge.svg)](https://github.com/k1rtsu/Bulbasaurus-ohtu/actions)

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

*Käynnistä sovellus virtuaaliympäristössä*

```bash
python3 src/index.py
```
*Suorita Robot-testit sovelluksen ollessa käynnissä*

```bash
robot src/story_tests
```