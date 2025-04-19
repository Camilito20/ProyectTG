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
        mensaje = '<a href="https://e.sfu-kras.ru/login/index.php">ekursi</a>' + '\n'
        await update.message.reply_text(mensaje + 'Esta es la pagina la cual nos mandan los deberes o informacion sobre las materias que tengamos', parse_mode="HTML")

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
        texto_htlm = '<a href = "https://structure.sfu-kras.ru/vii#staff">ВИИ</a>'
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
        help_text = "estos son los profesores de GI: \n\n"
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
        help_text = f"Это профессора {texto_html}"
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
        help_text = 'преподаватели <a href = "https://structure.sfu-kras.ru/iad#staff">ИАиД' + '\n\n'
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

        #Da informcaion acerca del bot


    async def Info(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Este es un bot que te va ayudar a encontar informacion sobre la universidad de SFU")


    #Da todos los comandos disponibles
    async def help_command(update: Update, context: CallbackContext) -> None:
        help_text = "Доступные команды:\n\n"
        for command, description in COMMANDS.COMMANDS_help.items():
            help_text += f"<b>{command}<b>: {description}\n"
        await update.message.reply_text(help_text)