create table aplicacao_vacina (
    id INTEGER NOT NULL AUTO_INCREMENT,
    tipo_servico VARCHAR(50) NOT NULL,
    data_vacina DATE NOT NULL,
    horario_vacina TIME NOT NULL,
    status_vacina VARCHAR(30),
    animal_id INTEGER NOT NULL,
    vacina_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_aplicacao_vacina_animal
        FOREIGN KEY (animal_id)
        REFERENCES animal(id),
    CONSTRAINT fk_aplicacao_vacina_vacina
        FOREIGN KEY (vacina_id)
        REFERENCES vacina(id)
);