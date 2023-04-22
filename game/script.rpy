# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Баба Алеся, повествование ведётся от её имени
define ba = Character(_("Баба Алеся"))
# Дед Николай (в случае, если повествование заканчивается отношениями с ним)
define dn = Character(_("Деда Николай"))
# Дед Ян (в случае, если повествование заканчивается отношениями с ним)
define dy = Character(_("Деда Ян"))
# Мама Алеси (в момент, когда Алеся молодая)
define ma = Character(_("Мама Алеси"))
# Молодая Алеся
define alesya = Character(_("Алеся"))
# Молодая Рая
define raya = Character(_("Рая"))
# Молодой Николай
define nikolai = Character(_("Николай"))
# Молодой Ян
define yan = Character(_("Ян"))

# (не требует вызова)
init:
    image indoor past = "indoor now.png"

    image baba norm = "ba norm.png"
    image alesya norm = "alesya norm.png"
    image raya norm = "raya norm.png"
    image yan norm = "yan norm.png"
    image nikolai norm = "nikolai norm.png"

    image house now = "house now.png"
    image house past = "house past.png"
    image wedding = "wedding.png"
    image club past = "club past.png"

    # Хочет ли идти Алеся на вечёрку с Яном?
    $ yan_chosen = False
    # Подарили ли венок Миколе?
    $ nikolai_chosen = False


# Появляется сразу после запуска и перед основным меню игры
# http://ru.renpypedia.shoutwiki.com/wiki/Добавление_заставки_(Adding_a_Splashscreen)
label splashscreen:

    scene black
    with Pause(1)

    show text _("Шуканне представляет...") with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    show text _("проект 2022 года...") with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

# Начало игры
label start:
    # jump credits

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene house past with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show ba norm at right

    # These display lines of dialogue.

    ba "Заходи, дитятко!"

    scene indoor past with dissolve
    show ba norm at right with dissolve

    ba "Ну что тебе ещё рассказать. Была одна история..."

    ba "Як я суженного ряженного выбирала. Дело было так.."

    hide ba norm at right with dissolve
    show alesya norm at right with dissolve

    alesya "Жила я с мамой, без отца. Годы были послевоенные, голодные..."

    alesya "Сложно было. На наших плечах было своё хозяйство. Ещё и налог этот... Три раза швейную машинку закладывали.."

    alesya "Впрочем о чём это я. Заходит ко мне как то подружка, Раечка"

    show raya norm at left

    alesya "Они с братом Николаем в соседней хате жили. Хата была добрая, семья работящие"
    alesya "Были мне ци восемнадцать ци нешта каля таго. Сам считай, было в 1956 году"

    raya "Пойдём на танцы, там Ян будет!"

    menu:
        "Совершите выбор вместе с Алесей"
        # Не нравится
        "Опять этот Ян, вся девки от него с ума сошли, шо дурные! Вон и Рая, похоже, туда же!":
            pass
        # Нравится
        "Ян завидный парень. Вельми мне падабается!":
            # Прыгаем на сцену с вышиванием
            jump vysh

    raya "Ну пойдем тогда на речку венки плести!"
    alesya "Долго мы были на речке, венки вышли зачётные. Кажется мне, что Рая для Яна венок плела :-) А я сплела и... в хозяйстве пригодится!"
    raya "Скоро стемнеет, Николай встретит нас!"

    hide raya norm at left
    show nikolai norm at left

    nikolai "Витаю, девчины. Красивые венки!"

    menu:
        "Подарить венок Николаю или оставить себе?"
        # Оставить
        "Спасибо!":
            # Что подарили венок Николаю
            $ nikolai_chosen = False

            alesya "Николай корешок мой детский, боюсь нелепо это будет, если венок ему отдам. Поймут ещё не так..."
            # Прыгаем на ночное похищение лавки (Рая хочет свести с Яном)
            jump lava
        # Подарить
        "Спасибо, Николай! Возьми мой венок?":
            # Что подарили венок Николаю
            $ nikolai_chosen = True

            alesya "На мгновение показалось, что Николай растерялся... Странно, я же его с детства знаю, чего тут такого, или подумал что?"
            alesya "Уже слегка стемнело и Рая предложила всё-таки пойти на вечёрку. Ну конечно, не зря же она венок плела, Янчику своему подарить хочет!"
            # Прыгаем на вечеринку
            jump vech

