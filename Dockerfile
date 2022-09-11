FROM python:3.8 

# Создаем директорию
WORKDIR /home/tmp

COPY nginx_p.py
COPY nginx.log

EXPOSE 8000

# Запускаем скрипт
CMD [ "python", "-u", "./nginx_p.py" ]
