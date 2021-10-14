## Курс валют. Приложение для bitrix24

Выводит курсы валют согласно дате взяты с cbr.ru 
Валюты:

- RUB-EUR

- RUB-USD

- RUB-KZT

- RUB-PLN


## Выбор технологий  

Для работы приложения btrix24 необходим удаленный сервер. Платформа делает POST запрос на сервер. Полчает ответ c html. Поэтому нужно написать полноценное приложение, которое умеет обробатывать POST запросы и имеет ssl сертификат. 

Для веб сервера используется flask с uwsgi интерфейсом. В качестве HTTP сервера используется nginx. Для создания ssl сертификатов можно использовать сервис certbot который создает сертификаты letsencrypt.
