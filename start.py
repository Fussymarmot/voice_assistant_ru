"""
Помощник умеет:
* распознавать и синтезировать речь;
* сообщать о прогнозе погоды в любой точке мира;
* производить поисковый запрос в поисковой системе Google;
* производить поисковый запрос видео в системе YouTube и открывать список результатов данного запроса;
* выполнять поиск определения в Wikipedia c дальнейшим прочтением;
* "подбрасывать монетку";
* воспроизводить случайное приветствие;
* воспроизводить случайное прощание с последующим завершением работы программы;
* Открывать вк, github, youtube, яндекс музыку, проводник, панель управления, калькулятор, блокнот;
* переводить фразы через гугл переводчик в браузере.

Голосовой ассистент использует для синтеза речи встроенные в операционную систему возможности

Для получения данных прогноза погоды мною был использован сервис OpenWeatherMap, который требует API-ключ.

Для быстрой установки всех требуемых зависимостей можно воспользоваться командой:
pip install requirements.txt
"""
import speech_recognition #инструменты для распознания речи
import pyttsx3 #синтез речи
import wave #создание и чтение файлов формата wav
import os
import random
import requests ,wikipedia, re #получение информации
import webbrowser #открытие ссылок в браузере
from termcolor import colored #подсветка текста
import datetime

class OwnerPerson:
    """
    Информация о владельце, включающая имя, город проживания
    """
    name = ""
    home_city = ""
    

def play_audio_assistant(text_to_speech):
    #воспроизведение аудио ответов голосового ассистента
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def recognize_audio(*args: tuple):
    # Запись и распознание аудио
    with microphone:
        recognize_data = ""

        #регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print(colored("Слушаю...","green"))
            audio = recognizer.listen(microphone, 7, 5) #распознание аудио с микрофона

            with open ("microphone-results.wav", "wb") as file: #сохранение распознанного аудио в файл
                file.write(audio.get_wav_data())
        
        except speech_recognition.WaitTimeoutError:
            print(colored("Проверьте включен ли ваш микрофон, и повторите попытку.","red"))
            return
        
        #online распознавание речи
        try:
            print(colored("Распознаваю...", "red"))
            recognize_data = recognizer.recognize_google(audio, language="ru").lower() #распознавание речи с микрофона
        except speech_recognition.UnknownValueError:
            pass

        return recognize_data

def play_greetings(*args: tuple): #воспроизведение приветствия
    greetings = (f"Здравствуй, {person.name}! Чем я могу помочь вам сегодня?", f"Хорошего дня {person.name}! Чем я могу помочь вам сегодня?")
    greetings_random = random.choice(greetings) #выбор случайного приветствия
    play_audio_assistant(greetings_random) #воспроизведение приветствия

def declension(n, forms): #проверка на правильное написание формы слова
            n = abs(n)
            nn = n % 100
            if 5 <= nn <= 20:
                return forms[2]
            nn = nn % 10
            if nn == 1:
                return forms[0]
            if 2 <= nn <= 4:
                return forms[1]
            return forms[2]

def weather_in_the_city(*args: tuple): #прогноз погоды
    city_arg = " ".join(args[0])
    if city_arg == "":
        city_arg = person.home_city

    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city_arg+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = requests.get(url).json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        weather_data = weather_data['weather'][0]['description']

        if int(temperature) == 0 or int(temperature) >= 5 or int(temperature) <= -5: # правильность написания слова градус
            degree = declension(int(temperature), [" градус", " градуса", " градусов"])
        else:
            degree = " градусов"

        if int(temperature_feels) == 0  or int(temperature_feels) >=5:
            degree_2 = declension(int(temperature_feels), [" градус", " градуса", " градусов"])
        else:
            degree_2 = " градусов"

        play_audio_assistant(f'Сейчас в городе{city_arg} {temperature} {degree} цельсия  ')
        play_audio_assistant(f"Ощущается как: {temperature_feels} {degree_2} цельсия")
        play_audio_assistant(f"{weather_data}")
    except:
        play_audio_assistant("Не удалось узнать погоду, повторите попытку чуть позже.")

