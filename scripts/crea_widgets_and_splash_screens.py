import os

def create_widgets_and_splashscreen(app_name):
    # Create the 'widgets' directory if it does not exist
    widgets_path = f'{app_name}/lib/widgets'
    os.makedirs(widgets_path, exist_ok=True)

    # Define the splash screen content
    splash_screen_content = f'''
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../styles.dart';  // Import AppStyles

class SplashScreen extends StatefulWidget {{
  final Widget nextPage;
  final String pathImage;

  const SplashScreen({{Key? key, required this.nextPage,  this.pathImage='assets/zorro.gif'}}) : super(key: key);

  @override
  SplashScreenState createState() => SplashScreenState();
}}

class SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {{
  late final AnimationController _controller;

  @override
  void initState() {{
    super.initState();

    _controller = AnimationController(
      duration: const Duration(seconds: 5),
      vsync: this,
    )..repeat();

    Future.delayed(
      const Duration(seconds: 5),
      () {{
        Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => widget.nextPage),
        );
      }},
    );
  }}

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      backgroundColor: AppStyles.appBarBackground,  // Use AppStyles
      body: Center(
        child: FractionallySizedBox(
          widthFactor: 1.0, // 100% of width
          heightFactor: 0.5, // 50% of height
          child: Stack(
            alignment: Alignment.center,
            children: [
              Image.asset(
                widget.pathImage,
                fit: BoxFit.fill,
              ),
              Text(
                '{app_name}',  // Use app_name here
                style: GoogleFonts.lobster(
                  // use the font you want from Google Fonts
                  fontSize: 52.0,
                  color: Colors.white,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }}

  @override
  void dispose() {{
    _controller.dispose();
    super.dispose();
  }}
}}
    '''

    # Create the splash_screen.dart file in the 'widgets' directory
    with open(f'{widgets_path}/splash_screen.dart', 'w') as f:
        f.write(splash_screen_content)


