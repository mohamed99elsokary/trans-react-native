from core.stubs import require, __pragma__, module  # __:skip
from components.Header import Header

React = require("react")
View = require("react-native").View


def App():
    return __pragma__(
        "js",
        "{}",
        """ (
        <View style={{ "flex": 1 }}>
            <Header header_text={"Albums"} />
        </View>
    ); """,
    )


module.exports = App
