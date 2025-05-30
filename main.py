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
application.add_handler( CommandHandler( "payments", TodoContollrer.pagos))
application.add_handler( CommandHandler( "stu", TodoContollrer.stu))
application.add_handler( CommandHandler( "Inte", TodoContollrer.Inte))
application.add_handler( CommandHandler( "resi", TodoContollrer.resi))
application.add_handler( CommandHandler( "Prepa", TodoContollrer.Prepa))
application.add_handler( CommandHandler( "Anti", TodoContollrer.Anti))
application.add_handler( CommandHandler( "publi", TodoContollrer.publi))
application.add_handler( CommandHandler( "event", TodoContollrer.event))
application.add_handler( CommandHandler( "servi", TodoContollrer.servi))


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

"""Институт математики и фундаментальной информатики"""
application.add_handler( CommandHandler( "IMIFI", TodoContollrer.IMIFI))
application.add_handler( CommandHandler( "address_IMIFI", TodoContollrer.direccion_IMIFI))
application.add_handler( CommandHandler( "techers_IMIFI", TodoContollrer.profesores_IMIFI))
application.add_handler( CommandHandler( "IMIFI_1", TodoContollrer.IMIFI_1))
application.add_handler( CommandHandler( "IMIFI_2", TodoContollrer.IMIFI_2))
application.add_handler( CommandHandler( "IMIFI_3", TodoContollrer.IMIFI_3))
application.add_handler( CommandHandler( "IMIFI_4", TodoContollrer.IMIFI_4))
application.add_handler( CommandHandler( "IMIFI_5", TodoContollrer.IMIFI_5))
application.add_handler( CommandHandler( "IMIFI_6", TodoContollrer.IMIFI_6))
application.add_handler( CommandHandler( "IMIFI_7", TodoContollrer.IMIFI_7))
application.add_handler( CommandHandler( "IMIFI_8", TodoContollrer.IMIFI_8))
application.add_handler( CommandHandler( "IMIFI_9", TodoContollrer.IMIFI_9))
application.add_handler( CommandHandler( "IMIFI_10", TodoContollrer.IMIFI_10))

""""Институт нефти и газа"""
application.add_handler( CommandHandler( "INIG", TodoContollrer.INIG))
application.add_handler( CommandHandler( "address_INIG", TodoContollrer.direccion_INIG))
application.add_handler( CommandHandler( "techers_INIG", TodoContollrer.profesoeres_INIG))
application.add_handler( CommandHandler( "INIG_1", TodoContollrer.INIG_1))
application.add_handler( CommandHandler( "INIG_2", TodoContollrer.INIG_2))
application.add_handler( CommandHandler( "INIG_3", TodoContollrer.INIG_3))
application.add_handler( CommandHandler( "INIG_4", TodoContollrer.INIG_4))
application.add_handler( CommandHandler( "INIG_5", TodoContollrer.INIG_5))
application.add_handler( CommandHandler( "INIG_6", TodoContollrer.INIG_6))
application.add_handler( CommandHandler( "INIG_7", TodoContollrer.INIG_7))
application.add_handler( CommandHandler( "INIG_8", TodoContollrer.INIG_8))
application.add_handler( CommandHandler( "INIG_9", TodoContollrer.INIG_9))
application.add_handler( CommandHandler( "INIG_10", TodoContollrer.INIG_10))
application.add_handler( CommandHandler( "INIG_11", TodoContollrer.INIG_11))
application.add_handler( CommandHandler( "INIG_12", TodoContollrer.INIG_12))
application.add_handler( CommandHandler( "INIG_13", TodoContollrer.INIG_13))
application.add_handler( CommandHandler( "INIG_14", TodoContollrer.INIG_14))
application.add_handler( CommandHandler( "INIG_15", TodoContollrer.INIG_15))
application.add_handler( CommandHandler( "INIG_16", TodoContollrer.INIG_16))

"""Институт педагогики, психологии и социологии"""
application.add_handler( CommandHandler( "IPPS", TodoContollrer.IPPS))
application.add_handler( CommandHandler( "address_IPPS", TodoContollrer.direccion_IPPS))
application.add_handler( CommandHandler( "techers_IPPS", TodoContollrer.profesores_IPPS))
application.add_handler( CommandHandler( "IPPS_1", TodoContollrer.IPPS_1))
application.add_handler( CommandHandler( "IPPS_2", TodoContollrer.IPPS_2))
application.add_handler( CommandHandler( "IPPS_3", TodoContollrer.IPPS_3))
application.add_handler( CommandHandler( "IPPS_4", TodoContollrer.IPPS_4))
application.add_handler( CommandHandler( "IPPS_5", TodoContollrer.IPPS_5))
application.add_handler( CommandHandler( "IPPS_6", TodoContollrer.IPPS_6))
application.add_handler( CommandHandler( "IPPS_7", TodoContollrer.IPPS_7))
application.add_handler( CommandHandler( "IPPS_8", TodoContollrer.IPPS_8))

