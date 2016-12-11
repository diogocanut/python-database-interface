import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='postgres',dbname='trabalhosbd')
cur = conn.cursor()

cur.execute('CREATE TABLE unidade_administrativa (sigla varchar, nome varchar PRIMARY KEY);')
cur.execute('CREATE TABLE unidade_academica (sigla varchar, nome varchar PRIMARY KEY, area_de_conhecimento varchar);')

cur.execute('CREATE TABLE pessoa (cpf varchar PRIMARY KEY, nome varchar NOT NULL, email_i varchar, email_s varchar, data_nascimento date);')
cur.execute('CREATE TABLE professores (SIAPE varchar, FOREIGN KEY (nome) REFERENCES unidade_academica(nome), regime_de_trabalho int) INHERITS (pessoa);')
cur.execute('CREATE TABLE alunos (nro_matricula int, curso varchar) INHERITS (pessoa);')
cur.execute('CREATE TABLE tecnicos (SIAPE varchar, FOREIGN KEY (nome) REFERENCES unidade_administrativa(nome)) INHERITS (pessoa);')
cur.execute('CREATE TABLE curso (sigla_c varchar PRIMARY KEY, nome varchar NOT NULL, FOREIGN KEY (nome) REFERENCES unidade_academica(nome));')
cur.execute('CREATE TABLE tercerizados (empresa varchar, setor_atuacao varchar) INHERITS (pessoa);')


cur.execute('CREATE TABLE respostas (ID int PRIMARY KEY, texto varchar, sim_nao boolean);')
cur.execute('CREATE TABLE questoes (descricao varchar, ID int PRIMARY KEY, FOREIGN KEY (ID) REFERENCES respostas(ID));')




