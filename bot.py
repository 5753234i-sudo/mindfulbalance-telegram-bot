import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

BOT_USERNAME = "@mindfulbalance_bot"
BOOKING_TELEGRAM = "https://t.me/irina_sexologist_coach"
WEBSITE = "https://mindfulbalance.online"
IMPRESSUM = "https://mindfulbalance.online/#impressum"
DATENSCHUTZ = "https://mindfulbalance.online/#datenschutz"

LANGS = {
    "ru": "🇷🇺 Русский",
    "de": "🇩🇪 Deutsch",
    "en": "🇬🇧 English",
}

TEXTS = {
    "ru": {
        "start": (
            "Добро пожаловать в Mindful Balance.\n\n"
            "Я Irina Minkovich — психологический и сексологический консультант, "
            "Health & Mental Coach.\n\n"
            "Выберите язык:"
        ),
        "menu": "Главное меню:",
        "about": (
            "Обо мне\n\n"
            "Меня зовут Irina Minkovich.\n\n"
            "Я — психологический и сексологический консультант, Health & Mental Coach, "
            "специалист по эмоциональной устойчивости и комплексному подходу к качеству жизни.\n\n"
            "В работе я объединяю психологическое консультирование, работу с эмоциональным состоянием, "
            "самооценкой, телесным восприятием, отношениями, сексуальностью и внутренней устойчивостью.\n\n"
            "Моя задача — помочь человеку лучше понять себя, свои реакции, внутренние паттерны "
            "и восстановить контакт с собой."
        ),
        "areas": (
            "С чем я работаю\n\n"
            "• стресс и эмоциональная перегрузка\n"
            "• эмоциональное выгорание\n"
            "• самооценка и внутренние ограничения\n"
            "• отношения и близость\n"
            "• трудности в сексуальной сфере\n"
            "• контакт с телом\n"
            "• эмоциональная устойчивость\n"
            "• жизненный баланс\n"
            "• повторяющиеся паттерны в отношениях\n"
            "• внутренние конфликты"
        ),
        "methods": (
            "Методы работы\n\n"
            "• психологическое консультирование\n"
            "• сексологическое консультирование\n"
            "• комплексный подход\n"
            "• работа с эмоциональными паттернами\n"
            "• элементы коучинга\n"
            "• практики эмоциональной устойчивости\n"
            "• телесно-ориентированный подход\n"
            "• системный взгляд на отношения и внутренние динамики\n\n"
            "Подход помогает увидеть повторяющиеся паттерны и лучше понять внутренние процессы."
        ),
        "services": (
            "Услуги и форматы\n\n"
            "• Индивидуальная онлайн-консультация\n"
            "• Глубокая ориентационная сессия\n"
            "• Индивидуальное сопровождение\n"
            "• Расширенная чат-поддержка в согласованное время\n\n"
            "Актуальные детали и стоимость указаны на сайте."
        ),
        "process": (
            "Как проходит консультация\n\n"
            "1. Онлайн-встреча\n"
            "2. Разбор запроса\n"
            "3. Определение целей\n"
            "4. Индивидуальное сопровождение\n\n"
            "Формат: Telegram / онлайн-встреча по договорённости."
        ),
        "faq": (
            "FAQ\n\n"
            "Это психотерапия?\n"
            "Нет. Консультации не заменяют психотерапию, медицинское или психиатрическое лечение.\n\n"
            "Консультации конфиденциальны?\n"
            "Да, вся информация остаётся конфиденциальной.\n\n"
            "Онлайн или офлайн?\n"
            "На данный момент основной формат — онлайн.\n\n"
            "На каких языках возможна консультация?\n"
            "Русский, немецкий, английский."
        ),
        "legal": (
            "Правовая информация\n\n"
            "Keine Diagnostik. Keine Psychotherapie. Keine Heilbehandlung.\n\n"
            "Мои консультации не заменяют медицинскую, психотерапевтическую или психиатрическую помощь."
        ),
        "contacts": (
            "Контакты\n\n"
            f"Сайт: {WEBSITE}\n"
            "Telegram для записи: @irina_sexologist_coach"
        ),
        "buttons": {
            "about": "Обо мне",
            "areas": "С чем я работаю",
            "methods": "Методы",
            "services": "Услуги",
            "process": "Как проходит консультация",
            "faq": "FAQ",
            "contacts": "Контакты",
            "legal": "Дисклеймер",
            "book": "Записаться на консультацию",
            "site": "Сайт",
            "back": "Назад",
            "langs": "Язык",
            "impressum": "Impressum",
            "privacy": "Datenschutz",
        },
    },
    "de": {
        "start": (
            "Willkommen bei Mindful Balance.\n\n"
            "Ich bin Irina Minkovich — psychologische und sexologische Beraterin, "
            "Health & Mental Coach.\n\n"
            "Bitte wählen Sie Ihre Sprache:"
        ),
        "menu": "Hauptmenü:",
        "about": (
            "Über mich\n\n"
            "Mein Name ist Irina Minkovich.\n\n"
            "Ich bin psychologische und sexologische Beraterin, Health & Mental Coach "
            "und arbeite mit einem ganzheitlichen Ansatz für mehr Lebensqualität.\n\n"
            "In meiner Arbeit verbinde ich psychologische Beratung, emotionale Stabilität, "
            "Selbstwert, Körperwahrnehmung, Beziehungen, Sexualität und Resilienz.\n\n"
            "Mein Ziel ist es, Menschen dabei zu begleiten, sich selbst besser zu verstehen "
            "und wieder mehr innere Stabilität und Selbstkontakt zu entwickeln."
        ),
        "areas": (
            "Themen\n\n"
            "• Stress und emotionale Belastung\n"
            "• emotionale Erschöpfung\n"
            "• Selbstwert und innere Begrenzungen\n"
            "• Beziehungen und Intimität\n"
            "• Schwierigkeiten im Bereich Sexualität\n"
            "• Körperwahrnehmung\n"
            "• emotionale Stabilität\n"
            "• innere Balance\n"
            "• wiederkehrende Beziehungsmuster\n"
            "• innere Konflikte"
        ),
        "methods": (
            "Arbeitsmethoden\n\n"
            "• psychologische Beratung\n"
            "• sexologische Beratung\n"
            "• ganzheitlicher Ansatz\n"
            "• Arbeit mit emotionalen Mustern\n"
            "• Coaching-Elemente\n"
            "• Resilienztraining\n"
            "• körperorientierter Ansatz\n"
            "• systemischer Blick auf Beziehungen und innere Dynamiken\n\n"
            "Der Ansatz kann helfen, wiederkehrende Muster sichtbar zu machen "
            "und innere Prozesse besser zu verstehen."
        ),
        "services": (
            "Leistungen & Formate\n\n"
            "• Individuelle Online-Beratung\n"
            "• Vertiefende Orientierungssitzung\n"
            "• Individuelle Begleitung\n"
            "• Erweiterte Chat-Begleitung innerhalb der vereinbarten Zeiten\n\n"
            "Aktuelle Details und Preise finden Sie auf der Webseite."
        ),
        "process": (
            "Wie läuft die Beratung ab?\n\n"
            "1. Online-Gespräch\n"
            "2. Klärung des Anliegens\n"
            "3. Gemeinsame Zieldefinition\n"
            "4. Individuelle Begleitung\n\n"
            "Format: Telegram / Online-Gespräch nach Vereinbarung."
        ),
        "faq": (
            "FAQ\n\n"
            "Ersetzt die Beratung eine Therapie?\n"
            "Nein. Die Beratung ersetzt keine Psychotherapie, medizinische oder psychiatrische Behandlung.\n\n"
            "Ist die Beratung vertraulich?\n"
            "Ja, alle Informationen bleiben vertraulich.\n\n"
            "Online oder offline?\n"
            "Derzeit findet die Beratung hauptsächlich online statt.\n\n"
            "In welchen Sprachen ist die Beratung möglich?\n"
            "Deutsch, Russisch und Englisch."
        ),
        "legal": (
            "Rechtlicher Hinweis\n\n"
            "Keine Diagnostik. Keine Psychotherapie. Keine Heilbehandlung.\n\n"
            "Meine Angebote ersetzen keine medizinische, psychotherapeutische oder psychiatrische Behandlung."
        ),
        "contacts": (
            "Kontakte\n\n"
            f"Webseite: {WEBSITE}\n"
            "Telegram für Terminbuchung: @irina_sexologist_coach"
        ),
        "buttons": {
            "about": "Über mich",
            "areas": "Themen",
            "methods": "Methoden",
            "services": "Leistungen",
            "process": "Ablauf",
            "faq": "FAQ",
            "contacts": "Kontakte",
            "legal": "Hinweis",
            "book": "Termin buchen",
            "site": "Webseite",
            "back": "Zurück",
            "langs": "Sprache",
            "impressum": "Impressum",
            "privacy": "Datenschutz",
        },
    },
    "en": {
        "start": (
            "Welcome to Mindful Balance.\n\n"
            "I am Irina Minkovich — psychological and sexological consultant, "
            "Health & Mental Coach.\n\n"
            "Please choose your language:"
        ),
        "menu": "Main menu:",
        "about": (
            "About me\n\n"
            "My name is Irina Minkovich.\n\n"
            "I am a psychological and sexological consultant, Health & Mental Coach, "
            "working with a holistic approach to quality of life.\n\n"
            "My work combines psychological consulting, emotional stability, self-worth, "
            "body awareness, relationships, sexuality, and resilience.\n\n"
            "My goal is to help people better understand themselves, their reactions, "
            "their emotional patterns, and reconnect with themselves."
        ),
        "areas": (
            "Areas I work with\n\n"
            "• stress and emotional overload\n"
            "• burnout and emotional exhaustion\n"
            "• self-worth and inner limitations\n"
            "• relationships and intimacy\n"
            "• difficulties in the area of sexuality\n"
            "• body awareness\n"
            "• emotional resilience\n"
            "• life balance\n"
            "• recurring relationship patterns\n"
            "• inner conflicts"
        ),
        "methods": (
            "Methods\n\n"
            "• psychological consulting\n"
            "• sexological consulting\n"
            "• holistic approach\n"
            "• emotional pattern work\n"
            "• coaching elements\n"
            "• resilience practices\n"
            "• body-oriented approach\n"
            "• systemic perspective on relationships and inner dynamics\n\n"
            "This approach may help identify recurring patterns and inner dynamics."
        ),
        "services": (
            "Services & formats\n\n"
            "• Individual online consultation\n"
            "• In-depth orientation session\n"
            "• Individual support\n"
            "• Extended chat support within agreed hours\n\n"
            "Current details and prices are available on the website."
        ),
        "process": (
            "How the consultation works\n\n"
            "1. Online meeting\n"
            "2. Clarifying your request\n"
            "3. Goal definition\n"
            "4. Individual support\n\n"
            "Format: Telegram / online meeting by agreement."
        ),
        "faq": (
            "FAQ\n\n"
            "Is this psychotherapy?\n"
            "No. Consultations do not replace psychotherapy, medical or psychiatric treatment.\n\n"
            "Is the consultation confidential?\n"
            "Yes, all information remains confidential.\n\n"
            "Online or offline?\n"
            "Currently, consultations are mainly online.\n\n"
            "Which languages are available?\n"
            "Russian, German, and English."
        ),
        "legal": (
            "Legal notice\n\n"
            "No diagnostics. No psychotherapy. No medical treatment.\n\n"
            "My services do not replace medical, psychotherapeutic, or psychiatric treatment."
        ),
        "contacts": (
            "Contacts\n\n"
            f"Website: {WEBSITE}\n"
            "Telegram for booking: @irina_sexologist_coach"
        ),
        "buttons": {
            "about": "About me",
            "areas": "Areas",
            "methods": "Methods",
            "services": "Services",
            "process": "Process",
            "faq": "FAQ",
            "contacts": "Contacts",
            "legal": "Legal notice",
            "book": "Book a session",
            "site": "Website",
            "back": "Back",
            "langs": "Language",
            "impressum": "Impressum",
            "privacy": "Privacy Policy",
        },
    },
}


