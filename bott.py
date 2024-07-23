from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Reemplaza con tu token
TOKEN = '7164312594:AAFM02rZbQYwhIu7Hus5Ur0aKVXvseutwsY'

# Manejador de comandos /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Estoy aquí para ayudarte.')

# Manejador de documentos
async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = update.message.document
    await update.message.reply_text(f"Documento recibido: {file.file_name}")

# Manejador de fotos
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo = update.message.photo[-1]
    await update.message.reply_text(f"Foto recibida: {photo.file_id}")

# Función principal
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Agregar manejadores de comandos y mensajes
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Document.ALL, handle_document))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    # Ejecutar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
