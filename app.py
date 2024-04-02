from flask import *
import analizador_lexico as lex

app = Flask("app")

@app.route("/")
def hola_mundo():
    return render_template("index.html")

@app.route('/api/v1/lexer', methods= ['POST'])
def lexer ():
    data = request.get_json()
    code = data.get('code')
    
    lex.lexer.input(code)
    
    tokens = []
    while True:
        tok = lex.lexer.token()
        if not tok:
            break 
        tokens.append({
            'type': tok.type,
            'value': tok.value,
            'line' : tok.lineno,
            'lexpos': tok.lexpos
        })
        
        
    print("code:", code)
    print("Tokens:",tokens)  
    
    return render_template('resultado.html', code=code, tokens=tokens) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)