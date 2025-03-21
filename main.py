from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

from Controles.todoController import TodoContollrer

application = ApplicationBuilder().token("7858416292:AAHK42x7K_TF1bPFhQT_wO8UiH0Fr25boSA").build()
#Comandos
"""MENU PRINCIPAL"""
application.add_handler( CommandHandler( "menu", TodoContollrer.menu))
application.add_handler( CommandHandler( "start", TodoContollrer.start))
application.add_handler( CommandHandler( "SFU", TodoContollrer.SFU))
application.add_handler( CommandHandler( "help", TodoContollrer.help_command))
application.add_handler( CommandHandler( "info_bot", TodoContollrer.Info))
application.add_handler( CommandHandler("menu_SFU", TodoContollrer.menu_sfu))
application.add_handler( CommandHandler( "ekursi", TodoContollrer.ekursi))
application.add_handler( CommandHandler("moi_sfu", TodoContollrer.moi_sfu))
application.add_handler( CommandHandler( "teachers", TodoContollrer.teachers))
"""MENU INSTITUTOS Y KAFEDRAS"""
application.add_handler( CommandHandler( "Bii", TodoContollrer.ВИИ))
application.add_handler( CommandHandler( "Gi", TodoContollrer.ГИ))
application.add_handler( CommandHandler( "gi_1", TodoContollrer.gi_1))


application.run_polling(allowed_updates=Update.ALL_TYPES)
