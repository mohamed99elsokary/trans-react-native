from js_libs.stubs import require, __pragma__  # __:skip
from js_libs.stubs import handleChange, validate
from js_libs.react import React, useState
from js_libs.requests import requests
from project.base_data import BASE_URL
from project.styles.login import styles
from js_libs.jsx import text, scroll_view, image, view, text_input, touchable_opacity

Formik = require("formik")


def Login(props):
    missing, set_missing = useState([])
    form_dict, set_form_dict = useState({})
    response, set_response = useState({})

    def login(form_dict):
        requests(
            set_response,
            {
                "method": "POST",
                "url": BASE_URL + "/users/login/",
                "headers": {},
                "data": form_dict,
            },
        )
        if response["data"]:
            print((response["data"]["token"]["access_token"]))
        return response

    def Submit():
        missing = validate(["phone", "password"], form_dict)
        if len(missing) == 0 and len(form_dict) != 0:
            token = login(form_dict)
        return set_missing(missing)

    # JSX
    def text_handler():
        persons = [
            {"id": 1, "name": "aaa", "show": True},
            {"id": 2, "name": "Khusm", "show": True},
            {"id": 3, "name": "Test", "show": True},
        ]
        return [text(styles["sokary"], person["name"]) for person in persons]

    return scroll_view(
        [
            image(styles["Logo"], "asd"),
            text_handler(),
            view(
                styles["formik"],
                [
                    text(
                        styles["text"],
                        "Phone",
                    ),
                    text_input(
                        styles["input"], form_dict, "Phone", False, "#2caca4", "numeric"
                    ),
                    text(
                        styles["text"],
                        "Password",
                    ),
                    text_input(
                        styles["input"],
                        form_dict,
                        "Password",
                        True,
                        "#2caca4",
                    ),
                    touchable_opacity(
                        styles["button"],
                        Submit,
                        [text(styles["buttonText"], "Login")],
                    ),
                ],
            ),
        ],
    )
