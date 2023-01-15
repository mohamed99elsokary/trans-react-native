from warpers.stubs import require, __pragma__  # __:skip
from warpers.react_native import (
    Text,
    react_native,
    View,
    TextInput,
    Image,
    StyleSheet,
    TouchableOpacity,
    ScrollView,
)
from warpers.stubs import handleChange, validate


def text(style: dict = {}, string_text: str = "Text"):
    return __pragma__(
        "js",
        "{}",
        """(
    <Text style={style}>
      {string_text}
    </Text>
  )""",
    )


def for_each(list: list, other_component: function):
    return __pragma__(
        "js",
        "{}",
        """list.map(element => {
		return (
			<View key={element.key}>
				{other_component(element)}
			</View>
		);
	});
 
  """,
    )


def cond(condition: bool, first_component: function, second_component: function):
    if condition:
        return first_component
    else:
        return second_component


def scroll_view(components: list):
    return __pragma__(
        "js",
        "{}",
        """(
        <ScrollView >
        {components}
        </ScrollView>
  )""",
    )


def image(style: dict, source: str):
    return __pragma__(
        "js",
        "{}",
        """(
        <Image
 			style={style}
 			source={require("../project/assets/Khusm.png")}
 		/>
  )""",
    )


def view(style: dict, components: list):
    return __pragma__(
        "js",
        "{}",
        """(
		<View style={style}>
        {components}
        </View>
  )""",
    )


def text_input(
    style: dict,
    form_dict: dict,
    placeholder: str,
    secureTextEntry: bool,
    placeholderTextColor: str,
    keyboardType: str = "default",
):

    return __pragma__(
        "js",
        "{}",
        """(
				<TextInput
					keyboardType={keyboardType}
					style={style}
					placeholder={placeholder}
				    secureTextEntry={secureTextEntry}
					placeholderTextColor={placeholderTextColor}
                    onChangeText={(x) => handleChange(form_dict,x,placeholder)}

				/>
    
  )""",
    )


def touchable_opacity(style: dict, on_press, components: list):
    return __pragma__(
        "js",
        "{}",
        """(
		<TouchableOpacity onPress={on_press} style={{
        "backgroundColor": "#2caca4",
        "borderRadius": 6,
        "padding": 15,
        "marginTop": 50,
        "zIndex": 1000,
    }}>
        {components}
        </TouchableOpacity>
  )""",
    )
