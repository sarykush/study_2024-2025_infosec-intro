---
## Front matter
title: "Отчет по этапу выполнения внешнего курса"
subtitle: "Безопасность в сети"
author: "Татьяна Александровна Буллер"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: IBM Plex Serif
romanfont: IBM Plex Serif
sansfont: IBM Plex Sans
monofont: IBM Plex Mono
mathfont: STIX Two Math
mainfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
romanfontoptions: Ligatures=Common,Ligatures=TeX,Scale=0.94
sansfontoptions: Ligatures=Common,Ligatures=TeX,Scale=MatchLowercase,Scale=0.94
monofontoptions: Scale=MatchLowercase,Scale=0.94,FakeStretch=0.9
mathfontoptions:
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Получение и закрепление на практике знаний об основных механизмах работы сети Интернет и их слабых местах.

# Выполнение контрольных заданий

## Как работает Интернет

![Задание 1](image/1.png){#fig:001 width=70%}

Протоколы TCP и UDP - протоколы транспортного уровня, IP - протокол сетевого уровня. Прикладным из перечисленных является только HTTPS. Это же рассуждение дает ответ на следующий вопрос.

![Задание 2](image/2.png){#fig:002 width=70%}

![Задание 3](image/3.png){#fig:003 width=70%}

Первый из адресов начинается с 421, второй содержит 256. Ни то, ни другое не может являться корректным адресом  IPv4, так как исловный максимальный адрес, который можно получить в этом стандарте - 255.255.255.255

![Задание 4](image/4.png){#fig:004 width=70%}

DNS (Domain Name Server) сопоставляет адрес сайта с его доменным именем и обеспечивает "навигацию" в Интернете. Он не сегментирует данные, не выбирает маршруты для пакетов и не занимается адресацией.

![Задание 5](image/5.png){#fig:005 width=70%}

Прикладной уровень должен быть "верхним", канальный - нижним, таким образом, корректна только последняя цепочка.

![Задание 6](image/6.png){#fig:006 width=70%}

HTTP не предполагает шифрования данных, поэтому считается небезопасным и устаревшим. Шифрует данные между клиентом и сервером HTTPS.

![Задание 7](image/7.png){#fig:007 width=70%}

HTTPS состоит из двух фаз: рукопожатия между клиентом и сервером, в результате которого устанавливаются "условия" общения, и обмена зашифрованными данными. Отсюда очевидно, что подходит только ответ 2.

![Задание 8](image/8.png){#fig:008 width=70%}

Версия протокола TLS определяется совместно сервером и клиентом. ни одна из сторон не может "диктовать" свои условия другой.

![Задание 9](image/9.png){#fig:009 width=70%}

В фазе рукопожатия не предусмотрено именно шифрования данных, так как оно выполняется после установки условий обмена данными в отдельной фазе.

## Персонализация сети

![Задание 10](image/10.png){#fig:010 width=70%}

По-хорошему куки не должны хранить конфиденциальную информацию, такую как пароль или адрес пользователя. поэтому подходят только два последних ответа: идентификатор пользователя и сессии.

![Задание 11](image/11.png){#fig:011 width=70%}

Куки хранят информацию, но не используются для обеспечения надежности соединения самого по себе. Хотя хранение информации на стороне клиента может в общем и целом снижать загруженность сервера.

![Задание 12](image/12.png){#fig:012 width=70%}

Куки присваиваются (генерируются) пользователю сервером и хранятся на стороне клиента.

![Задание 13](image/13.png){#fig:013 width=70%}

Сессионные куки отвечают за хранение данных, связанных с конкретной сессией (моментом посещения и использования) сайта. Они храняется в браузере только во время использования сайта (жизни сессии).

## Браузер ТОР. Анонимизация

![Задание 14](image/14.png){#fig:014 width=70%}

В сети ТОР минимум три промежуточных узла: охранный, промежуточный и выходной.

![Задание 15](image/15.png){#fig:015 width=70%}

Адрес получателя известен отправителю (он выбирает, кому направить сообщение) и выходному узлу (он передает сообщение, полученное от предыдущих узлов цепи, непосредственно получателю).

![Задание 16](image/16.png){#fig:016 width=70%}

Общий секретный ключ отправитель генерирует с каждым из узлов цепи для сохранения целостности передачи.

![Задание 17](image/17.png){#fig:017 width=70%}

Получатель не должен использовать браузер, основанный на луковой маршрутизации, так как доставка сообщения не зависит от него.

## Беспроводные сети Wi-Fi

![Задание 18](image/18.png){#fig:018 width=70%}

Wi-Fi - технология беспроводной сети; работает не только со смартфонами или компьютерами и описана в стандартве 802.11

![Задание 19](image/19.png){#fig:019 width=70%}

Wi-Fi - канал передачи данных, и работает, соответственно, на канальном уровне. На сетевом работает IP, на прикладном - HTTP/HTTPS, на транспортном - TCP/UDP.

![Задание 20](image/20.png){#fig:020 width=70%}

Наименее безопасен из перечисленных WEP, так как длина ключа в этом протоколе не могла превышать 40 бит.

![Задание 21](image/21.png){#fig:021 width=70%}

Данные между хостом и роутером передаются только после аутентификации устройства в сети в зашифрованном виде, поэтому все ответы, кроме 2, неверны.

![Задание 22](image/22.png){#fig:022 width=70%}

Энтерпрайс - решение для бизнеса. Для организации домашних сетей оно не используется.

# Выводы

Получены и закреплены на практике знания об основных механизмах работы сети Интернет и их слабых местах.