"""Институт Севера и Арктики"""
application.add_handler( CommandHandler( "ISIA", TodoContollrer.ISIA))
application.add_handler( CommandHandler( "address_ISIA", TodoContollrer.direccion_ISIA))
application.add_handler( CommandHandler( "techers_ISIA", TodoContollrer.profesores_ISIA))
application.add_handler( CommandHandler( "ISIA_1", TodoContollrer.ISIA_1))
application.add_handler( CommandHandler( "ISIA_2", TodoContollrer.ISIA_2))
application.add_handler( CommandHandler( "ISIA_3", TodoContollrer.ISIA_3))
application.add_handler( CommandHandler( "ISIA_4", TodoContollrer.ISIA_4))

"""Институт физической культуры, спорта и туризма"""
application.add_handler( CommandHandler( "IFKSIT", TodoContollrer.IFRSIT))
application.add_handler( CommandHandler( "techers_IFKSIT", TodoContollrer.profesores_IFRSIT))
application.add_handler( CommandHandler( "address_IFKSIT", TodoContollrer.direccion_IFRSIT))
application.add_handler( CommandHandler( "IFKSIT_1", TodoContollrer.IFRSIT_1))
application.add_handler( CommandHandler( "IFKSIT_2", TodoContollrer.IFRSIT_2))
application.add_handler( CommandHandler( "IFKSIT_3", TodoContollrer.IFRSIT_3))
application.add_handler( CommandHandler( "IFKSIT_4", TodoContollrer.IFRSIT_4))
application.add_handler( CommandHandler( "IFKSIT_5", TodoContollrer.IFRSIT_5))
application.add_handler( CommandHandler( "IFKSIT_6", TodoContollrer.IFRSIT_6))

"""Институт фундаментальной биологии и биотехнологии"""
application.add_handler( CommandHandler( "IFBIBT", TodoContollrer.IFBIBT))
application.add_handler( CommandHandler( "address_IFBIBT", TodoContollrer.direccion_IFBIBT))
application.add_handler( CommandHandler( "techers_IFBIBT", TodoContollrer.profesores_IFBIBT))
application.add_handler( CommandHandler( "IFBIBT_1", TodoContollrer.IFBIBT_1))
application.add_handler( CommandHandler( "IFBIBT_2", TodoContollrer.IFBIBT_2))
application.add_handler( CommandHandler( "IFBIBT_3", TodoContollrer.IFBIBT_3))
application.add_handler( CommandHandler( "IFBIBT_4", TodoContollrer.IFBIBT_4))
application.add_handler( CommandHandler( "IFBIBT_5", TodoContollrer.IFBIBT_5))
application.add_handler( CommandHandler( "IFBIBT_6", TodoContollrer.IFBIBT_6))
application.add_handler( CommandHandler( "IFBIBT_7", TodoContollrer.IFBIBT_7))
application.add_handler( CommandHandler( "IFBIBT_8", TodoContollrer.IFBIBT_8))
application.add_handler( CommandHandler( "IFBIBT_9", TodoContollrer.IFBIBT_9))
application.add_handler( CommandHandler( "IFBIBT_10", TodoContollrer.IFBIBT_10))
application.add_handler( CommandHandler( "IFBIBT_11", TodoContollrer.IFBIBT_11))
application.add_handler( CommandHandler( "IFBIBT_12", TodoContollrer.IFBIBT_12))
application.add_handler( CommandHandler( "IFBIBT_13", TodoContollrer.IFBIBT_13))
application.add_handler( CommandHandler( "IFBIBT_14", TodoContollrer.IFBIBT_14))

