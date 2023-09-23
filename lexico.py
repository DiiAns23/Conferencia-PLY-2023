import re
import ply.lex as lex

tokens = (
    'REVALUAR',
    'CORIZQ',
    'CORDER',
    'PARI',
    'PARD',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'DECIMAL',
    'ENTERO',
    'PTCOMA'
)

t_REVALUAR = r'Evaluar'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_PARI = r'\('
t_PARD = r'\)'
t_MAS = r'\+'
t_MENOS = r'\-'
t_POR = r'\*'
t_DIVIDIDO = r'/'
t_PTCOMA = r';'

def t_DECIMAL(t):
    r'\d+\.\d+' # d+.d+
    try:
        t.value = float(t.value)
    except ValueError:
        print("Valor decimal demasiado grande %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'  # d+ -> 1 o mas digitos
    try:
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande %d", t.value)
        t.value = 0
    return t

t_ignore = " \t" # Ignorar espacios en blanco y tabuladores

def t_newline(t):
    r'\n+' # \n+
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Error lexico: '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex(reflags=re.IGNORECASE)