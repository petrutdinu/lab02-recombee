# Laborator 2: Sistem de recomandare cu Recombee - înregistrare proprietăți

`PRIVATE_TOKEN` e lăsat gol intenționat. Repo ul e public și n am vrut să las tokenul la vedere, pentru că oricine l ar putea folosi.

## Dataset ul `books.csv`

Din fișierul `books.csv` din goodbooks-10k de pe [Kaggle](https://www.kaggle.com/datasets/zygmunt/goodbooks-10k) (10.000 de cărți, 23 de coloane) am păstrat primele 1.000 de rânduri și doar 7 coloane utile pentru recomandări, pe care le am redenumit:
  - `original_publication_year` a devenit `publication_year`;
  - `language_code` a devenit `language`. Variantele de engleză (`en-US`, `en-GB`, `en-CA`) au fost unificate sub codul `eng`.

## Properties

| Property | Tip | Descriere |
|---|---|---|
| `title` | string | titlul |
| `authors` | string | autorul (sau autorii) |
| `publication_year` | int | anul în care a apărut |
| `language` | string | limba |
| `average_rating` | double | rating ul mediu, de la 1 la 5 |
| `ratings_count` | int | câte rating uri are |
