import 'package:flutter/material.dart';
import 'package:carousel_slider/carousel_slider.dart';
import 'package:intl/intl.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    
    return Scaffold(
      appBar: AppBar(
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          mainAxisSize: MainAxisSize.min,
          children: [
            // Placeholder für Wappen (kann später durch Asset ersetzt werden)
            Container(
              width: 40,
              height: 40,
              decoration: BoxDecoration(
                color: theme.colorScheme.primaryContainer,
                shape: BoxShape.circle,
              ),
              child: Icon(
                Icons.shield,
                color: theme.colorScheme.onPrimaryContainer,
              ),
            ),
            const SizedBox(width: 12),
            const Text('Poxdorf'),
          ],
        ),
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Nächste Müllabfuhr Widget
            const _NextGarbageCollectionWidget(),
            
            const SizedBox(height: 24),
            
            // Nächste Events Karussell
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0),
              child: Text(
                'Nächste Events',
                style: theme.textTheme.titleLarge?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            
            const SizedBox(height: 16),
            
            const _EventsCarouselWidget(),
            
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }
}

/// Widget für die nächste Müllabfuhr
class _NextGarbageCollectionWidget extends StatelessWidget {
  const _NextGarbageCollectionWidget();

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    
    // Beispieldaten - später aus Backend/API holen
    final nextCollection = DateTime.now().add(const Duration(days: 3));
    final formattedDate = DateFormat('EEEE, dd. MMMM yyyy', 'de_DE').format(nextCollection);
    
    return Container(
      margin: const EdgeInsets.all(16),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: theme.colorScheme.primaryContainer,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.05),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                Icons.delete_outline,
                size: 32,
                color: theme.colorScheme.onPrimaryContainer,
              ),
              const SizedBox(width: 12),
              Text(
                'Nächste Müllabfuhr',
                style: theme.textTheme.titleLarge?.copyWith(
                  color: theme.colorScheme.onPrimaryContainer,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          Text(
            formattedDate,
            style: theme.textTheme.bodyLarge?.copyWith(
              color: theme.colorScheme.onPrimaryContainer,
            ),
          ),
          const SizedBox(height: 8),
          Row(
            children: [
              _GarbageTypeChip(
                label: 'Restmüll',
                color: Colors.grey.shade700,
              ),
              const SizedBox(width: 8),
              _GarbageTypeChip(
                label: 'Gelber Sack',
                color: Colors.amber.shade700,
              ),
            ],
          ),
        ],
      ),
    );
  }
}

/// Chip für Mülltonnen-Typ
class _GarbageTypeChip extends StatelessWidget {
  final String label;
  final Color color;
  
  const _GarbageTypeChip({
    required this.label,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(20),
      ),
      child: Text(
        label,
        style: const TextStyle(
          color: Colors.white,
          fontSize: 12,
          fontWeight: FontWeight.w600,
        ),
      ),
    );
  }
}

/// Karussell für kommende Events
class _EventsCarouselWidget extends StatelessWidget {
  const _EventsCarouselWidget();

  @override
  Widget build(BuildContext context) {
    // Beispiel-Events - später aus Backend/API holen
    final events = [
      _EventData(
        title: 'Gemeinderatssitzung',
        date: DateTime.now().add(const Duration(days: 5)),
        location: 'Rathaus Poxdorf',
        icon: Icons.groups,
      ),
      _EventData(
        title: 'Sommerfest',
        date: DateTime.now().add(const Duration(days: 14)),
        location: 'Dorfplatz',
        icon: Icons.celebration,
      ),
      _EventData(
        title: 'Sperrmüllsammlung',
        date: DateTime.now().add(const Duration(days: 21)),
        location: 'Gemeindegebiet',
        icon: Icons.local_shipping,
      ),
    ];

    return CarouselSlider.builder(
      itemCount: events.length,
      options: CarouselOptions(
        height: 180,
        enlargeCenterPage: true,
        autoPlay: true,
        autoPlayInterval: const Duration(seconds: 5),
        autoPlayAnimationDuration: const Duration(milliseconds: 800),
        viewportFraction: 0.85,
      ),
      itemBuilder: (context, index, realIndex) {
        final event = events[index];
        return _EventCard(event: event);
      },
    );
  }
}

/// Event-Karte für das Karussell
class _EventCard extends StatelessWidget {
  final _EventData event;
  
  const _EventCard({required this.event});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final formattedDate = DateFormat('dd. MMM yyyy', 'de_DE').format(event.date);
    
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.symmetric(horizontal: 5),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            theme.colorScheme.secondaryContainer,
            theme.colorScheme.secondaryContainer.withOpacity(0.7),
          ],
        ),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 8,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Padding(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              event.icon,
              size: 40,
              color: theme.colorScheme.onSecondaryContainer,
            ),
            const SizedBox(height: 12),
            Text(
              event.title,
              style: theme.textTheme.titleLarge?.copyWith(
                color: theme.colorScheme.onSecondaryContainer,
                fontWeight: FontWeight.bold,
              ),
              maxLines: 2,
              overflow: TextOverflow.ellipsis,
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Icon(
                  Icons.calendar_today,
                  size: 16,
                  color: theme.colorScheme.onSecondaryContainer.withOpacity(0.8),
                ),
                const SizedBox(width: 6),
                Text(
                  formattedDate,
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: theme.colorScheme.onSecondaryContainer.withOpacity(0.8),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 4),
            Row(
              children: [
                Icon(
                  Icons.location_on,
                  size: 16,
                  color: theme.colorScheme.onSecondaryContainer.withOpacity(0.8),
                ),
                const SizedBox(width: 6),
                Expanded(
                  child: Text(
                    event.location,
                    style: theme.textTheme.bodyMedium?.copyWith(
                      color: theme.colorScheme.onSecondaryContainer.withOpacity(0.8),
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

/// Datenmodell für Events
class _EventData {
  final String title;
  final DateTime date;
  final String location;
  final IconData icon;

  _EventData({
    required this.title,
    required this.date,
    required this.location,
    required this.icon,
  });
}
