from core.stubs import require, console, __pragma__, iii  # __:skip

axios = require("axios")


def request(values):
    request_body = {
        "method": values["method"],
        "url": values["url"],
        "headers": values["headers"],
        "data": values["data"],
    }

    __pragma__(
        "js",
        "{}",
        """ 
        return axios.default.request(request_body);
        """,
    )
