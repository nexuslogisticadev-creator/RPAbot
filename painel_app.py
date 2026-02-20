from flask import Flask, jsonify, request
import painel

app = Flask(__name__)

@app.route('/api/painel/status', methods=['GET'])
def painel_status():
    # Exemplo: retornar status do painel
    return jsonify({'status': 'Painel ativo'})

# Adicione endpoints conforme as funções do painel.py

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
