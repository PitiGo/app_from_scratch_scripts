import requests
import yaml
import os

def add_dependencies(app_name):
    # Define las librerías que deseas agregar
    libraries = ['provider', 'easy_localization', 'google_fonts','shared_preferences','flutter_native_splash']

    # Abre el archivo pubspec.yaml y agrega las dependencias
    with open(f'{app_name}/pubspec.yaml', 'r+') as f:
        pubspec = yaml.safe_load(f)

        # Agrega la dependencia de cada librería a la lista de dependencias
        if 'dependencies' not in pubspec:
            pubspec['dependencies'] = {}

        for library in libraries:
            # Obtiene la última versión de la librería
            response = requests.get(f'https://pub.dev/api/packages/{library}')
            library_version = response.json()['latest']['version']

            pubspec['dependencies'][library] = '^' + library_version

        # Agrega flutter_localizations a las dependencias
        pubspec['dependencies']['flutter_localizations'] = {'sdk': 'flutter'}

        # Escribe el archivo modificado de vuelta al sistema de archivos
        f.seek(0)
        yaml.safe_dump(pubspec, f, default_flow_style=False)
        f.truncate()


def add_assets(app_name):
    # Abre el archivo pubspec.yaml y agrega los assets
    with open(f'{app_name}/pubspec.yaml', 'r+') as f:
        pubspec = yaml.safe_load(f)

        # Agrega los assets a pubspec.yaml
        if 'flutter' not in pubspec:
            pubspec['flutter'] = {}
        if 'assets' not in pubspec['flutter']:
            pubspec['flutter']['assets'] = []
        
        # Check if asset is already in the list before adding
        if 'assets/translations/' not in pubspec['flutter']['assets']:
            pubspec['flutter']['assets'].append('assets/translations/')

        # Escribe el archivo modificado de vuelta al sistema de archivos
        f.seek(0)
        yaml.safe_dump(pubspec, f, default_flow_style=False)
        f.truncate()
