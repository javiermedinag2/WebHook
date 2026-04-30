from flask import Flask, request
# Este código crea un servidor Flask que escucha en el puerto 5000 para recibir solicitudes POST en la ruta /webhook. Cuando se recibe una solicitud, se extraen los datos JSON y se imprimen en la consola. Puedes personalizar el procesamiento de los datos según tus necesidades.   

# Para ejecutar este código, asegúrate de tener Flask instalado en tu entorno de Python. Puedes instalarlo usando pip:
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.get_json()
    print("Datos recibidos por NGROK desde Github:", data)
    # En este punto, puedes procesar los datos recibidos como desees
    return "Webhook recibido exitosamente", 200
if __name__ == '__main__':
    app.run(port=5000)
    