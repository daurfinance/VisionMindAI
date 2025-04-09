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

Сохрани этот код в файле, например, `app.py`, установи Flask (`pip install flask`) и запусти его командой `python app.py`. Теперь при переходе на `http://127.0.0.1:5000/hello` ты увидишь JSON `{"message": "Hello from bot!"}`.