from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

class InstitutionalTelegramBot:
    def __init__(self, config, trading_core):
        self.updater = Updater(config['telegram_token'])
        self.core = trading_core
        
        # Institutional-grade command handlers
        handlers = [
            CommandHandler('portfolio', self.show_portfolio),
            CommandHandler('buy', self.execute_buy_order),
            CommandHandler('autotrade', self.toggle_autotrade)
        ]
        
        for handler in handlers:
            self.updater.dispatcher.add_handler(handler)

    def show_portfolio(self, update: Update, context: CallbackContext):
        portfolio = self.core.get_portfolio()
        msg = (f"🏦 Institutional Portfolio:\n"
               f"Total Value: ${portfolio['total']:,.2f}\n"
               f"Active Positions: {portfolio['positions']}\n"
               f"24h Return: {portfolio['daily_return']}%")
        update.message.reply_text(msg)

    def execute_buy_order(self, update: Update, context: CallbackContext):
        args = context.args
        if len(args) == 3:  # /buy [chain] [token] [amount]
            self.core.manual_trade(args[0], args[1], float(args[2]))
            update.message.reply_text(f"⚡ Institutional Order Executed: {args[1]}")

    def toggle_autotrade(self, update: Update, context: CallbackContext):
        new_state = self.core.toggle_autotrade()
        status = "ENABLED" if new_state else "DISABLED"
        update.message.reply_text(f"🤖 Autotrade Status: {status}")
