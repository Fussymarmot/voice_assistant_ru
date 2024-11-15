![Awesome ReadME](https://avatars.mds.yandex.net/i?id=1bb1dfd9088da51d4096a5e1adc2943a_l-5277049-images-thumbs&n=13)

# Voice Assistant Python App for Windows, Linux & MacOS

[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)](https://img.shields.io/github/v/release/navendu-pottekkat/awesome-readme?include_prereleases)
[![GitHub last commit](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/last-commit/navendu-pottekkat/awesome-readme)
[![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
[![GitHub](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)](https://img.shields.io/github/license/navendu-pottekkat/awesome-readme)

<h1>Возможности приложения</h1>
<p>Данный проект голосового ассистента на Python 3 для Windows и Linux умеет:</p>
<li>распознавать и синтезировать речь;</li>
<li>сообщать о прогнозе погоды в любой точке мира;</li>
<li>производить поисковый запрос в поисковой системе Google;</li>
<li>производить поисковый запрос видео в системе YouTube и открывать список результатов данного запроса;</li>
<li>выполнять поиск определения в Wikipedia c дальнейшим прочтением;</li>
<li>"подбрасывать монетку";</li>
<li>воспроизводить случайное приветствие;</li>
<li>воспроизводить случайное прощание с последующим завершением работы программы;</li>
<li>Открывать вк, github, youtube, яндекс музыку, проводник, панель управления, калькулятор, блокнот;</li>
<li>переводить фразы через гугл переводчик в браузере.</li>


# Содержание
- [Название проекта](#voice-assistant-python-app-for-windows,-linux-&--macos)
- [Содержание](#содержание)
- [Установка](#установка)
- [Прочие зависимости](#прочие-зависимости)
- [Настройка получения прогноза погоды от OpenWeatherMap](#настройка-получения-прогноза-погоды-от-openweathermap)

# Установка
Установка ассистента:
```shell
git clone https://github.com/Fussymarmot/voice_assistant_ru.git
```

# Прочие зависимости
Команды для установки прочих сторонних библиотек:
```shell
pip install SpeechRecognition
pip install wikipedia
pip install pyttsx3
pip install termcolor
pip install request
pip install pyaudio
```
Вместо этого можно использовать:
```shell
pip install requirements.txt
```

# Настройка получения прогноза погоды от OpenWeatherMap
Для получения данных прогноза погоды мною был использован сервис `OpenWeatherMap`, который требует API-ключ. 
