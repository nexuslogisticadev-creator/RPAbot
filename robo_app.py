from flask import Flask, jsonify, request
import robo

app = Flask(__name__)

@app.route('/api/robo/config', methods=['GET'])
def get_config():
    config = robo.carregar_configuracoes()
    if config:
        return jsonify({'sucesso': True, 'config': config})
    else:
        return jsonify({'erro': 'Configuração não encontrada'}), 404

@app.route('/api/robo/telegram', methods=['POST'])
def send_telegram():
    mensagem = request.json.get('mensagem')
    if not mensagem:
        return jsonify({'erro': 'Mensagem não fornecida'}), 400
    robo.enviar_telegram(mensagem)
    return jsonify({'sucesso': True, 'mensagem': mensagem})

# Adicione outros endpoints conforme necessário

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
