#!/bin/bash
# =============================================================================
# Jonny Brain Backup
# =============================================================================
# Sichert alles was Jonny ausmacht (Persönlichkeit, Erinnerungen, Config)
# 
# Usage: ./brain-backup.sh [--destination /path/to/backup/folder]
#
# Standardmäßig: ~/JonnyBackups/
# Später: Cloud Drive Pfad
# =============================================================================

set -e

# Konfiguration
BACKUP_NAME="jonny-brain"
DATE=$(date +%Y-%m-%d_%H-%M)
DEFAULT_DESTINATION="${HOME}/JonnyBackups"

# Argument parsing
DESTINATION="${DEFAULT_DESTINATION}"
while [[ $# -gt 0 ]]; do
    case $1 in
        --destination|-d)
            DESTINATION="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Farben
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🦁 Jonny Brain Backup${NC}"
echo "================================"
echo "Datum: ${DATE}"
echo "Ziel:  ${DESTINATION}"
echo ""

# Zielordner erstellen
mkdir -p "${DESTINATION}"

# Temporärer Ordner für Backup-Sammlung
TEMP_DIR=$(mktemp -d)
BACKUP_DIR="${TEMP_DIR}/${BACKUP_NAME}"
mkdir -p "${BACKUP_DIR}"

echo "📦 Sammle Brain-Dateien..."

# 1. OpenClaw Workspace (nur wichtige Dateien, keine großen Assets)
echo "  → Workspace Dateien..."
mkdir -p "${BACKUP_DIR}/workspace"

# Alle .md Dateien im Root
cp ~/.openclaw/workspace/*.md "${BACKUP_DIR}/workspace/" 2>/dev/null || true

# Memory Ordner komplett
if [ -d ~/.openclaw/workspace/memory ]; then
    cp -r ~/.openclaw/workspace/memory "${BACKUP_DIR}/workspace/"
fi

# Projekt-Dokumentation (ohne Output/Assets)
if [ -d ~/.openclaw/workspace/projects ]; then
    mkdir -p "${BACKUP_DIR}/workspace/projects"
    find ~/.openclaw/workspace/projects -name "*.md" -exec cp --parents {} "${BACKUP_DIR}/" \; 2>/dev/null || \
    find ~/.openclaw/workspace/projects -name "*.md" | while read f; do
        rel_path="${f#$HOME/.openclaw/}"
        mkdir -p "${BACKUP_DIR}/$(dirname "$rel_path")"
        cp "$f" "${BACKUP_DIR}/$rel_path"
    done
fi

# 2. OpenClaw Config
echo "  → Config..."
cp ~/.openclaw/openclaw.json "${BACKUP_DIR}/" 2>/dev/null || true

# 3. Jonny Lab Repo-Referenz (nur README, nicht der ganze Code)
echo "  → Jonny Lab Info..."
if [ -d ~/jonny-lab ]; then
    mkdir -p "${BACKUP_DIR}/jonny-lab"
    cp ~/jonny-lab/README.md "${BACKUP_DIR}/jonny-lab/" 2>/dev/null || true
    # Git remote URL speichern für einfaches re-clonen
    cd ~/jonny-lab && git remote -v > "${BACKUP_DIR}/jonny-lab/git-remotes.txt" 2>/dev/null || true
fi

# 4. CLI Configs (falls vorhanden)
echo "  → CLI Configs..."
mkdir -p "${BACKUP_DIR}/cli-configs"
# GitHub CLI
if [ -f ~/.config/gh/hosts.yml ]; then
    cp ~/.config/gh/hosts.yml "${BACKUP_DIR}/cli-configs/gh-hosts.yml" 2>/dev/null || true
fi

# 4b. Secrets (Credentials, API Keys etc.)
echo "  → Secrets..."
if [ -d ~/.openclaw/secrets ]; then
    mkdir -p "${BACKUP_DIR}/secrets"
    cp -r ~/.openclaw/secrets/* "${BACKUP_DIR}/secrets/" 2>/dev/null || true
fi

# 5. Backup-Manifest erstellen
echo "  → Manifest..."
cat > "${BACKUP_DIR}/MANIFEST.md" << EOF
# Jonny Brain Backup

**Erstellt:** ${DATE}
**Host:** $(hostname)
**OpenClaw Version:** $(openclaw --version 2>/dev/null || echo "unbekannt")

## Inhalt

- \`workspace/\` - Meine Persönlichkeit, Erinnerungen, Projekte-Docs
- \`openclaw.json\` - OpenClaw Konfiguration
- \`jonny-lab/\` - GitHub Repo Info (Code ist auf GitHub)
- \`cli-configs/\` - CLI Tool Konfigurationen

## Restore

\`\`\`bash
# 1. OpenClaw installieren (falls nicht vorhanden)
npm install -g openclaw

# 2. Dieses Backup entpacken
tar -xzf ${BACKUP_NAME}-${DATE}.tar.gz

# 3. Restore-Script ausführen
./restore.sh
\`\`\`
EOF

# 6. Restore-Script erstellen
cat > "${BACKUP_DIR}/restore.sh" << 'RESTORE_EOF'
#!/bin/bash
# Jonny Brain Restore Script

set -e

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}🦁 Jonny Brain Restore${NC}"
echo "========================="

# Prüfe ob OpenClaw installiert ist
if ! command -v openclaw &> /dev/null; then
    echo -e "${RED}OpenClaw nicht gefunden!${NC}"
    echo "Installiere mit: npm install -g openclaw"
    exit 1
fi

# Zielordner erstellen
mkdir -p ~/.openclaw/workspace
mkdir -p ~/.openclaw/workspace/memory
mkdir -p ~/.openclaw/workspace/projects

# Workspace wiederherstellen
echo "📦 Stelle Workspace wieder her..."
cp -r workspace/* ~/.openclaw/workspace/

# Config wiederherstellen
echo "⚙️  Stelle Config wieder her..."
cp openclaw.json ~/.openclaw/

# Jonny Lab klonen (falls nicht vorhanden)
if [ -d jonny-lab ] && [ -f jonny-lab/git-remotes.txt ]; then
    if [ ! -d ~/jonny-lab ]; then
        echo "📂 Klone Jonny Lab..."
        REPO_URL=$(grep fetch jonny-lab/git-remotes.txt | awk '{print $2}' | head -1)
        git clone "$REPO_URL" ~/jonny-lab
    fi
fi

echo ""
echo -e "${GREEN}✅ Restore abgeschlossen!${NC}"
echo ""
echo "Nächste Schritte:"
echo "  1. openclaw gateway start"
echo "  2. Jonny ist zurück! 🦁"
RESTORE_EOF
chmod +x "${BACKUP_DIR}/restore.sh"

# 7. Archiv erstellen
ARCHIVE_NAME="${BACKUP_NAME}-${DATE}.tar.gz"
echo ""
echo "📦 Erstelle Archiv: ${ARCHIVE_NAME}"
cd "${TEMP_DIR}"
tar -czf "${DESTINATION}/${ARCHIVE_NAME}" "${BACKUP_NAME}"

# 8. Aufräumen
rm -rf "${TEMP_DIR}"

# 9. Größe anzeigen
SIZE=$(du -h "${DESTINATION}/${ARCHIVE_NAME}" | cut -f1)
echo ""
echo -e "${GREEN}✅ Backup erfolgreich!${NC}"
echo "   Datei: ${DESTINATION}/${ARCHIVE_NAME}"
echo "   Größe: ${SIZE}"
echo ""

# 10. Alte Backups aufräumen (behalte letzte 30)
echo "🧹 Räume alte Backups auf (behalte letzte 30)..."
ls -t "${DESTINATION}/${BACKUP_NAME}"*.tar.gz 2>/dev/null | tail -n +31 | xargs rm -f 2>/dev/null || true

echo -e "${GREEN}Done!${NC} 🦁"
