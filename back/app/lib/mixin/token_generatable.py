from abc import ABCMeta
import random
import string


class TokenGeneratable(metaclass=ABCMeta):
    def generate_token(self):
        seeds = string.digits + string.ascii_lowercase + string.ascii_uppercase
        self.token = ''.join([random.choice(seeds) for i in range(12)])
