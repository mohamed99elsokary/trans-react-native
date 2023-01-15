from warpers.stubs import require, __pragma__  # __:skip

axios = require("axios")


def requests(setter, request_body):
    __pragma__(
        "js",
        {},
        """
    return axios.default.request(request_body).then(setter)
    """,
    )
