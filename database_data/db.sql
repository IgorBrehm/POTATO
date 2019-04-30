CREATE TABLE Ano (
  nome_ano INTEGER(4) PRIMARY KEY
);

CREATE TABLE Mes (
  nome_mes NUMBER(2) NOT NULL,
  nome_ano NUMBER(4) NOT NULL,
  PRIMARY KEY (nome_mes, nome_ano),
  CONSTRAINT fk_mes_ano FOREIGN KEY (nome_ano) REFERENCES Ano (nome_ano)
    ON DELETE CASCADE
);

CREATE TABLE Venda (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  valor    NUMBER    NOT NULL,
  nome_mes NUMBER(2) NOT NULL,
  nome_ano NUMBER(4) NOT NULL,
  CONSTRAINT fk_compra_mes FOREIGN KEY (nome_mes, nome_ano) REFERENCES Mes (nome_mes, nome_ano)
    ON DELETE CASCADE
);

CREATE TABLE Compra (
  id       INTEGER PRIMARY KEY AUTOINCREMENT,
  valor    int       NOT NULL,
  nome_mes NUMBER(2) NOT NULL,
  nome_ano NUMBER(4) NOT NULL,
  CONSTRAINT fk_compra_mes FOREIGN KEY (nome_mes, nome_ano) REFERENCES Mes (nome_mes, nome_ano)
    ON DELETE CASCADE
);

CREATE UNIQUE INDEX id
  ON Venda (id);
CREATE UNIQUE INDEX id
  ON Compra (id);