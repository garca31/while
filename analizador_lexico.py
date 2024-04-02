import ply.lex as lex

resultado_lexico = []

reservadas = {
    'while' : 'While',
    'print' :  'Print'
}

tokens = [
    'NUMERO',
    'PARIZQ',
    'PARDER',
    'LLAVIZQ',
	'LLAVDER',
    'COMILLAS',
    'MAYOR',
    'MENOR',
    'ID'

] + list(reservadas.values())

t_NUMERO = r'\d+(\.\d+)*'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_LLAVIZQ = r'\{'
t_LLAVDER = r'\}'
t_COMILLAS = r'\"'
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_ignore = r'\t'


def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Caracter Ilegal %s" % (t.value[0]))
    t.lexer

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z0-9_]*'
   t.type = reservadas.get(t.value, 'ID')
   t.lineno = t.lexer.lineno
   return t

lexer = lex.lex()