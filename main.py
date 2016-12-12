import trabalhosbd
import psycopg2

conn = psycopg2.connect(host='localhost', user='postgres', password='postgres',dbname='xxx2')
cur = conn.cursor()

def main():
	try:
		cur.execute("SELECT * FROM formulario;")
	except psycopg2.ProgrammingError:
		trabalhosbd.cria_tabelas()
		trabalhosbd.povoamento_inicial()

	
	logado = False
	logado = trabalhosbd.login()
	

	while logado:
		print('1 - Responder formulario')
		print('2 - Criar novo formulario')
		escolha = input()
		if escolha == '1':
			trabalhosbd.responder_form_existente()
		




if __name__ == "__main__":
    main()