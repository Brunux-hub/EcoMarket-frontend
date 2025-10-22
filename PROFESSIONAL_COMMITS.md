# PROFESSIONAL COMMITS â€” EcoMarket-frontend

Este documento agrupa mensajes de commit profesionales destinados a describir de forma clara y consistente los cambios y su motivo. Se creÃ³ automÃ¡ticamente para profesionalizar el historial del repositorio sin reescribir commits existentes.

Formato usado
- Encabezado: <tipo>(<scope>): <breve descripciÃ³n>
- Cuerpo: explicaciÃ³n breve de quÃ© se hizo, por quÃ© y el impacto.

Tipos usados:
- feat: nueva funcionalidad
- fix: correcciÃ³n de errores
- chore: cambios menores/no funcionales (docs, build, tareas)
- refactor: reestructuraciÃ³n interna sin cambio funcional
- test: aÃ±adir/actualizar pruebas
- docs: documentaciÃ³n

Entradas sugeridas (resumen por Ã¡reas importantes)

1) feat(app): iniciar estructura base de la aplicaciÃ³n Angular

QuÃ©: Estructura inicial del proyecto Angular con componentes principales y rutas.
Por quÃ©: Establece la base para el desarrollo de la interfaz del marketplace.
Impacto: Proporciona componentes como `home`, `seller`, `admin`, y configuraciÃ³n de rutas y entornos.

2) feat(auth): aÃ±adir mÃ³dulos y componentes de autenticaciÃ³n

QuÃ©: Componentes y servicios para login y registro ubicados en `src/app/auth`.
Por quÃ©: Implementa la lÃ³gica de autenticaciÃ³n necesaria para controlar acceso y roles.
Impacto: Incluye guardias (`auth.guard`, `role.guard`) e interceptores para tokens de autenticaciÃ³n.

3) feat(ui): componentes UI reutilizables y layout

QuÃ©: Componentes de UI (header, footer, menu, product-card, filter-sidebar).
Por quÃ©: Facilitar la creaciÃ³n de interfaces consistentes y reutilizables.
Impacto: Mejora consistencia visual y facilita aÃ±adir nuevas vistas.

4) chore(config): aÃ±adir configuraciones y scripts de build/server

QuÃ©: Archivos de configuraciÃ³n como `angular.json`, `tsconfig.*`, `Dockerfile.dev`, y `main.server.ts`.
Por quÃ©: Facilitar builds, server-side rendering y despliegues en docker durante desarrollo.
Impacto: Entorno preparado para SSR y contenerizaciÃ³n.

5) docs(readme): aÃ±adir documentaciÃ³n bÃ¡sica y guÃ­as de uso

QuÃ©: `README.md`, `README_EXPORT.md` y documentaciÃ³n mÃ­nima de configuraciÃ³n.
Por quÃ©: Orientar a nuevos desarrolladores sobre cÃ³mo instalar y ejecutar la aplicaciÃ³n.
Impacto: Reduce la fricciÃ³n de onboarding.

6) chore(ci): rama para profesionalizar commits

QuÃ©: AÃ±ade este archivo `PROFESSIONAL_COMMITS.md` en la rama `professional-commits` con mensajes profesionales. No se reescribe el historial.
Por quÃ©: Mantener claridad en el historial sin alterar commits existentes.
Impacto: Permite revisar y luego decidir si se quiere reescribir el historial o mantener esta documentaciÃ³n.

Notas de uso
- Revisa manualmente las entradas y complÃ©talas con detalles por cada commit importante.
- Si deseas reescribir mensajes histÃ³ricos, contÃ¡ctame para generar un plan (requiere force-push y respaldo).

---

Archivo generado automÃ¡ticamente el 22 de octubre de 2025 por peticiÃ³n del propietario del repositorio.

### File: .editorconfig

Documento profesionalizado para el archivo: .editorconfig

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: .gitignore

Documento profesionalizado para el archivo: .gitignore

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: Dockerfile.dev

Documento profesionalizado para el archivo: Dockerfile.dev

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: README.md

Documento profesionalizado para el archivo: README.md

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: README_EXPORT.md

Documento profesionalizado para el archivo: README_EXPORT.md

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: angular.json

Documento profesionalizado para el archivo: angular.json

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: package.json

Documento profesionalizado para el archivo: package.json

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: postcss.config.js

Documento profesionalizado para el archivo: postcss.config.js

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: public/favicon.ico

Documento profesionalizado para el archivo: public/favicon.ico

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/admin.component.ts

Documento profesionalizado para el archivo: src/app/admin.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.config.server.ts

Documento profesionalizado para el archivo: src/app/app.config.server.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.config.ts

Documento profesionalizado para el archivo: src/app/app.config.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.html

Documento profesionalizado para el archivo: src/app/app.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.routes.server.ts

Documento profesionalizado para el archivo: src/app/app.routes.server.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.routes.ts

Documento profesionalizado para el archivo: src/app/app.routes.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.scss

Documento profesionalizado para el archivo: src/app/app.scss

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.spec.ts

Documento profesionalizado para el archivo: src/app/app.spec.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/app.ts

Documento profesionalizado para el archivo: src/app/app.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/guards/auth.guard.ts

Documento profesionalizado para el archivo: src/app/auth/guards/auth.guard.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/guards/role.guard.ts

