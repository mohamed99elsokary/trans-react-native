from js_libs.stubs import __pragma__, module  # __:skip
from js_libs.navigation import Stack, NavigationContainer
from native.screens.Auth.login import Login
from native.screens.Auth.sign_up import Register
from js_libs.react import React
from js_libs.react_native import react_native, View


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
