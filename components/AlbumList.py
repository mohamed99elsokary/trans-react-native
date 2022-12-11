from core.stubs import require, console, __pragma__, iii  # __:skip
from components.AlbumDetail import AlbumDetail
from components.core_functions import request

React = require("react")
ScrollView = require("react-native").ScrollView
Text = require("react-native").Text
__pragma__("skip")
__pragma__("noskip")


def AlbumList(props):
    request_data = {
        "method": "GET",
        "url": "https://grey-labs-staging.bit68.com/en/api/products/",
        "headers": {},
        "data": {},
    }
    data, setData = React.useState()

    def parse(request):
        setData(request.data)
        print("_______________")

    def hamda():
        request(request_data).then(parse)

    __pragma__(
        "js",
        "{}",
        """ (
    React.useEffect(() => {
		hamda()
	}, [])
            ); """,
    )
    return __pragma__(
        "js",
        "{}",
        """ (
                <Text>{data?.count}</Text>
        ); """,
    )