def language_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(LANGS["ru"], callback_data="lang:ru")],
        [InlineKeyboardButton(LANGS["de"], callback_data="lang:de")],
        [InlineKeyboardButton(LANGS["en"], callback_data="lang:en")],
    ])


def main_menu_keyboard(lang: str):
    b = TEXTS[lang]["buttons"]
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(b["about"], callback_data=f"page:{lang}:about"),
            InlineKeyboardButton(b["areas"], callback_data=f"page:{lang}:areas"),
        ],
        [
            InlineKeyboardButton(b["methods"], callback_data=f"page:{lang}:methods"),
            InlineKeyboardButton(b["services"], callback_data=f"page:{lang}:services"),
        ],
        [
            InlineKeyboardButton(b["process"], callback_data=f"page:{lang}:process"),
            InlineKeyboardButton(b["faq"], callback_data=f"page:{lang}:faq"),
        ],
        [
            InlineKeyboardButton(b["contacts"], callback_data=f"page:{lang}:contacts"),
            InlineKeyboardButton(b["legal"], callback_data=f"page:{lang}:legal"),
        ],
        [
            InlineKeyboardButton(b["book"], url=BOOKING_TELEGRAM),
        ],
        [
            InlineKeyboardButton(b["site"], url=WEBSITE),
            InlineKeyboardButton(b["langs"], callback_data="choose_lang"),
        ],
        [
            InlineKeyboardButton(b["impressum"], url=IMPRESSUM),
            InlineKeyboardButton(b["privacy"], url=DATENSCHUTZ),
        ],
    ])


