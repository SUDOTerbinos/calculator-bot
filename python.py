from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import re

TELEGRAM_BOT_TOKEN = "7722903971:AAGLv2brYFSggIc4DscNHJTxL9AsmBNHkko"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

async def start(update: Update, context):
    """Handles the /start command."""
    await update.message.reply_text("Hi! I'm a calculator bot made by Terbinos for other info click this link https://t.me/SUDOswap1 (please subscribe it). Use the format 5+3 to calculate.")

async def calculator(update: Update, context):
    """Handles calculator commands."""
    user_input = update.message.text.strip()

    pattern = r"^(\d+)\s*([+\-*/])\s*(\d+)$"
    match = re.match(pattern, user_input)
    
    if match:
        num1 = float(match.group(1))
        operation = match.group(2)
        num2 = float(match.group(3))
        
        if operation == "+":
            result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1, num2)
        elif operation == "/":
            result = divide(num1, num2)
        
        await update.message.reply_text(f"Result: {result}")
    else:
        await update.message.reply_text("Usage: Enter your calculation in the form '5+3' or '10*5'")

def main():
    """Main function to start the bot."""
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculator))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
