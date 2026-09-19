create table veterinario (
    id integer not null auto_increment,
    nome varchar(50) not null,
    cpf char(14) not null,
    telefone varchar(20) not null,
    rg varchar(9) not null,
    especialidade varchar(50) not null,
    primary key (id)
);