# XGAMEPLUS - Sitio web con Flask

Sitio web básico para la tienda **XGAMEPLUS**, hecho con **Python + Flask**, listo para subir a GitHub y desplegar en **Render**.

## Estructura

```bash
xgameplus_webapp/
├── app.py
├── requirements.txt
├── render.yaml
├── README.md
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       ├── banner.png
│       ├── logo.png
│       └── products/
│           ├── rtx5070_1.jpg
│           ├── rtx5070_2.jpg
│           ├── rtx5070_3.jpg
│           └── rtx5070_4.jpg
└── templates/
    ├── base.html
    └── index.html
```

## Cómo correrlo localmente

1. Crea y activa tu entorno virtual.
2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta:

```bash
python app.py
```

4. Abre en tu navegador:

```bash
http://127.0.0.1:5000
```

## Listo para Render

Este proyecto ya quedó preparado para desplegarse en Render.

### Opción 1: usando `render.yaml`
Solo sube el repo a GitHub y en Render importa el repositorio. Render detectará la configuración automáticamente.

### Opción 2: configuración manual en Render
Usa estos valores:

- **Environment:** Python
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

## Qué puedes editar rápido

- Datos del negocio: en `app.py`
- Producto destacado y fotos: en `app.py` y `static/images/products/`
- Colores y diseño: en `static/css/styles.css`
- Textos principales: en `templates/index.html`
- WhatsApp/Facebook reales: en `app.py`

## Nota

El formulario de contacto por ahora solo muestra un mensaje de confirmación. Después puedes conectarlo a:

- correo SMTP
- WhatsApp API
- base de datos
- Google Sheets
