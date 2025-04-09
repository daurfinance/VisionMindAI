import os
from github import Github
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
from brain.db import init_db, save_to_history

# Загружаем переменные окружения
load_dotenv()

# Инициализация клиентов
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_user().get_repo(os.getenv("REPO_NAME"))

# Пути внутри репозитория
PROMPTS_DIR = "autodev-bot/prompts"
AUTOGEN_DIR = "autodev-bot/autogen"

# Получение последнего .txt файла из prompts
def get_latest_prompt():
    try:
        contents = repo.get_contents(PROMPTS_DIR)
        prompts = [f for f in contents if f.name.endswith(".txt")]
        if not prompts:
            raise Exception("❌ Нет .txt файлов в prompts/")
        latest_prompt = sorted(prompts, key=lambda x: x.last_modified, reverse=True)[0]
        return latest_prompt.name, latest_prompt.decoded_content.decode()
    except Exception as e:
        print(f"❌ Ошибка при получении prompts из '{PROMPTS_DIR}':\n{e}")
        exit(1)

# Генерация кода через OpenAI
def generate_code(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # можно заменить на "gpt-4" при наличии доступа
            messages=[
                {"role": "system", "content": "Ты бот-программист, пишешь код по ТЗ."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("❌ Ошибка при обращении к OpenAI:")
        print(str(e))
        exit(1)

# Сохранение результата в репозиторий
def save_code_to_repo(filename, content):
    path = f"{AUTOGEN_DIR}/{filename}"
    try:
        existing_file = repo.get_contents(path)
        repo.update_file(path, f"Update {filename}", content, existing_file.sha)
        print(f"🔁 Обновлен файл: {path}")
    except:
        repo.create_file(path, f"Create {filename}", content)
        print(f"✅ Создан новый файл: {path}")

# Главная функция
def main():
    print("🚀 Запуск AutoDev в репозитории:", os.getenv("REPO_NAME"))
    
    # Инициализируем базу знаний
    init_db()

    # Получаем промт
    prompt_filename, prompt_text = get_latest_prompt()
    print(f"📄 Обработка промта: {prompt_filename}")

    # Получаем ответ от OpenAI
    generated_code = generate_code(prompt_text)

    # Сохраняем в базу знаний
    save_to_history(prompt_text, generated_code)

    # Генерация имени файла
    base_filename = prompt_filename.replace(".txt", "")

    # Если это задача на БД — разбиваем код на SQL и Python
    if any(word in prompt_text.lower() for word in ["база данных", "sqlalchemy", "таблицы", "модель sqlalchemy"]):
        if "```sql" in generated_code and "```python" in generated_code:
            sql_part = generated_code.split("```sql")[1].split("```")[0].strip()
            py_part = generated_code.split("```python")[1].split("```")[0].strip()
        else:
            sql_part = ""
            py_part = generated_code

        save_code_to_repo(f"{base_filename}_models.py", py_part)
        if sql_part:
            save_code_to_repo(f"{base_filename}_schema.sql", sql_part)
    else:
        output_filename = f"{base_filename}.py"
        save_code_to_repo(output_filename, generated_code)

    print("✅ Завершено успешно!")

if __name__ == "__main__":
    main()
# Код завершен
# Сохранение истории
# def save_to_history(prompt, result):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO history (prompt, result) VALUES (?, ?)",
#         (prompt, result)
#     )
#     conn.commit()
#     conn.close()
#     return result
# def get_latest_prompt():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT prompt FROM history ORDER BY id DESC LIMIT 1")
#     result = cursor.fetchone()
#     conn.close()
#     return result[0] if result else None
# def get_history():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT prompt, result FROM history ORDER BY id DESC")
#     results = cursor.fetchall()
#     conn.close()
#     return results
# def clear_history():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM history")
#     conn.commit()
#     conn.close()
# def get_all_prompts():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT prompt FROM history ORDER BY id DESC")
#     results = cursor.fetchall()
#     conn.close()
#     return [result[0] for result in results]
# def get_all_results():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT result FROM history ORDER BY id DESC")
#     results = cursor.fetchall()
#     conn.close()
#     return [result[0] for result in results]
# def get_all_history():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM history ORDER BY id DESC")
#     results = cursor.fetchall()
#     conn.close()
#     return results
# def delete_history_entry(entry_id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM history WHERE id = ?", (entry_id,))
#     conn.commit()
#     conn.close()
# def get_entry_by_id(entry_id):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM history WHERE id = ?", (entry_id,))
#     result = cursor.fetchone()
#     conn.close()
#     return result
# def get_all_history():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM history ORDER BY id DESC")
#     results = cursor.fetchall()
#     conn.close()
#     return results
# def update_entry(entry_id, prompt, result):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(
#         "UPDATE history SET prompt = ?, result = ? WHERE id = ?",
#         (prompt, result, entry_id)
#     )
#     conn.commit()
#     conn.close()
# def get_all_entries():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM history")
#     results = cursor.fetchall()
#     conn.close()
#     return results
# def get_all_history():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM history ORDER BY id DESC")
#     results = cursor.fetchall()
#     conn.close()
#     return results
# def update_entry(entry_id, prompt, result):
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute(
#         "UPDATE history SET prompt = ?, result = ? WHERE id = ?",
#         (prompt, result, entry_id)
#     )
#     conn.commit()
#     conn.close()
# def get_all_entries():
#     conn = sqlite3.connect(DB_PATH)
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM history")