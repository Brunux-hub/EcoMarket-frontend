# PROFESSIONAL COMMITS — EcoMarket-frontend

Este documento agrupa mensajes de commit profesionales destinados a describir de forma clara y consistente los cambios y su motivo. Se creó automáticamente para profesionalizar el historial del repositorio sin reescribir commits existentes.

Formato usado
- Encabezado: <tipo>(<scope>): <breve descripción>
- Cuerpo: explicación breve de qué se hizo, por qué y el impacto.

Tipos usados:
- feat: nueva funcionalidad
- fix: corrección de errores
- chore: cambios menores/no funcionales (docs, build, tareas)
- refactor: reestructuración interna sin cambio funcional
- test: añadir/actualizar pruebas
- docs: documentación

Entradas sugeridas (resumen por áreas importantes)

1) feat(app): iniciar estructura base de la aplicación Angular

Qué: Estructura inicial del proyecto Angular con componentes principales y rutas.
Por qué: Establece la base para el desarrollo de la interfaz del marketplace.
Impacto: Proporciona componentes como `home`, `seller`, `admin`, y configuración de rutas y entornos.

2) feat(auth): añadir módulos y componentes de autenticación

Qué: Componentes y servicios para login y registro ubicados en `src/app/auth`.
Por qué: Implementa la lógica de autenticación necesaria para controlar acceso y roles.
Impacto: Incluye guardias (`auth.guard`, `role.guard`) e interceptores para tokens de autenticación.

3) feat(ui): componentes UI reutilizables y layout

Qué: Componentes de UI (header, footer, menu, product-card, filter-sidebar).
Por qué: Facilitar la creación de interfaces consistentes y reutilizables.
Impacto: Mejora consistencia visual y facilita añadir nuevas vistas.

4) chore(config): añadir configuraciones y scripts de build/server

Qué: Archivos de configuración como `angular.json`, `tsconfig.*`, `Dockerfile.dev`, y `main.server.ts`.
Por qué: Facilitar builds, server-side rendering y despliegues en docker durante desarrollo.
Impacto: Entorno preparado para SSR y contenerización.

5) docs(readme): añadir documentación básica y guías de uso

Qué: `README.md`, `README_EXPORT.md` y documentación mínima de configuración.
Por qué: Orientar a nuevos desarrolladores sobre cómo instalar y ejecutar la aplicación.
Impacto: Reduce la fricción de onboarding.

6) chore(ci): rama para profesionalizar commits

Qué: Añade este archivo `PROFESSIONAL_COMMITS.md` en la rama `professional-commits` con mensajes profesionales. No se reescribe el historial.
Por qué: Mantener claridad en el historial sin alterar commits existentes.
Impacto: Permite revisar y luego decidir si se quiere reescribir el historial o mantener esta documentación.

Notas de uso
- Revisa manualmente las entradas y complétalas con detalles por cada commit importante.
- Si deseas reescribir mensajes históricos, contáctame para generar un plan (requiere force-push y respaldo).

---

Archivo generado automáticamente el 22 de octubre de 2025 por petición del propietario del repositorio.

### File: .editorconfig

Documento profesionalizado para el archivo: .editorconfig

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: .gitignore

Documento profesionalizado para el archivo: .gitignore

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: Dockerfile.dev

Documento profesionalizado para el archivo: Dockerfile.dev

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: README.md

Documento profesionalizado para el archivo: README.md

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: README_EXPORT.md

Documento profesionalizado para el archivo: README_EXPORT.md

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: angular.json

Documento profesionalizado para el archivo: angular.json

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: package.json

Documento profesionalizado para el archivo: package.json

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: postcss.config.js

Documento profesionalizado para el archivo: postcss.config.js

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: public/favicon.ico

Documento profesionalizado para el archivo: public/favicon.ico

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/admin.component.ts

Documento profesionalizado para el archivo: src/app/admin.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.config.server.ts

Documento profesionalizado para el archivo: src/app/app.config.server.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.config.ts

Documento profesionalizado para el archivo: src/app/app.config.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.html

Documento profesionalizado para el archivo: src/app/app.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.routes.server.ts

Documento profesionalizado para el archivo: src/app/app.routes.server.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.routes.ts

Documento profesionalizado para el archivo: src/app/app.routes.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.scss

Documento profesionalizado para el archivo: src/app/app.scss

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.spec.ts

Documento profesionalizado para el archivo: src/app/app.spec.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/app.ts

Documento profesionalizado para el archivo: src/app/app.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/guards/auth.guard.ts

Documento profesionalizado para el archivo: src/app/auth/guards/auth.guard.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/guards/role.guard.ts

Documento profesionalizado para el archivo: src/app/auth/guards/role.guard.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/login/login.component.ts

