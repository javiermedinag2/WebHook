from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.get_json()
    print("Datos recibidos por NGROK:", data)
    # En este punto, puedes procesar los datos recibidos como desees
    return "Webhook recibido exitosamente", 200
if __name__ == '__main__':
    app.run(port=5000)
    