def wikipedia_search(*args: tuple): #поиск в википедии
    wikipedia.set_lang("ru")
    try:
        requests_for_information = " ".join(args[0])
        
        ny = wikipedia.page(requests_for_information )
        # Получаем первую тысячу символов
        wikitext=ny.content[:500]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        
        # Возвращаем текстовую строку
        play_audio_assistant(wikitext2)

    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except:
        play_audio_assistant("Извините, но я не могу найти информацию по этому запросу")
   
def coin_toss(*args: tuple): #бросок монетки
    coins = ("решка", "орёл", "решка", "орёл", "решка", "орёл", "решка", "орёл", "решка", "орёл", "решка", "орёл", "решка", "орёл", "ребро")
    coin = random.choice(coins)
    if coin == "решка":
        play_audio_assistant("Выпала решка")
    elif coin == "орёл":
        play_audio_assistant("Выпал орёл")
    else:
        result_rebro_list = ("Ой, монетка укатилась за шкаф", "Монетка провалилась в щель, выпало ребро", "Куда она подевалась? Думаю это ничья")
        result_rebro = random.choice(result_rebro_list)
        play_audio_assistant(result_rebro)

def search_for_vidio_on_youtube(*args: tuple): #поиск видео на youtube
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    play_audio_assistant("Вот что я нашёл по вашему запросу на ютубе")

def open_app_or_website(*args: tuple): #открытие приложения или сайта
    if not args[0]: return
    search_term = " ".join(args[0])
    if search_term == "вк" or search_term == "вконтакте":
        url = "https://www.vk.com/"
        webbrowser.get().open(url)
        play_audio_assistant("Открываю Вконтакте")
    elif search_term == "github" or search_term == "git":
        url = "https://www.github.com/"
        webbrowser.get().open(url)
        play_audio_assistant("Открываю Гитхаб")
    elif search_term == "youtube" or search_term == "ютуб":
        url = "https://www.youtube.com/"
        webbrowser.get().open(url)
        play_audio_assistant("Открываю Ютуб")
    elif search_term == "музыка" or search_term == "музыку":
        url = "https://www.music.yandex.ru/home?from=tableau_yabro"
        webbrowser.get().open(url)
        play_audio_assistant("Открываю Яндекс музыку")
    elif search_term == "проводник": 
        os.system("start explorer")
        play_audio_assistant("Открываю Проводник")
    elif search_term == "панель управления":
        os.system("start control")
        play_audio_assistant("Открываю Панель управления")
    elif search_term == "блокнот":
        os.system("start notepad")
        play_audio_assistant("Открываю Блокнот")
    elif search_term == "калькулятор":
        os.system("start calc")
        play_audio_assistant("Открываю Калькулятор")
    else:
        play_audio_assistant("Извините, но я не могу открыть это приложение или сайт")
        url =  "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        play_audio_assistant("Вот что нашлось по вашему запросу в гугл.")

def search_google(*args: tuple): #поиск в гугле
    if not args[0]: return
    search_term = " ".join(args[0])
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)
    play_audio_assistant("Вот что я нашёл по вашему запросу в гугл.")

def google_translate(*args:tuple): #перевод
    if not args[0]: return
    search_term = " ".join(args[0])
    url = f"https://translate.google.ru/?sl=auto&tl=ru&text={search_term}&op=translate"
    webbrowser.get().open(url)
    play_audio_assistant("Открываю переводчик")

