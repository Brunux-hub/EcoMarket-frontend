// Funcional: src/app/app.routes.server.ts � descripci�n breve de la responsabilidad principal del archivo.
import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  {
    path: '**',
    renderMode: RenderMode.Prerender
  }
];

