from pydoc import describe

from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from Controles import COMMANDS
from Controles.COMMANDS import COMMANDS_main


class TodoContollrer:

    @staticmethod
    async def add_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join(update.message.text.split(command)[1])
        print(title)


    #Da la bienvenida al usuario
    async def start( update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Привет! Я твой бот. Используй команду /help, чтобы увидеть все доступные команды, или /menu, чтобы посмотреть меню")


    # Da el Menu principal
    async def menu(update: Update, context: CallbackContext) -> None:
        help_text = "Информация:\n\n"
        for command, description in COMMANDS.COMMANDS_main.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML")


    async def menu_sfu(update: Update, context: CallbackContext) -> None:
        help_text = "меню СФУ" + "\n\n"
        for command, description in COMMANDS.COMMANDS_menu_SFU.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML")


    #Da da informcion sobre la unicersidad
    async def SFU(update: Update, context: CallbackContext) -> None:
        help_text = "Инфорормация о СФУ" + ":\n\n"
        for command, description in COMMANDS.texto_SFU.items():
            help_text += f"{description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    #Explica sobre la paguina ekursi y da el link
    async def ekursi(update: Update, context: ContextTypes.DEFAULT_TYPE):
        mensaje = '<a href="https://e.sfu-kras.ru/login/index.php">Екурсы</a>' + '\n'
        await update.message.reply_text(mensaje + 'Это страница, на которую нам присылают домашние задания или информацию по изучаемым нами предметам.', parse_mode="HTML")


    async def moi_sfu(update: Update, context: CallbackContext):
        texto_html = '<a href="https://i.sfu-kras.ru/">Мой СФУ</a>' + '\n'

        await update.message.reply_text(texto_html + "Это страница новостей о университете, на которой вы можете проверить свои оценки, свой средний балл, предметы, которые будут у вас в течение года, и т.д.", parse_mode="HTML")


    async def teachers(update: Update, context: CallbackContext):
        help_text = "О каком институте вы хотите получить информацию?:\n\n"
        for command, description in COMMANDS.COMMANDS_inst.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML")

    """Военно-инженерном институте"""
    async def ВИИ(update: Update, context: CallbackContext):
        texto_htlm = '<a href="https://e.sfu-kras.ru/login/index.php">ВИИ</a>'
        help_text = f'Военно-инженерном институте ({texto_htlm}):\n\n'
        for command, description in COMMANDS.Bii.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def techers_BII(update: Update, context: ContextTypes):
        texto_htlm = 'это преподаватели <a href = "https://structure.sfu-kras.ru/vii#staff">ВИИ</a>'
        help_text = "Это профессора Военно-инженерного института."+ texto_htlm
        for command, description in COMMANDS.techers_BII.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def direccion_BII(update: Update, context: ContextTypes):
        help_text = 'Вот адрес иститута\n\n'
        primera_direccion = '<a href = "https://2gis.ru/krasnoyarsk/geo/986145966616740">улица Академгородок, 13а</a>\n и \n'
        segunda_direcion = '<a href = "https://2gis.ru/krasnoyarsk/geo/985690700180809">улица Борисова, 20</a>'
        await update.message.reply_text(help_text + primera_direccion + segunda_direcion, parse_mode="HTML")


    async def information_BII(update: Update, context: CallbackContext):
        help_text = '<a href= "https://vii.sfu-kras.ru/">Военно-инженерном институте</a>'
        texto = f'информация об {help_text}' + '\n\n'
        for commands, description in COMMANDS.information_BII.items():
            texto += f'<u><b>{commands}</b></u>: {description}'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    """Instituto Гуманитарный институт"""
    async def ГИ(upate: Update, context: CallbackContext):
        texto_html = '<a href = "https://hi.sfu-kras.ru/ru">ГИ</a>'
        help_text = f"Гуманитарный институт({texto_html}):\n\n"
        for command, description in COMMANDS.GI.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await upate.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def direcicion_GI(update: Update, context: CallbackContext):
        help_text = 'Вот адрес Гуманитарный институтa\n\n'
        primera_direccion = '<a href = "https://2gis.ru/krasnoyarsk/search/%D0%93%D1%83%D0%BC%D0%B0%D0%BD%D0%B8%D1%82%D0%B0%D1%80%D0%BD%D1%8B%D0%B9%20%D0%B8%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82/firm/986145966535350/92.766171%2C56.004086?m=92.768947%2C56.003373%2F17.87&traffic">Свободный проспект, 82а</a>\n и \n'
        await update.message.reply_text(help_text + primera_direccion, parse_mode="HTML")


    async def profesir_GI(update: Update, context: CallbackContext):
        help_text = "это преподаватели: \n\n"
        for command, description in COMMANDS.profesores_Gi.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML")


    async def gi_1(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/355#staff">Кафедра информационных технологий в креативных и культурных индустриях</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/355#staff">КИТвКиКИ</a>'
        for command, description in COMMANDS.gi_1.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_2(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/352#staff">Кафедра истории России, мировых и региональных цивилизацийх</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/352#staff">КИРМиРЦ</a>'
        for command, description in COMMANDS.gi_2.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_3(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/358#staff">Кафедра культурологии и искусствоведения</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/358#staff">ККИИ</a>'
        for command, description in COMMANDS.gi_3.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async  def gi_4(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/357">Кафедра рекламы и социально-культурной деятельности</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/357#staff">КРиСКД</a>'
        for command, description in COMMANDS.gi_4.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_5(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/354">Кафедра философии</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/354#staff">КФ</a>'
        for command, description in COMMANDS.gi_5.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async  def gi_6(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/359#main">Лаборатория археологии Енисейской Сибири</a>' + '\n\n'
        for command, description in COMMANDS.gi_6.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_7(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/360#main">Лаборатория естественнонаучных методов в археологии и истории</a>' + '\n\n'
        for command, description in COMMANDS.gi_7.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_8(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/55860">Лаборатория компьютерной графики</a>' + '\n\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text("No hay profesores")


    async def gi_9(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/2382#staff">Музей археологии и этнографии Енисейской Сибири</a>' + '\n\n'
        for command, description in COMMANDS.gi_9.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_10(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/351#staff">Учебно-организационный отдел</a>' + '\n\n'
        for command, description in COMMANDS.gi_10.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    """Istututo Инженерно-строительный институт"""
    async def ICI(upate: Update, context: CallbackContext):
        texto_html = '<a href = "https://isi.sfu-kras.ru/">ИСИ</a>'
        help_text = f"Инженерно-строительный институт({texto_html}):\n\n"
        for command, description in COMMANDS.ICI.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await upate.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def direcion_ICI(update: Update, contexto: ContextTypes):
        help_text = "Вот адрес  Инженерно-строительный института\n\n"
        direccion_1 = '<a href = "https://2gis.ru/krasnoyarsk/search/%D0%98%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%BD%D0%BE-%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%B8%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82/firm/986145966616742/92.767035%2C56.005701?m=92.836468%2C56.003324%2F12.61&traffic">Свободный проспект, 82, Красноярск</a>'
        await update.message.reply_text(help_text + direccion_1, parse_mode="HTML")


    async def profesores_ICI(update: Update, context: CallbackContext):
        texto_html = '<a href = "https://structure.sfu-kras.ru/isi#structure">Инженерно-строительный институт</a>\n\n'
        help_text = f"Это преподаватели {texto_html}"
        for command, description in COMMANDS.profesores_ICI.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def ici_1(update: Update, context: CallbackContext):
        mensaje = '<a href= "https://structure.sfu-kras.ru/node/478#staff">КПЗЭН</a>'
        help_text = '<a href= "https://structure.sfu-kras.ru/node/478#staff">Кафедра проектирования зданий и экспертизы недвижимости</a>' + '\n\n'
        for command, description in COMMANDS.ici_1.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text("si necesitas mas informacion de profesores puedes encontrar aqui: " + mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def ici_2(update: Update, context: CallbackContext):
        mensaje = '<a href= "https://structure.sfu-kras.ru/node/473#staff">КСКУС</a>'
        help_text = '<a href= "https://structure.sfu-kras.ru/node/473">Кафедра строительных конструкций и управляемых систем</a>' + '\n\n'
        for command, description in COMMANDS.ici_2.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text("aqui puedes encontrar mas informacion: "+ mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def ici_3(update: Update, context: CallbackContext):
        mensaje = '<a href= "https://structure.sfu-kras.ru/node/473#staff">КСМТС</a>'
        help_text = '<a href= "https://structure.sfu-kras.ru/node/473">Кафедра строительных материалов и технологии строительства</a>' + '\n\n'
        for command, description in COMMANDS.ici_3.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text("Aqui puedes encontrar mas informacion: " + mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def ici_4(update: Update, context: CallbackContext):
        mensaje = '<a href= "https://structure.sfu-kras.ru/node/464#staff">КАДИГС</a>'
        help_text = '<a href= "https://structure.sfu-kras.ru/node/464#staff">Кафедра автомобильных дорог и городских сооружений</a>' + '\n\n'
        for command, description in COMMANDS.ici_4.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text("Aqui puedes encontrar mas informacion: " + mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def ici_5(update: Update, context: CallbackContext):
        mensaje = '<a href= "https://structure.sfu-kras.ru/node/468#staff">КИСЗС</a>'
        help_text = '<a href= "https://structure.sfu-kras.ru/node/468#staff">Кафедра инженерных систем зданий и сооружений</a>' + '\n\n'
        for command, description in COMMANDS.ici_5.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text("Aqui puedes encontrar mas informacion: " + mensaje, parse_mode="HTML", disable_web_page_preview=True)


    #Институт архитектуры и дизайна
    async def iaid(update: Update, context: CallbackContext):
        help_text = '<a href= "https://iad.sfu-kras.ru/">Кафедра инженерных систем зданий и сооружений</a>' +'\n\n'
        for command, description in COMMANDS.IAID.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def adress_IAID(update: Update, context: CallbackContext):
        direcion = '<a href = "https://2gis.ru/krasnoyarsk/geo/986145966853046">Svobodnyy Ave, 82А, Krasnoyarsk, Krasnoyarsk Krai</a>'
        await update.message.reply_text("Адрес Института архитектуры и дизайна \n\n" + direcion, parse_mode="HTML")


    async def profesores_IAID(update: Update, contexto: CallbackContext):
        help_text = 'это преподаватели <a href = "https://structure.sfu-kras.ru/iad#staff">ИАиД' + '\n\n'
        for command, description in COMMANDS.profesores_IAID.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iaid_1(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/218">Кафедра архитектурного проектирования</a>' + '\n\n'
        for command, description in COMMANDS.iaid_1.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iaid_2(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/216">Кафедра градостроительства</a>' + '\n\n'
        for command, description in COMMANDS.iaid_2.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iaid_3(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/222">Кафедра дизайна</a>' + '\n\n'
        for command, description in COMMANDS.iaid_3.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iaid_4(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/217">Кафедра дизайна архитектурной среды</a>' + '\n\n'
        for command, description in COMMANDS.iaid_4.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iaid_5(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/220">Кафедра изобразительного искусства и компьютерной графики</a>' + "\n\n"
        for command, description in COMMANDS.iaid_5.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iaid_6(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/223">Учебно-организационный отдел ИАиД</a>' + '\n\n'
        for command, description in COMMANDS.iaid_6.items():
            help_text += f'<u><b>{command}</b></u>: {description}'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    #Институт инженерной физики и радиоэлектроники
    async def iifire(update: Update, context: CallbackContext):
        help_text = '<a href="https://efir.sfu-kras.ru/">ИНСТИТУТ ИНЖЕНЕРНОЙ ФИЗИКИ И РАДИОЭЛЕКТРОНИКИ</a>' + '\n\n'
        for command, description in COMMANDS.iifire.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def direccion_IIFIRE(update: Update, context: CallbackContext):
        direccion = '<a href = "https://2gis.ru/krasnoyarsk/geo/986145966616735">улица Академика Киренского, 28</a>'
        await update.message.reply_text("Адрес Институт инженерной физики и радиоэлектроники\n\n" + direccion, parse_mode="HTML")


    async  def profesore_iifire(update: Update, context: CallbackContext):
        help_text = 'Это преподаватели <a href = "https://structure.sfu-kras.ru/efir#structure">ИИФиРЭ</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_iifire.items():
            help_text += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_1(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/227#staff">Базовая кафедра инфокоммуникаций</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_1.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_2(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/236#staff">Базовая кафедра радиоэлектронной техники информационных систем</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_2.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_3(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/237#staff">Базовая кафедра физики твёрдого тела и нанотехнологий</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_3.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_4(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/225#staff">Базовая кафедра фотоники и лазерных технологий</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_4.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_5(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/238#staff">Кафедра общей физики</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_5.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_6(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/229#staff">Кафедра приборостроения и наноэлектроники</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_6.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_7(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/228#staff">Кафедра радиотехники</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_7.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_8(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/230#staff">Кафедра радиоэлектронных систем</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_8.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_9(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/226#staff">Кафедра теоретической физики и волновых явлений</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_9.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_10(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/224#staff">Кафедра теплофизики</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_10.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_11(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/239">Кафедра физики</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_11.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_12(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/240">Кафедра экспериментальной физики и инновационных технологий</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_12.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_13(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/361#staff">Кафедра ЮНЕСКО «Новые материалы и технологии»</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_13.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_14(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/231">Лаборатория беспроводных систем передачи информации</a>' + '\n\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def iifire_15(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/237#staff">Базовая кафедра физики твёрдого тела и нанотехнологий</a>' + '\n\n'
        for command, descriptopn in COMMANDS.iifire_15.items():
            help_text += f'<u><b>{command}</b></u>: {descriptopn}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    #Институт космических и информационных технологий
    async  def IKIT(update: Update, context: CallbackContext):
        help_text = "Институт космических и информационных технологий " + '<a href = "https://ikit.sfu-kras.ru/">ИКИТ</a>' + '\n\n'
        for command, description in COMMANDS.IKIT.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def direccion_IKIT(update: Update, context: CallbackContext):
        direccion = '<a href = "https://2gis.ru/krasnoyarsk/geo/986145966616730/92.797026,55.994337">улица Академика Киренского, 26 к1</a>'
        await update.message.reply_text("Адрес Институт космических и информационных технологий \n\n" + direccion, parse_mode="HTML")

    async def profesores_IKIT(update: Update, context: CallbackContext):
        help_text = 'Это преподаватели<a href = "ИКИТ"></a>' + '\n\n'
        for command, description in COMMANDS.profesores_IKIT.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_1(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/385#staff">Базовая кафедра геоинформационных систем</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_1.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_2(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/2146#staff">Базовая кафедра интеллектуальных систем управления</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_2.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_3(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/392#staff">Базовая кафедра информационных технологий на радиоэлектронном производстве</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_3.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_4(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/363#staff">Информационно-телекоммуникационный центр</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_4.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_5(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/391#staff">Кафедра высокопроизводительных вычислений</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_5.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_6(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/372#staff">Кафедра вычислительной техники </a>' + '\n\n'
        for command, description in COMMANDS.IKIT_6.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_7(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/383#staff">Кафедра информационной безопасности</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_7.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_8(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/380#staff">Кафедра информационных систем</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_8.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_9(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/381#staff">Кафедра прикладной математики и анализа данных</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_9.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_10(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/387#staff">Кафедра программной инженерии</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_10.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_11(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/386#staff">Кафедра разговорного иностранного языка</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_11.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_12(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/367#staff">Кафедра систем автоматики, автоматизированного управления и проектирования </a>' + '\n\n'
        for command, description in COMMANDS.IKIT_12.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async  def IKIT_13(update: Update, context: CallbackContext):
        help_text ='<a href = "https://structure.sfu-kras.ru/node/376#staff">Кафедра систем искусственного интеллекта</a>' + '\n\n'
        for command, description in COMMANDS.IKIT_13.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    ##Институт космических и информационных технологий
    async  def IMIFI(update: Update, context: CallbackContext):
        help_text = 'Институт математики и фундаментальной информатики(<a href = "http://math.sfu-kras.ru/">ИМиФИ</a>)' + '\n\n'
        for command, description in COMMANDS.IMIFI.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IMIFI(update: Update, context: CallbackContext):
        direccion_IMIFI = '<a href = "https://go.2gis.com/xkQcf">Свободный проспект, 79</a>'
        await update.message.reply_text(direccion_IMIFI, parse_mode="HTML")

    async def profesores_IMIFI(update: Update, context: CallbackContext):
        help_text = 'Это преподаватели <a href = "https://structure.sfu-kras.ru/math#main">ИМиФИ</a>' + '\n\n'
        for command, description in COMMANDS.profesores_IMIFI.items():
            help_text += f'{command}: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_1(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/159#staff">Базовая кафедра вычислительных и информационных технологий</a>' + '\n\n'
        for command, descripton in COMMANDS.IMIFI_1.items():
            help_text += f'<b><u>{command}</u></b>: {descripton}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_2(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/160#staff">Базовая кафедра математического моделирования и процессов управления</a>' + '\n\n'
        for command, description in COMMANDS.IMIFI_2.items():
            help_text += f'<u><b>{command}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_3(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/168#staff">Директорат ИМиФИ</a>' + '\n\n'
        for command, descripton in COMMANDS.IMIFI_3.items():
            help_text += f'<u><b>{command}</b></u>: {descripton}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_4(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/156">Кафедра алгебры и математической логики</a>' + '\n\n'
        for commands, description in COMMANDS.IMIFI_4.items():
            help_text += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_5(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/161">Кафедра высшей и прикладной математики</a>' + '\n\n'
        for commands, description in COMMANDS.IMIFI_5.items():
            help_text += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_6(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/162">Кафедра высшей математики № 2</a>' + '\n\n'
        for commands, description in COMMANDS.IMIFI_6.items():
            help_text += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_7(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/157">Кафедра математического анализа и дифференциальных уравнений</a>' + '\n\n'
        for commands,  description in COMMANDS.IMIFI_7.items():
            help_text += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_8(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/164">Кафедра математического обеспечения дискретных устройств и систем</a>' + '\n\n'
        for commands, description in COMMANDS.IMIFI_8.items():
            help_text += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_9(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/node/158">Кафедра теории функций</a>' + '\n\n'
        for commands, description in COMMANDS.IMIFI_9.items():
            help_text += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    async def IMIFI_10(update: Update, context: CallbackContext):
        help_text = '<a href = "https://structure.sfu-kras.ru/complex-lab#staff">Лаборатория комплексного анализа и дифференциальных уравнений</a>' + '\n\n'
        for commands, description in COMMANDS.IMIFI_10.items():
            help_text += f"<u><b>{commands}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    #Институт нефти и газа
    async def INIG(update: Update, context: CallbackContext):
        texto = 'Институт нефти и газа(<a href ="http://inig.sfu-kras.ru/">Иниг</a>)' + "\n\n"
        for commands, description in COMMANDS.INIG.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_INIG(update: Update, context: CallbackContext):
        direccion = '<a href = "https://go.2gis.com/ysjjZ">Свободный проспект, 82 ст6</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesoeres_INIG(update: Update, context: CallbackContext):
        texto = 'Это преподаватели <a href = "https://structure.sfu-kras.ru/node/2143#staff">ИНиГ</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_INIG.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_1(update: Update, context: CallbackContext):
        texto = '<a href = "https://structure.sfu-kras.ru/node/2143#staff">Базовая кафедра проектирования объектов нефтегазового комплекса</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_2(update: Update, context: CallbackContext):
        texto = '<a href = "https://structure.sfu-kras.ru/node/121#staff">Базовая кафедра химии и технологии природных энергоносителей и углеродных материалов</a>' + '\n\n'
        for commands, descrption in COMMANDS.INIG_2.items():
            texto += f'<u><b>{commands}</b></u>: {descrption}\n'  + '\n\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_3(update: Update, context: CallbackContext):
        texto = '<a href = "https://structure.sfu-kras.ru/node/130#staff">Кафедра авиационных горюче-смазочных материалов</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_4(update: Update, context: CallbackContext):
        texto = '<a href = "https://structure.sfu-kras.ru/node/127#staff">Кафедра бурения нефтяных и газовых скважин</a>'  + '\n\n'
        for commands, description in COMMANDS.INIG_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/124">Кафедра геологии нефти и газа</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/126#staff">Кафедра геофизики</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/120">Кафедра машин и оборудования нефтяных и газовых промыслов</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_7.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_8(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/134">Кафедра пожарной безопасности</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_8.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_9(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/131">Кафедра проектирования и эксплуатации газонефтепроводов</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_9.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_10(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/129">Кафедра разработки и эксплуатации нефтяных и газовых месторождений</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_10.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_11(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/132">Кафедра технологических машин и оборудования нефтегазового комплекса</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_11.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_12(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/119">Кафедра топливообеспечения и горюче-смазочных материалов</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_12.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_13(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/1993">Научно-образовательный центр «Корпоративный нефтегазовый центр СФУ</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_13.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_14(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/5708">Учебно-научная лаборатория</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_14.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_15(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/114">Учебно-организационный отдел ИНиГ</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_15.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def INIG_16(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/ckp">Центр коллективного пользования</a>' + '\n\n'
        for commands, description in COMMANDS.INIG_16.items():
            texto += f'<u><b>{commands}</b></u>\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт педагогики, психологии и социологии
    async def IPPS(update: Update, context: CallbackContext):
        texto = 'Институт педагогики, психологии и социологии(<a href="http://www.ipps.sfu-kras.ru/ru/">ИППС</a>)' + '\n\n'
        for commands, description in COMMANDS.IPPS.items():
            texto += f"{commands}: {description}\n"
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IPPS(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/aEu09">Свободный проспект, 79 ст1</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IPPS(update: Update, context: CallbackContext):
        texto = 'Это преподаватели <a href="https://structure.sfu-kras.ru/ipps#main">ИППС</a>' + "\n\n"
        for commands, description in COMMANDS.profesores_IPPS.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_1(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/264#staff">Кафедра информационных технологий обучения и непрерывного образования</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_1.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_2(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/271#staff">афедра общей и социальной педагогики</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_2.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_3(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/266#staff">Кафедра психологии развития и консультирования</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_3.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_4(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/274#staff">Кафедра современных образовательных технологий</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_4.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_5(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/273#staff">Кафедра социологии</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_5.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_6(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/270">Студия изобразительного искусства</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_6.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_7(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/257#staff">Учебно-организационный отдел</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_7.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IPPS_8(updates: Update, contexto: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4936">Центр медиации в образовании</a>' + '\n\n'
        for commmands, description in COMMANDS.IPPS_8.items():
            texto += f'<u><b>{commmands}</b></u>: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт Севера и Арктики
    async def ISIA(update: Update, context: CallbackContext):
        texto = 'Институт Севера и Арктики(<a href="https://arctic.sfu-kras.ru/">ИСИА</a>' + "\n\n"
        for commands, description in COMMANDS.ISIA.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_ISIA(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/KudXl">Улица Борисова, 5</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_ISIA(update: Update, context: CallbackContext):
        texto = 'Это Професорра <a href="https://structure.sfu-kras.ru/node/4797">ИСИА</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_ISIA.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ISIA_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4847#staff">Кафедра северных и арктических исследований</a>' + '\n\n'
        for commands, description in COMMANDS.ISIA_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ISIA_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4848#staff">Международная бизнес-школа «Арктика»</a>' + '\n\n'
        for commands, description in COMMANDS.ISIA_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ISIA_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4849">Международная северная школа</a>' + '\n\n'
        for commands, description in COMMANDS.ISIA_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ISIA_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/5458#staff">Проектный офис</a>' + '\n\n'
        for commands, description in COMMANDS.ISIA_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт физической культуры, спорта и туризма
    async def IFRSIT(update: Update, context: CallbackContext):
        texto = 'Институт физической культуры, спорта и туризма(<a href="https://ifksit.sfu-kras.ru/">ИФКСиТ</a>)' + '\n\n'
        for commands,description in COMMANDS.IFKSIT.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IFRSIT(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/x9LRd">Свободный проспект, 79Б</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IFRSIT(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="">ИФКСиТ</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_IFIKSIT.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto,parse_mode="HTML", disable_web_page_preview=True)

    async def IFRSIT_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/504#staff">Кафедра теоретических основ и менеджмента физической культуры и туризма</a>' + '\n\n'
        for commands,  description in COMMANDS.IFKSIT_1.items():
            texto += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFRSIT_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/507#staff">Кафедра теории и методики спортивных дисциплин</a>' + '\n\n'
        for commands,  description in COMMANDS.IFKSIT_2.items():
            texto += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFRSIT_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/508#staff">Кафедра физической культуры</a>' + '\n\n'
        for commands,  description in COMMANDS.IFKSIT_3.items():
            texto += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFRSIT_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/6195#staff">Лаборатория спорта и туризма</a>' + '\n\n'
        for commands,  description in COMMANDS.IFKSIT_4.items():
            texto += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFRSIT_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/sportclub#staff">Спортивный клуб</a>' + '\n\n'
        for commands,  description in COMMANDS.IFKSIT_5.items():
            texto += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFRSIT_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/524#staff">Учебно-организационный отдел</a>' + '\n\n'
        for commands,  description in COMMANDS.IFKSIT_6.items():
            texto += f'<b><u>{commands}</u></b>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт фундаментальной биологии и биотехнологии
    async def IFBIBT(updates: Update, context: CallbackContext):
        texto = 'Институт фундаментальной биологии и биотехнологии(<a href = "https://bio.sfu-kras.ru/">ИФБиБТ</a>)' + '\n\n'
        for commands, description in COMMANDS.IFBIBT.items():
            texto += f'{commands}: {description}\n'
        await updates.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IFBIBT(update: Update, context: CallbackContext):
        direccion = '<a href = "https://go.2gis.com/N8kZ9">Свободный проспект, 79</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IFBIBT(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/bio">ИФБиБТ</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_IFBIBT.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/101#staff">Базовая кафедра биотехнологии</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/1791#staff">Базовая кафедра медико-биологических систем и комплексов</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/103#staff">Ботанический сад</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/106#staff">Виварий</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/107"> Деканат ИФБиБТ</a>' + '\n\n'
        await update.message.reply_text(texto, parse_mode="HTML")

    async def IFBIBT_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/99#staff">Кафедра биофизики</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/102#staff">Кафедра водных и наземных экосистем</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_7.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_8(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/111#staff">Кафедра геномики и биоинформатики</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_8.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_9(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/100#staff">Кафедра медицинской биологии</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_9.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_10(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/108#staff">Лаборатория «Гербарий»</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_10.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_11(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/1819#staff">Лаборатория биотехнологии новых биоматериалов</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_11.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_12(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/1793#staff">Лаборатория лесной геномики</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_12.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_13(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/1812#staff">Лаборатория научного английского языка</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_13.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IFBIBT_14(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/110#staff">Научно-практическая лаборатория молекулярно-генетических методов исследований</a>' + '\n\n'
        for commands, description in COMMANDS.IFBIBT_14.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт цветных металлов
    async def ITSM(update: Update, context: CallbackContext):
        texto = 'Институт цветных металлов(<a href = "http://icmim.sfu-kras.ru/">ИЦМ</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_ITSM(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/opp0c">Проспект им. газеты Красноярский Рабочий, 95</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_ITSM(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/icmim">ИЦМ</a>' + '\n\n'
        for commands,  description in COMMANDS.profesores_ITSM.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/154#staff">Базовая кафедра технологии золотосодержащих руд</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/149#staff">Кафедра автоматизации производственных процессов в металлургии</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/2159#staff">Кафедра инженерного бакалавриата</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/144#staff">Кафедра композиционных материалов и физико-химии металлургических процессов</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/140#staff">Кафедра литейного производства</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/141#staff">Кафедра металловедения и термической обработки металлов имени В. С. Биронта</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/148">Кафедра металлургии цветных металлов</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_7.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_8(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/147#staff">Кафедра обогащения полезных ископаемых</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_8.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_9(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/142#staff)">Кафедра обработки металлов давлением</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_9.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_10(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/2161#staff">Кафедра общей металлургии</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_10.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_11(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/146#staff)">Кафедра органической и аналитической химии</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_11.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_12(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/143#staff">Кафедра техносферной безопасности горного и металлургического производств</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_12.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_13(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/145#staff">Кафедра физической и неорганической химии</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_13.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITSM_14(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/139#staff">Кафедра фундаментального естественнонаучного образования</a>' + '\n\n'
        for commands, description in COMMANDS.ITSM_14.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт экологии и географии
    async def IEIG(update: Update, context: CallbackContext):
        texto = 'Институт экологии и географии(<a href="https://ieig.sfu-kras.ru/">ИЭиГ</a>)' + '\n\n'
        for commands, descritption in COMMANDS.IEIG.items():
            texto += f'{commands}: {descritption}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IEIG(update: Update, context: CallbackContext):
        direccion = '<a href="https://2gis.ru/krasnoyarsk/search/%D0%98%D0%BD%D1%81%D1%82%D0%B8%D1%82%D1%83%D1%82%20%D1%8D%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D0%B8%20%D0%B8%20%D0%B3%D0%B5%D0%BE%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D0%B8/firm/70000001046070743/92.77086%2C56.004426?m=92.831925%2C56.006804%2F10.58">Свободный проспект, 79 к4</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IEIG(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/ieig">ИЭиГ</a>' + '\n\n'
        for commands,  description in COMMANDS.profesores_IEIG.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEIG_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/339#staff">Кафедра географии</a>' + '\n\n'
        for commands, description in COMMANDS.IEIG_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEIG_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/344#staff">Кафедра охотничьего ресурсоведения и заповедного дела</a>' + '\n\n'
        for commands, description in COMMANDS.IEIG_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEIG_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/342#staff">Кафедра экологии и природопользования</a>' + '\n\n'
        for commands, description in COMMANDS.IEIG_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEIG_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/biogeochemistry#staff">Лаборатории биогеохимии экосистем</a>' + '\n\n'
        for commands, description in COMMANDS.IEIG_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEIG_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/2136#staff">Учебно-организационный отдел</a>' + '\n\n'
        for commands, description in COMMANDS.IEIG_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт гастрономии
    async def IG(update: Update,context: CallbackContext):
        texto = 'Институт гастрономии(<a href="https://gastronomyinstitute.ru/">ИГ</a>)' + '\n\n'
        for commands, decription in COMMANDS.IG.items():
            texto += f'{commands}: {decription}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def dereccion_IG(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/mqOws">Свободный проспект, 82</a>' + '\n\n'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IG(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/node/3857">ИГ</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_IG.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/3727#staff">Базовая кафедра</a>' + '\n\n'
        for commands, description in COMMANDS.IG_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/bellini#staff">Базовая кафедра</a>' + '\n\n'
        for commands, description in COMMANDS.IG_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4733#staff">Центр взаимодействия с внешними контрагентами</a>' + '\n\n'
        for commands, description in COMMANDS.IG_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4744#staff">Центр дополнительного профессионального образования</a>' + '\n\n'
        for commands, description in COMMANDS.IG_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4724#staff">Центр инноваций и инвестиций</a>' + '\n\n'
        for commands, description in COMMANDS.IG_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4735#staff">Центр международного сотрудничества</a>' + '\n\n'
        for commands, description in COMMANDS.IG_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IG_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/5563#staff">Центр предпринимательства и консалтинга</a>' + '\n\n'
        for commands, description in COMMANDS.IG_7.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт торговли и сферы услуг
    async def ITISU(update: Update, context: CallbackContext):
        texto = 'Институт торговли и сферы услуг(<a href="https://economics.sfu-kras.ru/">ИТиСУ</a>)' + '\n\n'
        for commands, description in COMMANDS.ITISU.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_ITISU(update: Update, cotext: CallbackContext):
        direccion = '<a href="https://go.2gis.com/CAnAe">Улица Лиды Прушинской</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_ITISU(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/tei">ИТиСУ</a>' + '\n\n'
        for commands,  description in COMMANDS.profesores_ITISU.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITISU_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4897#staff">Базовая кафедра таможенного дела</a>' + '\n\n'
        for commands, description in COMMANDS.ITISU_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITISU_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4898#staff">Кафедра гостиничного дела</a>' + '\n\n'
        for commands, description in COMMANDS.ITISU_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITISU_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/194#staff">Кафедра математических методов и информационных технологий в торговле и сфере услуг</a>' + '\n\n'
        for commands, description in COMMANDS.ITISU_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITISU_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/199#staff">Кафедра технологии и организации общественного питания</a>' + '\n\n'
        for commands, description in COMMANDS.ITISU_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITISU_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/200#staff">Кафедра товароведения и экспертизы товаров</a>' + '\n\n'
        for commands, description in COMMANDS.ITISU_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def ITISU_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/187#staff">Кафедра торгового дела и маркетинга</a>' + '\n\n'
        for commands, description in COMMANDS.ITISU_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт управления бизнес-процессами
    async def IUBP(update: Update, context: CallbackContext):
        texto = 'Институт управления бизнес-процессами(<a href="https://iubp.sfu-kras.ru/">ИУБП</a>)' + '\n\n'
        for commands, description in COMMANDS.IUBP.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IUBP(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/VB4G0">Улица Академика Киренского, 26а</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IUBP(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://iubp.sfu-kras.ru/">ИУБП</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_IUBP.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IUBP_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/499#staff">Кафедра бизнес-информатики и моделирования бизнес-процессами</a>' + '\n\n'
        for commands, description in COMMANDS.IUBP_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IUBP_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/493#staff">Кафедра маркетинга и международного администрирования</a>' + '\n\n'
        for commands, description in COMMANDS.IUBP_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IUBP_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/491#main">Кафедра теоретических основ экономики</a>' + '\n\n'
        for commands, description in COMMANDS.IUBP_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IUBP_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/497#staff">Кафедра цифровых технологий управления</a>' + '\n\n'
        for commands, description in COMMANDS.IUBP_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IUBP_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/485#staff">Кафедра экономики и управления бизнес-процессами</a>' + '\n\n'
        for commands, description in COMMANDS.IUBP_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IUBP_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4965#staff">Кафедра экономической и финансовой безопасности</a>' + '\n\n'
        for commands, description in COMMANDS.IUBP_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Институт экономики, государственного управления и финансов
    async def IEGUIF(update: Update, context: CallbackContext):
        texto = 'Институт экономики, государственного управления и финансов(<a href="https://eco.sfu-kras.ru/">ИЭГУиФ</a>)' + '\n\n'
        for commands, description in COMMANDS.IEGUIF.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_IEGUIF(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/EjNGr">Свободный проспект, 79 ст3</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_IEGUIF(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/eco">ИЭГУиФ</a>' + '\n\n'
        for commands, descrition in COMMANDS.profesores_IEGUIF.items():
            texto += f'{commands}: {descrition}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/4882#staff">Базовая кафедра антимонопольного и тарифного регулирования рынков ФАС</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/2131#staff">Базовая кафедра цифровых финансовых технологий Сбербанка России</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/317#staff">Кафедра бухгалтерского учёта и статистики</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/329#staff">Кафедра международной и управленческой экономики</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/320#staff">Кафедра социально-экономического планирования</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/333#staff">Кафедра теоретической экономики</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/331#staff">Кафедра управления человеческими ресурсами</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_7.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def IEGUIF_8(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/322#staff">Кафедра финансов и управления рисками</a>' + '\n\n'
        for commands, description in COMMANDS.IEGUIF_8.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI(update: Update, context: CallbackContext):
        texto = 'Политехнический институт(<a href="https://polytech.sfu-kras.ru/">ПИ</a>)' + '\n\n'
        for commands, description in COMMANDS.PI.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_PI(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/pae9S">Улица Академика Киренского, 26а</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_PI(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/pi#structure">ПИ</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_PI.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/medved#staff">Базовая кафедра высшей школы автомобильного сервиса</a>' + '\n\n'
        for commands, description in COMMANDS.PI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/396#staff">Кафедра конструкторско-технологического обеспечения машиностроительных производств</a>' + '\n\n'
        for commands, description in COMMANDS.PI_2.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/401#staff">Кафедра материаловедения и технологии обработки материалов</a>' + '\n\n'
        for commands, description in COMMANDS.PI_3.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/400#staff">Кафедра машиностроения></a>' + '\n\n'
        for commands, description in COMMANDS.PI_4.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/398#staff">Кафедра прикладной механики</a>' + '\n\n'
        for commands, description in COMMANDS.PI_5.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/428#staff">Кафедра робототехники и технической кибернетики</a>' + '\n\n'
        for commands, description in COMMANDS.PI_6.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/397#staff">Кафедра стандартизации, метрологии и управления качеством</a>' + '\n\n'
        for commands, description in COMMANDS.PI_7.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_8(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/429#staff">Кафедра тепловых электрических станций</a>' + '\n\n'
        for commands, description in COMMANDS.PI_8.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_9(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/431#staff">Кафедра теплотехники и гидрогазодинамики</a>' + '\n\n'
        for commands, description in COMMANDS.PI_9.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_10(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/430#staff">Кафедра техносферной и экологической безопасности</a>' + '\n\n'
        for commands, description in COMMANDS.PI_10.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_11(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/406#staff">Кафедра транспорта</a>' + '\n\n'
        for commands, description in COMMANDS.PI_11.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_12(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/405#staff">Кафедра транспортных и технологических машин</a>' + '\n\n'
        for commands, description in COMMANDS.PI_12.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_13(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/432#staff">Кафедра химии</a>' + '\n\n'
        for commands, description in COMMANDS.PI_13.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_14(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/426#staff">Кафедра электротехники</a>' + '\n\n'
        for commands, description in COMMANDS.PI_14.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def PI_15(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/425#staff">Кафедра электроэнергетики</a>' + '\n\n'
        for commands, description in COMMANDS.PI_15.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #Юридический институт
    async def YUI(update: Update, context: CallbackContext):
        texto = 'Юридический институт(<a href="https://law.sfu-kras.ru/">Юи</a>)' + '\n\n'
        for commands, description in COMMANDS.YUI.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def direccion_YUI(update: Update, context: CallbackContext):
        direccion = '<a href="https://go.2gis.com/3GTur">Улица Маерчака, 6</a>'
        await update.message.reply_text(direccion, parse_mode="HTML")

    async def profesores_YUI(update: Update, context: CallbackContext):
        texto = 'это преподаватели <a href="https://structure.sfu-kras.ru/ui#structure">Юи</a>' + '\n\n'
        for commands, description in COMMANDS.profesores_YUI.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_1(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/455#staff">Кафедра теории и методики социальной работы</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_2(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/435#staff">Кафедра уголовного процесса и криминалистики</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_3(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/440#staff">Кафедра гражданского права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_4(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/439#staff">Кафедра гражданского процесса</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_5(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/447#staff">Кафедра деликтологии и криминологии</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_6(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/448#staff">Кафедра иностранного права и сравнительного правоведения</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_7(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/442#staff">Кафедра конституционного, административного и муниципального права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_8(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/441#staff">Кафедра международного права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_9(update: Update, context: CallbackContext):
        texto = '<a href=https://structure.sfu-kras.ru/node/443#staff"">Кафедра предпринимательского, конкурентного и финансового права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_10(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/445#staff">Кафедра теории и истории государства и права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_11(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/444#staff">Кафедра трудового и экологического права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def YUI_12(update: Update, context: CallbackContext):
        texto = '<a href="https://structure.sfu-kras.ru/node/434#staff">Кафедра уголовного права</a>' + '\n\n'
        for commands, description in COMMANDS.YUI_1.items():
            texto += f'<u><b>{commands}</b></u>: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    #pagos
    async def pagos(update: Update, context: CallbackContext):
        texto = '<a href="https://pay.sfu-kras.ru/">Оплата услуг СФУ</a>' + '\n\n'
        for commands, description in COMMANDS.pagos.items():
            texto += f'{commands}: {description}\n'
        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

    async def stu(update: Update, context: CallbackContext):
        texto = '<u><b>Плата за обучение</b></u>' + '\n\n'
        texto_2 = 'Оплата обучения в СФУ по программам бакалавриата, специалитета, магистратуры, аспирантуры и дополнительного образования' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/edu">Пзо</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def Inte(update: Update, context: CallbackContext):
        texto = '<u><b>Плата за Интернет</b></u>' + '\n\n'
        texto_2 = 'Оплата доступа в Интернет в общежитиях СФУ' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/internet">Пзи</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def resi(update: Update, context: CallbackContext):
        texto = '<u><b>Плата за общежитие</b></u>' + '\n\n'
        texto_2 = 'Оплата проживания в общежитии СФУ студентов, аспирантов, сотрудников и иных лиц' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/hostels">Пзобщ</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def Prepa(update: Update, context: CallbackContext):
        texto = '<u><b>Плата за подготовительные курсы</b></u>' + '\n\n'
        texto_2 = 'Оплата за подготовительные курсы для абитуриентов СФУ' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/courses">Пзпк</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def Anti(update: Update, context: CallbackContext):
        texto = '<u><b>Покупка проверок в системе «Антиплагиат»</b></u>' + '\n\n'
        texto_2 = 'Покупка дополнительных проверок в системе «Антиплагиат», доступных через личный кабинет читателя на сайте Научной библиотеки СФУ.' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/antiplagiat">Антиплагиат</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def publi(update: Update, context: CallbackContext):
        texto = '<u><b>Покупка электронного издания СФУ</b></u>' + '\n\n'
        texto_2 = 'Оплата доступа сторонних лиц к электронным (полнотекстовым) документам в научной библиотеке СФУ' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/ebook">Пэи</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def event(update: Update, context: CallbackContext):
        texto = '<u><b>Оргвзнос за участие в мероприятии</b></u>' + '\n\n'
        texto_2 = 'Оплата организационного взноса за участие в олимпиаде, конференции, семинаре или ином мероприятии СФУ' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/events">Озувм</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)

    async def servi(update: Update, context: CallbackContext):
        texto = '<u><b>Плата за иные услуги СФУ</b></u>' + '\n\n'
        texto_2 = 'Оплата услуги СФУ, которой нет в перечне выше. Возможность онлайн-оплаты и формулировку назначения платежа следует уточнить у сотрудника университета, с которым вы сотрудничали по вопросам оплаты услуги.' + '\n'
        texto_3 = 'Для перехода на сайт нажмите здесь -->(<a href="https://pay.sfu-kras.ru/services/other">Пзиу</a>)'
        await update.message.reply_text(texto + texto_2 + texto_3, parse_mode="HTML", disable_web_page_preview=True)


    #Da informcaion acerca del bot
    async def Info(update: Update, context: CallbackContext):
        await update.message.reply_text("Это бот, который поможет вам найти информацию об университете СФУ.")

    #Da todos los comandos disponibles
    async def help_command(update: Update, context: CallbackContext) -> None:
        help_text = "Доступные команды:\n\n"
        for command, description in COMMANDS.COMMANDS_help.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text)