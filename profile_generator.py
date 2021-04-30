import os
from random import randint
from load_data import loadInTxt

def_settings = "chrome_path: \nlanguage: RU"
alert_ru = "*Все браузеры откроются одновременно, учитывайте нагрузку на систему."
alert_en = "*All browsers will open at the same time, take into account the load on the system."

ask_ru = 'Сколько профилей создать?\nПользователь: '
ask_en = 'How many profiles to create?\nUser: '

error_ru = 'Похоже вы ввели не число...'
error_en = 'It looks like your enter is not a digit...'

success_ru = 'Профили успешно созданы.'
success_en = 'Profiles created successfully.'

wait_ru = "Нажмите Enter чтобы закрыть..."
wait_en = "Press Enter to close"

print(
"""




                 _______________________________________
                |                                       |
                |        Chrome profiles Creator        |
                |            by @abuz.trade             |
                |                                       |
                |      Creator: vk.com/abuz.trade       |
                |      Group: vk.com/lowbank.trade      |
                |                                       |
                 ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
 
 
 
"""
)

def get_text(p: str):
    return eval(f'{p}_{l}')

settings = loadInTxt(create=True).get("settings.txt", create_data="chrome_path: \nlanguage: RU\noptions: ")

if settings.get('language') is None or \
   settings.get('chrome_path') is None or \
   settings.get('options') is None:
       
    print('settings.txt filled incorrectly. Refill it')
    with open('settings.txt', 'w') as f: f.write(def_settings)
    input(get_text('wait'))
    
elif settings.get('language').upper() not in ['RU', 'EN']:
    print('Language must be RU or EN...')
    print('Program will use English')
    settings['language'] = 'EN'
    
l = settings['language'].lower()

cmd = f'start "Chrome" "{settings["chrome_path"]}" --profile-directory="RANDOM_INT" {settings["options"]}'
print(get_text('alert'))
while True:
    count = input(get_text('ask'))
    if not count.isdigit():
        print(get_text('error'))
        continue
    print()
    count = int(count)
    
    _file = ""
    for _ in range(count):
        _file += cmd.replace('RANDOM_INT', str(randint(1, 999999999999999))) + '\n'
    else:
        _file += "DEL \"%~f0\" && (exit) || (exit)\n"
    
    filename = f'create_{count}_profiles.bat'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(_file)
    os.system(f'start {filename}')
    print(get_text('success'))
    
