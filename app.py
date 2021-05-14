from enum import unique
from flask import Flask, jsonify, request
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# String de conexão
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=comp-dristri.database.windows.net;DATABASE=comp-dirtri;UID=admim;PWD=CompDistri1")

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

# As classes abaixo se associam aos schemas do servidor de dados no Azure
class Account(db.Model):
    __tablename__ = 'dim_accounts'
    account_id = db.Column(db.Integer, primary_key=True, unique=True)
    valor = db.Column(db.Float, nullable=False)

class Logs(db.Model):
    __tablename__ = 'fact_logs_operations_transactions'
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    log_id = db.Column(db.Integer, primary_key=True, unique=True)
    server_id = db.Column(db.Integer, nullable=False)
    operation_id = db.Column(db.Integer, nullable=False)
    operation_type = db.Column(db.String, nullable=False)
    account_id = db.Column(db.Integer, nullable=False)
    transaction_value = db.Column(db.Float, nullable=False)

@app.route("/", methods=["GET", "POST"])
def home():
	sTIA = "<p><strong>Jin Uema - 3184382-4</strong></p> <p><strong>Lucas Micael Accorsi Freitas da Silva - 3216484-1</strong></p> <p><strong>Tharcisio Neles - 3189120-9</strong></p>"
	return sTIA

@app.route("/deposito/<acnt>/<amt>", methods=["GET"])
def deposito(acnt,amt):

    # Ler o valor da conta no banco de dados e adiciona os valores da conta
    Acc = Account.query.filter_by(account_id = acnt).first()
    Acc.valor = Acc.valor + float(amt)
    db.session.commit()

    # Adicionar a transação nos logs
    dep = Logs(timestamp = datetime.now(), server_id=1, operation_id=1, operation_type='DEPOSITO', account_id=acnt, transaction_value=float(amt))
    db.session.add(dep)
    db.session.commit()

    ret = f'Depósito de: {str(amt)} na conta {str(acnt)} concluído!'
    return ret

@app.route("/saque/<acnt>/<amt>", methods=["GET"])
def saque(acnt,amt):

    # Ler o valor da conta no banco de dados e tira os valores da conta
    Acc = Account.query.filter_by(account_id = acnt).first()
    Acc.valor = Acc.valor - float(amt)
    db.session.commit()

    # Adicionar a transação nos logs
    dep = Logs(timestamp = datetime.now(), server_id=1, operation_id=2, operation_type='SAQUE', account_id=acnt, transaction_value=float(amt))
    db.session.add(dep)
    db.session.commit()

    ret = f'Saque de: {str(amt)} na conta {str(acnt)} concluído!'
    return ret

@app.route("/saldo/<acnt>", methods=["GET"])
def saldo(acnt):

	# Ler o valor da conta no banco de dados
    Acc = Account.query.filter_by(account_id = acnt).first()
    ret = f'O saldo da conta {str(acnt)} é de: {str(Acc.valor)}'

	# Adicionar a transação nos logs
    dep = Logs(timestamp = datetime.now(), server_id=1, operation_id=3, operation_type='SALDO', account_id=acnt, transaction_value=float(Acc.valor))
    db.session.add(dep)
    db.session.commit()

    return ret

@app.route("/transferencia/<acnt_orig>/<acnt_dest>/<amt>", methods=["GET"])
def transferencia(acnt_orig,acnt_dest,amt):

	# Ler o valor da conta no banco de dados & Remove valor da conta A
    Acc_A = Account.query.filter_by(account_id = acnt_orig).first()
    Acc_A.valor = Acc_A.valor - float(amt)
    db.session.commit()

	# Ler o valor da conta no banco de dados & Adiciona valor da conta B
    Acc_B = Account.query.filter_by(account_id = acnt_dest).first()
    Acc_B.valor = Acc_B.valor + float(amt)
    db.session.commit()
    
	# Adicionar a transação nos logs
    dep = Logs(timestamp = datetime.now(), server_id=1, operation_id=4, operation_type='TRANSFERENCIA', account_id=acnt_orig, transaction_value=float(amt))
    db.session.add(dep)
    db.session.commit()

    ret = f"Foi transferido {str(amt)} da conta {acnt_orig} para a {acnt_dest}."
    return ret

if __name__ == "__main__":
	app.run()
