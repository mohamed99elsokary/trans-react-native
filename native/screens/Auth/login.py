from js_libs.stubs import require, __pragma__  # __:skip
from js_libs.stubs import handleChange, validate
from js_libs.react import React, useState
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
from native.styles.login import styles

Formik = require("formik")


def Login(props):
    def handelLogin(form):
        props.navigation.navigate("register")

    def image():
        persons = [
            {"id": 1, "name": "POS", "show": False},
            # {"id": 2, "name": "Khusm", "show": True},
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
				source={require("../native/assets/Khusm.png")}
			/>
			 { image() }
			<View style={styles.formik}>
				<Text style={{ fontSize: 14, fontWeight: "bold", color: "#2caca4" }}>
					Phone
				</Text>
				<TextInput
					keyboardType="numeric"
					style={styles.input}
					// value={values.phone}
					// onChangeText={handleChange("phone")}
					// onBlur={() => setFieldTouched("phone")}
					placeholder="Phone"
					placeholderTextColor="#2caca4"
				/>
				{/* {touched.phone && errors.phone && (
					<Text style={styles.erorrText}>{errors.phone}</Text>
				)} */}

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
					// value={values.password}
					// onChangeText={handleChange("password")}
					// onBlur={() => setFieldTouched("password")}
					placeholder="Password"
					secureTextEntry={true}
					placeholderTextColor="#2caca4"
				/>
				{/* Login  button */}

				<TouchableOpacity onPress={handelLogin} style={styles.button}>
					<Text style={styles.buttonText}> LOGIN </Text>
				</TouchableOpacity>
			</View>
		</ScrollView>)""",
    )
