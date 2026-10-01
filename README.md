# CliniVet - Sistema de Clinica Veterinária
É um sistema destinado ao cadastro de tutores e animais para possibilitar o agendamento de consultas veterinárias e outros procedimentos.

---

## Sobre o projeto 
O nosso projeto, CliniVet foi desenvolvido durante o curso de Desenvolvimento de Sistemas na disciplina de projeto integrador, colocando em prática o que aprendemos nas aulas. O sistema possui uma interface gráfica e utiliza um banco de dados para armazenar e organizar as informações. Durante sua criação, pudemos aprender mais sobre programação, banco de dados e como organizar o código de forma que o sistema funcione corretamente.
--- 

## Principais Objetivos
O projeto da Clinica Veterinária foi desenvolvido na disciplina de Projeto Integrador, e tem como objetivo facilitar o atendimento da clínica através do cadastro digital antecipado, tornar o histórico de vacinação visível aos tutores e também permitir com que o agendamento seja feita de forma antecipada pelo nível de necessidade de cada animal.

---

## Tecnologias Utilizadas
Para o desenvolvimento do sistema, utilizamos diferentes tecnologias para complementar nosso projeto. A arquitetura geral foi desenvolvida em linguagem Python, onde, para a interfácie gráfica utilizamos o TKinter e para complementação das funções utilizamos bibliotecas como TKCalenda (Datas) e Pillow(imagens). Para o armazenamento de dados, utilizamos o MySQL.

---

## Funcionalidades
- Cadastro de tutores. 
- Cadastro de animais. 
- Cadastro de veterinários. 
- Agendamento de consultas e vacinas. 
- Registrar atendimentos. 
- Acesso ao histórico do animal. 
- Controle de vacinação. 

---

## Arquitetura do Sistema 
O sistema utiliza como base o padrão arquitetural MVC, dividido em Model, View e Controller. Além dessas camadas, também utiliza a camada DAO para separar operações de acesso ao banco de dados. As três camadas principais do padrão MVC são divididas em: 

- **Model** - representa as entidades e os dados utilizados pelo sistema. 
- **View** - representa a interface gráfica utilizada pelo usuário. 
- **Controller** - recebe as ações realizadas na interface e coordena a execução das operações. 
- **DAO** - O padrão DAO é utilizado para separar as operações relacionadas ao banco de dados das demais partes da aplicação.

---

## Banco de Dados
O banco de dados utilizado no projeto é o MySQL, responsável por armazenar as informações utilizadas pelo sistema. O banco deste projeto é composto pelas seguintes tabelas:

[Cliente] - [ID, NOME, TELEFONE, CPF];
[Especie] - [ID, NOME];
[Raca] - [ID, NOME, ESPECIE_ID]
[Animal] - [ID, NOME, DATA_NASCIMENTO, SEXO, PESO, CLIENTE_ID, ESPECIE_ID, RACA_ID];
[Consulta] - [ID, DATA_CONSULTA, OBSERVACOES, ANIMAL_ID, VETERINARIO_ID];
[Veterinario] - [ID, NOME, CPF, TELEFONE, RG, ESPECIALIDADE];
[Vacina] - [ID, NOME, DESCRICAO];
[Agendamento] - [ID, SERVICO, DATA_AGENDAMENTO, HORARIO_AGENDAMENTO, STATUS_AGENDAMENTO, ANIMAL_ID];
[Aplicacao_vacina] - [ID, TIPO_SERVICO, DATA_VACINA, HORARIO_VACINA, STATUS_VACINA, ANIMAL_ID, VACINA_ID].

---

## Público alvo 
Osistema da Clinica Veterinária é mais focado para pessoas que buscam por atendimento para seus animais, que querem agendar vacinações para os seus pets e pessoas que desejam acompanhar o histórico de saúde de seus animais. 

---

## Como executar
1. Clone o repositório.
2. Instale as dependências.
3. Configure o banco de dados.
4. Execute o arquivo principal.

---

## Integrantes 
O projeto foi desenvolvido por 3 estudantes: Yasmim Schuck, Danielly dos Santos e Alana Milk. 

- Instituição de ensino: Senac Novo Hamburgo;
- Curso: Desenvolvimento de Sistemas
- Turma: 8711
- Professor(a): Eduardo Reus
- Ano: 2026