-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 11-Out-2024 às 00:12
-- Versão do servidor: 5.7.36
-- versão do PHP: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `escolar`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `aluno`
--

CREATE TABLE `aluno` (
  `matricula` smallint(6) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `idade` smallint(6) NOT NULL,
  `sexo` varchar(15) NOT NULL,
  `numero` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `disciplina`
--

CREATE TABLE `disciplina` (
  `codigo` smallint(6) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `carga_horaria` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `professor`
--

CREATE TABLE `professor` (
  `matricula` smallint(6) NOT NULL,
  `nome` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `codigo` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura da tabela `turma`
--

CREATE TABLE `turma` (
  `numero` smallint(6) NOT NULL,
  `sala` smallint(6) NOT NULL,
  `andar` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `aluno`
--
ALTER TABLE `aluno`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `numero` (`numero`);

--
-- Índices para tabela `disciplina`
--
ALTER TABLE `disciplina`
  ADD PRIMARY KEY (`codigo`);

--
-- Índices para tabela `professor`
--
ALTER TABLE `professor`
  ADD PRIMARY KEY (`matricula`),
  ADD KEY `codigo` (`codigo`);

--
-- Índices para tabela `turma`
--
ALTER TABLE `turma`
  ADD PRIMARY KEY (`numero`);

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `aluno`
--
ALTER TABLE `aluno`
  ADD CONSTRAINT `aluno_ibfk_1` FOREIGN KEY (`numero`) REFERENCES `turma` (`numero`);

--
-- Limitadores para a tabela `professor`
--
ALTER TABLE `professor`
  ADD CONSTRAINT `professor_ibfk_1` FOREIGN KEY (`codigo`) REFERENCES `disciplina` (`codigo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


CREATE TABLE mae(
    nome VARCHAR NOT NULL,
    endereço VARCHAR NOT NULL,
    telefone VARCHAR NOT NULL,
    PRIMARY KEY (cpf)
    )

    CREATE TABLE Equipe_medica (
    codigo INTEGER (15) NOT NULL,
    nome_equipe VARCHAR (60) NOT NULL,
    PRIMARY KEY (codigo)
    )

    CREATE TABLE bebe(
    codigo INTEGER (15) NOT NULL,
    nome VARCHAR (60) NOT NULL,
    data VARCHAR (10) NOT NULL,
    especialidade VARCHAR (20) NOT NULL,
    peso FLOAT,
    altura FLOAT,
    PRIMARY KEY (codigo),
    FOREIGN KEY(codigo) REFERENCES equipe_medica(codigo),
    FOREIGN KEY (cpf) REFERENCES mae (cpf)
    )

    INSERT INTO profissional(crm,nome, telefone, especialidade, codigo_eq) VALUES
    (225566,"Antonio","98800-1111","cardiologista",1122),
    (113388,"Maria","97711-0099","pediatra",1133),
    (446655,"Teresa","96543-667","obstetra",1133),
    (110022,"Pedro","97600-1122","pediatra",1122),
    (876543,"Marcelo","96422-0102","anestesista",1122), 
    (123456,"Lucas","99780-8191","anestesista",1144)


    INSERT INTO mae(cpf, nome, endereço, telefone) VALUES
(22556611,"Erika Amorim","Rua das Flores",98800-1111),
(11338800,"Maria da Penha","Avenida dos Amores",97711-0099),
(44665522,"Helena Costa","Rua da Curva",96543-6677),
(11002233,"Patrícia da Silva","Rua da Conceição",97600-1122)