
import shutil
import subprocess
from scripts.add_libraries_to_yaml import add_assets, add_dependencies
from scripts.crea_icon import create_icon, generate_native_splash

from scripts.crea_main import create_flutter_app
from scripts.crea_provider import create_language_provider
from scripts.crea_assets_and_files import create_assets_and_files
from scripts.crea_responsive import create_responsive_layout
from scripts.crea_styles import create_styles_class
from scripts.crea_themes import create_theme_files
from scripts.crea_widgets_and_splash_screens import create_widgets_and_splashscreen
from scripts.crea_user_preferences import create_user_preferences


app_name = 'weekplanner'

create_flutter_app(app_name)
add_dependencies(app_name)
create_assets_and_files(app_name)
create_widgets_and_splashscreen(app_name)
create_styles_class(app_name)
add_assets(app_name)
create_responsive_layout(app_name)
create_language_provider(app_name)
create_user_preferences(app_name)
create_icon(app_name, app_name)

generate_native_splash('./'+app_name)
# Replace 'my_app' with the name of your app
print("Creando themes...")
create_theme_files(app_name)


#Borra carpeta test
shutil.rmtree(f'{app_name}/test', ignore_errors=True)

