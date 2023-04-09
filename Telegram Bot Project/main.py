from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import constants as const
import responses as res
import image_conversion as imgconv

print('Bot started...')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hey, in order to get started type /help to get information how I work.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Sorry, information is on maintanance at the moment :(')


async def process_masage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg_text = str(update.message.text).lower()
    response = res.chat_responses(msg_text)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    app = Application.builder().token(const.API_KEY).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, process_masage))
    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=5)
