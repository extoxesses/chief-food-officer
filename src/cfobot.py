# --- Bot modules ---------
from modules.breakfast import Breakfast
from modules.config import Config

import constants.constants as Const


# --- Third part modules ---------
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton

import logging
logging.basicConfig(format=Const.LOGGER_FORMAT, level=logging.INFO)
LOGGER = logging.getLogger('CFO-Bot')



class CfoBot:
  def __init__(self, config):
    self.bot = Updater(config.TOKEN)
    self.dispatcher = self.bot.dispatcher
    self.createBot(config)
    self.breakfast = None

  def createBot(self, config):
    LOGGER.info('Start bot configuration...')

    startBreakfastPollHandler = CommandHandler("startBreakfastPoll", lambda up, ctx: self.startBreakfastPoll(up, ctx))
    self.dispatcher.add_handler(startBreakfastPollHandler)
    
    stopBreakfastPollHandler = CommandHandler("stopBreakfastPoll", lambda up, ctx: self.stopBreakfastPoll(up, ctx))
    self.dispatcher.add_handler(stopBreakfastPollHandler)

    addCoffeeHandler = CommandHandler("addCoffee", lambda up, ctx: self.addCoffee(up, ctx))
    self.dispatcher.add_handler(addCoffeeHandler)

    addCappuccinoHandler = CommandHandler("addCappuccino", lambda up, ctx: self.addCappuccino(up, ctx))
    self.dispatcher.add_handler(addCappuccinoHandler)

    addBriocheHandler = CommandHandler("addBrioche", lambda up, ctx: self.addBrioche(up, ctx))
    self.dispatcher.add_handler(addBriocheHandler)

    addMignonHandler = CommandHandler("addMignon", lambda up, ctx: self.addMignon(up, ctx))
    self.dispatcher.add_handler(addMignonHandler)

    # dp.add_error_handler(Helper.errorHandler)
    LOGGER.info('Bot configuration completed!')

  def startBot(self):
    LOGGER.info('Listener started...')
    self.bot.start_polling()
    self.bot.idle()


  def startBreakfastPoll(self, update, context):
    LOGGER.info('Starting a new breakfast poll...')
    self.breakfast = Breakfast()
    keyboardLayout = [[KeyboardButton('/addcoffee'), 'Cappuccino'], ['Brioche', 'Mignon'], ['Ordina...']]
    keyboard = ReplyKeyboardMarkup(keyboardLayout, one_time_keyboard=False)
    context.message.reply_text("It's breakfast time...", reply_markup=keyboard)


  def stopBreakfastPoll(self, update, context):
    if (self.breakfast == None):
      LOGGER.info('No poll started!')
      context.message.reply_text("Attenzione! Non e' stato creato nessuno poll!")
    else:
      LOGGER.info('Breakfast poll completed!')
      context.message.reply_text(self.breakfast.toMessage())
      self.breakfast = None
  
  def addCoffee(self, update, context):
    if (self.breakfast == None):
      self.coffee = self.coffee + 1

  def addCappuccino(self, update, context):
    if (self.breakfast == None):
      self.cappuccino = self.cappuccino + 1

  def addBrioche(self, update, context):
    if (self.breakfast == None):
      self.brioche = self.brioche + 1

  def addMignon(self, update, context):
    if (self.breakfast == None):
      self.mignon = self.mignon + 1