def back_keyboard(lang: str):
    b = TEXTS[lang]["buttons"]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(b["book"], url=BOOKING_TELEGRAM)],
        [InlineKeyboardButton(b["back"], callback_data=f"menu:{lang}")],
    ])


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Welcome to Mindful Balance\n"
        "Добро пожаловать в Mindful Balance\n"
        "Willkommen bei Mindful Balance\n\n"
        "Please choose your language:\n"
        "Пожалуйста, выберите язык:\n"
        "Bitte wählen Sie Ihre Sprache:"
    )
    await update.message.reply_text(text, reply_markup=language_keyboard())


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "choose_lang":
        await query.edit_message_text(
            "Please choose your language / Выберите язык / Bitte wählen Sie Ihre Sprache:",
            reply_markup=language_keyboard(),
        )
        return

    if data.startswith("lang:"):
        lang = data.split(":")[1]
        await query.edit_message_text(
            TEXTS[lang]["menu"],
            reply_markup=main_menu_keyboard(lang),
        )
        return

    if data.startswith("menu:"):
        lang = data.split(":")[1]
        await query.edit_message_text(
            TEXTS[lang]["menu"],
            reply_markup=main_menu_keyboard(lang),
        )
        return

    if data.startswith("page:"):
        _, lang, page = data.split(":")
        await query.edit_message_text(
            TEXTS[lang][page],
            reply_markup=back_keyboard(lang),
            disable_web_page_preview=True,
        )
        return


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Use /start to open the menu.\n"
        "Используйте /start, чтобы открыть меню.\n"
        "Nutzen Sie /start, um das Menü zu öffnen."
    )


def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is missing. Add it as an environment variable.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(handle_callback))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()