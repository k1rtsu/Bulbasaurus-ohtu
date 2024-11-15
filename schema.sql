-- Users save references into this table. The column 'type' tells the type of the 
-- reference e.g. a book or an article.
CREATE TABLE reference
(
    id SERIAL PRIMARY KEY,
    type TEXT
);

-- Authors are saved into this table. A separate table is needed, because the number of 
-- authors may vary.
CREATE TABLE author
(
    id SERIAL PRIMARY KEY,
    reference_id INTEGER REFERENCES reference,
    name TEXT
);

-- Information about books is saved here.
CREATE TABLE book
(
    id SERIAL PRIMARY KEY,
    reference_id INTEGER REFERENCES reference,
    title TEXT,
    year INTEGER,
    publisher TEXT
);



