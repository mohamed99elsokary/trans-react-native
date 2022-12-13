from core.stubs import require, __pragma__  # __:skip
from core.stubs import handleChange, validate

React = require("react")
useState = require("react").useState

Text = require("react-native").Text
View = require("react-native").View
TextInput = require("react-native").TextInput
TouchableOpacity = require("react-native").TouchableOpacity


def Register(props):
    form_dict = {}
    missing, set_missing = useState([])

    def action(missing):
        print(missing)

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
        """ (
<View style={styles.viewStyle}>
<View style={styles.nameViewStyle}>

<TextInput
placeholder="First Name"
style={styles.nameStyle}
onChangeText={(x) => handleChange( form_dict,x ,"firstname")}
/>
{missing.includes("firstname") && <Text>This field is required</Text>}

<TextInput
placeholder="Last Name"
style={styles.nameStyle}
onChangeText={(x) => handleChange( form_dict,x ,"lastname")}
/>
</View>

<TextInput
placeholder="Email"
keyboardType="email-address"
style={styles.inputStyles}
onChangeText={(x) => handleChange( form_dict,x ,"email")}
/>

<TextInput
placeholder="Password"
secureTextEntry={true}
style={styles.inputStyles}
onChangeText={(x) => handleChange( form_dict,x ,"password")}

/>

<TextInput
placeholder="Date of birth"
style={styles.inputStyles}
onChangeText={(x) => handleChange( form_dict,x ,"date")}

/>

<TouchableOpacity
style={styles.buttonstyle}
onPress={()=>handleSubmit(form_dict)}
>
<Text
style={styles.buttonTextStyle}
>
Sign Up
</Text>
</TouchableOpacity>
</View>

    ); """,
    )


styles = {
    "homeStyle": {
        "height": "auto",
        "flex": 1,
    },
    "textStyle": {
        "color": "white",
    },
    "buttonTextStyle": {
        "color": "white",
        "alignSelf": "center",
        "fontSize": 25,
    },
    "signUpStyle": {
        "flexDirection": "row",
        "justifyContent": "center",
        "alignItems": "center",
        "marginBottom": 100,
        "marginTop": 15,
    },
    "textSignStyle": {
        "color": "#875C5C",
    },
    "inputStyles": {
        "backgroundColor": "#FFF",
        "width": "85%",
        "padding": 20,
        "marginVertical": 7,
        "borderRadius": 10,
        "color": "#8D8D8D",
    },
    "viewStyle": {
        "alignItems": "center",
        "marginTop": "20%",
    },
    "nameViewStyle": {
        "width": "85%",
        "flexDirection": "row",
        "justifyContent": "space-between",
    },
    "nameStyle": {
        "width": "48%",
        "backgroundColor": "#FFF",
        "padding": 20,
        "marginVertical": 7,
        "borderRadius": 10,
        "color": "#8D8D8D",
    },
    "buttonstyle": {
        "color": "white",
        "alignSelf": "center",
        "justifyContent": "center",
        "width": "85%",
        "height": 50,
        "backgroundColor": "#ED6623",
        "borderRadius": 10,
        "marginTop": 50,
    },
    "pickerSelect": {
        "borderColor": "red",
        "borderWidth": 2,
    },
}
