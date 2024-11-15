-- Users save references into this table. The column 'type' tells the type of the 
-- reference eg. a book or an article.
CREATE TABLE reference
(
    id SERIAL PRIMARY KEY,
    type VARCHAR
);

-- Information about the reference is saved in this table. The column 'field' tells the
-- type of the saved information (eg. author, title, year) and the information is saved 
-- in the column 'value'. 
CREATE TABLE info
(
    id SERIAL PRIMARY KEY,
    reference_id INTEGER REFERENCES reference,
    field VARCHAR,
    value TEXT
);

