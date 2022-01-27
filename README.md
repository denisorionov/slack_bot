# Программа для отправки сообщений в Slack

Программа принимает на вход json-файл и отправляет текстовые сообщения в каналы Slack из этого json-файла.


Пример запроса:
   ```shell script
    curl -X 'POST' \
  'http://127.0.0.1:8000/message/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "bot_token": "string",
  "channels": [
    {
      "channel": "string",
      "text": "string"
    }
  ] 
  }
 ```

Запуск сервера:
uvicorn main:api --reload
