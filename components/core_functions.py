__pragma__("skip")
from core.stubs import require, __pragma__

__pragma__("noskip")

React = require("react")
axios = require("axios")


def requests(values):
    response, setData = React.useState()
    request_body = values

    def request():

        __pragma__(
            "js",
            "{}",
            """ 
            return axios.default.request(request_body);
            """,
        )

    def parse(request):
        setData(request.data)
        print("_______________")

    __pragma__(
        "js",
        "{}",
        """ (
    React.useEffect(() => {
		request(request_body).then(parse)
	}, [])
            ); """,
    )
    return response
