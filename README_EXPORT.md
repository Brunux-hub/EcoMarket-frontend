# EcoMarket Frontend — Exportado

Este directorio contiene la app frontend extraída de `apps/frontend` del monorepo EcoMarket.

Instrucciones rápidas

1) Eliminar dependencias (no subir `node_modules`) antes de crear el repo:

Remove-Item -Recurse -Force .\node_modules

2) Instalar dependencias y arrancar:

npm install -g pnpm
pnpm install
pnpm start

3) Inicializar git y subir (ejemplo):

git init
git add .
git commit -m "Initial import: frontend"
git branch -M main
git remote add origin https://github.com/<TU_USUARIO>/<REPO_FRONTEND>.git
git push -u origin main

Notas
- Revisa `.gitignore` antes de hacer commit.
- Si quieres, puedo crear el commit inicial aquí y prepararlo para push (necesitarás crear el repo remoto y darme la URL).

---
Exportado desde: EcoMarket (`apps/frontend`) — 2025-10-22
