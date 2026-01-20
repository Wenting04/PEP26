CREATE TABLE series (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    genero VARCHAR(100)
);

INSERT INTO series (titulo, genero) VALUES ('Breaking Bad', 'Drama');
INSERT INTO series (titulo, genero) VALUES ('Stranger Things', 'Ciencia ficción');
INSERT INTO series (titulo, genero) VALUES ('The Office', 'Comedia');
INSERT INTO series (titulo, genero) VALUES ('Game of Thrones', 'Fantasía');
INSERT INTO series (titulo, genero) VALUES ('Sherlock', 'Misterio');
