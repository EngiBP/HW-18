Задание
1.Написать и протестировать Telegram-бота, в котором будет реализован следующий функционал:

2.Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
3.При написании бота необходимо использовать библиотеку pytelegrambotapi.
4.Человек должен отправить сообщение боту в виде <имя валюты цену которой он хочет узнать> <имя валюты в которой надо узнать цену первой валюты> <количество первой валюты>.
5.При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
6.При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
7.Для взятия курса валют необходимо использовать API и отправлять к нему запросы с помощью библиотеки Requests.
8.Для парсинга полученных ответов использовать библиотеку JSON.
9.При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
10.Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
11.Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента: имя валюты, цену на которую надо узнать, — base, имя валюты, цену в которой надо узнать, — quote, количество переводимой валюты — amount и возвращает нужную сумму в валюте.
12.Токен telegramm-бота хранить в специальном конфиге (можно использовать .py файл).
13.Все классы спрятать в файле extensions.py.
