-- SQLite
CREATE TABLE IF NOT EXISTS students ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    first_name VARCHAR(50), 
    last_name VARCHAR(50), 
    email VARCHAR(250));


ALTER TABLE students ADD COLUMN phone varchar(20);
ALTER TABLE students ADD COLUMN address TEXT(200);
-- DROP TABLE students;

-- Antra užduotis

-- Sukurkite lentelę "dėstytojai", kuri turės šiuos stulpelius:
-- vardas: tekstas, maksimalus ilgis - 50 simbolių
-- pavardė: tekstas, maksimalus ilgis - 50 simbolių
-- skyrius: tekstas, maksimalus ilgis - 100 simbolių
-- el_paštas: tekstas, maksimalus ilgis - 50 simbolių
-- Prie "dėstytojai" lentelės pridėkite naują stulpelį "kabineto_nr" su sveiko skaičiaus tipu.

-- Pašalinkite "dėstytojai" lentelę iš duomenų bazės.


CREATE TABLE IF NOT EXISTS destytojai ( destytojo_id INT PRIMARY KEY,
                                        vardas VARCHAR(50) NOT NULL,
                                        pavarde VARCHAR(50) NOT NULL,
                                        skyrius TEXT(100) NOT NULL,
                                        el_pastas TEXT(50)NOT NULL);

ALTER TABLE destytojai ADD COLUMN kabineto_nr INT;




