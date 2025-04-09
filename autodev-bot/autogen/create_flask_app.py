Конечно, вот пример минимального Flask-приложения с одним маршрутом /hello:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from bot!"})

if __name__ == '__main__':
    app.run()
```

Сохраните код в файле, например, app.py, запустите его, и затем откройте в браузере http://127.0.0.1:5000/hello. Вы увидите JSON {"message": "Hello from bot!"}.