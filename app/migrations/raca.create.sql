create table raca (
    id integer not null auto_increment,
    nome varchar(50) not null,
    especie_id integer not null,
    primary key (id),
    constraint fk_raca_especie foreign key(especie_id) references especie(id)
);