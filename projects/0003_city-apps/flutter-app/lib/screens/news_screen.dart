import 'package:flutter/material.dart';

class NewsScreen extends StatelessWidget {
  const NewsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    
    // Beispiel-News - später aus Backend/API holen
    final news = [
      _NewsItem(
        title: 'Neue Spielplatzausstattung am Dorfplatz',
        summary: 'Die Gemeinde investiert in moderne Spielgeräte für unsere Kinder.',
        date: DateTime.now().subtract(const Duration(days: 2)),
        category: 'Infrastruktur',
      ),
      _NewsItem(
        title: 'Gemeinderatssitzung: Wichtige Beschlüsse',
        summary: 'In der letzten Sitzung wurden mehrere wichtige Entscheidungen getroffen.',
        date: DateTime.now().subtract(const Duration(days: 5)),
        category: 'Politik',
      ),
      _NewsItem(
        title: 'Sommerfest 2026 - Save the Date',
        summary: 'Das traditionelle Sommerfest findet am 15. Juli statt.',
        date: DateTime.now().subtract(const Duration(days: 7)),
        category: 'Veranstaltungen',
      ),
    ];
    
    return Scaffold(
      appBar: AppBar(
        title: const Text('News'),
        actions: [
          IconButton(
            icon: const Icon(Icons.search),
            onPressed: () {
              // TODO: Suchfunktion
            },
          ),
        ],
      ),
      body: news.isEmpty
          ? Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    Icons.article_outlined,
                    size: 80,
                    color: theme.colorScheme.primary.withOpacity(0.3),
                  ),
                  const SizedBox(height: 24),
                  Text(
                    'Keine News verfügbar',
                    style: theme.textTheme.headlineSmall?.copyWith(
                      color: theme.colorScheme.onSurface.withOpacity(0.6),
                    ),
                  ),
                ],
              ),
            )
          : ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: news.length,
              itemBuilder: (context, index) {
                return _NewsCard(newsItem: news[index]);
              },
            ),
    );
  }
}

class _NewsCard extends StatelessWidget {
  final _NewsItem newsItem;
  
  const _NewsCard({required this.newsItem});

  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);
    final daysAgo = DateTime.now().difference(newsItem.date).inDays;
    final dateText = daysAgo == 0 
        ? 'Heute'
        : daysAgo == 1 
            ? 'Gestern'
            : 'Vor $daysAgo Tagen';
    
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
        side: BorderSide(
          color: theme.colorScheme.outlineVariant,
          width: 1,
        ),
      ),
      child: InkWell(
        onTap: () {
          // TODO: Zu Detail-Seite navigieren
        },
        borderRadius: BorderRadius.circular(12),
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 8,
                      vertical: 4,
                    ),
                    decoration: BoxDecoration(
                      color: theme.colorScheme.primaryContainer,
                      borderRadius: BorderRadius.circular(4),
                    ),
                    child: Text(
                      newsItem.category,
                      style: theme.textTheme.labelSmall?.copyWith(
                        color: theme.colorScheme.onPrimaryContainer,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                  const Spacer(),
                  Text(
                    dateText,
                    style: theme.textTheme.bodySmall?.copyWith(
                      color: theme.colorScheme.onSurface.withOpacity(0.6),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              Text(
                newsItem.title,
                style: theme.textTheme.titleMedium?.copyWith(
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                newsItem.summary,
                style: theme.textTheme.bodyMedium?.copyWith(
                  color: theme.colorScheme.onSurface.withOpacity(0.7),
                ),
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
              const SizedBox(height: 12),
              Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  TextButton(
                    onPressed: () {
                      // TODO: Artikel öffnen
                    },
                    child: const Text('Weiterlesen'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _NewsItem {
  final String title;
  final String summary;
  final DateTime date;
  final String category;

  _NewsItem({
    required this.title,
    required this.summary,
    required this.date,
    required this.category,
  });
}