"""Институт цветных металлов"""
application.add_handler( CommandHandler( "ITSM", TodoContollrer.ITSM))
application.add_handler( CommandHandler( "address_ITSM", TodoContollrer.direccion_ITSM))
application.add_handler( CommandHandler( "techers_ITSM", TodoContollrer.profesores_ITSM))
application.add_handler( CommandHandler( "ITSM_1", TodoContollrer.ITSM_1))
application.add_handler( CommandHandler( "ITSM_2", TodoContollrer.ITSM_2))
application.add_handler( CommandHandler( "ITSM_3", TodoContollrer.ITSM_3))
application.add_handler( CommandHandler( "ITSM_4", TodoContollrer.ITSM_4))
application.add_handler( CommandHandler( "ITSM_5", TodoContollrer.ITSM_5))
application.add_handler( CommandHandler( "ITSM_6", TodoContollrer.ITSM_6))
application.add_handler( CommandHandler( "ITSM_7", TodoContollrer.ITSM_7))
application.add_handler( CommandHandler( "ITSM_8", TodoContollrer.ITSM_8))
application.add_handler( CommandHandler( "ITSM_9", TodoContollrer.ITSM_9))
application.add_handler( CommandHandler( "ITSM_10", TodoContollrer.ITSM_10))
application.add_handler( CommandHandler( "ITSM_11", TodoContollrer.ITSM_11))
application.add_handler( CommandHandler( "ITSM_12", TodoContollrer.ITSM_12))
application.add_handler( CommandHandler( "ITSM_13", TodoContollrer.ITSM_13))
application.add_handler( CommandHandler( "ITSM_14", TodoContollrer.ITSM_14))

"""Институт экологии и географии"""
application.add_handler( CommandHandler( "IEIG", TodoContollrer.IEIG))
application.add_handler( CommandHandler( "address_IEIG", TodoContollrer.direccion_IEIG))
application.add_handler( CommandHandler( "techers_IEIG", TodoContollrer.profesores_IEIG))
application.add_handler( CommandHandler( "IEIG_1", TodoContollrer.IEIG_1))
application.add_handler( CommandHandler( "IEIG_2", TodoContollrer.IEIG_2))
application.add_handler( CommandHandler( "IEIG_3", TodoContollrer.IEIG_3))
application.add_handler( CommandHandler( "IEIG_4", TodoContollrer.IEIG_4))
application.add_handler( CommandHandler( "IEIG_5", TodoContollrer.IEIG_5))

"""Институт гастрономии"""
application.add_handler( CommandHandler( "IG", TodoContollrer.IG))
application.add_handler( CommandHandler( "address_IG", TodoContollrer.dereccion_IG))
application.add_handler( CommandHandler( "techers_IG", TodoContollrer.profesores_IG))
application.add_handler( CommandHandler( "IG_1", TodoContollrer.IG_1))
application.add_handler( CommandHandler( "IG_2", TodoContollrer.IG_2))
application.add_handler( CommandHandler( "IG_3", TodoContollrer.IG_3))
application.add_handler( CommandHandler( "IG_4", TodoContollrer.IG_4))
application.add_handler( CommandHandler( "IG_5", TodoContollrer.IG_5))
application.add_handler( CommandHandler( "IG_6", TodoContollrer.IG_6))
application.add_handler( CommandHandler( "IG_7", TodoContollrer.IG_7))

"""Институт торговли и сферы услуг"""
application.add_handler( CommandHandler( "ITISU", TodoContollrer.ITISU))
application.add_handler( CommandHandler( "address_ITISU", TodoContollrer.direccion_ITISU))
application.add_handler( CommandHandler( "techers_ITISU", TodoContollrer.profesores_ITISU))
application.add_handler( CommandHandler( "ITISU_1", TodoContollrer.ITISU_1))
application.add_handler( CommandHandler( "ITISU_2", TodoContollrer.ITISU_2))
application.add_handler( CommandHandler( "ITISU_3", TodoContollrer.ITISU_3))
application.add_handler( CommandHandler( "ITISU_4", TodoContollrer.ITISU_4))
application.add_handler( CommandHandler( "ITISU_5", TodoContollrer.ITISU_5))
application.add_handler( CommandHandler( "ITISU_6", TodoContollrer.ITISU_6))

"""Институт управления бизнес-процессами"""
application.add_handler( CommandHandler( "IUBP", TodoContollrer.IUBP))
application.add_handler( CommandHandler( "address_IUBP", TodoContollrer.direccion_IUBP))
application.add_handler( CommandHandler( "techers_IUBP", TodoContollrer.profesores_IUBP))
application.add_handler( CommandHandler( "IUBP_1", TodoContollrer.IUBP_1))
application.add_handler( CommandHandler( "IUBP_2", TodoContollrer.IUBP_2))
application.add_handler( CommandHandler( "IUBP_3", TodoContollrer.IUBP_3))
application.add_handler( CommandHandler( "IUBP_4", TodoContollrer.IUBP_4))
application.add_handler( CommandHandler( "IUBP_5", TodoContollrer.IUBP_5))
application.add_handler( CommandHandler( "IUBP_6", TodoContollrer.IUBP_6))

