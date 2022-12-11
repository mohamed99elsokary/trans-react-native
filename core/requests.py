from core.stubs import require, __pragma__  # __:skip

React = require("react")
axios = require("axios")


def requests(request_body):
    __pragma__(
        "js",
        {},
        """
const [response, setData] = React.useState()
React.useEffect(() => {
    axios.default.request(request_body).then(setData)
}, [])
return response?.data
    """,
    )
