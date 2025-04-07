from telegram import Update
from telegram.ext import ContextTypes, CallbackContext
from Controles import COMMANDS


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
        help_text = "Из какого института вы хотите преподавателей?:\n\n"
        for command, description in COMMANDS.COMMANDS_inst.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML")

    async def ВИИ(update: Update, context: CallbackContext):
        texto_htlm = '<a href="https://e.sfu-kras.ru/login/index.php">ВИИ</a>'
        help_text = f'profesores del instituto {texto_htlm}:\n\n'
        for command, description in COMMANDS.Bii.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)

    """Instituto Гуманитарный институт"""
    async def ГИ(upate: Update, context: CallbackContext):
        help_text = "DE que cafedra deceas saver los profesores:\n\n"
        for command, description in COMMANDS.Gi.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await upate.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


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
        help_text = "De que cafedra deceas saver los profesores:\n\n"
        for command, description in COMMANDS.ICI.items():
            help_text += f"<u><b>{command}</b></u>: {description}\n"
        await upate.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


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
        help_text = '<a href= "https://structure.sfu-kras.ru/node/468#staff">Кафедра инженерных систем зданий и сооружений</a>' +'\n\n'
        for command, description in COMMANDS.IAID.items():
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