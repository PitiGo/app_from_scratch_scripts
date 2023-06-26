import os
import textwrap

def create_user_preferences(app_name):
    # Path to the preferences directory
    preferences_path = f"{app_name}/lib/preferences"

    # Check if the directory exists
    if not os.path.exists(preferences_path):
        os.makedirs(preferences_path, exist_ok=True)

    # Check if the file exists
    if not os.path.isfile(os.path.join(preferences_path, "user_preferences.dart")):

        # Define the Flutter code for the user preferences
        flutter_code = textwrap.dedent("""\
        import 'package:shared_preferences/shared_preferences.dart';

        class UserPreferences {
            static final UserPreferences _instance = UserPreferences._internal();

            factory UserPreferences() {
                return _instance;
            }

            UserPreferences._internal();

            SharedPreferences? _prefs;

            initData() async {
                _prefs = await SharedPreferences.getInstance();
            }

            // GET y SET del nombre
            String get name {
                return _prefs?.getString('name') ?? '0';
            }

            set name(String value) {
                _prefs?.setString('name', value);
            }

            void clear() {
                _prefs?.clear();
            }

            // GET y SET del idioma
            String get language {
                return _prefs?.getString('language') ?? 'en';
            }

            set language(String value) {
                _prefs?.setString('language', value);
            }
        }
        """)

        # Write the Flutter code to a file
        with open(os.path.join(preferences_path, "user_preferences.dart"), "w") as f:
            f.write(flutter_code)
    else:
        print("File user_preferences.dart already exists.")

