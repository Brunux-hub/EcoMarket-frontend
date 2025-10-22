import sys, re

text = sys.stdin.read()
if not text:
    sys.stdout.write(text)
    sys.exit(0)

replacements = [
    (r"Initial import: frontend from EcoMarket", "chore(inicio): importación inicial del frontend (EcoMarket)"),
    (r"Initial import: frontend", "chore(inicio): importación inicial del frontend"),
    (r"Initial import", "chore(inicio): importación inicial"),
    (r"Initial Import", "chore(inicio): importación inicial"),
    (r"document functionality for", "documentar funcionalidad de"),
    (r"document functionality", "documentar funcionalidad"),
    (r"add functionality comment to", "añadir comentario de funcionalidad a"),
    (r"add header comment", "añadir comentario de cabecera"),
    (r"normalize EOF newline for", "normalizar salto final de línea para"),
    (r"normalize EOF newline", "normalizar salto final de línea"),
    (r"touch (.+?) to update metadata display", r"tocar \1 para actualizar metadatos (sin cambio funcional)"),
    (r"chore\(([^)]+)\):", r"tarea(\1):"),
    (r"docs\(([^)]+)\):", r"docs(\1):"),
    (r"document functionality for postcss.config.js", "documentar funcionalidad de postcss.config.js"),
]

for pat, repl in replacements:
    text = re.sub(pat, repl, text, flags=re.IGNORECASE)

# Common verbs
verbs = [
    (r"\badd\b", "añadir"),
    (r"\bupdate\b", "actualizar"),
    (r"\bremove\b", "eliminar"),
    (r"\bfix\b", "corregir"),
    (r"\bdocument\b", "documentar"),
    (r"\bnormalize\b", "normalizar"),
    (r"\breplace\b", "reemplazar"),
    (r"\bmerge\b", "fusionar"),
]
for pat, repl in verbs:
    text = re.sub(pat, repl, text, flags=re.IGNORECASE)

# Ensure trailing newline
if not text.endswith('\n'):
    text += '\n'

sys.stdout.write(text)
+