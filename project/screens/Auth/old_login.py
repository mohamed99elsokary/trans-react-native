from js_libs.stubs import require, __pragma__  # __:skip
from js_libs.stubs import handleChange, validate
from js_libs.react import React, useState
from js_libs.requests import requests
from project.base_data import BASE_URL
from js_libs.react_native import (
    react_native,
    View,
    TextInput,
    Text,
    Image,
    StyleSheet,
    TouchableOpacity,
    ScrollView,
)
from project.styles.login import styles

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

    def Submit(form_dict):
        missing = validate(["phone", "password"], form_dict)
        if len(missing) == 0 and len(form_dict) != 0:
            token = login(form_dict)
            # print(token["data"]["token"]["access_token"])
        return set_missing(missing)

        # props.navigation.navigate("register")

    # JSX
    def text_handler():
        persons = [
            {"id": 1, "name": "POS", "show": False},
            {"id": 2, "name": "Khusm", "show": True},
        ]
        result = []
        keyyy = 0
        for person in persons:
            keyyy += 1
            person_name = person["name"]
            if person["show"] == False:
                style = styles["mahmoud"]

            if person["show"] == True:
                style = styles["sokary"]

            result.append(
                __pragma__(
                    "js",
                    "{}",
                    """(
                    <Text
                        key = {keyyy}
                        style={style}
                    >
                        {person_name}
                    </Text>
                    )""",
                )
            )
        return result

    return __pragma__(
        "js",
        "{}",
        """ (		<ScrollView style={styles.container}>
        <Image
				style={styles.Logo}
				source={require("../project/assets/Khusm.png")}
			/>
			 { text_handler() }
			<View style={styles.formik}>
				<Text style={{ fontSize: 14, fontWeight: "bold", color: "#2caca4" }}>
					Phone
				</Text>
				<TextInput
					keyboardType="numeric"
					style={styles.input}
					placeholder="Phone"
					placeholderTextColor="#2caca4"
                    onChangeText={(x) => handleChange(form_dict,x,"phone")}

				/>
                    {missing.includes("phone") && <Text>This field is required</Text>}


				<Text
					style={{
						fontSize: 14,
						fontWeight: "bold",
						color: "#2caca4",
						marginTop: 30,
					}}
				>
					Password
				</Text>
				<TextInput
					style={styles.input}
					placeholder="Password"
					secureTextEntry={true}
					placeholderTextColor="#2caca4"
                    onChangeText={(x) => handleChange(form_dict,x,"password")}

				/>
                {missing.includes("password") && <Text>This field is required</Text>}
                
				{/* Login  button */}

				<TouchableOpacity onPress={()=>Submit(form_dict)} style={styles.button}>
					<Text style={styles.buttonText}> LOGIN </Text>
				</TouchableOpacity>
			</View>
		</ScrollView>)""",
    )
