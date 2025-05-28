from attr import dataclass


@dataclass
class UserData:
    name:  str = "Evgeny"
    email: str = "testpc99@ya.com"
    password: str = "123456"


