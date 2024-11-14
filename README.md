# Bulbasaurus ohtu
Ohjelmistotuotanto 2024 miniprojekti

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
Avaa virtuaaliympäristö

```bash
poetry shell
```

Lataa riippuvuudet

```bash
poetry install
```

Käynnistä sovellus

```bash
poetry src/index.py
```