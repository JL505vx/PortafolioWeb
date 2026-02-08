# Portafolio CV - Jesus del Angel Lugardo Rodriguez

Este proyecto es una web tipo CV en una sola página, enfocada a perfil técnico de Ingeniería en Sistemas.

## 1) Estructura del proyecto

- `index.html`: estructura y contenido (texto, secciones, enlaces).
- `styles.css`: diseño visual (colores, tipografía, espacios, responsive).

## 2) Qué significa "placeholder"

`Placeholder` significa "texto temporal de ejemplo".

En este proyecto, aparece como:
- `[Métrica pendiente]`
- `[Plataforma y año]`

Debes reemplazarlo por datos reales cuando los tengas.

Ejemplo:
- Antes: `Impacto: [Métrica pendiente] menos tiempo de captura semanal.`
- Después: `Impacto: 35% menos tiempo de captura semanal (de 6 horas a 3.9 horas).`

## 3) Datos personales ya integrados

Ya quedaron cargados:
- Nombre: `Jesus del Angel Lugardo Rodriguez`
- GitHub: `https://github.com/JL505vx`
- Correo: `gpdev13@gmail.com`
- WhatsApp: `https://wa.me/529222275962`
- Universidad: `UGM Campus Minatitlán`
- Periodo: `2022 - 2026`

## 4) Secciones de la página (qué contiene cada una)

1. `Header/Nav`
- Nombre profesional corto.
- Menú para navegar entre secciones.

2. `Hero`
- Tu posicionamiento profesional en una frase.
- Resumen de enfoque técnico.
- CTA para ver proyectos y contacto.

3. `Sobre mí`
- Perfil narrativo serio.
- Lista de fortalezas técnicas concretas.

4. `Habilidades`
- Backend, bases de datos, sistemas/DevOps, datos/seguridad.
- Niveles: básico/intermedio/en progreso.

5. `Proyectos`
- Problema, solución, stack, impacto y aprendizaje.
- Imágenes libres de apoyo.

6. `Formación`
- Carrera + cursos/certificaciones.

7. `Contacto`
- Correo, GitHub y WhatsApp en botones directos.

## 5) Dónde editar cada cosa (rápido)

En `index.html`:
- Nombre visible en navbar: busca `Ing. <span>Jesus Lugardo</span>`
- Título principal: busca `<h1>`
- Sobre mí: sección `id="sobre-mi"`
- Proyectos: sección `id="proyectos"`
- Formación: sección `id="formacion"`
- Contacto: sección `id="contacto"`

## 6) Cambiar imágenes libres por tuyas

Cada imagen se carga con `src="https://images.pexels.com/..."`

Para reemplazar:
1. Sube tu imagen a una carpeta local (ejemplo `assets/img/mi-foto.jpg`).
2. Cambia el `src` por tu ruta local.
3. Mantén textos `alt` descriptivos para SEO y accesibilidad.

## 7) Guía de estilo y mantenimiento

- Mantén textos concretos, sin exagerar logros.
- No cambies demasiados colores: usa el acento azul para consistencia.
- No agregues animaciones pesadas.
- Usa métricas reales y comparables (antes/después).

## 8) Métricas recomendadas para reemplazar placeholders

Usa al menos una de estas por proyecto:
- Tiempo ahorrado (ej. horas por semana).
- Errores reducidos (ej. porcentaje de incidencias).
- Registros procesados (ej. tickets/usuarios/datos por día).
- Tiempo de despliegue (ej. minutos para levantar ambiente).

## 9) Checklist para dejarlo listo a prácticas/junior

- [ ] Corregiste todos los placeholders con datos reales.
- [ ] Incluiste 3 a 6 proyectos con stack y resultado medible.
- [ ] Verificaste links: GitHub, correo, WhatsApp.
- [ ] Ortografía revisada en todas las secciones.
- [ ] Probaste en móvil y desktop.
- [ ] Actualizaste cursos reales (si los tienes).
- [ ] Subiste el proyecto a GitHub Pages o Vercel.

## 10) Próximo paso recomendado

Agregar dos archivos opcionales para completar perfil:
- `cv-jesus-lugardo.pdf` (botón de descarga).
- `foto-perfil.jpg` profesional para hero.

## 10.1) Nuevas secciones agregadas

- `#experiencia`: servicios técnicos y experiencia aplicada.
- `#certificaciones`: lista de cursos/certificaciones para completar con constancias reales.
- Botón flotante de WhatsApp: abre chat directo a `9222275962`.
- Botón `Descargar CV`: apunta a `assets/cv/CV-Jesus-del-Angel-Lugardo-Rodriguez.pdf`.

Si aún no tienes el PDF:
1. Crea carpeta `assets/cv`.
2. Coloca tu CV con ese nombre exacto.
3. Si usas otro nombre, actualiza el `href` del botón en `index.html`.

## 11) Proyectos cargados actualmente

1. Bet or Lie - Juego por turnos
- Demo: `https://jl505vx.github.io/bet-or-lie/juego.html`
- Código: `https://github.com/JL505vx/bet-or-lie`

2. Sitio web para consultorio de anestesiología
- Demo: `https://jl505vx.github.io/danielapaginaanesteciologa/`
- Código: `https://github.com/JL505vx/danielapaginaanesteciologa`

3. Página web para clínica dental
- Demo: `https://paginadentista.onrender.com/`
- Código: `https://github.com/JL505vx/PaginaDentista`

4. Página web para anestesiólogo
- Demo: `https://paginatioricardo.onrender.com/`
- Código: `https://github.com/JL505vx/PaginaTioRicardo`

5. Blog informativo sobre TID (ELE Blog)
- Demo: `https://jl505vx.github.io/ELE_Blog-/`
- Código: `https://github.com/JL505vx/ELE_Blog-`

Si luego cambias un enlace, edítalo en la sección `id="proyectos"` dentro de `index.html`.

## 12) ¿Se puede migrar este portafolio a Django/Python?

Sí, y es recomendable para crecer a producción.

Ruta sugerida:
1. Mantener este diseño como base visual.
2. Pasar `index.html` a plantilla Django (`templates/`).
3. Pasar `styles.css` a `static/css/`.
4. Crear modelos para proyectos/certificaciones y cargarlos desde admin.
5. Migrar de SQLite a PostgreSQL cuando pases a producción estable.

## 13) Deploy en Render (Django)

Config recomendada para un `Web Service`:

- Build Command:
`bash build.sh`

- Start Command:
`gunicorn core.wsgi:application`

Variables de entorno mínimas:
- `SECRET_KEY`: (usa Generate en Render)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `.onrender.com`

Opcional para PostgreSQL (recomendado en producción):
- `DATABASE_URL`: cadena de conexión de Render PostgreSQL.

Nota:
- GitHub Pages no ejecuta Django backend.
- Para app Django completa usa Render.
