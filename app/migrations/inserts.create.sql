INSERT INTO raca (id, nome) VALUES (15, 'BULLDOG FRANCÊS');
INSERT INTO raca (id, nome) VALUES (1, 'GOLDEN RETRIEVER');
INSERT INTO raca (id, nome) VALUES (14, 'LABRADOR RETRIEVER');
INSERT INTO raca (id, nome) VALUES (19, 'MAINE COON');
INSERT INTO raca (id, nome) VALUES (17, 'PERSA');
INSERT INTO raca (id, nome) VALUES (16, 'PINSCHER');
INSERT INTO raca (id, nome) VALUES (18, 'SCOTTISH FOLD');
INSERT INTO raca (id, nome) VALUES (2, 'SHIH-TZU');

INSERT INTO especie (id, nome, raca_id) VALUES (1, 'Cachorro', 1);
INSERT INTO especie (id, nome, raca_id) VALUES (75, 'Cachorro', 16);
INSERT INTO especie (id, nome, raca_id) VALUES (76, 'Cachorro', 2);
INSERT INTO especie (id, nome, raca_id) VALUES (77, 'Cachorro', 14);
INSERT INTO especie (id, nome, raca_id) VALUES (74, 'Gato', 18);
INSERT INTO especie (id, nome, raca_id) VALUES (78, 'Gato', 17);
INSERT INTO especie (id, nome, raca_id) VALUES (79, 'Gato', 19);

INSERT INTO cliente (id, nome, telefone, cpf) VALUES (9, 'ANTONIO DOS SANTOS', '51998645213', '054308706549');
INSERT INTO cliente (id, nome, telefone, cpf) VALUES (10, 'GUILHERME PAZ', '51994444909', '05109383010');
INSERT INTO cliente (id, nome, telefone, cpf) VALUES (1, 'MARIA SILVA', '(51) 12345-1234', '111.222.333-44');

INSERT INTO vacina (id, nome, descricao) VALUES (11, 'Antirrábica', 'Prevenção de doenças');
INSERT INTO vacina (id, nome, descricao) VALUES (10, 'V10', 'Vacina para cães');

INSERT INTO veterinario (id, nome, especialidade) VALUES (1, 'Ana Oliveira', 'Clínica Geral');
INSERT INTO veterinario (id, nome, especialidade) VALUES (2, 'Carlos Mendes', 'Dermatologia');