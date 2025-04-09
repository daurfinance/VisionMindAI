Конечно, вот пример кода для Flask-приложения:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello from bot!'})

if __name__ == '__main__':
    app.run()
```

Этот код создает простое Flask-приложение с одним маршрутом /hello, который возвращает JSON {"message": "Hello from bot!"}. Вы можете запустить это приложение и обратиться к http://127.0.0.1:5000/hello в браузере или через curl, чтобы получить ответ.

Если у вас возникнут дополнительные вопросы, не стесняйтесь спрашивать.