FROM ubuntu:22.04

# Установка системных пакетов
RUN apt-get update && apt-get install -y \
    xvfb \
    fluxbox \
    x11vnc \
    python3 \
    python3-pip \
    python3-tk \
    python3-pygame \
    net-tools \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Установка Guacamole (опционально)
# RUN wget https://archive.apache.org/dist/guacamole/1.5.0/binary/guacamole-1.5.0.war -O /tmp/guacamole.war

WORKDIR /app

# Копирование приложения
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

# Скрипт запуска
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 5900 8080

CMD ["/start.sh"]
