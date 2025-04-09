1. Состояние Бота:
```
const botState = {
  name: "Бот-программист",
  language: "JavaScript",
  framework: "Node.js",
  status: "Активен",
};
```

2. Создание UI через Vercel AI SDK:
```
import { createUI } from 'vercel-ai-sdk';

const UI = createUI({
  person: "Бот-программист",
  status: "Активен",
  language: "JavaScript",
  framework: "Node.js",
});

UI.render();
```

3. Создание API:
```
const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.json({
    name: botState.name,
    language: botState.language,
    framework: botState.framework,
    status: botState.status,
  });
});

app.listen(port, () => {
  console.log(`API запущено на порту ${port}`);
});
```

Данный код задает состояние бота, создает UI через Vercel AI SDK и создает API для получения информации о боте. После запуска сервера, можно обращаться к API для получения информации о состоянии бота.