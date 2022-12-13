from js_libs.stubs import require, __pragma__  # __:skip
from js_libs.stubs import handleChange, validate

React = require("react")
useState = require("react").useState
Formik = require("formik")

TextInput = require("react-native").TextInput
Text = require("react-native").Text
View = require("react-native").View
Image = require("react-native").Image
StyleSheet = require("react-native").StyleSheet
TouchableOpacity = require("react-native").TouchableOpacity
ScrollView = require("react-native").ScrollView


def Login(props):
    form_dict = {}
    missing, set_missing = useState([])

    def action(missing):
        print(missing)

    def handelLogin(form):
        props.navigation.navigate("register")

    def handleSubmit(form_dict):
        missing = validate(
            [
                "firstname",
                "lastname",
                "email",
                "password",
                "date",
            ],
            form_dict,
        )
        set_missing(missing)
        action(missing)

    return __pragma__(
        "js",
        "{}",
        """ (		<ScrollView style={styles.container}>
			<Image
				style={styles.Logo}
				source={require("../native/assets/Khusm.png")}
			/>

			<Text
				style={{
					fontSize: 22,
					fontWeight: "bold",
					color: "#000000",
					alignSelf: "center",
					marginBottom: 20,
				}}
			>
				POS
			</Text>

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


styles = {
    "container": {
        "backgroundColor": "white",
    },
    "Logo": {
        "alignSelf": "center",
        "flex": 1,
        "width": 280,
        "height": 200,
        "marginTop": 50,
        "resizeMode": "contain",
    },
    "formik": {
        "paddingStart": 25,
        "paddingEnd": 25,
    },
    "input": {
        "borderWidth": 1,
        "borderColor": "#2caca4",
        "borderRadius": 6,
        "padding": 10,
        "marginTop": 15,
    },
    "erorrText": {
        "fontSize": 12,
    },
    "button": {
        "backgroundColor": "#2caca4",
        "borderRadius": 6,
        "padding": 15,
        "marginTop": 50,
        "zIndex": 1000,
    },
    "buttonText": {
        "textAlign": "center",
        "color": "white",
        "fontSize": 15,
        "fontWeight": "bold",
    },
    "forgetPassword": {
        "marginTop": 2,
        "textDecorationLine": "underline",
    },
    "SignUpParent": {
        "marginTop": 5,
        "flex": 1,
        "display": "flex",
        "flexDirection": "row",
        "justifyContent": "center",
    },
    "SignUpText": {
        "display": "flex",
    },
    "SignUp": {
        "textDecorationLine": "underline",
    },
    "or": {
        "marginTop": 7,
        "fontSize": 16,
        "textAlign": "center",
    },
    "skip": {
        "marginTop": 10,
        "fontSize": 16,
        "textAlign": "center",
    },
}
