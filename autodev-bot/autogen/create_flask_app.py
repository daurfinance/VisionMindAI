Вот минимальное Flask-приложение, которое отвечает на данное ТЗ:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return jsonify({"message": "Hello from bot!"})

if __name__ == '__main__':
    app.run()
```

Запустите это приложение и откройте свой web-браузер по адресу `http://127.0.0.1:5000/hello`, чтобы увидеть ответ в формате JSON.