# Cцена с вышиванием
label vysh:

    alesya "Нравился мне он так сильно, что ночами сидела, вышивала подарок ему"
    # Прыгаем на сцену с предложением Яна пойти на вечёрку
    jump yan_offer

# Сцена с предложением Яна пойти на вечёрку
label yan_offer:

    hide raya norm at left with dissolve
    show yan norm at left with dissolve
    alesya "А вот и он, тут как тут, стучится в окно, як мотылёк!"
    yan "Витаю! Вечёрка грядёт, слыхала? Пойдёшь?"

    menu:
        "Пойдёте ли вы с Яном?"
        # Пойдём
        "Окей":
            # Запоминаем, что Алеся хочет идти с Яном
            $ yan_chosen = True
        # Не пойдём
        "А тебе дело!?":
            # Запоминаем, что Алеся НЕ хочет идти с Яном
            $ yan_chosen = False

    # Идём на вечёрку
    jump vech

# Вечерка
label vech:

    scene club past with dissolve
    show alesya norm at left with dissolve
    if yan_chosen:
        show yan norm at right with dissolve

    alesya "Танцы были што надо, у \"гармониста песня льётся чисто\""
    # Если Алеся пришла по приглашению Яна
    if yan_chosen:
        alesya "Какой был вечер, прекрасно провели вечер!"

    # Если Алеся отказала Яну и пришла сама
    if not yan_chosen:
        show yan norm at right with dissolve
        alesya "Все шло хорошо, пока не прибежали хлопцы ды Ян и проявили токсичную мускулиность (сорвали фартук)!"

        if not nikolai_chosen:
            alesya "Я половину года дома просидели, выйти не могла от стыда"

        if nikolai_chosen:
            hide alesya norm at left with dissolve
            show nikolai norm at left with dissolve
            alesya "Хорошо, что Николай с нами был. Заступился за меня, долго Ян жалеть о шалости своей будет!"
            alesya "Но всё равно срам, из дому теперь не выйдешь..."
            # Побег от реальности
            jump escape

    # Увы и ах, Ян идёт в армию
    jump army

# Армия
label army:

    scene forest past with dissolve
    show alesya norm at left with dissolve
    show yan norm at right with dissolve

    alesya "В следующий раз я увидела его на проводах... в советскую армию его забрали"
    alesya "Вспомнила я как вышивала ночами для него, заколотилося у груди"

    menu:
        "Тольки что с этим рабиць?"
        # Отдать сама
        "Отдам сама":
            alesya "Нашла возможность, поймала его перед самым отъездом и отдала!"
            jump yan
        # Не отдавать
        "Вот ещё. В хозяйстве пригодится":
            alesya "Ох, горюшко... Фартук задрал, срам какой. А теперь ещё и сам по армиям всяким собрался..."
            # Прыгаем на побег от реальности... В другой колхоз :-)
            jump escape
        # Попросить Раю
        "Попрошу Раечку. Ей ничаго не страшно":
            jump raya
        # Попросить Миколу
        "Попрошу Николая, он всегда рядом и рад помочь":
            alesya "Николай не смог мне отказать, обещался всё передать. Сердечко бъётся..."
            alesya "Некоторое время ждала я Яна. Письма ему не писала, но не отправляла, ждала, что он первый напишет..."
            hide alesya norm at left with dissolve
            show raya norm at left with dissolve
            alesya "А потом слухи поползли... Оказалось, что Ян и Рая..."
            # Прыгаем на побег от реальности... В другой колхоз :-)
            jump escape

# Прыгаем на ночное похищение лавки (Рая хочет свести с Яном)
label lava:

    scene house past with dissolve
    show alesya norm at right with dissolve
    alesya "Ночью случилась неприятно. Лаву кто-то нашу со двора упёр и к хате Яна поставил. Ума не приложу, кто мог до этого додуматься. Узнаю, поколочу!"
    show raya norm at left with dissolve
    alesya "Чтобы как-то отвлечься от неприятности этой, решили мы с Раей на вечёрку всё-таки сходить..."
    # Прыгаем на вечёрку (Ян не был выбран ранее)
    jump vech

