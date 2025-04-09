import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "knowledge.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def save_to_history(prompt, result):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO history (prompt, result) VALUES (?, ?)",
        (prompt, result)
    )
    conn.commit()
    conn.close()
def get_latest_prompt():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT prompt FROM history ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
def get_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT prompt, result FROM history ORDER BY id DESC")
    results = cursor.fetchall()
    conn.close()
    return results
def clear_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()
def get_all_prompts(): 
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT prompt FROM history ORDER BY id DESC")
    results = cursor.fetchall()
    conn.close()
    return [result[0] for result in results]
def get_all_results():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT result FROM history ORDER BY id DESC")
    results = cursor.fetchall()
    conn.close()
    return [result[0] for result in results]
def get_all_history():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    results = cursor.fetchall()
    conn.close()
    return results
def delete_history_entry(entry_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
def get_entry_by_id(entry_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE id = ?", (entry_id,))
    result = cursor.fetchone()
    conn.close()
    return result
def update_entry(entry_id, prompt, result): 
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE history SET prompt = ?, result = ? WHERE id = ?", (prompt, result, entry_id))
    conn.commit()
    conn.close()
def get_all_entries():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history")
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM history")
    count = cursor.fetchone()[0]
    conn.close()
    return count
def get_prompt_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT prompt) FROM history")
    count = cursor.fetchone()[0]
    conn.close()
    return count
def get_result_count():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT result) FROM history")
    count = cursor.fetchone()[0]
    conn.close()
    return count
def get_last_entry():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result
def get_first_entry():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY id ASC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result
def get_random_entry():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result
def get_entry_by_prompt(prompt):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE prompt = ?", (prompt,))
    result = cursor.fetchone()
    conn.close()
    return result
def get_entry_by_result(result):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE result = ?", (result,))
    result = cursor.fetchone()
    conn.close()
    return result
def get_entry_by_date(date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE date = ?", (date,))
    result = cursor.fetchone()
    conn.close()
    return result
def get_entry_by_date_range(start_date, end_date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE date BETWEEN ? AND ?", (start_date, end_date))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_keyword(keyword): 
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE prompt LIKE ? OR result LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_author(author):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE author = ?", (author,))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_tags(tags):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE tags LIKE ?", ('%' + tags + '%',))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_file(filename):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE filename = ?", (filename,))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_file_and_author(filename, author):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE filename = ? AND author = ?", (filename, author))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_file_and_date(filename, date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE filename = ? AND date = ?", (filename, date))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_file_and_tags(filename, tags):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE filename = ? AND tags LIKE ?", (filename, '%' + tags + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_author_and_date(author, date):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE author = ? AND date = ?", (author, date))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_author_and_tags(author, tags):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE author = ? AND tags LIKE ?", (author, '%' + tags + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_date_and_tags(date, tags):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE date = ? AND tags LIKE ?", (date, '%' + tags + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_author_date_tags(author, date, tags):  
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE author = ? AND date = ? AND tags LIKE ?", (author, date, '%' + tags + '%'))
    results = cursor.fetchall()
    conn.close()
    return results
def get_entry_by_author_and_file(author, filename):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM history WHERE author = ? AND filename = ?", (author, filename))
    results = cursor.fetchall()
    conn.close()
    return results 