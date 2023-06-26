import os
import textwrap

def create_language_provider(app_name):
    # Path to the provider directory
    provider_path = f"{app_name}/lib/provider"

    # Check if the directory exists
    if not os.path.exists(provider_path):
        os.makedirs(provider_path, exist_ok=True)

    # Check if the file exists
    if not os.path.isfile(os.path.join(provider_path, "language_provider.dart")):

        # Define the Flutter code for the language provider
        flutter_code = textwrap.dedent("""\
        import 'package:flutter/material.dart';
        import 'package:easy_localization/easy_localization.dart';
        import '../preferences/user_preferences.dart';

        class LanguageProvider extends ChangeNotifier {
            void changeLanguage(BuildContext context, Locale locale) {
                EasyLocalization.of(context)!.setLocale(locale);

                // Guarda el idioma en las preferencias cuando se cambie
                final prefs = UserPreferences();
                prefs.language = locale.languageCode;

                notifyListeners();
            }
        }
        """)

        # Write the Flutter code to a file
        with open(os.path.join(provider_path, "language_provider.dart"), "w") as f:
            f.write(flutter_code)
    else:
        print("File language_provider.dart already exists.")


