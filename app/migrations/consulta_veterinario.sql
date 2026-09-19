create table consulta_veterinario
(
	id_consulta int not null,
	id_veterinario int not null,
	constraint fk_consulta_consulta_veterinario
		foreign key(id_consulta)
		references consulta(id),
	constraint fk_veterinario_consulta_veterinario
		foreign key(id_veterinario)
		references veterinario(id)
);