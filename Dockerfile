FROM python:3.10

# Создаем директорию
WORKDIR /home/tmp

COPY . .

# Запускаем скрипт
ENTRYPOINT [ "python", "./nginx_p.py" ]

EXPOSE 8000