# Концовка с Яном
label yan:

    scene wedding with dissolve
    alesya "Судьбоносное это решение было. С Яншиком мы моими шестьдесят гадов прожили. Ни разу руку на меня не поднял, золотой человек был!"

    jump credits

# Ян + Рая
label raya:

    scene house past with dissolve
    show raya norm at right with dissolve
    show yan norm at left with dissolve

    alesya "Судьбоносное это решение было. Давно Рая на Яна глаз положила. Выдала вышивку за свою, призналася ему в чувствах своих..."
    alesya "Слышала я потом, что дождалась она его, парой они стали, детишки пошли..."

    jump escape

# Побег от проблемы
label escape:

    scene forest past with dissolve
    show alesya norm at right with dissolve

    alesya "Бежать... Бежать... Видеть никого не хочу... Думать ни о чём..."
    alesya "В соседнем колхозе новых сотрудников набирали, поеду туда, подальше отседа!"
    alesya "Но как же мне добраться? Пешком слишком далеко, а на дворе почти ночь!"

    menu:
        "Помогите решить Алесе"
        # Попросить Николая
        "Попрошу Николая, славный он парень, всегда готов помочь":
            hide alesya norm at right with dissolve
            show ba norm at right with dissolve
            ba "Николай был очень рад моей просьбе. Оказалось, что он и сам думал откликнуться на вакансию и мы решили ехать вместе!"
            ba "Спустя некоторое время я поняла, какой брилиант всё время был со мной рядом, защищал и оберегал меня!"
            ba "Прожили мы с ним долгую и счастливую жизнь. Детишек у нас много было, помогали нам. Не один раз вспоминала мои приключения и благодарила судьбу за то, что она сложилась именно так."
        # Поехать самой (Николая не просить)
        "Да в конце концов, сколько можно. Я самостоятельная взрослая женщина, могу со всем справиться!":
            alesya "Спокойно вернусь домой, переночую, соберу вещи, попрощаюсь с мамой, а завтра спокойно доеду на автобусе!"
            hide alesya norm at right with dissolve
            show ba norm at right with dissolve
            ba "Так и поступила. Мама не хотела отпускать, но потом поняла и приняла моё решение."
            ba "Прожила я счастливую жизнь и в каком-то смысле даже благодарна Рае за её поступок."
            ba "Ведь это позволило мне найти в себе силы, благодаря которым я перестала оглядываться на то, что обо мне могут подумать другие!"

    jump credits

# Появляется при окончании игры (требует вызова)
# https://lemmasoft.renai.us/forums/viewtopic.php?t=22481
label credits:
    $ end_title = _("Конец")

    image splash = Text("{size=90}Šukańnie Fest", text_align=0.5, ypos=0.5) #Placeholder code if you don't have anything to use as a splash image or are just pure lazy.
#    image splash = "images/Company-Logo.png" #This is usually going to be located in an init block executed early in the code to show it when the game loads up as a splash screen.
#    image cred = Text(credits_s, font="myfont.ttf", text_align=0.5) #use this if you want to use special fonts
#    image cred = Text(credits_s, font="./fonts/Montserrat-VariableFont_wght.ttf", text_align=0.1)
    $ cred = Text(credits_s, text_align=0.0)
    #image theend = Text("{size=80}[end_title]", text_align=0.5)
    $ theend = Text("{size=80}[end_title!t]", text_align=0.5)

    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    show expression cred at Move((0.1, 3.0), (0.1, 0.0), credits_speed, repeat=False, bounce=False, xanchor="left", yanchor="bottom")
    #show theend:
    show expression theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(2)
    hide theend
    with dissolve
    with Pause(credits_speed - 4)
    show splash
    with dissolve
    with Pause(3)
    hide splash
    with dissolve
    with Pause(1)
    return

