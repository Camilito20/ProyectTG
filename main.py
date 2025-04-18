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
application.add_handler( CommandHandler( "institute", TodoContollrer.teachers))

"""Instituto 'Военно-инженерный институт'"""
application.add_handler( CommandHandler( "Bii", TodoContollrer.ВИИ))
application.add_handler( CommandHandler( "information_BII", TodoContollrer.information_BII))
application.add_handler( CommandHandler( "address_BII", TodoContollrer.direccion_BII))
application.add_handler( CommandHandler( "techers_BII", TodoContollrer.techers_BII))


"""Instituto 'Гуманитарный институт'"""
application.add_handler( CommandHandler( "Gi", TodoContollrer.ГИ))
application.add_handler( CommandHandler( "address_GI", TodoContollrer.direccion_BII))
application.add_handler( CommandHandler( "techers_GI", TodoContollrer.profesir_GI))
application.add_handler( CommandHandler( "gi_1", TodoContollrer.gi_1))
application.add_handler( CommandHandler( "gi_2", TodoContollrer.gi_2))
application.add_handler( CommandHandler( "gi_3", TodoContollrer.gi_3))
application.add_handler( CommandHandler( "gi_4", TodoContollrer.gi_4))
application.add_handler( CommandHandler( "gi_5", TodoContollrer.gi_5))
application.add_handler( CommandHandler( "gi_6", TodoContollrer.gi_6))
application.add_handler( CommandHandler( "gi_7", TodoContollrer.gi_7))
application.add_handler( CommandHandler( "gi_8", TodoContollrer.gi_8))
application.add_handler( CommandHandler( "gi_9", TodoContollrer.gi_9))
application.add_handler( CommandHandler( "gi_9", TodoContollrer.gi_9))
application.add_handler( CommandHandler( "gi_10", TodoContollrer.gi_10))

"""Institudo 'Инженерно-строительный институт'"""
application.add_handler( CommandHandler( "ICI", TodoContollrer.ICI))
application.add_handler( CommandHandler( "address_ICI", TodoContollrer.direccion_BII))
application.add_handler( CommandHandler( "techers_ICI", TodoContollrer.profesores_ICI))
application.add_handler( CommandHandler( "ici_1", TodoContollrer.ici_1))
application.add_handler( CommandHandler( "ici_2", TodoContollrer.ici_2))
application.add_handler( CommandHandler( "ici_3", TodoContollrer.ici_3))
application.add_handler( CommandHandler( "ici_4", TodoContollrer.ici_4))
application.add_handler( CommandHandler( "ici_5", TodoContollrer.ici_5))

"""Институт архитектуры и дизайна"""
application.add_handler( CommandHandler( "IAID", TodoContollrer.iaid))
application.add_handler( CommandHandler( "address_IAID", TodoContollrer.adress_IAID))
application.add_handler( CommandHandler( "techers_IAID", TodoContollrer.profesores_ICI))
application.add_handler( CommandHandler( "IAID_1", TodoContollrer.iaid_1))
application.add_handler( CommandHandler( "IAID_2", TodoContollrer.iaid_2))
application.add_handler( CommandHandler( "IAID_3", TodoContollrer.iaid_3))
application.add_handler( CommandHandler( "IAID_4", TodoContollrer.iaid_4))
application.add_handler( CommandHandler( "IAID_5", TodoContollrer.iaid_5))
application.add_handler( CommandHandler( "IAID_6", TodoContollrer.iaid_6))




application.run_polling(allowed_updates=Update.ALL_TYPES)
