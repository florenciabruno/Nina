import json
import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Cargar respuestas desde JSON
with open("respuestas.json", "r", encoding="utf-8") as f:
    RESPUESTAS = json.load(f)


# Función principal del chatbot
def chatbot(mensajeUsuario: str):
    text = mensajeUsuario.lower()

    if any(word in text for word in ["horario", "hora", "abren", "cierran", "días", "atención", "atender", "atendido", "atenderte"]):
        reply = random.choice(RESPUESTAS["horario"])
    elif any(word in text for word in ["novedades", "noticias", "qué pasó", "que paso", "actualidad", "contame algo", "qué hay de nuevo", "que hay de nuevo"]):
        reply = random.choice(RESPUESTAS["noticias"])
    elif any(word in text for word in ["servicios", "qué hacen", "que hacen", "qué ofrecen", "que ofrecen", "ofrecen", "hacen"]):
        reply = random.choice(RESPUESTAS["servicios"])
    elif any(word in text for word in ["donaciones", "donar", "donarles", "donarles libros", "donar libros", "donar algo", "donación", "donacion", "cómo donar", "como donar", "cómo hacer una donación", "como hacer una donación", "cómo hacer una donacion", "como hacer una donacion"]):
        reply = random.choice(RESPUESTAS["donaciones"])
    elif any(word in text for word in ["sabes de mí", "quien soy", "qué sabes de mí", "qué sabes sobre mí", "qué sabes de mi", "qué sabes sobre mi", "quién soy", "me conoces", "me conoces?"]):
        reply = random.choice(RESPUESTAS["pregunta_sobre_usuario"])
    elif any(word in text for word in ["equipo", "quiénes son", "quienes son", "quiénes trabajan", "quienes trabajan", "quiénes forman parte", "quienes forman parte", "trabajan", "forman parte"]):
        reply = random.choice(RESPUESTAS["equipo"])
    elif any(word in text for word in ["catálogo", "catalogo", "cómo buscar", "como buscar", "buscar en el catálogo", "buscar en el catalogo", "cómo busco", "como busco", "ayuda para buscar", "ayuda para buscar en el catálogo", "ayuda para buscar en el catalogo", "ayuda para buscar un libro", "ayuda para buscar una obra"]):
        reply = random.choice(RESPUESTAS["catalogo"])
    elif any(word in text for word in ["chiste", "chistes", "broma", "bromas", "cuento un chiste", "contame un chiste", "cuéntame un chiste", "cuentame un chiste", "hazme reír", "hacerme reír", "reír", "reir", "reflexión", "reflexion", "reflexiones", "divertido", "gracioso"]):
        reply = random.choice(RESPUESTAS["chiste"])
    elif any(word in text for word in ["hola", "buenas", "buen día", "buenos días", "buenas tardes", "buenas noches", "un gusto", "hi", "hello", "menu", "menú"]):
        reply = random.choice(RESPUESTAS["hola"])
    elif any(word in text for word in ["gracias", "genia", "muchas gracias", "te lo agradezco", "muy amable"]):
        reply = random.choice(RESPUESTAS["gracias"])
    else:
        reply = random.choice(RESPUESTAS["default"])

    return reply


# Endpoint de la API
@app.route("/chat", methods=["POST"])
def chat_api():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"response": "No recibí ningún mensaje 😅"}), 400

    if user_message.lower() in ["salir", "chau", "adiós"]:
        return jsonify({"response": "¡Chau! 👋 Estoy acá por si necesitas hacer otra consulta"})

    respuesta = chatbot(user_message)
    return jsonify({"response": respuesta})


if __name__ == "__main__":
    app.run(debug=True)
