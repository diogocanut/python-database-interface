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

def povoamento_inicial():
	cur.execute('INSERT INTO unidade_academica VALUES ("facom","faculdade de computacao","exatas");')
	cur.execute('INSERT INTO unidade_academica VALUES ("famat","faculdade de matematica","exatas");')
	cur.execute('INSERT INTO unidade_academica VALUES ("fagen","faculdade de gestao de negocios","adminsitrativa");')
	cur.execute('INSERT INTO unidade_academica VALUES ("IH","instituto de historia","humanas");')
	cur.execute('INSERT INTO unidade_academica VALUES ("ifilo","instituto de filosofia","humanas");')
	cur.execute('INSERT INTO unidade_academica VALUES ("ig","instituto de geografia","humanas");')
	cur.execute('INSERT INTO unidade_academica VALUES ("iciag","instituto de ciencias agrarias","agrarias");')
	cur.execute('INSERT INTO unidade_academica VALUES ("feciv","faculdade de engenharia civil","exatas");')

	cur.execute('INSERT INTO unidade_administrativa VALUES ("stam","unidade santa monica");')
	cur.execute('INSERT INTO unidade_administrativa VALUES ("ed","unidade engenheiro diniz");')
	cur.execute('INSERT INTO unidade_administrativa VALUES ("fd","fazenda do gloria");')
	cur.execute('INSERT INTO unidade_administrativa VALUES ("umu","campus umuarama");')
	cur.execute('INSERT INTO unidade_administrativa VALUES ("educa","campus educacao fisica");')
	cur.execute('INSERT INTO unidade_administrativa VALUES ("cp","campos pontal");')
	cur.execute('INSERT INTO unidade_administrativa VALUES ("santa","campus santa monica");')

	cur.execute('INSERT INTO cursos ("CC","ciencia da computacao","faculdade de computacao");')
	cur.execute('INSERT INTO cursos ("MAT","matematica","faculdade de matematica");')
	cur.execute('INSERT INTO cursos ("ADM","administracao","faculdade de gestao de negocios");')
	cur.execute('INSERT INTO cursos ("HIST","historia","instituto de historia");')
	cur.execute('INSERT INTO cursos ("FILO","filosofia","instituto de filosofia");')
	cur.execute('INSERT INTO cursos ("IG","geografia","instituto de geografia");')
	cur.execute('INSERT INTO cursos ("AGRO","agronomia","instituto de ciencias agrarias");')
	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')

	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')
	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')
	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')
	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')
	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')
	cur.execute('INSERT INTO cursos ("CIV","engenharia civil","faculdade de engenharia civil");')
	




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
		print('LOGADO')










nova_pessoa()

