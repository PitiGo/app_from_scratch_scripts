import os


def create_theme_files(app_name):
    # Define the directory path
    dir_path = f'./lib/themes'
    # Create the directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)

    # Define the theme files and their content
    theme_files = {
        'dark_theme.dart': '''import 'package:flutter/material.dart';

final darkTheme = ThemeData(
  brightness: Brightness.dark,
  // Add other theme properties here
);
''',
        'light_theme.dart': '''import 'package:flutter/material.dart';

final lightTheme = ThemeData(
  brightness: Brightness.light,
  // Add other theme properties here
);
'''
    }

    # Create the theme files
    for filename, content in theme_files.items():
        file_path = f'{dir_path}/{filename}'
        # Create the file if it doesn't exist
        if not os.path.exists(file_path):
            with open(file_path, 'w') as theme_file:
                theme_file.write(content)
