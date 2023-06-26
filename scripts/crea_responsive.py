import os
import textwrap

def create_responsive_layout(app_name):
    create_responsive_layout_file(app_name)
    create_mobile_screen(app_name)
    create_tablet_screen(app_name)
    create_desktop_screen(app_name)

def create_responsive_layout_file(app_name):
    # Create the directories
    base_path = f"{app_name}/lib/responsive"
    
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
        os.makedirs(os.path.join(base_path, "mobile"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "tablet"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "desktop"), exist_ok=True)

        # Define the Flutter code
        flutter_code = textwrap.dedent("""\
        import 'package:flutter/material.dart';

        class ResponsiveLayout extends StatelessWidget {
            const ResponsiveLayout(
                {Key? key,
                required this.mobileScaffold,
                required this.tabletScaffold,
                required this.desktopScaffold})
                : super(key: key);

            final Widget mobileScaffold;
            final Widget tabletScaffold;
            final Widget desktopScaffold;

            @override
            Widget build(BuildContext context) {
                return LayoutBuilder(
                builder: (context, constraints) {
                    if (constraints.maxWidth < 500) {
                    return mobileScaffold;
                    } else if (constraints.maxWidth < 1100) {
                    return tabletScaffold;
                    } else {
                    return desktopScaffold;
                    }
                },
                );
            }
        }
        """)

        # Write the Flutter code to a file
        with open(os.path.join(base_path, "responsive_layout.dart"), "w") as f:
            f.write(flutter_code)
    else:
        print("Responsive layout already exists.")

def create_mobile_screen(app_name):
    # Path to the mobile directory
    mobile_path = f"{app_name}/lib/responsive/mobile"
    file_path = os.path.join(mobile_path, "mobile_screen.dart")

    # Check if the directory exists
    if not os.path.exists(mobile_path):
        os.makedirs(mobile_path, exist_ok=True)
        
    # Check if the file exists
    if not os.path.isfile(file_path):
        # Define the Flutter code for a basic screen
        flutter_code = textwrap.dedent("""\
        import 'package:flutter/material.dart';

        class MobileScreen extends StatelessWidget {
            const MobileScreen({Key? key}) : super(key: key);

            @override
            Widget build(BuildContext context) {
                return Scaffold(
                appBar: AppBar(
                    title: const Text('Mobile Screen'),
                ),
                body: Center(
                    child: Text(
                    'This is the Mobile Screen',
                    style: Theme.of(context).textTheme.headlineMedium,
                    ),
                ),
                );
            }
        }
        """)

        # Write the Flutter code to a file
        with open(file_path, "w") as f:
            f.write(flutter_code)
    else:
        print("Mobile screen file already exists.")


def create_tablet_screen(app_name):
    # Path to the tablet directory
    tablet_path = f"{app_name}/lib/responsive/tablet"
    file_path = os.path.join(tablet_path, "tablet_screen.dart")

    # Check if the directory exists
    if not os.path.exists(tablet_path):
        os.makedirs(tablet_path, exist_ok=True)

    # Check if the file exists
    if not os.path.isfile(file_path):
        # Define the Flutter code for a basic screen
        flutter_code = textwrap.dedent("""\
        import 'package:flutter/material.dart';

        class TabletScreen extends StatelessWidget {
            const TabletScreen({Key? key}) : super(key: key);

            @override
            Widget build(BuildContext context) {
                return Scaffold(
                appBar: AppBar(
                    title: const Text('Tablet Screen'),
                ),
                body: Center(
                    child: Text(
                    'This is the Tablet Screen',
                    style: Theme.of(context).textTheme.headlineMedium,
                    ),
                ),
                );
            }
        }
        """)

        # Write the Flutter code to a file
        with open(file_path, "w") as f:
            f.write(flutter_code)
    else:
        print("Tablet screen file already exists.")

def create_desktop_screen(app_name):
    # Path to the desktop directory
    desktop_path = f"{app_name}/lib/responsive/desktop"
    file_path = os.path.join(desktop_path, "desktop_screen.dart")

    # Check if the directory exists
    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path, exist_ok=True)

    # Check if the file exists
    if not os.path.isfile(file_path):
        # Define the Flutter code for a basic screen
        flutter_code = textwrap.dedent("""\
        import 'package:flutter/material.dart';

        class DesktopScreen extends StatelessWidget {
            const DesktopScreen({Key? key}) : super(key: key);

            @override
            Widget build(BuildContext context) {
                return Scaffold(
                appBar: AppBar(
                    title: const Text('Desktop Screen'),
                ),
                body: Center(
                    child: Text(
                    'This is the Desktop Screen',
                    style: Theme.of(context).textTheme.headlineMedium,
                    ),
                ),
                );
            }
        }
        """)

        # Write the Flutter code to a file
        with open(file_path, "w") as f:
            f.write(flutter_code)
    else:
        print("Desktop screen file already exists.")
        

