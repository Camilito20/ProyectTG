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
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text)


    async def menu_sfu(update: Update, context: CallbackContext) -> None:
        help_text = "меню СФУ" + "\n\n"
        for command, description in COMMANDS.COMMANDS_menu_SFU.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text)


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
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text)

    async def ВИИ(update: Update, context: CallbackContext):
        texto_htlm = '<a href="https://e.sfu-kras.ru/login/index.php">ВИИ</a>'
        help_text = f'profesores del instituto {texto_htlm}:\n\n'
        for command, description in COMMANDS.Bii.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def ГИ(upate: Update, context: CallbackContext):
        help_text = "DE que cafedra deceas saver los profesores:\n\n"
        for command, description in COMMANDS.Gi.items():
            help_text += f"{command}: {description}\n"
        await upate.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_1(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/355#staff">Кафедра информационных технологий в креативных и культурных индустриях</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/355#staff">КИТвКиКИ</a>'
        for command, description in COMMANDS.gi_1.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_2(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/352#staff">Кафедра истории России, мировых и региональных цивилизацийх</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/352#staff">КИРМиРЦ</a>'
        for command, description in COMMANDS.gi_2.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_3(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/358#staff">Кафедра культурологии и искусствоведения</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/358#staff">ККИИ</a>'
        for command, description in COMMANDS.gi_3.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async  def gi_4(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/357">Кафедра рекламы и социально-культурной деятельности</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/357#staff">КРиСКД</a>'
        for command, description in COMMANDS.gi_4.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)


    async def gi_5(update: Update, context: CallbackContext):
        help_text = '<a href= "https://structure.sfu-kras.ru/node/354">Кафедра философии</a>' + '\n\n'
        mensaje = 'si necesitas mas informacion sobre profesores la puedes encontrarla aqui ' + '<a href= "https://structure.sfu-kras.ru/node/354#staff">КФ</a>'
        for command, description in COMMANDS.gi_5.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text, parse_mode="HTML", disable_web_page_preview=True)
        await update.message.reply_text(mensaje, parse_mode="HTML", disable_web_page_preview=True)

        #Da informcaion acerca del bot
    async def Info(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Este es un bot que te va ayudar a encontar informacion sobre la universidad de SFU")


    #Da todos los comandos disponibles
    async def help_command(update: Update, context: CallbackContext) -> None:
        help_text = "Доступные команды:\n\n"
        for command, description in COMMANDS.COMMANDS_help.items():
            help_text += f"{command}: {description}\n"
        await update.message.reply_text(help_text)