def data_time(*args: tuple):
    if not args[0]: return
    args = " ".join(args[0])
    current_time = datetime.datetime.now()
    if int(current_time.hour) == 0 or int(current_time.hour) >= 5 or int(current_time.hour) <= -5: # правильность написания слова час
        hour = declension(int(current_time.hour), [" час", " часа", " часов"])
    else:
        hour = " часов"
    
    if int(current_time.minute) == 0 or int(current_time.minute) >= 5 or int(current_time.minute) <= -5: # правильность написания слова минута
        minute = declension(int(current_time.hour), [" минута", " минуты", " минут"])
    else:
        minute = " минут"

    month = {1: "января", 2: "февраля", 3: "марта", 4:"апреля", 5:"мая",6:"июня", 7:"июля", 8:"августа", 9:"сентября", 10:"октября", 11:"ноября", 12:"декабря"}

    if args =="время" or args == "времени":
        play_audio_assistant(f"Сейчас {current_time.hour}{hour}{current_time.minute}{minute}" )
    elif args == "дата" or args == "число" or args == "сегодня число" or args == "сегодня дата":
        play_audio_assistant(f"Сегодня {current_time.day} {month[current_time.month]} {current_time.year} года.")

def bye_bye(*args: tuple):
    byes = (f"До свидания, {person.name}! Хорошего дня!", f"До скорой встречи, {person.name}!")
    bye = random.choice(byes)
    play_audio_assistant(bye)
    exit()

def initial_greetings(): # приветствие при включении
    current_time = datetime.datetime.now()
    if current_time.hour >= 4 and current_time.hour < 12 :
        play_audio_assistant(f"Доброе утро, {person.name}!")
    elif current_time.hour >= 12 and current_time.hour < 18:
        play_audio_assistant(f"Добрый день, {person.name}!")
    elif current_time.hour >= 18 and current_time.hour < 22:
        play_audio_assistant(f"Добрый вечер, {person.name}!")
    else:
        play_audio_assistant(f"Доброй ночи, {person.name}!")


commands = { #команды голосового помошника, которые можно использовать
    ("привет", "здравствуй", "приветствую"): play_greetings,
    ("погода", "погоду"): weather_in_the_city ,
    ("объясни", "поясни", "расскажи", "подскажи", "что", "кто"): wikipedia_search,
    ("орёл", "решка", "подбрось", "подкинь", "брось", "кинь", "монетка", "монетку"): coin_toss,
    ("видео", "ролик", "видеоролик"): search_for_vidio_on_youtube,
    ("открой", "запусти", "включи"): open_app_or_website,
    ("найди", ): search_google,
    ("переведи", "перевод", "перевести"): google_translate,
    ("какой", "сколько","какая", "какое"): data_time,
    ("пока", "до", "прощай",   ): bye_bye

   
} 

def execute_command_with_name(command_name: str, *args: list):
    """
    Выполнение заданной пользователем команды с дополнительными аргументами
    :param command_name: название команды
    :param args: аргументы, которые будут переданы в функцию
    :return:
    """
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
        else:
            pass  # print("Комманда не найдена")

if __name__ == "__main__":
    #инструменты для распознания и ввода речи
    recognizer = speech_recognition.Recognizer() #инструмент для распознания речи
    microphone = speech_recognition.Microphone() #переменная для ввода речи с микрофона

    ttsEngine = pyttsx3.init() #инструмент для синтеза речи

    #установка голоса по умолчанию
    voice = ttsEngine.getProperty("voices")
    ttsEngine.setProperty("voice", voice[3].id)
   
   #настройки пользователя
    person = OwnerPerson()
    person.name = "Дмитрий" #ваше имя
    person.home_city = "шахунья" #ваш город
  

    initial_greetings() #приветствие при включении
    
    while True:
        #старт записи речи с распознаванием
        #и удаление записанного в микрофон аудио
        voice_input = recognize_audio()
        os.remove("microphone-results.wav") #удаление записанного в микрофон аудио
        print(colored(voice_input, "blue"))

        # отделение комманд от дополнительной информации (аргументов)
        voice_input = voice_input.split(" ")
        command = voice_input[0]
        command_options = [str(input_part) for input_part in voice_input[1:len(voice_input)]]
        execute_command_with_name(command, command_options)

        