# Подготовка кредитов для показа (не требует вызова)
# https://lemmasoft.renai.us/forums/viewtopic.php?t=22481
init python:
    
    thanks_title = _("Благодарности")
    team_title = _("Команда")
    authors_title = _("Авторы")
    partners_title = _("Благодарим наших партнеров")

    thanks_line_1 = _("EHU, а в особенности Степану Захаркевичу за экспедиционные и житейские советы")
    thanks_line_2 = _("Сергею Харевскому за консультации по деревенским гулянкам и обрядам")
    thanks_line_3 = _("Степану Стурейко за веру и поддержку наших студенческих начинаний")
    thanks_line_4 = _("Алине Деревянко за экскурс в лучшие практики менеджмента культурных проектов")
    thanks_line_5 = _("34mag travel, в особенности Касе Сырамалот за распространение анонсов нашего \n{space=50}мероприятия и теплые слова")
    thanks_line_6 = _("Команде культурного пространства Kablys, в особенности Valda Arbačiauskaitė за то, \n{space=50}что позволила нам провести фест в этих чудесных стенах")
    thanks_line_7 = _("Марыі Барысёнак і Зміцеру Макарчуку за дапамогу з перакладам на беларускую мову")

    team_line_1 = _("Полина Лябихова - идейная вдохновительница и менеджерка фестиваля и \n{space=50}культурного онлайн-проекта Šukańnie")
    team_line_2 = _("Аляксандра Навіцкая - консультант, автор проекта Скародзіца")
    team_line_3 = _("Саша Метлицкая - менеджерка фестиваля, кураторка арт блока")
    team_line_4 = _("Аліна Дрожжа – менеджерка проекта онлайн-проекта shukannie, полевая этнографка")
    team_line_5 = _("Рома Енотов – художник, иллюстратор, любитель каласоў")
    team_line_6 = _("Анна Титова-Тубаш – художница, сценограф, консультант по перформативной части")
    team_line_7 = _("Серж Тубаш – междисциплинарный современный художник, исследователь видеоигр")
    team_line_8 = _("Аня Кастюченко - авторка фотовыставки")
    team_line_9 = _("Катя Дорофеева - саунд-художница")
    team_line_10 = _("Яна Веренчук - режиссерка")

    authors_line_1 = _("Анастасия Пастухова")
    authors_line_2 = _("Станислав Турко")
    authors_line_3 = _("Леонид Прусов")
    authors_line_4 = _("Наталья Пухова")

    partners_line_1 = _("Kitchen Coffee Roasters за то, что поддержали нас хрустящими круассанами и вкусным кофе")
    partners_line_2 = _("VEHA за предоставление уникальных архивных кадров и фотокнигу, которую нам удалось \n{space=50}привезти в Вильнюс и разыграть среди участников")

    credits = ("[thanks_title!t]", "[thanks_line_1!t]"),\
    ("[thanks_title!t]", "[thanks_line_2!t]"),\
    ("[thanks_title!t]", "[thanks_line_3!t]"),\
    ("[thanks_title!t]", "[thanks_line_4!t]"),\
    ("[thanks_title!t]", "[thanks_line_5!t]"),\
    ("[thanks_title!t]", "[thanks_line_6!t]"),\
    ("[thanks_title!t]", "[thanks_line_7!t]"),\
    ("[team_title!t]", "[team_line_1!t]"),\
    ("[team_title!t]", "[team_line_2!t]"),\
    ("[team_title!t]", "[team_line_3!t]"),\
    ("[team_title!t]", "[team_line_4!t]"),\
    ("[team_title!t]", "[team_line_5!t]"),\
    ("[team_title!t]", "[team_line_6!t]"),\
    ("[team_title!t]", "[team_line_7!t]"),\
    ("[team_title!t]", "[team_line_8!t]"),\
    ("[team_title!t]", "[team_line_9!t]"),\
    ("[team_title!t]", "[team_line_10!t]"),\
    ("[authors_title!t]", "[authors_line_1!t]"),\
    ("[authors_title!t]", "[authors_line_2!t]"),\
    ("[authors_title!t]", "[authors_line_3!t]"),\
    ("[authors_title!t]", "[authors_line_4!t]"),\
    ("[partners_title!t]", "[partners_line_1!t]"),\
    ("[partners_title!t]", "[partners_line_2!t]")


    # Šukańnie
    credits_s = "{size=80}Šukańnie Fest\n\n"

    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "{vspace=10}"
        credits_s += "{size=26}" + c[1] + "{vspace=1}"
        c1=c[0]
    # credits_s += "\n{size=40}Engine\n{size=40}" + renpy.version()
