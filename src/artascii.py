# https://github.com/chubin/wttr.in/blob/master/lib/constants.py

art: dict = {
    "neutral": """
        \033[1;5;37m     .--.    \033[0m
        \033[1;5;37m  .-(    ).  \033[0m
        \033[1;5;37m (___.__)__) \033[0m
        """,

    "cloud": """
        \033[1;5;37m     .--.    \033[0m
        \033[1;5;37m  .-(    ).  \033[0m
        \033[1;5;37m (___.__)__) \033[0m""",

    "rain":"""
    \033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m
        \033[38;5;111m   ‘ ‘ ‘ ‘   \033[0m
        """,

    "thunder":
        """\033[38;5;228;5m  ⚡\033[38;5;111;25m‘ ‘\033[38;5;228;5m⚡\033[38;5;111;25m‘ ‘ \033[0m
        \033[38;5;111m  ‘ ‘ ‘ ‘  \033[0m
        """,

    "fog": """
        \033[38;5;251m _ - _ - _ - \033[0m
        \033[38;5;251m  _ - _ - _  \033[0m
        \033[38;5;251m _ - _ - _ - \033[0m
        """,

    "clear": """
        \033[38;5;226m    \\   /    \033[0m
        \033[38;5;226m     .-.     \033[0m
        \033[38;5;226m  ― (   ) ―  \033[0m
        \033[38;5;226m     `-’     \033[0m
        \033[38;5;226m    /   \\    \033[0m
        """,

    "sunny": """
        \033[38;5;226m    \\   /    \033[0m
        \033[38;5;226m     .-.     \033[0m
        \033[38;5;226m  ― (   ) ―  \033[0m
        \033[38;5;226m     `-’     \033[0m
        \033[38;5;226m    /   \\    \033[0m
        """,

    "partly": """
        \033[38;5;226m   \\  /\033[0m
        \033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m
        \033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m
        \033[38;5;226m   /\033[38;5;250m(___(__) \033[0m
      """
}
