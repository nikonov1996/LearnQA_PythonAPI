# LearnQA_PythonAPI
Данный репозиторий содержит проект из курса "Автоматизация тестирования REST API на Python"

Ссылка на официальный курс: https://software-testing.ru/edu/3-online/321-rest-api-python 

Ссылка на курс на CourseHunter.ru : https://coursehunter.net/course/avtomatizaciya-testirovaniya-rest-api-na-python 

Курс брался с торрента. Домашние задания выполнены, но без разбора и советов преподавателя.

Материалы по курсу, приложены на CourseHunter.ru.
Используемое api:  https://playground.learnqa.ru/api/ 

# Домашние задания:

**x1: Отправка формы авторизации**

Давайте представим, что мы тестируем форму авторизации на любом веб-сайте. Пользователь должен заполнить email, пароль и отправить форму. Соответственно, в момент отправки сформируется и отправится HTTP-запрос. Какой тип запроса вы бы ожидали увидеть в этом случае: GET или POST? Почему?

=============================================================



**Ex2: Структура HTTP запроса**

На уроке мы рассказывали о структуре HTTP-запроса. Определите с помощью Chrome DevTools или любым другим способом:
1) в какой части запроса отправляются cookie от клиента к серверу.
2) в какой части ответа сервер указывает клиенту какие cookie нужно выставить.

=============================================================



**Ex3: Создание репозитория**

В дальнейшем мы будем все домашние заданий сдавать в виде ссылок на коммиты в Github. Так что давайте к этому подготовимся.
Создайте проект в PyCharm или любой удобной вам IDE. Напишите программу, которая выводит: “Hello from <ваше_имя>”.
На Github создайте репозиторий LearnQA_Python_API и выложите проект туда. Не забудьте сделать репозиторий публичным.


=============================================================


**Ex4: GET-запрос**

В проекте создать скрипт, который отправляет GET-запрос по адресу: https://playground.learnqa.ru/api/get_text
Затем с помощью функции print вывести содержимое текста в ответе на запрос. 
Когда скрипт будет готов - давайте его закоммитим в наш репозиторий.

Ex5: Парсинг JSON

Давайте создадим пустой Python-скрипт.
Внутри него создадим переменную json_text. Значение этой переменной должно быть таким, как указано тут: https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37

Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.

=============================================================



**Ex6: Длинный редирект**
Необходимо написать скрипт, который создает GET-запрос на метод: https://playground.learnqa.ru/api/long_redirect

С помощью конструкции response.history необходимо узнать, сколько редиректов происходит от изначальной точки назначения до итоговой. И какой URL итоговый.

=============================================================

**Ex7: Запросы и методы**

Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE

При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос. Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’. И так далее.

Надо написать скрипт, который делает следующее:

1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. 
Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. 
И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, 
но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

Не забывайте, что для GET-запроса данные надо передавать через params=
А для всех остальных через data=

=============================================================


**Ex8: Токены**

Иногда API-метод выполняет такую долгую задачу, что за один HTTP-запрос от него нельзя сразу получить готовый ответ. 
Это может быть подсчет каких-то сложных вычислений или необходимость собрать информацию по разным источникам.
В этом случае на первый запрос API начинает выполнения задачи, а на последующие ЛИБО говорит, что задача еще не готова, 
ЛИБО выдает результат. Сегодня я предлагаю протестировать такой метод.
Сам API-метод находится по следующему URL: https://playground.learnqa.ru/ajax/api/longtime_job

Если мы вызываем его БЕЗ GET-параметра token, метод заводит новую задачу, а в ответ выдает нам JSON со следующими полями:

* seconds - количество секунд, через сколько задача будет выполнена
* token - тот самый токен, по которому можно получить результат выполнения нашей задачи

Если же вызвать метод, УКАЗАВ GET-параметром token, то мы получим следующий JSON:

* error - будет только в случае, если передать token, для которого не создавалась задача. В этом случае в ответе будет следующая надпись - No job linked to this token
* status - если задача еще не готова, будет надпись Job is NOT ready, если же готова - будет надпись Job is ready
* result - будет только в случае, если задача готова, это поле будет содержать результат

