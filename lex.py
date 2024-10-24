    # ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
reservadas = {
    'begin': 'BEGIN',
    'end': 'END',
    'const': 'CONST',
    'type': 'TYPE',
    'var': 'VAR',
    'integer': 'INTEGER',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'array': 'ARRAY',
    'of': 'OF',
    'record': 'RECORD',
    'procedure': 'PROCEDURE',
    'while': 'WHILE',
    'do': 'DO',
    'if': 'IF',
    'then': 'THEN',
    'for': 'FOR',
    'write': 'WRITE',
    'read': 'READ',
    'to': 'TO',
    'else': 'ELSE',
    'false': 'FALSE',
    'true': 'TRUE',
    'and': 'AND',
    'or': 'OR'
}


tokens = (
   'ID',
   'NUMERO',
   'CONST_VALOR',
   'IGUAL',
   'PONTO_VIRGULA',
   'VIRGULA',
   'COLCHETE_ESQ',
   'COLCHETE_DIR',
   'DOIS_PONTOS',
   'PARENTESE_ESQ',
   'PARENTESE_DIR',
   'ATRIBUICAO',
   'OP_COMP',
   'OP_MAT',
   'PONTO',
   'COMENTARIO'
)

# Regular expression rules for simple tokens

t_ID = r'^[a-zA-Z][a-zA-Z0-9]*$'
t_NUMERO = r'^\d+(\.\d+)?$'
t_CONST_VALOR = r'^".+"$'
t_IGUAL = r'\='
t_PONTO_VIRGULA = r'\;'
t_VIRGULA = r'\,'
t_COLCHETE_ESQ = r'\['
t_COLCHETE_DIR = r'\]'
t_DOIS_PONTOS = r'\:'
t_PARENTESE_ESQ = r'\('
t_PARENTESE_DIR = r'\)'
t_ATRIBUICAO = r'\:\='
t_OP_COMP = r'^(>|<|==|!=|>=|<=)$'
t_OP_MAT = r'^(\+|\-|*|\/)$'
t_PONTO = r'\.'
t_COMENTARIO = r'\#'


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
3 + 4 * 10
  + -20 *2
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
