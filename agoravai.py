import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='postgres',dbname='trabalhosbd')
cur = conn.cursor()


def cria_tabelas():

	cur.execute('CREATE TABLE unidade_administrativa (sigla varchar, nome varchar PRIMARY KEY, senha int);')
	cur.execute('CREATE TABLE unidade_academica (sigla varchar, nome varchar PRIMARY KEY, area_de_conhecimento varchar);')

	cur.execute('CREATE TABLE pessoa (nome varchar NOT NULL, CPF varchar PRIMARY KEY, email_i varchar, email_s varchar, data_nascimento date);')
	cur.execute('CREATE TABLE professores (SIAPE varchar, FOREIGN KEY (nome) REFERENCES unidade_academica(nome), regime_de_trabalho int) INHERITS (pessoa);')
	cur.execute('CREATE TABLE alunos (nro_matricula int, curso varchar) INHERITS (pessoa);')
	cur.execute('CREATE TABLE tecnicos (SIAPE varchar, FOREIGN KEY (nome) REFERENCES unidade_administrativa(nome)) INHERITS (pessoa);')
	cur.execute('CREATE TABLE curso (sigla_c varchar PRIMARY KEY, nome varchar NOT NULL, FOREIGN KEY (nome) REFERENCES unidade_academica(nome));')
	cur.execute('CREATE TABLE tercerizados (empresa varchar, setor_atuacao varchar) INHERITS (pessoa);')


	cur.execute('CREATE TABLE respostas (ID int PRIMARY KEY, texto varchar, sim_nao boolean);')
	cur.execute('CREATE TABLE questoes (descricao varchar, ID int PRIMARY KEY, FOREIGN KEY (ID) REFERENCES respostas(ID));')

	cur.execute('CREATE TABLE formulario (ID int PRIMARY KEY, FOREIGN KEY (ID) REFERENCES questoes(ID), inicio date, fim date);')
	conn.commit()


def nova_pessoa():
	print('Digite seu nome')
	nome = input()
	print('Digite seu cpf')
	cpf = input()
	print('Digite seu email institucional')
	emaili = input()
	print('Digite seu email secundario')
	emails = input()
	print('Digite sua data de nascimento')
	datanascimento = input()
	cur.execute("INSERT INTO pessoa VALUES (%s,%s,%s,%s,%s)", (nome,cpf,emaili,emails,datanascimento,))
	conn.commit()

nova_pessoa()