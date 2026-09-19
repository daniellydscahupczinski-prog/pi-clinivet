crate table animal (
    id integer not null auto_increment,
    nome varchar(50) not null,
    data_nascimento date not null,
    sexo varchar(20) not null,
    peso decimal(5,2) not null,
    cliente_id integer not null,
    especie_id integer not null,
    raca_id integer not null,
    constraint fk_animal_cliente foreign key (cliente_id) references cliente(id),
    constraint fk_animal_especie foreign key (especie_id) references especie(id),
    constraint fk_animal_raca foreign key (raca_id) references raca(id)
);