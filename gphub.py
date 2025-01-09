from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Define the function to process the input and format the output
async def process_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text

    # Split the input by commas
    parts = user_message.split(", ")

    # Validate input
    if len(parts) != 8:
        await update.message.reply_text("দয়া করে সঠিক ফরম্যাটে তথ্য দিন: নাম, লেখক, প্রস্তুতকারক, ধরন, লিংক, তারিখ, পর্ব, সময়।")
        return

    name, writer, producer, genre, link, date, part, time = parts

    # Create the formatted output
    formatted_message = (
        f"**গল্পের নাম:-** {name}\n"
        f"**লেখক:-** {writer}\n"
        f"**প্রস্তুতকারক:-** {producer}\n"
        f"**গল্পের ধরন:-** {genre}\n"
        f"**লিংক:-** {link}\n"
        f"**প্রকাশ তারিখ:-** {date}\n"
        f"**পর্ব:-** {part}\n"
        f"**সময়:-** {time}"
    )

    # Send the formatted message to the channel
    await context.bot.send_message(chat_id="@golpoohub", text=formatted_message, parse_mode="Markdown")

# Start command to welcome the user
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("আপনার গল্পের তথ্য পাঠান এই ফরম্যাটে: নাম, লেখক, প্রস্তুতকারক, ধরন, লিংক, তারিখ, পর্ব, সময়।")

# Main function to run the bot
def main():
    # Set your bot token
    token = "7678457397:AAGuHvDy3xGgBAS9HwOhxftifS0DCT0nC-M"
    
    application = Application.builder().token(token).build()

    # Register the commands and message handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

    # Start the bot
    application.run_polling()

# Run the bot
if __name__ == "__main__":
    main()
