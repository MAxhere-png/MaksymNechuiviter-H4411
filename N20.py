'''Огляд бібліотеки "colorama"'''
import colorama

'''Інтроспекція'''
print(dir(colorama)) 
'''['AnsiToWin32', 'Back', 'Cursor', 'Fore', 'Style',
 '__builtins__', '__cached__', '__doc__', '__file__',
 '__loader__', '__name__', '__package__', '__path__',
 '__spec__', '__version__', 'ansi', 'ansitowin32',
 'colorama_text', 'deinit', 'init', 'initialise',
 'just_fix_windows_console', 'reinit', 'win32',
 'winterm']'''

'''Найважливіші атрибути та методи:'''
colorama.init() #- Ініціалізує підтримку кольорів
''''''
from colorama import Fore 
'''Основні атрибути:'''
Fore.RED
Fore.GREEN
Fore.BLUE
Fore.YELLOW
Fore.WHITE
Fore.RESET
'''Як працює:'''
print(Fore.RED + "Червоний текст")
''''''
from colorama import Back
'''Основні атрибути:'''
Back.RED
Back.GREEN
Back.BLUE
Back.YELLOW
Back.RESET
'''Як працює:'''
print(Back.GREEN + "Текст із зеленим фоном")
''''''
from colorama import Style
'''Основні атрибути:'''
Style.BRIGHT
Style.DIM
Style.NORMAL
Style.RESET_ALL
'''Як працює:'''
print(Style.BRIGHT + "Яскравий текст")
''''''
colorama.deinit() #- Вимикає обробку ANSI



