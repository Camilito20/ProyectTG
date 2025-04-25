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

"""Институт инженерной физики и радиоэлектроники"""
application.add_handler( CommandHandler( "IIFIRE", TodoContollrer.iifire))
application.add_handler( CommandHandler( "techers_IIFIRE", TodoContollrer.profesore_iifire))
application.add_handler( CommandHandler( "address_IIFIRE", TodoContollrer.direccion_IIFIRE))
application.add_handler( CommandHandler( "IIFIRE_1", TodoContollrer.iifire_1))
application.add_handler( CommandHandler( "IIFIRE_2", TodoContollrer.iifire_2))
application.add_handler( CommandHandler( "IIFIRE_3", TodoContollrer.iifire_3))
application.add_handler( CommandHandler( "IIFIRE_4", TodoContollrer.iifire_4))
application.add_handler( CommandHandler( "IIFIRE_5", TodoContollrer.iifire_5))
application.add_handler( CommandHandler( "IIFIRE_6", TodoContollrer.iifire_6))
application.add_handler( CommandHandler( "IIFIRE_7", TodoContollrer.iifire_7))
application.add_handler( CommandHandler( "IIFIRE_8", TodoContollrer.iifire_8))
application.add_handler( CommandHandler( "IIFIRE_9", TodoContollrer.iifire_9))
application.add_handler( CommandHandler( "IIFIRE_10", TodoContollrer.iifire_10))
application.add_handler( CommandHandler( "IIFIRE_11", TodoContollrer.iifire_11))
application.add_handler( CommandHandler( "IIFIRE_12", TodoContollrer.iifire_12))
application.add_handler( CommandHandler( "IIFIRE_13", TodoContollrer.iifire_13))
application.add_handler( CommandHandler( "IIFIRE_14", TodoContollrer.iifire_14))
application.add_handler( CommandHandler( "IIFIRE_15", TodoContollrer.iifire_15))

"""Институт космических и информационных технологий"""
application.add_handler( CommandHandler( "IKIT", TodoContollrer.IKIT))
application.add_handler( CommandHandler( "address_IKIT", TodoContollrer.direccion_IKIT))
application.add_handler( CommandHandler( "techers_IKIT", TodoContollrer.profesores_IKIT))
application.add_handler( CommandHandler( "IKIT_1", TodoContollrer.IKIT_1))
application.add_handler( CommandHandler( "IKIT_2", TodoContollrer.IKIT_2))
application.add_handler( CommandHandler( "IKIT_3", TodoContollrer.IKIT_3))
application.add_handler( CommandHandler( "IKIT_4", TodoContollrer.IKIT_4))
application.add_handler( CommandHandler( "IKIT_5", TodoContollrer.IKIT_5))
application.add_handler( CommandHandler( "IKIT_6", TodoContollrer.IKIT_6))
application.add_handler( CommandHandler( "IKIT_7", TodoContollrer.IKIT_7))
application.add_handler( CommandHandler( "IKIT_8", TodoContollrer.IKIT_8))
application.add_handler( CommandHandler( "IKIT_9", TodoContollrer.IKIT_9))
application.add_handler( CommandHandler( "IKIT_10", TodoContollrer.IKIT_10))
application.add_handler( CommandHandler( "IKIT_11", TodoContollrer.IKIT_11))
application.add_handler( CommandHandler( "IKIT_12", TodoContollrer.IKIT_12))
application.add_handler( CommandHandler( "IKIT_13", TodoContollrer.IKIT_13))



application.run_polling(allowed_updates=Update.ALL_TYPES)
