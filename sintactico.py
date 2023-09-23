import ply.yacc as yacc
import ply.lex as lex
from lexico import lexer, tokens

# Jerarquia de operadores

precedence = (
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIVIDIDO'),
    ('right', 'UMENOS')
)

# Definicion de la gramatica

def p_instrucciones(t):
    '''instrucciones : instruccion instrucciones
                    | instruccion'''

def p_instruccion(t):
    '''instruccion : REVALUAR CORIZQ expresion CORDER PTCOMA'''
    print('El valor de la expresion es: ', t[3])


def p_expresion_binaria(t):
    '''expresion : expresion MAS expresion
                | expresion MENOS expresion
                | expresion POR expresion
                | expresion DIVIDIDO expresion'''
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/':
        if t[3] == 0:
            print('Division entre cero')
            t[0] = 0
        else:
            t[0] = t[1] / t[3]

def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS'''
    t[0] = -t[2]

def p_expresion_numero(t):
    '''expresion : ENTERO
                | DECIMAL'''
    t[0] = t[1]

def p_expresion_parentesis(t):
    '''expresion : PARI expresion PARD'''
    t[0] = t[2]

def p_error(t):
    print('Error sintactico en: ', t.value)

parser = yacc.yacc()

f = open('entrada.txt', 'r')
input = f.read()
print(input)
parser.parse(input)