Documento profesionalizado para el archivo: src/app/auth/guards/role.guard.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/login/login.component.ts

Documento profesionalizado para el archivo: src/app/auth/login/login.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/pages/login/login.component.html

Documento profesionalizado para el archivo: src/app/auth/pages/login/login.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/pages/login/login.component.ts

Documento profesionalizado para el archivo: src/app/auth/pages/login/login.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/pages/register/register.component.html

Documento profesionalizado para el archivo: src/app/auth/pages/register/register.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/pages/register/register.component.ts

Documento profesionalizado para el archivo: src/app/auth/pages/register/register.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/register/register.component.ts

Documento profesionalizado para el archivo: src/app/auth/register/register.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/auth/services/auth.service.ts

Documento profesionalizado para el archivo: src/app/auth/services/auth.service.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/guards/auth.guard.ts

Documento profesionalizado para el archivo: src/app/guards/auth.guard.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/home.component.ts

Documento profesionalizado para el archivo: src/app/home.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/interceptors/auth.interceptor.ts

Documento profesionalizado para el archivo: src/app/interceptors/auth.interceptor.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/seller.component.ts

Documento profesionalizado para el archivo: src/app/seller.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/services/auth.service.ts

Documento profesionalizado para el archivo: src/app/services/auth.service.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/components/menu/menu.component.html

Documento profesionalizado para el archivo: src/app/shared/components/menu/menu.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/components/menu/menu.component.ts

Documento profesionalizado para el archivo: src/app/shared/components/menu/menu.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/filter-sidebar/filter-sidebar.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/filter-sidebar/filter-sidebar.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/filter-sidebar/filter-sidebar.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/filter-sidebar/filter-sidebar.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/footer/footer.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/footer/footer.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/footer/footer.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/footer/footer.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/header/header.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/header/header.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/header/header.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/header/header.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/product-card/product-card.component.html

Documento profesionalizado para el archivo: src/app/shared/ui/product-card/product-card.component.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/shared/ui/product-card/product-card.component.ts

Documento profesionalizado para el archivo: src/app/shared/ui/product-card/product-card.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/app/unauthorized.component.ts

Documento profesionalizado para el archivo: src/app/unauthorized.component.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/environments/environment.ts

Documento profesionalizado para el archivo: src/environments/environment.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/index.html

Documento profesionalizado para el archivo: src/index.html

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/main.server.ts

Documento profesionalizado para el archivo: src/main.server.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/main.ts

Documento profesionalizado para el archivo: src/main.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/server.ts

Documento profesionalizado para el archivo: src/server.ts

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/styles.css

Documento profesionalizado para el archivo: src/styles.css

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: src/styles.scss

Documento profesionalizado para el archivo: src/styles.scss

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: tsconfig.app.json

Documento profesionalizado para el archivo: tsconfig.app.json

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: tsconfig.json

Documento profesionalizado para el archivo: tsconfig.json

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: tsconfig.spec.json

Documento profesionalizado para el archivo: tsconfig.spec.json

- Resumen: Añade contexto y propósito del archivo.
- Impacto: Describe el impacto en la aplicación.



### File: .editorconfig

- Funcionalidad: Descripción detallada del propósito y uso de .editorconfig.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: .gitignore

- Funcionalidad: Descripción detallada del propósito y uso de .gitignore.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: README.md

- Funcionalidad: Descripción detallada del propósito y uso de README.md.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: README_EXPORT.md

- Funcionalidad: Descripción detallada del propósito y uso de README_EXPORT.md.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: angular.json

- Funcionalidad: Descripción detallada del propósito y uso de angular.json.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: tsconfig.app.json

- Funcionalidad: Descripción detallada del propósito y uso de tsconfig.app.json.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: tsconfig.json

- Funcionalidad: Descripción detallada del propósito y uso de tsconfig.json.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### File: tsconfig.spec.json

- Funcionalidad: Descripción detallada del propósito y uso de tsconfig.spec.json.
- Impacto: Indica cómo afecta al build, lint o al comportamiento de la app.


### Archivo: .editorconfig

- Funcionalidad: Este archivo controla la configuración/propósito de .editorconfig en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: .gitignore

- Funcionalidad: Este archivo controla la configuración/propósito de .gitignore en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: README.md

- Funcionalidad: Este archivo controla la configuración/propósito de README.md en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: README_EXPORT.md

- Funcionalidad: Este archivo controla la configuración/propósito de README_EXPORT.md en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: angular.json

- Funcionalidad: Este archivo controla la configuración/propósito de angular.json en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: tsconfig.app.json

- Funcionalidad: Este archivo controla la configuración/propósito de tsconfig.app.json en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: tsconfig.json

- Funcionalidad: Este archivo controla la configuración/propósito de tsconfig.json en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: tsconfig.spec.json

- Funcionalidad: Este archivo controla la configuración/propósito de tsconfig.spec.json en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: package.json

- Funcionalidad: Este archivo controla la configuración/propósito de package.json en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: postcss.config.js

- Funcionalidad: Este archivo controla la configuración/propósito de postcss.config.js en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.


### Archivo: Dockerfile.dev

- Funcionalidad: Este archivo controla la configuración/propósito de Dockerfile.dev en el proyecto. Descripción breve en español.
- Impacto: Afecta al build/linters/ejecución según corresponda.

