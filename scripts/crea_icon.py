import os
import subprocess
import time
from PIL import Image, ImageDraw, ImageFont
import yaml

def create_icon(app_name, text):
    # Define the directory and make sure it exists
    directory = f"{app_name}/assets/icons"
    os.makedirs(directory, exist_ok=True)

    # Create a new image with white background
    img = Image.new('RGB', (500, 500), color = (73, 109, 137))

    d = ImageDraw.Draw(img)
     # Define la fuente y el tamaño
    font = ImageFont.load_default()

    d.text((10,10), text, font=font, fill=(255, 255, 0))

    # Save the image in the defined directory
    img.save(f'{directory}/logo.png')

    # Add the image to the flutter_native_splash in pubspec.yaml
    with open(f'{app_name}/pubspec.yaml', 'r+') as f:
        pubspec = yaml.safe_load(f)

        if 'flutter_native_splash' not in pubspec:
            pubspec['flutter_native_splash'] = {}
        pubspec['flutter_native_splash']['color'] = '#ffffff'
        pubspec['flutter_native_splash']['image'] = 'assets/icons/logo.png'

        # Write the updated pubspec back to file
        f.seek(0)
        yaml.safe_dump(pubspec, f, default_flow_style=False)
        f.truncate()
        
def generate_native_splash(app_directory):
    # Change to the app directory
    os.chdir(app_directory)

    # Print the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Print the output of "dart --version" and "flutter --version"
    print("Dart version:")
    subprocess.run(["dart", "--version"])
    print("Flutter version:")
    subprocess.run(["flutter", "--version"])

    # Execute the command
    #subprocess.run(["dart", "run", "flutter_native_splash:create"], check=True)
    subprocess.run("echo Wating 5 seconds for the files to be created...", shell=True, check=True)
    time.sleep(5)  # Wait for 5 seconds
    subprocess.run("pwd", shell=True, check=True)
    # Specify the full path to the 'dart' executable.
    dart_path = "/Users/dantecollazzi/flutter/bin//dart"

    # Construct the full command as a string.
    command = f"{dart_path} run flutter_native_splash:create"
  

    # Use the full command in the subprocess.run() call.
    subprocess.run(command, shell=True, check=True)

        
 