from warpers.stubs import __pragma__  # __:skip

__pragma__(
    "js",
    "{}",
    """
import {
     NavigationContainer as NC
} from "@react-navigation/native";
import {
     createStackNavigator 
} from "@react-navigation/stack";
export var NavigationContainer = NC;
export var Stack = createStackNavigator ();

    """,
)
__pragma__("skip")
Stack = False
NavigationContainer = False