Наша задача - написать скрипт, который делал бы следующее:

1) создавал задачу
2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
3) ждал нужное количество секунд с помощью функции time.sleep() - для этого надо сделать import time
4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
=============================================================


**Ex9*: Подбор пароля**

Это необязательное задание повышенной сложности. Если вы хотите диплом с отличием - вам нужно его выполнить. 
В остальных случаях - нет.

Сегодня к нам пришел наш коллега и сказал, что забыл свой пароль от важного сервиса. Он просит нас помочь ему написать программу, которая подберет его пароль.
Условие следующее. Есть метод: https://playground.learnqa.ru/ajax/api/get_secret_password_homework
Его необходимо вызывать POST-запросом с двумя параметрами: login и password
Если вызвать метод без поля login или указать несуществующий login, метод вернет 500
Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.

У метода существует защита от перебора. Если верно указано поле login, но передан неправильный password, 
то авторизационная cookie все равно вернется. НО с "неправильным" значением, которое на самом деле не позволит создавать авторизованные запросы. Только если и login, и password указаны верно, вернется cookie с "правильным" значением. 
Таким образом используя только метод get_secret_password_homework невозможно узнать, передали ли мы верный пароль или нет.

По этой причине нам потребуется второй метод, который проверяет правильность нашей авторизованной cookie: https://playground.learnqa.ru/ajax/api/check_auth_cookie

Если вызвать его без cookie с именем auth_cookie или с cookie, у которой выставлено "неправильное" значение, метод вернет фразу "You are NOT authorized".
Если значение cookie “правильное”, метод вернет: “You are authorized”

Коллега говорит, что точно помнит свой login - это значение super_admin
А вот пароль забыл, но точно помнит, что выбрал его из списка самых популярных паролей на Википедии (вот тебе и супер админ...).
Ссылка: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
Искать его нужно среди списка Top 25 most common passwords by year according to SplashData

Итак, наша задача - написать скрипт и указать в нем login нашего коллеги и все пароли из Википедии в виде списка. Программа должна делать следующее:

1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework. В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.

2. Далее эту cookie мы должна передать во второй метод check_auth_cookie. Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный. В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.

=============================================================

**Ex10: Тест на оротую фразу**

В рамах этой заачи с помощью pytest неохоимо написать тест, оторый просит ввести в онсоли люую фразу ороче 15 символов. А затем с помощью assert проверет, что фраза ействительно ороче 15 символов.

Чтоы в переменную получить значение, ввеенное из онсоли, неохоимо написать вот таой о:
phrase = input("Set a phrase: ")

Внимание, чтоы pytest не игнорировал оману ввоа с лавиатуры, запусать тест нужно с лючиом "-s": python -m pytest -s my_test.py

=========================================

**Ex11: Тест запроса на мето cookie**

еохоимо написать тест, оторый елает запрос на мето: https://playground.learnqa.ru/api/homework_cookie
тот мето возвращает аую-то cookie с аим-то значением. еохоимо с помощью фунции print() понть что за cookie и с аим значением, и зафисировать это повеение с помощью assert

Чтоы pytest не игнорировал print() неохоимо использовать лючи "-s": python -m pytest -s my_test.py

=================================================


**Ex12: Тест запроса на мето header**

еохоимо написать тест, оторый елает запрос на мето: https://playground.learnqa.ru/api/homework_header
тот мето возвращает headers с аим-то значением. еохоимо с помощью фунции print() понть что за headers и с аим значением, и зафисировать это повеение с помощью assert

Чтоы pytest не игнорировал print() неохоимо использовать лючи "-s": python -m pytest -s my_test.py

=============================================================


**Ex13: User Agent**

User Agent - это оин из заголовов, позволющий серверу узнавать, с аого евайса и раузера пришел запрос.
н формируетс автоматичеси лиентом, например раузером.
преелив, с аого евайса или раузера пришел нам пользователь мы сможем отать ему тольо тот онтент, оторый ему нужен.

аш разраотчи написал мето: https://playground.learnqa.ru/ajax/api/user_agent_check
ето опреелет по строе заголова User Agent слеующие параметры:

