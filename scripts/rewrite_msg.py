import sys, re
text = sys.stdin.read()
if not text:
    sys.stdout.write(text)
    sys.exit(0)
# Simple replacements English -> Spanish
repls = [
    (r"Initial import: frontend from EcoMarket", "chore(inicio): importación inicial del frontend (EcoMarket)"),
    (r"Initial import: frontend", "chore(inicio): importación inicial del frontend"),
    (r"Initial import", "chore(inicio): importación inicial"),
    (r"document functionality for", "documentar funcionalidad de"),
    (r"add functionality comment to", "añadir comentario de funcionalidad a"),
    (r"normalize EOF newline", "normalizar salto final de línea"),
    (r"touch (.+?) to update metadata display", r"tocar \1 para actualizar metadatos (sin cambio funcional)"),
    (r"docs\(([^)]+)\):", r"docs(\1):"),
    (r"chore\(([^)]+)\):", r"tarea(\1):"),
    (r"document," , "documentar,"),
]
for p,r in repls:
    text = re.sub(p, r, text, flags=re.IGNORECASE)
# verb replacements
verbs = [(r"\badd\b","añadir"),(r"\bupdate\b","actualizar"),(r"\bremove\b","eliminar"),(r"\bfix\b","corregir")]
for p,r in verbs:
    text = re.sub(p, r, text, flags=re.IGNORECASE)
if not text.endswith('\n'):
    text += '\n'
sys.stdout.write(text)
