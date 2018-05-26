from models import User
from movie_controller import MovieController
import sys
from getpass import getpass


class Reservation:

    @classmethod
    def make_reservation(cls):
        username = input('Hello!\nProvide your user_name:\n>>> ')
        # username = input('username: ')
        #password = getpass(prompt='password: ')
        password =  input('password: ')
        user = User.check_user(username, password)
        if user:
            User.login_user(username)

        else:
            print('Unknown user!\n Would you like to create new user?')
            create_new = input('>>> ')
            if create_new.lower() in ['y', 'yes']:
                username = input('username: ')
                password = getpass('password ')
                User.register_user(username, password)
                User.login_user(username)
        if User.loged_in(username) == 1:
            print('Hello, {}'.format(username))
            while True:
                tickests = input('Step 1 (User): Choose number of tickets> ')
                print('Current movies:')
                MovieController.show_all_movies()
                movie_id = int(input('Step 2 (Movie): Choose a movie> '))
                result = MovieController.show_movies_by_id(movie_id)
                for i in result:
                    print(i)






Reservation.make_reservation()
