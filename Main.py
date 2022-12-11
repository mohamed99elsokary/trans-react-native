from core.stubs import require, __pragma__, module  # __:skip
from native.components.Header import Header
from native.screens.Auth.login import Auth

React = require("react")
View = require("react-native").View


def App():
    return __pragma__(
        "js",
        "{}",
        """ (
        <View style={{ "flex": 1 }}>
            <Header header_text={"Albums"} />
            <Auth header_text={"Albums"} />
        </View>
    ); """,
    )


module.exports = App