Documento profesionalizado para el archivo: src/app/auth/login/login.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/pages/login/login.component.html

Documento profesionalizado para el archivo: src/app/auth/pages/login/login.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/pages/login/login.component.ts

Documento profesionalizado para el archivo: src/app/auth/pages/login/login.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/pages/register/register.component.html

Documento profesionalizado para el archivo: src/app/auth/pages/register/register.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/pages/register/register.component.ts

Documento profesionalizado para el archivo: src/app/auth/pages/register/register.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/register/register.component.ts

Documento profesionalizado para el archivo: src/app/auth/register/register.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/auth/services/auth.service.ts

Documento profesionalizado para el archivo: src/app/auth/services/auth.service.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/guards/auth.guard.ts

Documento profesionalizado para el archivo: src/app/guards/auth.guard.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/home.component.ts

Documento profesionalizado para el archivo: src/app/home.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/interceptors/auth.interceptor.ts

Documento profesionalizado para el archivo: src/app/interceptors/auth.interceptor.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/seller.component.ts

Documento profesionalizado para el archivo: src/app/seller.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/services/auth.service.ts

Documento profesionalizado para el archivo: src/app/services/auth.service.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/components/menu/menu.component.html

Documento profesionalizado para el archivo: src/app/shared/components/menu/menu.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/components/menu/menu.component.ts

Documento profesionalizado para el archivo: src/app/shared/components/menu/menu.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/filter-sidebar/filter-sidebar.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/filter-sidebar/filter-sidebar.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/filter-sidebar/filter-sidebar.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/filter-sidebar/filter-sidebar.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/footer/footer.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/footer/footer.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/footer/footer.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/footer/footer.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/header/header.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/header/header.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/header/header.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/header/header.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/product-card/product-card.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/product-card/product-card.component.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/shared/ui/product-card/product-card.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/product-card/product-card.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/app/unauthorized.component.ts

Documento profesionalizado para el archivo: src/app/unauthorized.component.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/environments/environment.ts

Documento profesionalizado para el archivo: src/environments/environment.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/index.html

Documento profesionalizado para el archivo: src/index.html

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/main.server.ts

Documento profesionalizado para el archivo: src/main.server.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/main.ts

Documento profesionalizado para el archivo: src/main.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/server.ts

Documento profesionalizado para el archivo: src/server.ts

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/styles.css

Documento profesionalizado para el archivo: src/styles.css

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: src/styles.scss

Documento profesionalizado para el archivo: src/styles.scss

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: tsconfig.app.json

Documento profesionalizado para el archivo: tsconfig.app.json

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: tsconfig.json

Documento profesionalizado para el archivo: tsconfig.json

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: tsconfig.spec.json

Documento profesionalizado para el archivo: tsconfig.spec.json

- Resumen: A�ade contexto y prop�sito del archivo.
- Impacto: Describe el impacto en la aplicaci�n.



### File: .editorconfig

- Funcionalidad: Descripci�n detallada del prop�sito y uso de .editorconfig.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: .gitignore

- Funcionalidad: Descripci�n detallada del prop�sito y uso de .gitignore.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: README.md

- Funcionalidad: Descripci�n detallada del prop�sito y uso de README.md.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: README_EXPORT.md

- Funcionalidad: Descripci�n detallada del prop�sito y uso de README_EXPORT.md.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: angular.json

- Funcionalidad: Descripci�n detallada del prop�sito y uso de angular.json.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: tsconfig.app.json

- Funcionalidad: Descripci�n detallada del prop�sito y uso de tsconfig.app.json.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: tsconfig.json

- Funcionalidad: Descripci�n detallada del prop�sito y uso de tsconfig.json.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### File: tsconfig.spec.json

- Funcionalidad: Descripci�n detallada del prop�sito y uso de tsconfig.spec.json.
- Impacto: Indica c�mo afecta al build, lint o al comportamiento de la app.


### Archivo: .editorconfig

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de .editorconfig en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: .gitignore

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de .gitignore en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: README.md

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de README.md en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: README_EXPORT.md

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de README_EXPORT.md en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: angular.json

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de angular.json en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: tsconfig.app.json

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de tsconfig.app.json en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: tsconfig.json

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de tsconfig.json en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: tsconfig.spec.json

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de tsconfig.spec.json en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: package.json

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de package.json en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: postcss.config.js

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de postcss.config.js en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.


### Archivo: Dockerfile.dev

- Funcionalidad: Este archivo controla la configuraci�n/prop�sito de Dockerfile.dev en el proyecto. Descripci�n breve en espa�ol.
- Impacto: Afecta al build/linters/ejecuci�n seg�n corresponda.

