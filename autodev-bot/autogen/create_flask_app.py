Конечно, вот пример минимального Flask-приложения:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from bot!"})

if __name__ == '__main__':
    app.run()
```

Этот код создает Flask-приложение с одним маршрутом `/hello`, который возвращает JSON `{"message": "Hello from bot!"}`. Чтобы запустить приложение, сохраните его в файл, например `app.py`, и выполните команду `python app.py` в командной строке. После этого приложение будет доступно по адресу `http://127.0.0.1:5000/hello`.