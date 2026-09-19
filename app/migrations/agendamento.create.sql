create table agendamento (
     id INTEGER NOT NULL AUTO_INCREMENT,
    servico VARCHAR(50) NOT NULL,
    data_agendamento DATE NOT NULL,
    horario_agendamento TIME NOT NULL,
    status_agendamento VARCHAR(50) NOT NULL,
    animal_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_agendamento_animal FOREIGN KEY (animal_id) REFERENCES animal(id)
)