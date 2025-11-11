#!/bin/bash
set -e

# Настройка переменных окружения
export DISPLAY=:1
RESOLUTION=${RESOLUTION:-1280x720}
VNC_PASSWORD=${VNC_PASSWORD:-password}

# Создание виртуального дисплея
Xvfb $DISPLAY -screen 0 ${RESOLUTION}x24 +extension RANDR &

# Ожидание инициализации X сервера
sleep 2

# Запуск оконного менеджера
fluxbox &

# Настройка VNC пароля (если требуется)
if [ ! -z "$VNC_PASSWORD" ]; then
    mkdir -p ~/.vnc
    x11vnc -storepasswd "$VNC_PASSWORD" ~/.vnc/passwd
fi

# Запуск VNC сервера
x11vnc -display $DISPLAY \
       -forever \
       -shared \
       -rfbauth ~/.vnc/passwd \
       -bg \
       -noxdamage &

# Запуск Guacamole (опционально)
# if [ "$ENABLE_GUACAMOLE" = "true" ]; then
#     java -jar /tmp/guacamole.war &
# fi

# Запуск Python приложения
python3 /app/main.py
