Sure! Вот пример минимального Flask-приложения:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from bot!"})

if __name__ == '__main__':
    app.run()
```

Сохраните этот код в файле `app.py` и запустите его. После этого вы сможете обратиться к маршруту `/hello` и получить JSON-ответ `{"message": "Hello from bot!"}`.