import allure
from base.base_page import BasePage

from data.locators import AuthData, AuthLocs
from utilities.logger import Logger


class LoginPage(BasePage):
    # getters:
    def input_user(self):
        return self.is_visible(AuthLocs.input_user)

    def input_pass(self):
        return self.is_visible(AuthLocs.input_pass)

    def login_btn(self):
        return self.is_clickable(AuthLocs.login_btn)

    # actions:
    def fill_input_user(self, username):
        return self.is_visible(AuthLocs.input_user).send_keys(username)

    def fill_pass_user(self, password):
        return self.is_visible(AuthLocs.input_pass).send_keys(password)

    def click_login_btn(self):
        return self.is_clickable(AuthLocs.login_btn).click()

    # methods:
    @staticmethod
    def passw():
        return AuthData.pass_word

    @staticmethod
    def locked_msg():
        return AuthLocs.locked_msg

    @staticmethod
    def login_err_msg():
        return AuthLocs.login_err_msg

    # authorization:
    def auth(self, username, password):
        Logger.add_start_step('auth')
        self.open()
        with allure.step('fill in the fields...'):
            self.fill_input_user(username)
            self.fill_pass_user(password)
        with allure.step('click the login button...'):
            self.click_login_btn()
        return self

    def login(self, username, password=''):
        Logger.add_start_step('login')
        users = {
            'standard_user': AuthData.standard_user,
            'locked_user': AuthData.locked_user,
            'problem_user': AuthData.problem_user,
            'glitch_user': AuthData.glitch_user
        }

        for user, val in users.items():
            if username == user:
                with allure.step(f'Login: {username}...'):
                    print(f'\nLogin: {username}...')
                    return self.auth(val, self.passw())
            elif username not in users:
                print(f'\nWrong login... {self.login_err_msg()}')
                return self.auth(username, password)
