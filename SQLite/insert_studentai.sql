INSERT INTO students (first_name, last_name, email)
VALUES ("Geras", "Studentas", "geras@gmail.com");

INSERT INTO students (first_name, last_name, email) 
VALUES ("Smagulis", "Linksmas", "smagulis@gmail.com");

INSERT INTO students (first_name, last_name, email) 
VALUES ("Tikras", "Vyras", "vyras@gmail.com");

INSERT INTO students (first_name, last_name, email, address) 
VALUES ("Linksma", "Gerule", "linksma@gerule.lt", "visur");


SELECT * FROM students WHERE NOT address IS NULL;
SELECT * FROM students;
SELECT * FROM students WHERE address IS NULL;
SELECT * FROM students WHERE first_name = "Geras";


DELETE FROM students WHERE id > 4;
UPDATE students SET phone = "3705333237";
UPDATE students SET address = "niekur" WHERE address IS NULL;
UPDATE students SET last_name = "Smagulis" WHERE id = 2;
UPDATE students SET first_name = "Linksmas" WHERE id = 2;

ALTER TABLE students ADD COLUMN
subject_id INTEGER REFERENCES dalykai(id);


-- Pirma užduotis

-- Sukurkite lentelę "mokytojai" su šiais stulpeliais: "id", "vardas", "pavarde", "specialybe" ir "patirtis_metais".

CREATE TABLE IF NOT EXISTS mokytojai (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                vardas VARCHAR(50) NOT NULL,
                                pavarde VARCHAR(50) NOT NULL,
                                specialybe VARCHAR(100) NOT NULL,
                                patirtis_matais INT(50));


-- Antra užduotis

-- Įterpkite šiuos įrašus į sukurtą lentelę "mokytojai":

-- Mokytojas su ID 1, vardu Petras, pavarde Petraitis, specialybe Matematika ir dirba nuo 2013 metų.
INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_matais)
VALUES ("Petras", "Petraitis", "Matematika", "2013");

-- Mokytojas su ID 2, vardu Ona, pavarde Onaitė, specialybe Fizika ir dirba nuo 2012 metų.
INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_matais)
VALUES ("Ona", "Onaite", "Fizika", "2012");
-- Mokytojas su ID 3, vardu Marius, pavarde Marijus, specialybe Biologija ir dirba nuo 2015 metų.
INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_matais)
VALUES ("Marius", "Marijus", "Biologija", "2015");
-- Mokytojas su ID 4, vardu Rasa, pavarde Rasaitė, specialybe Anglų kalba ir dirba nuo 2011 metų.
INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_matais)
VALUES ("Rasa", "Rasaite", "Anglu kalba", "2011");
-- Mokytojas su ID 5, vardu Aurimas, pavarde Aurimaitis, specialybe Lietuvių kalba ir dirba nuo 2018 metų.
INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_matais)
VALUES ("Aurimas", "Aurimaitis", "Lietuviu kalba", "2018");
-- Mokytojas su ID 6, vardu Gintare, pavarde Gintarėlė, specialybe Istorija ir dirba nuo 2020 metų.
INSERT INTO mokytojai (vardas, pavarde, specialybe, patirtis_matais)
VALUES ("Gintare", "Gintaraite", "Istorija", "2020");


-- Trečia užduotis

-- Parodykite visus įrašus iš lentelės "mokytojai", kurių specialybė yra "Matematika".
SELECT * FROM mokytojai WHERE specialybe = "Matematika";

-- Ketvirta užduotis

-- Raskite visus mokytojus, kurių stažas yra ilgesnis nei 8 arba 9 metai, ir atvaizduokite tik jų vardą, pavardę bei specialybę.
SELECT vardas, pavarde, specialybe FROM mokytojai WHERE (2023 - patirtis_matais) > 8 OR (2023 - patirtis_matais) > 9; 

-- Penkta užduotis

-- Pakeiskite mokytojos, vardu Rasa ir pavarde Rasaitė, pavardę į "Žolienė".
UPDATE mokytojai SET pavarde = "Zoliene" WHERE id = 4;

-- Šešta užduotis

-- Ištrinkite iš lentelės "mokytojai" mokytoją, kurio ID yra 4.
DELETE FROM mokytojai WHERE id = 4;
