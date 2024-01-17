from flask import Flask

app = Flask(__name__)

@app.route("/")
def hmepage():
    return "<p>CERTIFICADO AUTENTICO:</p><p>Certificado emitido em nome de: WGNER LOPES DINIZ</p><p>Documento ou TOKEN: 947.838.025-72</P><P>Evento: POP-OO T2.23 BONFIM FORMAÇÃO -</p><p>CLEUSON/ERICKSON</p><p>Certificado emitido por:</p><p>CEZÁRIOS CONSULTORIA E TREINAMENTOS</P><p>Documento:</p><p>09.629.728/0001-06</p><p>Responsável:</p><p>CLEUSON SILVA CEZÁRIOS</p><p>ATENÇÃO:</p><p> Verifique se os dados a cima confere com os dados apresentados ne certificado recebido.</p>"



if __name__ == "__main__":
    app.run(debug=True)