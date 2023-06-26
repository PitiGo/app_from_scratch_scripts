import os
import json
import plistlib

def create_assets_and_files(app_name):
    # Create the 'assets' folder if it doesn't exist
    assets_path = f'{app_name}/assets/translations'
    os.makedirs(assets_path, exist_ok=True)

    # Define the json files and content
    json_files = {
        'es-ES.json': {"appName": app_name, "hello_world": "Hola", "mainMessage": "Bienvenido a mi aplicación"},
        'en-EN.json': {"appName": app_name, "hello_world": "Hello", "mainMessage": "Welcome to my app"},
        'fr-FR.json': {"appName": app_name, "hello_world": "Bonjour", "mainMessage": "Bienvenue sur mon application"},
        'pt-PT.json': {"appName": app_name, "hello_world": "Olá", "mainMessage": "Bem-vindo ao meu aplicativo"},
    }

    # Create the json files in the 'assets' folder
    for filename, content in json_files.items():
        file_path = f'{assets_path}/{filename}'
        
        if os.path.exists(file_path):
            # If the file already exists, load the existing content
            with open(file_path, 'r') as json_file:
                existing_content = json.load(json_file)
            # Merge the existing content with the new content
            merged_content = {**existing_content, **content}
        else:
            # If the file doesn't exist, use the new content
            merged_content = content

        # Write the content to the file
        with open(file_path, 'w') as json_file:
            json.dump(merged_content, json_file, ensure_ascii=False, indent=4)

    # Modify the Info.plist file for iOS
    info_plist_path = f'{app_name}/ios/Runner/Info.plist'
    with open(info_plist_path, 'rb') as plist_file:
        plist_content = plistlib.load(plist_file)
    
    # Add the supported locales
    plist_content['CFBundleLocalizations'] = ['en', 'es', 'fr', 'pt']

    # Write the modified content back to the Info.plist file
    with open(info_plist_path, 'wb') as plist_file:
        plistlib.dump(plist_content, plist_file)
