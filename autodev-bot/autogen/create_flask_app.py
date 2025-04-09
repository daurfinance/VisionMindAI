Конечно, вот пример кода для такого Flask-приложения:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return jsonify({"message": "Hello from bot!"})

if __name__ == '__main__':
    app.run()
```

Сохраните этот код в файле `app.py`, убедитесь, что у вас установлен Flask (можно установить с помощью `pip install Flask`), а затем запустите приложение с помощью команды `python app.py`. После этого вы сможете обратиться к маршруту `/hello` и получить JSON `{"message": "Hello from bot!"}`.