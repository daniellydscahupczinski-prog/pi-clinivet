create table consulta (
    id integer not null auto_increment,
    data_consulta date not null,
    horario_consulta time not null,
    observacoes varchar(50) not null,
    animal_id integer not null,
    veterinario_id integer not null,
    primary key (id),
    constraint fk_consulta_animal foreign key (animal_id) references animal(id),
    constraint fk_consulta_veterinario foreign key (veterinario_id) references veterinario(id)
);