device - iOS или Android

browser - Chrome, Firefox или ругой раузер

platform - моильное приложение или ве

Если мето не может опреелить аой-то из параметров, он выставлет значение Unknown.

аша заача написать параметризированный тест. тот тест олжен рать из ата-провайера User Agent и ожиаемые значени, GET-елать запрос с этим User Agent и уежатьс, что результат раоты нашего метоа правильный - т.е. в ответе ожиаемое значение всех трех полей.

Списо User Agent и ожиаемых значений можно найти по этой ссыле: https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26

ример того, а олжен выглеть запрос с уазанным User Agent:

requests.get(

"https://playground.learnqa.ru/ajax/api/user_agent_check",

headers={"User-Agent": "Some value here"}

)

============================================================


**Ex14: Формирование фреймвора**

а этом урое мы начали созавать свой фреймвор.
н нам пригоитс в альнейшим, та а омашние заани слеующего уроа уут опиратьс на метоы из этого фреймвора.

отом эта заача в том, чтоы повторить то, что мы проелали на урое:

- созать ласс BaseCase в иретории lib/

- созать ласс Assertions в иретории lib/

- созать тест TestUserAuth в иретории tests/

===========================================================================

**Ex15: Тесты на метод user**

В соответствующем классе TestUserRegister, который мы создали на уроке,
необходимо написать больше тестов на создающий пользователя POST-метод: https://playground.learnqa.ru/api/user/

Список тестов:

- Создание пользователя с некорректным email - без символа @

- Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить, что отсутствие любого параметра не дает зарегистрировать пользователя

- Создание пользователя с очень коротким именем в один символ

- Создание пользователя с очень длинным именем - длиннее 250 символов

========================================


**Ex16: Запрос данных другого пользователя**

На занятиях в классе TestUserGet мы писали тест на запрос, показывающий данные пользователя. Мы покрыли тестами два кейса:

- неавторизованный запрос на данные - там мы получили только username

- авторизованный запрос - мы были авторизованы пользователем с ID 2 и делали запрос для получения данных того же пользователя,
в этом случае мы получали все поля

В этой задаче нужно написать тест, который авторизовывается одним пользователем, но получает данные другого (т.е. с другим ID).
И убедиться, что в этом случае запрос также получает только username, так как мы не должны видеть остальные данные чужого пользователя.

===================================================


**Ex17: Негативные тесты на PUT**

На занятиях мы написали только позитивный тест на PUT-метод редактирования пользователя.
Давайте напишем несколько негативных:

- Попытаемся изменить данные пользователя, будучи неавторизованными
- Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
- Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем, на новый email без символа @
- Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем, на очень короткое значение в один символ

=====================


**Ex18: Тесты на DELETE**

У нас есть метод, который удаляет пользователя по ID - DELETE-метод https://playground.learnqa.ru/api/user/{id}
Само собой, удалить можно только того пользователя, из-под которого вы авторизованы.
Необходимо в директории tests/ создать новый файл test_user_delete.py с классом TestUserDelete.

Там написать следующие тесты.

Первый - на попытку удалить пользователя по ID 2. Его данные для авторизации:


        data = {

            'email': 'vinkotov@example.com',

            'password': '1234'

        }



Убедиться, что система не даст вам удалить этого пользователя.

Второй - позитивный. Создать пользователя, авторизоваться из-под него, удалить, затем попробовать получить его данные по ID и убедиться, что пользователь действительно удален.

Третий - негативный, попробовать удалить пользователя, будучи авторизованными другим пользователем.

==========================================


**Ex19: Теги Allure**

Давайте добавим больше Allure-тегов во все написанные нами тесты.
Выбирайте любые, которые понравятся из официальной документации - https://docs.qameta.io/allure/

Цель задания - поэкспериментировать с бОльшим количеством тегов, узнать, где именно в отчете они отображаются.
В этом задании не будет правильных и неправильных результатов.
Но все же нам очень интересно посмотреть, какие теги вы сочтете особенно полезными для вашего фреймворка.

==================================================
