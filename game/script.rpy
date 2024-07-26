﻿define gui.text_outlines = [(4, "0124", 0, 0), (3, "0124", 0, 0), (1, "0124", 0, 0), (1, "0124", 0, 0)]
# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
# define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


label splashscreen:
    # громкость по умолчанию
    python:
        # при первом запуске
        if not persistent.set_volumes:
            persistent.set_volumes = True
            # музыку потише
            _preferences.volumes['music'] = .5
            _preferences.volumes['sfx'] = .5
            # игра на весь экран
            _preferences.fullscreen = True
    return


# Игра начинается здесь:
label start:

    # scene bg room

    # show eileen happy

    # e "Вы создали новую игру Ren'Py."

    # e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    # определим фон игры, время игры в секундах
    # и зададим параметры игры - спрайты и положение для собираемых предметов
    $ hf_init("bg room", 5,
        ("beer", 1013, 705, _("Мишка")),
        ("elf", 111, 560, _("Эльф")),
        ("flowers", 700, 615, _("Букет")),
        ("skull", 1813, 161, _("Череп")),
        ("sprite", 355, 240, _("Дотти-чан")),
        # НЕОБЯЗАТЕЛЬНЫЕ ПАРАМЕТРЫ:
        # включаем смену курсора при наведении
        mouse=True,
        # включаем инвентарь с убиранием из него найденных предметов
        inventory=False,
        # включаем подсказки
        hint=True,
        # включаем подсветку предмета при наведении
        hover=brightness(.05),
        # уменьшаем размеры ячеек инвентаря, чтобы не мешали собирать предметы
        w=200,
        h=200
    )

    # покажем вместе с фоном и фигурки на нём
    $ hf_bg()
    with dissolve

    centered "{size=+24}Нужно собрать все предметы за 5 секунд.\nНачинаем!"

    # запустим игру
    $ hf_start()

    # жёсткая пауза, чтобы игрок перестал кликать и не пропустил результаты
    $ renpy.pause(1, hard=True)

    # результаты
    if hf_return == 0:
        centered "{size=+24}Ура! Все предметы собраны!"
    else:
        centered "{size=+24}GAME OVER\nНе собрано предметов: [hf_return]."

    menu:
        "Ещё раз":
            jump start

        "Хватит":
            pass

    $ hf_hide()
    with dissolve
    return