"""Институт экономики, государственного управления и финансов"""
application.add_handler( CommandHandler( "IEGUIF", TodoContollrer.IEGUIF))
application.add_handler( CommandHandler( "address_IEGUIF", TodoContollrer.direccion_IEGUIF))
application.add_handler( CommandHandler( "techers_IEGUIF", TodoContollrer.profesores_IEGUIF))
application.add_handler( CommandHandler( "IEGUIF_1", TodoContollrer.IEGUIF_1))
application.add_handler( CommandHandler( "IEGUIF_2", TodoContollrer.IEGUIF_2))
application.add_handler( CommandHandler( "IEGUIF_3", TodoContollrer.IEGUIF_3))
application.add_handler( CommandHandler( "IEGUIF_4", TodoContollrer.IEGUIF_4))
application.add_handler( CommandHandler( "IEGUIF_5", TodoContollrer.IEGUIF_5))
application.add_handler( CommandHandler( "IEGUIF_6", TodoContollrer.IEGUIF_6))
application.add_handler( CommandHandler( "IEGUIF_7", TodoContollrer.IEGUIF_7))
application.add_handler( CommandHandler( "IEGUIF_8", TodoContollrer.IEGUIF_8))

"""Политехнический институт"""
application.add_handler( CommandHandler( "PI", TodoContollrer.PI))
application.add_handler( CommandHandler( "address_PI", TodoContollrer.direccion_PI))
application.add_handler( CommandHandler( "techers_PI", TodoContollrer.profesores_PI))
application.add_handler( CommandHandler( "PI_1", TodoContollrer.PI_1))
application.add_handler( CommandHandler( "PI_2", TodoContollrer.PI_2))
application.add_handler( CommandHandler( "PI_3", TodoContollrer.PI_3))
application.add_handler( CommandHandler( "PI_4", TodoContollrer.PI_4))
application.add_handler( CommandHandler( "PI_5", TodoContollrer.PI_5))
application.add_handler( CommandHandler( "PI_6", TodoContollrer.PI_6))
application.add_handler( CommandHandler( "PI_7", TodoContollrer.PI_7))
application.add_handler( CommandHandler( "PI_8", TodoContollrer.PI_8))
application.add_handler( CommandHandler( "PI_9", TodoContollrer.PI_9))
application.add_handler( CommandHandler( "PI_10", TodoContollrer.PI_10))
application.add_handler( CommandHandler( "PI_11", TodoContollrer.PI_11))
application.add_handler( CommandHandler( "PI_12", TodoContollrer.PI_12))
application.add_handler( CommandHandler( "PI_13", TodoContollrer.PI_13))
application.add_handler( CommandHandler( "PI_14", TodoContollrer.PI_14))
application.add_handler( CommandHandler( "PI_15", TodoContollrer.PI_15))

"""Юридический институт"""
application.add_handler( CommandHandler( "YUI", TodoContollrer.YUI))
application.add_handler( CommandHandler( "address_YUI", TodoContollrer.direccion_YUI))
application.add_handler( CommandHandler( "techers_YUI", TodoContollrer.profesores_YUI))
application.add_handler( CommandHandler( "YUI_1", TodoContollrer.YUI_1))
application.add_handler( CommandHandler( "YUI_2", TodoContollrer.YUI_2))
application.add_handler( CommandHandler( "YUI_3", TodoContollrer.YUI_3))
application.add_handler( CommandHandler( "YUI_4", TodoContollrer.YUI_4))
application.add_handler( CommandHandler( "YUI_5", TodoContollrer.YUI_5))
application.add_handler( CommandHandler( "YUI_6", TodoContollrer.YUI_6))
application.add_handler( CommandHandler( "YUI_7", TodoContollrer.YUI_7))
application.add_handler( CommandHandler( "YUI_8", TodoContollrer.YUI_8))
application.add_handler( CommandHandler( "YUI_9", TodoContollrer.YUI_9))
application.add_handler( CommandHandler( "YUI_10", TodoContollrer.YUI_10))
application.add_handler( CommandHandler( "YUI_11", TodoContollrer.YUI_11))
application.add_handler( CommandHandler( "YUI_12", TodoContollrer.YUI_12))


application.run_polling(allowed_updates=Update.ALL_TYPES)
