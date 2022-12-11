from core.stubs import require, __pragma__  # __:skip
from components.core_functions import requests

React = require("react")
ScrollView = require("react-native").ScrollView
Text = require("react-native").Text


def AlbumList(props):
    request_data = {
        "method": "GET",
        "url": "https://grey-labs-staging.bit68.com/en/api/products/",
        "headers": {},
        "data": {},
    }
    data = requests(request_data)

    return __pragma__(
        "js",
        "{}",
        """ (
                <Text>{data?.count}</Text>
        ); """,
    )
