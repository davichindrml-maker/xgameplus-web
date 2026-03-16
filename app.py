from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cambia-esta-clave-por-una-mas-segura'

STORE_INFO = {
    'name': 'XGAMEPLUS',
    'brand_display': 'X Game Plus',
    'slogan': 'Computación y Videojuegos',
    'location': 'Plaza Constitución, San Luis Potosí',
    'experience_since': 2006,
    'phone': '+52 444 000 0000',
    'whatsapp_link': 'https://wa.me/524440000000',
    'facebook_link': 'https://facebook.com/',
    'hours': [
        'Lunes a sábado: 10:00 a.m. - 8:00 p.m.',
        'Domingo: horario sujeto a disponibilidad'
    ],
    'services': [
        {
            'title': 'Consolas, videojuegos y accesorios',
            'description': 'Venta de consolas, controles, discos, accesorios y productos gamer para distintas plataformas.'
        },
        {
            'title': 'Laptops y computación',
            'description': 'Equipos de cómputo, laptops gamer y asesoría para elegir el equipo ideal según tu presupuesto.'
        },
        {
            'title': 'Reparación y mantenimiento',
            'description': 'Mantenimiento preventivo y correctivo para PC, laptops y consolas, con atención profesional.'
        },
        {
            'title': 'Instalación de juegos digitales',
            'description': 'Apoyo con instalación de juegos digitales y configuración básica para que empieces a jugar cuanto antes.'
        }
    ],
    'highlights': [
        'Experiencia desde 2006',
        'Ubicación céntrica en San Luis Potosí',
        'Atención personalizada',
        'Enfoque en gaming y computación'
    ],
    'about': (
        'En XGAMEPLUS somos apasionados de la tecnología y los videojuegos. '
        'Somos un local ubicado en Plaza Constitución, en una zona céntrica de San Luis Potosí, '
        'donde ofrecemos productos y servicios para la comunidad gamer y para quienes buscan soluciones '
        'de computación confiables. Además de consolas y accesorios, también realizamos reparaciones, '
        'mantenimiento de PC y consolas, e instalación de juegos digitales. Nuestra experiencia desde 2006 '
        'nos respalda para brindarte una atención cercana, práctica y profesional.'
    )
}

PRODUCTS = [
    {
        'name': 'Xbox y consolas en existencia',
        'description': 'Modelos disponibles según inventario. Ideales para publicaciones futuras con precio y fotos reales.',
        'tag': 'Gaming'
    },
    {
        'name': 'Laptops gamer',
        'description': 'Equipos para estudio, trabajo y gaming con distintas configuraciones.',
        'tag': 'Computación'
    },
    {
        'name': 'Accesorios',
        'description': 'Controles, audífonos, cables, bases de carga y más.',
        'tag': 'Accesorios'
    }
]

TESTIMONIALS = [
    {
        'name': 'Clientes gamers',
        'text': 'Atención rápida, buena orientación y variedad de productos para consola y PC.'
    },
    {
        'name': 'Servicio técnico',
        'text': 'Mantenimiento y reparación con enfoque práctico para que tu equipo vuelva a rendir bien.'
    }
]


@app.route('/')
def home():
    return render_template('index.html', store=STORE_INFO, products=PRODUCTS, testimonials=TESTIMONIALS)


@app.route('/contacto', methods=['POST'])
def contact():
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    if not name or not email or not message:
        flash('Completa todos los campos antes de enviar el mensaje.', 'error')
        return redirect(url_for('home') + '#contacto')

    # Aquí después puedes conectar correo, WhatsApp API o guardar en base de datos.
    flash('Tu mensaje se registró correctamente. Ahora puedes conectar este formulario a correo o WhatsApp.', 'success')
    return redirect(url_for('home') + '#contacto')


if __name__ == '__main__':
    app.run(debug=True)
