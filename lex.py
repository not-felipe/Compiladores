import ply.lex as lex
class Lex:
    
    def __init__(self):
        self.lexer = lex.lex(module=self)
        self.tokens_lista = [] # estrutura utilizada para armazenar os tokens na memoria
        
    reservadas = {
        'begin': 'BEGIN',
        'end': 'END',
        'const': 'CONST',
        'type': 'TYPE',
        'var': 'VAR',
        'integer': 'INTEGER',
        'real': 'REAL',
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

    tokens = [
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
    ] + list(reservadas.values())

    # Regular expressions for simple tokens
    t_NUMERO = r'\d+(\.\d+)?'
    t_CONST_VALOR = r'"[^"]*"'
    t_IGUAL = r'\='
    t_PONTO_VIRGULA = r'\;'
    t_VIRGULA = r'\,'
    t_COLCHETE_ESQ = r'\['
    t_COLCHETE_DIR = r'\]'
    t_DOIS_PONTOS = r'\:'
    t_PARENTESE_ESQ = r'\('
    t_PARENTESE_DIR = r'\)'
    t_ATRIBUICAO = r'\:\='
    t_OP_COMP = r'(\>|\<|\=\=|\!\=|\>\=|\<\=)'
    t_OP_MAT = r'\+|\-|\*|\/'
    t_PONTO = r'\.'

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Recognizes identifiers and reserved words
    def t_ID(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.type = self.reservadas.get(t.value, 'ID') # Check for reserved words
        return t
    
    def t_COMENTARIO(self, t):
        r'\{[^}]*\}' # Reconhece comentários como blocos entre { }, como em Pascal
        t.lexer.lineno += t.value.count('\n')
        pass  
    
    # Tracks line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}' at line '{t.lineno}'")
        t.lexer.skip(1)

    # Test function for lexer
    def test(self, data):
        # Give lexer some input
        self.lexer.input(data)

        # Tokenize and store results
        while True:
            tok = self.lexer.token()
            if not tok: 
                break      # No more input
            self.tokens_lista.append(tok)
            #print(tok)

# Exemplo de uso

file = open("exemplo1.sp","r")
programa = file.read()

lexer = Lex()
lexer.test(programa)
for tokens in lexer.tokens_lista:
 print(tokens)