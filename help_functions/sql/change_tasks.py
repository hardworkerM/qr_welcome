from loader import db


def user_tasks_db(user_id):
    tasks = db.fetchall(f"SELECT title FROM memo WHERE user_id = {user_id}")
    tasks = [i[0] for i in tasks]
    return tasks


def delete_tasks_db(user_id, title):
    db.query(f"DELETE FROM memo WHERE user_id = {user_id} AND title = '{title}'")
