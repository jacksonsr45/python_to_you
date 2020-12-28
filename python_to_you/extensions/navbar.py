from typing import NoReturn
from flask_nav.elements import Navbar, View
from flask_nav import Nav

nav = Nav()


@nav.navigation()
def top_navbar():
    return Navbar(
        View('Home', 'index'),
    )


def init_app(app) -> NoReturn:
    nav.register_element('top', top_navbar)
    nav.init_app(app)