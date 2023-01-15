from warpers.stubs import __pragma__, module  # __:skip
from warpers.navigation import Stack, NavigationContainer
from project.screens.Auth.login import Login
from project.screens.Auth.sign_up import Register
from warpers.react import React
from warpers.react_native import react_native, View


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
