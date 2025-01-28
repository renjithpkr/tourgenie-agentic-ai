CREATE TABLE IF NOT EXISTS artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    bio TEXT,
    category VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS cultural_events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    date DATE,
    location VARCHAR(100)
);

INSERT INTO artists (name, bio, category, location) VALUES
('Kalamandalam Gopi', 'A legendary Kathakali artist', 'Kathakali', 'Kerala'),
('Guru Chemancheri Kunhiraman Nair', 'Renowned Koodiyattam performer', 'Koodiyattam', 'Kannur');

INSERT INTO cultural_events (title, description, date, location) VALUES
('Theyyam Festival', 'A spectacular ritualistic performance', '2025-01-15', 'Kannur'),
('Koodiyattam Workshop', 'An ancient Sanskrit theatre art form', '2025-02-10', 'Kozhikode');
