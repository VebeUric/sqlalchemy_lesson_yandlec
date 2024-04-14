from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    team_data = [
        ['Nick', 'Petrson', 'scientist', 'explore envir', 'module_3', 'Nick_Pete@mars.org'],
        ['Gans', 'Castrop', 'engineer', 'build_rockets', 'module_2', 'GansiCatrostrop@mars.org'],
        ['Jams', 'Lamark', 'doctor', 'keep team healthy', 'module_5', 'JimyNitron@mars.org'],
        ["Scott", "Ridley", "captain", "research engineer",  "module_1", "scott_chief@mars.org"]
    ]
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    for i in team_data:
        existing_user = db_sess.query(User).filter_by(email=i[5]).first()
        if not existing_user:
            tmp_user = User()
            tmp_user.name = i[0]
            tmp_user.surname = i[1]
            tmp_user.position = i[2]
            tmp_user.speciality = i[3]
            tmp_user.address = i[4]
            tmp_user.email = i[5]
            try:
                db_sess.merge(tmp_user)
                db_sess.commit()
                print("Пользователь успешно добавлен")
            except Exception as e:
                db_sess.rollback()
                print(f"Ошибка при добавлении пользователя: {e}")
    db_sess.commit()
    db_sess.close()

    # app.run()


if __name__ == '__main__':
    main()
