import os
import subprocess
import textwrap

def create_flutter_app(app_name):
    # Usa subprocess para ejecutar el comando flutter create
    subprocess.run(["flutter", "create", app_name], check=True)

    # Ahora genera el archivo main.dart
    with open(f'{app_name}/lib/main.dart', 'w') as f:
        f.write(f"""
import 'package:flutter/material.dart';
import 'package:easy_localization/easy_localization.dart';
import 'package:{app_name}/responsive/responsive_layout.dart';
import 'package:{app_name}/responsive/mobile/mobile_screen.dart';
import 'package:{app_name}/responsive/tablet/tablet_screen.dart';
import 'package:{app_name}/responsive/desktop/desktop_screen.dart';
import 'package:provider/provider.dart';
import 'package:{app_name}/provider/language_provider.dart';


void main() async {{
  WidgetsFlutterBinding.ensureInitialized();
  await EasyLocalization.ensureInitialized();
  runApp(EasyLocalization(
     supportedLocales: const [
          Locale('en', 'EN'),
          Locale('es', 'ES'),
          Locale('fr', 'FR'),
          Locale('pt', 'PT')
        ],
    path: 'assets/translations', // <-- cambiar a la ruta de tus archivos de traducción
    fallbackLocale: const Locale('en', 'EN'),
    child: const MyApp(),
  ));
}}

class MyApp extends StatelessWidget {{
  const MyApp({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (context) => LanguageProvider()),
   
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        localizationsDelegates: context.localizationDelegates,
        supportedLocales: context.supportedLocales,
        locale: context.locale,
        home: const ResponsiveLayout(
          mobileScaffold: MobileScreen(),
          tabletScaffold: TabletScreen(),
          desktopScaffold: DesktopScreen(),
        ),
      ),
    );
  }}
}}
        """)

