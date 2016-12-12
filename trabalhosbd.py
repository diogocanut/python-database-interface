import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='postgres',dbname='xxx2')
cur = conn.cursor()
curr = conn.cursor()


def cria_tabelas():

	cur.execute('CREATE TABLE unidade_administrativa (sigla varchar, nome varchar PRIMARY KEY);')
	cur.execute('CREATE TABLE unidade_academica (sigla varchar, nome varchar PRIMARY KEY, area_de_conhecimento varchar);')

	cur.execute('CREATE TABLE pessoa (nome varchar NOT NULL, CPF varchar PRIMARY KEY, email_i varchar, email_s varchar, data_nascimento date, senha varchar);')
	cur.execute('CREATE TABLE professores (SIAPE varchar, nome_u varchar, FOREIGN KEY (nome_u) REFERENCES unidade_academica(nome), regime_de_trabalho int) INHERITS (pessoa);')
	cur.execute('CREATE TABLE alunos (nro_matricula int, curso varchar) INHERITS (pessoa);')
	cur.execute('CREATE TABLE tecnicos (SIAPE varchar, nome_a varchar, FOREIGN KEY (nome_a) REFERENCES unidade_administrativa(nome)) INHERITS (pessoa);')
	cur.execute('CREATE TABLE curso (sigla_c varchar PRIMARY KEY, nome_a varchar, nome varchar NOT NULL, FOREIGN KEY (nome) REFERENCES unidade_academica(nome));')
	cur.execute('CREATE TABLE tercerizados (empresa varchar, setor_atuacao varchar) INHERITS (pessoa);')

	
	cur.execute('CREATE TABLE formulario (ID int PRIMARY KEY,nome_form varchar, nome_criador varchar, inicio date, fim date);')

	cur.execute('CREATE TABLE questoes (descricao varchar, ID_q int PRIMARY KEY,ID_form int, FOREIGN KEY (ID_form) REFERENCES formulario(ID));')
	cur.execute('CREATE TABLE respostas (texto varchar , sim_nao boolean, ID int, FOREIGN KEY (ID) REFERENCES questoes(ID_q));')

	
	conn.commit()

def povoamento_inicial():
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("facom","faculdade de computacao","exatas",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("famat","faculdade de matematica","exatas",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("fagen","faculdade de gestao de negocios","adminsitrativa",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("IH","instituto de historia","humanas",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("ifilo","instituto de filosofia","humanas",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("ig","instituto de geografia","humanas",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("iciag","instituto de ciencias agrarias","agrarias",))
	cur.execute('INSERT INTO unidade_academica VALUES (%s,%s,%s);' ,("feciv","faculdade de engenharia civil","exatas",))

	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("stam","unidade santa monica",))
	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("ed","unidade engenheiro diniz",))
	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("fd","fazenda do gloria",))
	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("umu","campus umuarama",))
	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("educa","campus educacao fisica",))
	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("cp","campos pontal",))
	cur.execute('INSERT INTO unidade_administrativa VALUES (%s,%s);' ,("santa","campus santa monica",))

	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("CC","ciencia da computacao","faculdade de computacao",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("MAT","matematica","faculdade de matematica",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("ADM","administracao","faculdade de gestao de negocios",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("HIST","historia","instituto de historia",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("FILO","filosofia","instituto de filosofia",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("IG","geografia","instituto de geografia",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("AGRO","agronomia","instituto de ciencias agrarias",))
	cur.execute('INSERT INTO curso VALUES (%s,%s,%s);' ,("CIV","engenharia civil","faculdade de engenharia civil",))

	
	cur.execute('INSERT INTO formulario VALUES (%s,%s,%s,%s,%s);' ,(1,"Tráfico de drogas no campus","knut","01-12-2016","01-04-2017",))

	cur.execute('INSERT INTO questoes VALUES (%s,%s,%s);' ,("Você é a favor da livre entrada da policia militar no campus universitário?(S/N)?",1,1,))
	cur.execute('INSERT INTO questoes VALUES (%s,%s,%s);' ,("Você utiliza algum tipo de droga dentro do campus(Alcool/Cigarro/Ilegais)?",2,1,))
	cur.execute('INSERT INTO questoes VALUES (%s,%s,%s);' ,("Você é a favor de novas medidas para impedir o tráfico de drogas no campus(S/N)?",3,1,))
	cur.execute('INSERT INTO questoes VALUES (%s,%s,%s);' ,("Você considera a segurança atual do campus é satisfatória(S/N)?",4,1,))
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
	print('Digite 1 para aluno, 2 para professor, 3 para tecnico e 4 para tercerizados')
	escolha = input()
	if escolha == '1':
		print('Digite seu nro_matricula')
		matricula = input()
		print('Digite seu curso')
		curso = input()
		cur.execute("INSERT INTO alunos (nro_matricula,curso,cpf,nome,email_i,email_s,data_nascimento,senha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (matricula,curso,cpf,nome,emaili,emails,datanascimento,senha,))
		conn.commit()
		print("Criado com sucesso")

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
		return True
	else:
		return False

def login():
	while True:
		print('1 - Criar novo usuário')
		print('2 - Entrar em usuário existinte')
		escolha = input()
		if escolha == '1':
			nova_pessoa()
		elif escolha == '2':
			if pessoa_existente():
				break
			else:
				print('CPF ou senha não existentes')
		elif escolha != '1' and escolha != '2':
			print('Opcões são apenas 1 ou 2')

def responder_form_existente():
	cur.execute("SELECT * FROM formulario;")
	for record in cur:
		print("Nome do formulário: %s Código: %d" % (record[1],record[0]))
	print("Digite o código do formulário em que deseja responder")
	codigo = input()
	cur.execute("SELECT descricao FROM questoes WHERE ID_form = %s", (codigo,))
	for record in cur:
		print(record[0])
		resp = input()
		if resp == 'S':
			curr.execute("INSERT INTO respostas VALUES (%s,%s,%s)", ("sim","1",codigo,))
			conn.commit()
		elif resp == 'N':
			curr.execute("INSERT INTO respostas VALUES (%s,%s,%s)", ("nao","0",codigo,))
			conn.commit()
		elif resp != 'N' and resp != 'S':
			curr.execute("INSERT INTO respostas VALUES (%s,%s,%s)", (resp,"1",codigo,))
			conn.commit()


responder_form_existente()













