CREATE DATABASE IF NOT EXISTS sars_mexico;
USE sars_mexico;

CREATE TABLE IF NOT EXISTS secuencias (
    seq_id INT AUTO_INCREMENT PRIMARY KEY,
    seq_name VARCHAR(255) UNIQUE NOT NULL,
    year INT NOT NULL,
    clade VARCHAR(50),
    clade_who VARCHAR(50),
    qc_status VARCHAR(20),
    total_missing INT
);

CREATE TABLE IF NOT EXISTS mutaciones (
    mut_id INT AUTO_INCREMENT PRIMARY KEY,
    seq_name VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    mutation VARCHAR(20) NOT NULL,
    position INT NOT NULL,
    gene VARCHAR(20),
    codon INT,
    aa_mutation VARCHAR(50),
    type VARCHAR(20),
    FOREIGN KEY (seq_name) REFERENCES secuencias(seq_name)
);

CREATE TABLE IF NOT EXISTS frecuencias_aa (
    freq_id INT AUTO_INCREMENT PRIMARY KEY,
    aa_mutation VARCHAR(50) NOT NULL,
    gene VARCHAR(20),
    year INT NOT NULL,
    frequency DECIMAL(6,4),
    UNIQUE KEY (aa_mutation, gene, year)
);

CREATE TABLE IF NOT EXISTS densidad_por_gen (
    gene VARCHAR(20) PRIMARY KEY,
    length_nt INT NOT NULL,
    unique_mutations INT NOT NULL,
    mutations_per_kb DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS resultados_estadisticos (
    stat_id INT AUTO_INCREMENT PRIMARY KEY,
    mutation VARCHAR(50) NOT NULL,
    gene VARCHAR(20),
    nivel VARCHAR(20),
    delta DECIMAL(6,4),
    p_value_periodos DECIMAL(10,6),
    coef_year DECIMAL(10,4),
    odds_ratio DECIMAL(10,4),
    p_value_tendencia DECIMAL(10,6),
    significativo_periodos BOOLEAN,
    significativo_tendencia BOOLEAN,
    direccion VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS frecuencias_nt (
    freq_id INT AUTO_INCREMENT PRIMARY KEY,
    mutation VARCHAR(20) NOT NULL,
    gene VARCHAR(20),
    year INT NOT NULL,
    frequency DECIMAL(6,4),
    UNIQUE KEY (mutation, gene, year)
);