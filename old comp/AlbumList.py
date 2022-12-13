from js_libs.stubs import require, __pragma__  # __:skip
from js_libs.requests import requests

React = require("react")
ScrollView = require("react-native").ScrollView
Text = require("react-native").Text


def AlbumList(props):
    response = requests(
        {
            "method": "GET",
            "url": "https://grey-labs-staging.bit68.com/en/api/products/",
            "headers": {},
            "data": {},
        }
    )
    return __pragma__(
        "js",
        "{}",
        """ (
                <Text>{response?.results?.[0]?.id}</Text>
        ); """,
    )
