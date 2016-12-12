import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='postgres',dbname='trabalhosbd')
cur = conn.cursor()


def cria_tabelas():

	cur.execute('CREATE TABLE unidade_administrativa (sigla varchar, nome varchar PRIMARY KEY);')
	cur.execute('CREATE TABLE unidade_academica (sigla varchar, nome varchar PRIMARY KEY, area_de_conhecimento varchar);')

	cur.execute('CREATE TABLE pessoa (nome varchar NOT NULL, CPF varchar PRIMARY KEY, email_i varchar, email_s varchar, data_nascimento date, senha varchar);')
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
	print('Digite sua senha')
	senha = input()
	cur.execute("INSERT INTO pessoa VALUES (%s,%s,%s,%s,%s,%s)", (nome,cpf,emaili,emails,datanascimento,senha,))
	print('Digite 1 para aluno, 2 para professor, 3 para tecnico e 4 para tercerizados')
	escolha = input()
	if escolha == '1':
		print('Digite seu nro_matricula')
		matricula = input()
		print('Digite seu curso')
		curso = input()
		cur.execute("INSERT INTO alunos (nro_matricula,curso,cpf,nome,email_i,email_s,data_nascimento,senha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (matricula,curso,cpf,nome,emaili,emails,datanascimento,senha,))
		conn.commit()

	elif escolha == '2':
		print('Digite seu SIAPE')
		siape = input()

	elif escolha == '3':
		print('Digite seu SIAPE')
		siape = input()

	elif escolha == '4':
		print('Digite a empresa')
		empresa = input()
		print('Digite o setor de atuacao')
		setor = input()
		cur.execute("INSERT INTO tercerizados (empresa,setor_atuacao,cpf,nome,email_i,email_s,data_nascimento,senha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (empresa,setor,cpf,nome,emaili,emails,datanascimento,senha,))
		conn.commit()

def pessoa_existente():
	print('Digite seu cpf')
	cpf = input()
	print('Digite sua senha')
	senha = input()
	cur.execute('SELECT senha FROM pessoa WHERE cpf = %s', (cpf,))
	x = cur.fetchone()
	if senha == x[0]:
		print('LOGADOs')










nova_pessoa()

