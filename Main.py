from core.stubs import require, __pragma__, module  # __:skip
from core.navigation import Stack, NavigationContainer
from native.screens.Auth.login import Login
from native.screens.Auth.sign_up import Register

React = require("react")
View = require("react-native").View


def App():
    return __pragma__(
        "js",
        "{}",
        """ (
		<View style={{ flex: 1 }}>
			<NavigationContainer>
				<Stack.Navigator initialRouteName="login">
					<Stack.Screen
						options={{ headerShown: false }}
						component={Login}
						name="login"
					/>
                    <Stack.Screen
						options={{ headerShown: false }}
						component={Register}
						name="register"
					/>
				</Stack.Navigator>
			</NavigationContainer>
		</View>
    ); """,
    )


module.exports = App
