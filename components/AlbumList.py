from Component_py.stubs import require, console, __pragma__  # __:skip
from Component_py.component import Component
from components.AlbumDetail import AlbumDetail

React = require("react")
ScrollView = require("react-native").ScrollView
Text = require("react-native").Text

__pragma__("skip")


def fetch(s):
    return None


__pragma__("noskip")


class AlbumList(Component):
    def __init__(self, props):
        super().__init__(props)
        self.state = {"albums": []}

    def render(self, props):
        return __pragma__(
            "js",
            "{}",
            """ (
                <Text>asd</Text>

        ); """,
        )
