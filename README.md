# 🐾 CliniVet - Sistema de Clinica Veterinária

É um sistema destinado ao cadastro de tutores e animais para possibilitar o agendamento de consultas veterinárias e outros procedimentos.

---

## 📖 Sobre o projeto

O nosso projeto, CliniVet foi desenvolvido durante o curso de Desenvolvimento de Sistemas na disciplina de projeto integrador, colocando em prática o que aprendemos nas aulas. O sistema possui uma interface gráfica e utiliza um banco de dados para armazenar e organizar as informações. Durante sua criação, pudemos aprender mais sobre programação, banco de dados e como organizar o código de forma que o sistema funcione corretamente.

---

## 🎯 Principais Objetivos

O projeto da Clinica Veterinária foi desenvolvido na disciplina de Projeto Integrador, e tem como objetivo facilitar o atendimento da clínica através do cadastro digital antecipado, tornar o histórico de vacinação visível aos tutores e também permitir com que o agendamento seja feita de forma antecipada pelo nível de necessidade de cada animal.

---

## 💻 Tecnologias Utilizadas

Para o desenvolvimento do sistema, utilizamos diferentes tecnologias para complementar nosso projeto. A arquitetura geral foi desenvolvida em linguagem Python, onde, para a interfácie gráfica utilizamos o TKinter e para complementação das funções utilizamos bibliotecas como TKCalenda (Datas) e Pillow(imagens). Para o armazenamento de dados, utilizamos o MySQL.

---

## ⚙️ Funcionalidades

* 👤 Cadastro de tutores.
* 🐶 Cadastro de animais.
* 🩺 Cadastro de veterinários.
* 📅 Agendamento de consultas e vacinas.
* 📝 Registrar atendimentos.
* 📋 Acesso ao histórico do animal.
* 💉 Controle de vacinação.

---

## 🏗️ Arquitetura do Sistema

O sistema utiliza como base o padrão arquitetural MVC, dividido em Model, View e Controller. Além dessas camadas, também utiliza a camada DAO para separar operações de acesso ao banco de dados. As três camadas principais do padrão MVC são divididas em:

* **Model** - representa as entidades e os dados utilizados pelo sistema.
* **View** - representa a interface gráfica utilizada pelo usuário.
* **Controller** - recebe as ações realizadas na interface e coordena a execução das operações.
* **DAO** - O padrão DAO é utilizado para separar as operações relacionadas ao banco de dados das demais partes da aplicação.

---

## 🗄️ Banco de Dados

O banco de dados utilizado no projeto é o MySQL, responsável por armazenar as informações utilizadas pelo sistema. O banco deste projeto é composto pelas seguintes tabelas:

Cliente - [ID, NOME, TELEFONE, CPF]; 
Especie - [ID, NOME]; 
Raca - [ID, NOME, ESPECIE_ID] 
Animal - [ID, NOME, DATA_NASCIMENTO, SEXO, PESO, CLIENTE_ID, ESPECIE_ID, RACA_ID]; 
Consulta - [ID, DATA_CONSULTA, OBSERVACOES, ANIMAL_ID, VETERINARIO_ID]; 
Veterinario - [ID, NOME, CPF, TELEFONE, RG, ESPECIALIDADE]; 
Vacina - [ID, NOME, DESCRICAO]; 
Agendamento - [ID, SERVICO, DATA_AGENDAMENTO, HORARIO_AGENDAMENTO, STATUS_AGENDAMENTO, ANIMAL_ID]; 
Aplicacao_vacina - [ID, TIPO_SERVICO, DATA_VACINA, HORARIO_VACINA, STATUS_VACINA, ANIMAL_ID, VACINA_ID].


📜 Script do Banco de Dados

<details> 

<summary>

CREATE DATABASE IF NOT EXISTS CliniVet;
USE CliniVet;

CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    cpf CHAR(14) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS especie(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS raca(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    especie_id INTEGER NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_raca_especie
        FOREIGN KEY (especie_id)
        REFERENCES especie(id)
);

CREATE TABLE IF NOT EXISTS especie_raca(
    especie_id INTEGER NOT NULL,
    raca_id INTEGER NOT NULL,
    PRIMARY KEY (especie_id, raca_id),
    CONSTRAINT fk_especie_raca_especie
        FOREIGN KEY (especie_id)
        REFERENCES especie(id),
    CONSTRAINT fk_especie_raca_raca
        FOREIGN KEY (raca_id)
        REFERENCES raca(id)
);

CREATE TABLE IF NOT EXISTS animal(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo VARCHAR(20) NOT NULL,
    peso DECIMAL(5,2) NOT NULL,
    cliente_id INTEGER NOT NULL,
    especie_id INTEGER NOT NULL,
    raca_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_animal_cliente
        FOREIGN KEY (cliente_id)
        REFERENCES cliente(id),
    CONSTRAINT fk_animal_especie
        FOREIGN KEY (especie_id)
        REFERENCES especie(id),
    CONSTRAINT fk_animal_raca
        FOREIGN KEY (raca_id)
        REFERENCES raca(id)
);

CREATE TABLE IF NOT EXISTS veterinario(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    cpf CHAR(14) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    rg VARCHAR(9) NOT NULL,
    especialidade VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS consulta(
    id INTEGER NOT NULL AUTO_INCREMENT,
    data_consulta DATE NOT NULL,
    horario_consulta TIME NOT NULL,
    observacoes VARCHAR(50),
    animal_id INTEGER NOT NULL,
    veterinario_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_consulta_animal
        FOREIGN KEY (animal_id)
        REFERENCES animal(id),
    CONSTRAINT fk_consulta_veterinario
        FOREIGN KEY (veterinario_id)
        REFERENCES veterinario(id)
);

CREATE TABLE IF NOT EXISTS vacina(
    id INTEGER NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) NOT NULL,
    descricao VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS agendamento(
    id INTEGER NOT NULL AUTO_INCREMENT,
    servico VARCHAR(50) NOT NULL,
    data_agendamento DATE NOT NULL,
    horario_agendamento TIME NOT NULL,
    status_agendamento VARCHAR(50) NOT NULL,
    animal_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_agendamento_animal
        FOREIGN KEY (animal_id)
        REFERENCES animal(id)
);

CREATE TABLE IF NOT EXISTS aplicacao_vacina(
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

CREATE OR REPLACE VIEW historico_consultas AS
SELECT
    c.id AS consulta_id,
    a.id AS animal_id,
    a.nome AS animal_nome,
    c.data_consulta,
    c.horario_consulta,
    c.observacoes,
    v.nome AS veterinario_nome
FROM consulta c
INNER JOIN animal a
    ON c.animal_id = a.id
INNER JOIN veterinario v
    ON c.veterinario_id = v.id
WHERE c.data_consulta <= CURDATE();

---

## 🚀 Como executar
🔧 Passo a passo

1. Clone o repositório

git clone https://github.com/daniellydscahupczinski-prog/pi-clinivet.git ,
cd pi-clinivet

2. Crie e ative o ambiente virtual
No Windows:
- python -m venv venv
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
- venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

- Instalar manualmente:
pip install mysql-connector-python tkcalendar pillow python-dotenv

---

## 👥 Público alvo

Osistema da Clinica Veterinária é mais focado para pessoas que buscam por atendimento para seus animais, que querem agendar vacinações para os seus pets e pessoas que desejam acompanhar o histórico de saúde de seus animais.

---

## 🎓 Integrantes

O projeto foi desenvolvido por 3 estudantes: Yasmim Schuck, Danielly dos Santos e Alana Milk.

* 🏫 **Instituição de ensino:** Senac Novo Hamburgo;
* 📚 **Curso:** Desenvolvimento de Sistemas
* 🔢 **Turma:** 8711
* 👨‍🏫 **Professor(a):** Eduardo Reus
* 📆 **Ano:** 2026