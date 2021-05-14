from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	sTIA = "<p><strong>Jin Uema - 3184382-4</strong></p> <p><strong>Lucas Micael Accorsi Freitas da Silva - 3216484-1</strong></p> <p><strong>Tharcisio Neles - 3189120-9</strong></p>"
	return sTIA

@app.route("/deposito/<acnt>/<amt>", methods=["GET"])
def deposito(acnt,amt):
	hArgs = {
        	"Operation" : "Deposito",
        	"Account" : acnt,
        	"Amount" : amt,
	}
	return jsonify(hArgs)

@app.route("/saque/<acnt>/<amt>", methods=["GET"])
def saque(acnt,amt):
	hArgs = {
        	"Operation" : "Saque",
        	"Account" : acnt,
        	"Amount" : amt,
	}
	return jsonify(hArgs)

@app.route("/saldo/<acnt>", methods=["GET"])
def saldo(acnt):
	hArgs = {
		"Operation" : "Saldo",
		"Amount" : acnt,
	}
	return jsonify(hArgs)

@app.route("/transferencia/<acnt_orig>/<acnt_dest>/<amt>", methods=["GET"])
def transferencia(acnt_orig,acnt_dest,amt):
	hArgs = {
		"Operation" : "Transferencia",
		"Account A" : acnt_orig,
		"Account B" : acnt_dest,
		"Amount" : amt,
	}
	return jsonify(hArgs)

if __name__ == "__main__":
	app.run()
