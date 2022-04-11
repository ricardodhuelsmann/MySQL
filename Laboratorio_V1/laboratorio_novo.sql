CREATE DATABASE IF NOT EXISTS laboratorio_novo
DEFAULT CHARSET = utf8
DEFAULT COLLATE = utf8_general_ci;


CREATE TABLE IF NOT EXISTS classe (
  idClasse INT NOT NULL AUTO_INCREMENT,
  nomeClasse VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idClasse`)
);


CREATE TABLE IF NOT EXISTS usuario (
  idUsuario INT NOT NULL AUTO_INCREMENT,
  nomeUsuario VARCHAR(45) NOT NULL,
  classe_idClasse INT NOT NULL,
  PRIMARY KEY (idUsuario),
  FOREIGN KEY (classe_idClasse) REFERENCES classe(idClasse)
);


CREATE TABLE IF NOT EXISTS equipamento (
  idEquipamento INT NOT NULL AUTO_INCREMENT,
  nomeEquipamento VARCHAR(45) NOT NULL,
  PRIMARY KEY (idEquipamento),
);


CREATE TABLE IF NOT EXISTS usoEquipamento (
  idUsoEquipamento INT NOT NULL AUTO_INCREMENT,
  data DATE NOT NULL,
  equipamento_idEquipamento INT NOT NULL,
  usuario_idUsuario INT NOT NULL,
  PRIMARY KEY (idUsoEquipamento),
  FOREIGN KEY (equipamento_idEquipamento) REFERENCES equipamento(idEquipamento),
  FOREIGN KEY (usuario_idUsuario) REFERENCES usuario(idUsuario)
);

INSERT INTO classe (nomeClasse) 
VALUES ('Iniciação Científica', 'Mestrado', 'Doutorado', 'Pós-Doutorado', 'Professores', 'Alunos', 'Funcionários', 'Servidores', 'Outros');

