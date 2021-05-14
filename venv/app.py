from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Função que chama a homepage, Dentro dela se encontram os TIAs dos alunos.
    """

    sTIA = '''
    <p><strong>Jin Uema - 3184382-4</strong></p>
    <p><strong>Lucas Micael Accorsi Freitas da Silva - 3216484-1</strong></p>
    <p><strong>Tharc&iacute;sio N&eacute;les - 3189120-9</strong></p>   
    '''

    return sTIA

@app.route('/deposito/<acnt>/<amt>', methods=['GET'])
def deposito(acnt,amt):
    """
    Aumenta o saldo da conta acnt pelo valor amt.
    """

    hArgs = {
        'Operation' : 'Deposito',
        'Account' : acnt,
        'Amount' : amt,
    }
    return jsonify(hArgs)

@app.route('/saque/<acnt>/<amt>', methods=['GET'])
def saque(acnt,amt):
    """
    Diminui o saldo da conta acnt pelo valor amt.
    """

    hArgs = {
        'Operation' : 'Saque',
        'Account' : acnt,
        'Amount' : amt,
    }
    return jsonify(hArgs)

@app.route('/saldo/<acnt>', methods=['GET'])
def saldo(acnt):
    """
    Diminui o saldo da conta acnt pelo valor amt.
    """

    hArgs = {
        'Operation' : 'Saldo',
        'Amount' : acnt,
    }
    return jsonify(hArgs)

@app.route('transferencia/<acnt_orig>/<acnt_dest>/<amt>', methods=['GET'])
def transferencia(acnt_orig,acnt_dest,amt):
    """
    Transferência da conta acnt_orig para a conta acnt_dest do valor amt.
    """

    # Saque da conta A o amt
    # Deposito da conta B o amt 

    hArgs = {
        'Operation' : 'Transferencia',
        'Account A' : acnt_orig,
        'Account B' : acnt_dest,
        'Amount' : amt,
    }
    
    return jsonify(hArgs)