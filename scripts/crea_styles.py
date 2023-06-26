import os

def create_styles_class(app_name):
    # Define the styles class content
    styles_class_content = '''
import 'package:flutter/material.dart';

class AppStyles {
  // Primary color for the app, dark indigo
  static const Color appBarBackground = Color(0xFF0f0b1f);
  static const Color iconsColor = Color(0xFF814a94);

  static const Color colorIconoCorazonTabla = Color(0xFFaf36a6);
  static const Color colorIconoCompatibleTabla = Color(0xFF0fd947);
  static const Color colorIconoNeutralTabla = Color(0xFF3f75df);
  static const Color colorIconoProhibidoTabla = Color(0xFFb41834);

  static const Color colorMarcoTabla = Color(0xFFb9a6e7);

  // Accent color for the app, deep purple
  static const Color accent = Colors.deepPurple;

  // Color for secondary buttons, darker shade of deep purple
  static final Color button2 = Colors.deepPurple.shade600;

  // Color for buttons in general
  static const Color button = Colors.deepPurple;

  // Color for text in general
  static const Color text = Colors.black87;

  // Additional colors for more interesting design
  static Color background = Colors.deepPurple.withOpacity(0.80);
  static const Color textPrimary = Colors.white;
  static const Color textSecondary = Colors.black87;
  static final Color error = Colors.red.shade700;
  static final Color success = Colors.green.shade600;

  static const Color buttonDisabled = Color(0xFFCCCCCC);
  static const Color normalButton = Color(0xFF2e264f);
  static const Color corlorItemDropDownDesplegado = Color(0xFF2d2250);
  static const Color corlorBackgroundBigButton = Color(0xFF0f0b1f);
  static const Color corlorBackgroundSmallButton = Color(0xFF2d214f);

  static const Color corlorBotonActivado = Color(0xFFd0bcff);

  static const Color corlorTextNormalButton = Color(0xFFbca9e9);
}
    '''

    # Create the styles.dart file in the 'lib' directory
    with open(f'{app_name}/lib/styles.dart', 'w') as f:
        f.write(styles_class_content)


