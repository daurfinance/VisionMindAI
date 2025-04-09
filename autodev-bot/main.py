import os
import openai
from github import Github
from dotenv import load_dotenv

load_dotenv()

# Загружаем переменные окружения
openai.api_key = os.getenv("OPENAI_API_KEY")
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_user().get_repo(os.getenv("REPO_NAME"))

# Получаем последнее задание
def get_latest_prompt():
    contents = repo.get_contents("prompts")
    latest_prompt = sorted(contents, key=lambda x: x.last_modified, reverse=True)[0]
    return latest_prompt.name, latest_prompt.decoded_content.decode()

# Отправляем промт в OpenAI
def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты бот-программист, пишешь код по ТЗ."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

# Сохраняем результат в GitHub
def save_code_to_repo(filename, content):
    path = f"autogen/{filename}"
    try:
        file = repo.get_contents(path)
        repo.update_file(path, f"Update {filename}", content, file.sha)
    except:
        repo.create_file(path, f"Create {filename}", content)

# Главная функция
def main():
    prompt_filename, prompt_text = get_latest_prompt()
    print(f"[PROMPT] {prompt_filename}")

    result = generate_code(prompt_text)

    filename = prompt_filename.replace(".txt", ".py")
    save_code_to_repo(filename, result)

    print(f"[DONE] Сохранено в autogen/{filename}")

if __name__ == "__main__":
    main()
