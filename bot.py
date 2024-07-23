from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import logging

# Configura el logging para depuración
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Token del bot obtenido del BotFather
TOKEN = '7164312594:AAFM02rZbQYwhIu7Hus5Ur0aKVXvseutwsY'

# Diccionario con preguntas frecuentes y respuestas
FAQ = {
    '¿Cómo cultivo plantas sagradas?': 'Para cultivar plantas sagradas, asegúrate de proporcionar el suelo adecuado, la cantidad correcta de luz y agua, y seguir las guías específicas para cada planta.',
    '¿Qué métodos de extracción existen?': 'Los métodos comunes de extracción incluyen la destilación, la maceración y la infusión. Cada método tiene sus propias técnicas y aplicaciones.',
    '¿Cuáles son los cuidados básicos para las plantas sagradas?': 'Los cuidados básicos incluyen el riego adecuado, el control de plagas y enfermedades, y la poda cuando sea necesario.',
    # Agrega más preguntas y respuestas aquí
}

# Función para manejar comandos desconocidos
async def unknown(update: Update, context):
    await update.message.reply_text("Lo siento, no entiendo ese comando. Usa /start para ver las opciones disponibles.")

# Función para responder a preguntas frecuentes
async def faq_response(update: Update, context):
    text = update.message.text
    response = FAQ.get(text, "No tengo una respuesta para esa pregunta. Por favor, consulta la guía de cultivo.")
    await update.message.reply_text(response)

# Función para manejar el comando /start
async def start(update: Update, context):
    await update.message.reply_text('¡Hola! Envía tus preguntas frecuentes sobre plantas sagradas para obtener respuestas.')

# Nueva función para el comando /help
async def help_command(update: Update, context):
    await update.message.reply_text(
        "Aquí están los comandos disponibles:\n"
        "/start - Inicia el bot\n"
        "/faq - Responde a preguntas frecuentes\n"
        "/about - Información sobre el bot"
    )

# Función para manejar documentos
async def handle_document(update: Update, context):
    document = update.message.document
    await update.message.reply_text(f"Recibido documento: {document.file_name}")

# Función para manejar imágenes
async def handle_photo(update: Update, context):
    photo = update.message.photo[-1]  # Obtiene la foto más grande
    await update.message.reply_text(f"Recibida una foto con ID: {photo.file_id}")

def main():
    # Crea la instancia de la aplicación del bot
    application = Application.builder().token(TOKEN).build()

    # Maneja el comando /start
    application.add_handler(CommandHandler('start', start))

    # Maneja el comando /help
    application.add_handler(CommandHandler('help', help_command))

    # Maneja mensajes que coincidan con preguntas frecuentes
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, faq_response))

    # Maneja documentos enviados
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))

    # Maneja imágenes enviadas
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Maneja comandos desconocidos
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Inicia el bot
    application.run_polling()

if __name__ == '__main__':
    main()
