# Documentacion Tecnica del Proyecto (Django + Portafolio)

Este documento es independiente de `README.md` y describe el codigo a nivel tecnico.

## 1) Objetivo tecnico

Migrar el portafolio estatico (HTML/CSS) a una base Django para que pueda crecer a:
- contenido dinamico desde base de datos,
- panel admin,
- mejor mantenimiento de rutas, templates y estaticos.

## 2) Arquitectura actual

- Proyecto Django: `core`
- App principal: `siteapp`
- Template principal: `templates/siteapp/home.html`
- CSS activo en Django: `static/css/styles.css`
- Base de datos local: `db.sqlite3`

## 3) Flujo de peticion HTTP

1. El navegador solicita `/`.
2. `core/urls.py` delega a `siteapp.urls`.
3. `siteapp/urls.py` enruta a `views.home`.
4. `siteapp/views.py` renderiza `templates/siteapp/home.html`.
5. El template carga CSS usando el tag `static` de Django.

## 4) Archivos Python (comentados)

### `core/settings.py`
- Configura apps (`INSTALLED_APPS`) incluyendo `siteapp`.
- Configura templates globales con `DIRS = [BASE_DIR / 'templates']`.
- Configura archivos estaticos:
  - `STATICFILES_DIRS = [BASE_DIR / "static"]`
  - `STATIC_ROOT = BASE_DIR / "staticfiles"`
- Region:
  - `LANGUAGE_CODE = 'es-mx'`
  - `TIME_ZONE = 'America/Mexico_City'`
- `ALLOWED_HOSTS` preparado para local y Render.

### `core/urls.py`
- `admin/` para panel Django.
- `''` incluye rutas de `siteapp`.

### `siteapp/urls.py`
- Ruta unica:
  - `"" -> views.home`

### `siteapp/views.py`
- `home(request)` devuelve:
  - `render(request, "siteapp/home.html")`

### `siteapp/models.py`
Modelos base para escalar:
- `Project`:
  - titulo, problema, solucion, stack, impacto, aprendizaje, repo/demo, orden.
- `Certification`:
  - nombre, proveedor, anio, resumen, orden.

### `siteapp/admin.py`
- Registra `Project` y `Certification`.
- Define `list_display`, filtros, busqueda y orden.

### `siteapp/tests.py`
- Prueba `HomePageTests`:
  - verifica que `/` responde HTTP 200.

## 5) Archivos HTML/CSS (comentados)

### `templates/siteapp/home.html`
- Incluye carga de `static` de Django para servir archivos estaticos.
- Secciones principales:
  - Hero
  - Sobre mi
  - Habilidades
  - Experiencia
  - Proyectos
  - Certificaciones
  - Formacion
  - Contacto
- Incluye boton flotante WhatsApp con tu numero.
- Incluye boton de descarga de CV via static.

### `static/css/styles.css`
- Organizado por bloques de comentarios:
  - variables globales
  - reset
  - navbar
  - hero
  - cards
  - proyectos
  - certificaciones
  - responsive
- Listo para mantenimiento modular.

## 6) Importante sobre archivos "duplicados"

Se mantienen estos archivos como referencia:
- `index.html` (version estatica legada)
- `styles.css` (copia legada)

Pero en Django debes editar principalmente:
- `templates/siteapp/home.html`
- `static/css/styles.css`

## 7) Comandos de operacion

### Levantar proyecto
```bash
python manage.py runserver
```

### Crear migraciones
```bash
python manage.py makemigrations
```

### Aplicar migraciones
```bash
python manage.py migrate
```

### Ejecutar pruebas
```bash
python manage.py test
```

### Crear usuario admin
```bash
python manage.py createsuperuser
```

## 8) Estado de validacion

Validaciones ejecutadas:
- `makemigrations` OK
- `migrate` OK
- `test` OK (1 prueba)

## 9) Proximos pasos tecnicos recomendados

1. Mover datos de proyectos/certificaciones a modelos y renderizar desde base de datos.
2. Crear formulario de contacto con envio de correo.
3. Migrar SQLite a PostgreSQL para produccion.
4. Integrar WhiteNoise y gunicorn para despliegue estable.
5. Agregar `.env` para secretos y ajustes por entorno.
