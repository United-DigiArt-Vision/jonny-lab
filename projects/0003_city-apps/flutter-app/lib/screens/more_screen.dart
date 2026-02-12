import 'package:flutter/material.dart';

class MoreScreen extends StatelessWidget {
  const MoreScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    
    return Scaffold(
      appBar: AppBar(
        title: const Text('Mehr'),
      ),
      body: ListView(
        children: [
          // Gemeinde-Info Header
          Container(
            padding: const EdgeInsets.all(24),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  theme.colorScheme.primaryContainer,
                  theme.colorScheme.secondaryContainer,
                ],
              ),
            ),
            child: Column(
              children: [
                Container(
                  width: 80,
                  height: 80,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.1),
                        blurRadius: 10,
                        offset: const Offset(0, 4),
                      ),
                    ],
                  ),
                  child: Icon(
                    Icons.shield,
                    size: 50,
                    color: theme.colorScheme.primary,
                  ),
                ),
                const SizedBox(height: 16),
                Text(
                  'Gemeinde Poxdorf',
                  style: theme.textTheme.headlineSmall?.copyWith(
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'Ihre digitale Gemeinde-App',
                  style: theme.textTheme.bodyMedium?.copyWith(
                    color: theme.colorScheme.onSurface.withOpacity(0.7),
                  ),
                ),
              ],
            ),
          ),
          
          const SizedBox(height: 8),
          
          // Menü-Kategorien
          _MenuSection(
            title: 'Informationen',
            items: [
              _MenuItem(
                icon: Icons.info_outline,
                title: 'Über Poxdorf',
                subtitle: 'Geschichte, Zahlen & Fakten',
              ),
              _MenuItem(
                icon: Icons.location_city,
                title: 'Rathaus & Verwaltung',
                subtitle: 'Öffnungszeiten, Kontakt',
              ),
              _MenuItem(
                icon: Icons.groups,
                title: 'Gemeinderat',
                subtitle: 'Mitglieder & Sitzungen',
              ),
            ],
          ),
          
          _MenuSection(
            title: 'Services',
            items: [
              _MenuItem(
                icon: Icons.description,
                title: 'Formulare & Anträge',
                subtitle: 'Downloads & Online-Services',
              ),
              _MenuItem(
                icon: Icons.phone,
                title: 'Notrufnummern',
                subtitle: 'Wichtige Kontakte',
              ),
              _MenuItem(
                icon: Icons.local_parking,
                title: 'Parkplätze & Verkehr',
                subtitle: 'Parkmöglichkeiten',
              ),
            ],
          ),
          
          _MenuSection(
            title: 'App',
            items: [
              _MenuItem(
                icon: Icons.notifications_outlined,
                title: 'Benachrichtigungen',
                subtitle: 'Push-Mitteilungen verwalten',
              ),
              _MenuItem(
                icon: Icons.settings,
                title: 'Einstellungen',
                subtitle: 'App-Konfiguration',
              ),
              _MenuItem(
                icon: Icons.help_outline,
                title: 'Hilfe & Feedback',
                subtitle: 'Support kontaktieren',
              ),
              _MenuItem(
                icon: Icons.info_outline,
                title: 'Über die App',
                subtitle: 'Version 1.0.0',
              ),
            ],
          ),
          
          const SizedBox(height: 16),
          
          // Footer
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text(
              '© 2026 United DigiArt Vision\nGemeinde Poxdorf',
              textAlign: TextAlign.center,
              style: theme.textTheme.bodySmall?.copyWith(
                color: theme.colorScheme.onSurface.withOpacity(0.5),
              ),
            ),
          ),
          
          const SizedBox(height: 32),
        ],
      ),
    );
  }
}

class _MenuSection extends StatelessWidget {
  final String title;
  final List<_MenuItem> items;
  
  const _MenuSection({
    required this.title,
    required this.items,
  });

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
          child: Text(
            title,
            style: theme.textTheme.titleSmall?.copyWith(
              color: theme.colorScheme.primary,
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
        ...items.map((item) => _MenuItemTile(item: item)),
      ],
    );
  }
}

class _MenuItemTile extends StatelessWidget {
  final _MenuItem item;
  
  const _MenuItemTile({required this.item});

  @override
  Widget build(BuildContext context) {
    return ListTile(
      leading: Icon(item.icon),
      title: Text(item.title),
      subtitle: item.subtitle != null ? Text(item.subtitle!) : null,
      trailing: const Icon(Icons.chevron_right),
      onTap: () {
        // TODO: Navigation implementieren
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('${item.title} - Coming Soon'),
            duration: const Duration(seconds: 1),
          ),
        );
      },
    );
  }
}

class _MenuItem {
  final IconData icon;
  final String title;
  final String? subtitle;

  _MenuItem({
    required this.icon,
    required this.title,
    this.subtitle,
  });
}
