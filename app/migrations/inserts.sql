-- ESPECIES
INSERT INTO especie (id, nome) VALUES (1,  'Cachorro');
INSERT INTO especie (id, nome) VALUES (75, 'Cachorro');
INSERT INTO especie (id, nome) VALUES (76, 'Cachorro');
INSERT INTO especie (id, nome) VALUES (77, 'Cachorro');
INSERT INTO especie (id, nome) VALUES (74, 'Gato');
INSERT INTO especie (id, nome) VALUES (78, 'Gato');
INSERT INTO especie (id, nome) VALUES (79, 'Gato');

-- RACAS
INSERT INTO raca (id, nome) VALUES (1, 'GOLDEN RETRIEVER');
INSERT INTO raca (id, nome) VALUES (2, 'SHIH-TZU');
INSERT INTO raca (id, nome) VALUES (14, 'LABRADOR RETRIEVER');
INSERT INTO raca (id, nome) VALUES (15, 'BULLDOG FRANCÊS');
INSERT INTO raca (id, nome) VALUES (16, 'PINSCHER');
INSERT INTO raca (id, nome) VALUES (17, 'PERSA');
INSERT INTO raca (id, nome) VALUES (18, 'SCOTTISH FOLD');
INSERT INTO raca (id, nome) VALUES (19, 'MAINE COON');

-- ESPECIE_RACA
INSERT INTO especie_raca (especie_id, raca_id) VALUES (1,  1);
INSERT INTO especie_raca (especie_id, raca_id) VALUES (75, 16);
INSERT INTO especie_raca (especie_id, raca_id) VALUES (76, 2);
INSERT INTO especie_raca (especie_id, raca_id) VALUES (77, 14);
INSERT INTO especie_raca (especie_id, raca_id) VALUES (74, 18);
INSERT INTO especie_raca (especie_id, raca_id) VALUES (78, 17);
INSERT INTO especie_raca (especie_id, raca_id) VALUES (79, 19);

-- CLIENTES
INSERT INTO cliente (id, nome, telefone, cpf) VALUES (1,  'MARIA SILVA', '(51) 12345-1234', '111.222.333-44');
INSERT INTO cliente (id, nome, telefone, cpf) VALUES (9,  'ANTONIO DOS SANTOS', '51998645213', '054308706549');
INSERT INTO cliente (id, nome, telefone, cpf) VALUES (10, 'GUILHERME PAZ', '51994444909', '05109383010');

-- VETERINARIOS
INSERT INTO veterinario (id, nome, telefone, cpf, rg, especialidade) VALUES (1, 'Ana Oliveira',  '(51) 1551-1515',  '985.453.625.87', '456789123', 'Clínica Geral');
INSERT INTO veterinario (id, nome, telefone, cpf, rg, especialidade) VALUES (2, 'Carlos Mendes', '(51) 23232-2323', '928.752.700.05', '321654987', 'Dermatologia');

-- ANIMAIS
INSERT INTO animal (id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id) VALUES (1,  'Thor',    '2022-01-01', 'Macho', 25.50, 1,  1,  1);
INSERT INTO animal (id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id) VALUES (2,  'Bobi',    '2023-01-01', 'Macho', 6.20,  1,  1,  2);
INSERT INTO animal (id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id) VALUES (3,  'Thor',    '2022-01-01', 'Macho', 25.50, 1,  1,  1);
INSERT INTO animal (id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id) VALUES (14, 'Quindin', '2021-01-01', 'Macho', 5.00,  10, 1,  1);
INSERT INTO animal (id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id) VALUES (15, 'Theo',    '2024-01-01', 'Macho', 5.00,  1,  75, 16);
INSERT INTO animal (id, nome, data_nascimento, sexo, peso, cliente_id, especie_id, raca_id) VALUES (16, 'Nuke',    '2023-10-01', 'Macho', 7.00,  10, 74, 19);

-- AGENDAMENTOS
INSERT INTO agendamento (id, servico, horario_agendamento, data_agendamento, status_agendamento, animal_id) VALUES (5, 'Banho e tosa', '00:00:00', '2026-11-01', 'Concluido', 1);
INSERT INTO agendamento (id, servico, horario_agendamento, data_agendamento, status_agendamento, animal_id) VALUES (6, 'Consulta',     '10:00:00', '2026-10-06', 'Concluido', 3);

-- CONSULTAS
INSERT INTO consulta (id, data_consulta, horario_consulta, observacoes, veterinario_id, animal_id) VALUES (2, '2026-09-05', '10:30:00', 'Retorno',            2, 1);
INSERT INTO consulta (id, data_consulta, horario_consulta, observacoes, veterinario_id, animal_id) VALUES (7, '2026-08-20', '14:00:00', 'Consulta de rotina', 1, 1);

-- VACINAS
INSERT INTO vacina (id, nome, descricao) VALUES (10, 'V10',         'Vacina para cães');
INSERT INTO vacina (id, nome, descricao) VALUES (11, 'Antirrábica', 'Prevenção de doenças');