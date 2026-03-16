# XGAMEPLUS - Sitio web con Flask

Sitio web básico para la tienda **XGAMEPLUS**, hecho con **Python + Flask**, listo para subir a GitHub.

## Estructura

```bash
xgameplus_webapp/
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       ├── banner.png
│       └── logo.png
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

## Qué puedes editar rápido

- Datos del negocio: en `app.py`
- Colores y diseño: en `static/css/styles.css`
- Textos principales: en `templates/index.html`
- WhatsApp/Facebook reales: en `app.py`

## Recomendación para GitHub

Sube esta carpeta tal cual como repositorio. Luego, si quieres desplegarla gratis, puedes usar:

- Render
- Railway
- PythonAnywhere

## Nota

El formulario de contacto por ahora solo muestra un mensaje de confirmación. Después puedes conectarlo a:

- correo SMTP
- WhatsApp API
- base de datos
- Google Sheets
