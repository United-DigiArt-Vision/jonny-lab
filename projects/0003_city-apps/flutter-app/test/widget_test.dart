import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:poxdorf_city_app/main.dart';

void main() {
  testWidgets('App should load with bottom navigation', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const PoxdorfCityApp());

    // Verify that the app title is present
    expect(find.text('Poxdorf'), findsOneWidget);

    // Verify that all 5 navigation items are present
    expect(find.text('Home'), findsOneWidget);
    expect(find.text('Kalender'), findsOneWidget);
    expect(find.text('Scanner'), findsOneWidget);
    expect(find.text('News'), findsOneWidget);
    expect(find.text('Mehr'), findsOneWidget);
  });

  testWidgets('Navigation should switch between screens', (WidgetTester tester) async {
    await tester.pumpWidget(const PoxdorfCityApp());

    // Tap on the Kalender tab
    await tester.tap(find.text('Kalender'));
    await tester.pumpAndSettle();

    // Verify we're on the Kalender screen
    expect(find.text('Kalender'), findsNWidgets(2)); // One in AppBar, one in BottomNav

    // Tap on the News tab
    await tester.tap(find.text('News'));
    await tester.pumpAndSettle();

    // Verify we're on the News screen
    expect(find.text('News'), findsNWidgets(2));
  });

  testWidgets('Home screen should show garbage collection widget', (WidgetTester tester) async {
    await tester.pumpWidget(const PoxdorfCityApp());

    // Check if garbage collection widget is visible
    expect(find.text('Nächste Müllabfuhr'), findsOneWidget);
    expect(find.byIcon(Icons.delete_outline), findsOneWidget);
  });

  testWidgets('Home screen should show events carousel', (WidgetTester tester) async {
    await tester.pumpWidget(const PoxdorfCityApp());

    // Check if events section is visible
    expect(find.text('Nächste Events'), findsOneWidget);
    
    // Wait for carousel to load
    await tester.pumpAndSettle();
    
    // Verify at least one event is visible
    expect(find.text('Gemeinderatssitzung'), findsOneWidget);
  });
}
