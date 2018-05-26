from connector import Connector
from queries import CREATE_MOVIE_TABLE, LIST_MOVIES, GET_MOVIE_IN_PROJECTIONS, CREATE_MOVIE
import sqlite3
conn = sqlite3.connect("cinema.db")
cursor = conn.cursor()



class MovieModel:
    def __init__(self):
        self.conn = Connector()

    def create(self, name, rating):
        query = CREATE_MOVIE
        self.conn.execute_query(query, (name, rating))

    def list(self):
        query = LIST_MOVIES
        return self.conn.all(query)

    @classmethod
    def get_movie_id(self, id):
        query = GET_MOVIE_IN_PROJECTIONS
        a = conn.execute(query, (id,))
        result = []
        for i in a.fetchall():
            result.append(i)
        return result


class Cinema:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.whole = []

    def create_cinema(self):
        for i in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append('.')
            self.whole.append(row)

        for i in range(self.rows):
            for j in range(self.cols):
                print(self.whole[i][j], end=',')
            print(end='\n')

        return self.whole

    @staticmethod
    def calculate_free_seats(projection_id):
        a = 0
        result = conn.execute('SELECT COUNT(*) FROM RESERVATIONS WHERE PROJECTION_ID=?', (projection_id, ))
        for i in result.fetchone():
            a = i

        return 100 - a



    

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def check_user(cls, username, password):

        a = conn.execute('SELECT USERNAME FROM USERS WHERE USERNAME=? AND PASSWORD=?',
                 (username, password))
        try:
            for i in a.fetchone():
                return i
        except Exception:
            return None

    @classmethod
    def register_user(cls, username, password):
        conn.execute('INSERT INTO USERS (USERNAME, PASSWORD) VALUES (?, ?)', (username, password))
        conn.commit()

    @classmethod
    def login_user(cls, username):
        conn.execute('UPDATE USERS SET IS_ACTIVE = 1 WHERE USERNAME=?', (username,))
        conn.commit()

    @classmethod
    def loged_in(cls, username):
        result = conn.execute('SELECT IS_ACTIVE FROM USERS WHERE USERNAME=?', (username,))
        for i in result.fetchone():
            return i
        conn.commit()


# cinema = Cinema()
# cinema.create_cinema()
# print(Cinema.calculate_free_seats(1))
a = MovieModel.get_movie_id(1)
for i in a:
    print(i)
