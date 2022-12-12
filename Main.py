from core.stubs import require, __pragma__, module  # __:skip
from native.screens.Auth.login import Login

React = require("react")
View = require("react-native").View


def App():
    return __pragma__(
        "js",
        "{}",
        """ (
        <View style={{ "flex": 1 }}>
            <Login />
        </View>
    ); """,
    )


module.exports = App
