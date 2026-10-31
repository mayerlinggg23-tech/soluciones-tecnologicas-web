"""Genera la web de Soluciones Tecnológicas.

Rellena CONFIG (y, si quieres, los precios de PACKS), luego ejecuta:
    python build.py
Todo lo que esté entre [corchetes] sale resaltado en amarillo en la web
para que se vea que falta rellenarlo.
"""
from html import escape
import json
from pathlib import Path

OUT = Path(__file__).parent

# ---------------------------------------------------------------- datos ---
CONFIG = {
    "nombre": "Soluciones Tecnológicas",
    "lema": "Tecnología que trabaja para tu negocio",
    "ciudad": "Madrid",
    "zona": "Madrid y alrededores",
    "correo": "",  # vacío = no se muestra
    "telefono": "643 640 411",
    "whatsapp": "34668543184",  # solo números con prefijo, p. ej. "34600111222"
    "dominio": "mayerlinggg23-tech.github.io/soluciones-tecnologicas-web",  # p. ej. "solucionestecnologicas.es" (activa sitemap.xml)
    "instagram": "",  # URL completa
    "tiktok": "",  # URL completa
    "titular_legal": "[NOMBRE Y APELLIDOS O RAZÓN SOCIAL]",
    "nif": "[NIF/NIE/CIF]",
    "direccion_legal": "[DIRECCIÓN FISCAL]",
    "forma_pago": "Te lo detallamos por escrito en la propuesta, antes de empezar.",
}

ICONS = {
    "web": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/></svg>',
    "tienda": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h16l-1.5 11a2 2 0 0 1-2 1.7H7.5a2 2 0 0 1-2-1.7z"/><path d="M9 7V5.5a3 3 0 0 1 6 0V7"/></svg>',
    "reels": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M10.5 9.5v5l4-2.5z"/></svg>',
    "ia": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="7" width="14" height="11" rx="3"/><path d="M12 3v4M9 12h.01M15 12h.01M9.5 15h5M2 12h3M19 12h3"/></svg>',
    "it": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3.5" width="18" height="6" rx="1.5"/><rect x="3" y="14.5" width="18" height="6" rx="1.5"/><path d="M7 6.5h.01M7 17.5h.01M12 9.5v5"/></svg>',
}

SERVICIOS = [
    {
        "slug": "paginas-web",
        "icono": "web",
        "titulo": "Páginas web",
        "seo": "Diseño de páginas web para negocios en Madrid",
        "corto": "Webs rápidas y claras para comercios y profesionales, pensadas primero para el móvil.",
        "intro": "Una web que explica en segundos qué haces, carga rápido en el móvil y lleva al cliente a escribirte, llamarte o reservar.",
        "tags": ["Corporativas", "Comercios", "Profesionales"],
        "incluye": [
            "Diseño a medida a partir de tu marca",
            "Adaptada a móvil, tablet y ordenador",
            "Textos revisados para que se entiendan y se encuentren en Google",
            "Formulario y botón directo a WhatsApp",
            "Ficha de Google Business conectada",
            "Velocidad optimizada (imágenes ligeras, sin librerías pesadas)",
            "Aviso legal, privacidad y cookies",
            "Formación para que puedas cambiar textos y fotos",
        ],
        "faqs": [
            ("¿Puedo cambiar yo los textos después?", "Sí. Te enseñamos a cambiar textos e imágenes y, si lo prefieres, lo hacemos nosotros dentro del mantenimiento."),
            ("¿El dominio y la web son míos?", "Sí. El dominio se registra a tu nombre y te entregamos todos los accesos al terminar."),
            ("¿Saldré en Google?", "Dejamos la web preparada para Google (títulos, descripciones, velocidad, mapa del sitio) y conectada a tu ficha de Google Business. Subir posiciones depende también de la competencia y del tiempo."),
        ],
    },
    {
        "slug": "tiendas-online",
        "icono": "tienda",
        "titulo": "Tiendas online",
        "seo": "Creación de tiendas online y Shopify en Madrid",
        "corto": "Tiendas en Shopify o a medida, con catálogo, pagos, stock y panel para gestionar pedidos.",
        "intro": "Montamos tu tienda para vender de verdad: catálogo ordenado, fichas de producto que convencen, pago fácil y un panel para controlar pedidos y stock.",
        "tags": ["Shopify", "A medida", "Inventario"],
        "incluye": [
            "Tienda en Shopify o desarrollada a medida",
            "Carga de catálogo con tallas, colores y variantes",
            "Pagos con tarjeta, Bizum o transferencia",
            "Control de stock y avisos de pedido",
            "Panel de administración de pedidos y clientes",
            "Códigos de barras para el inventario (opcional)",
            "Reservas de citas o cursos si tu negocio los necesita",
            "Textos legales de compra, envíos y devoluciones",
        ],
        "faqs": [
            ("¿Shopify o tienda a medida?", "Shopify es rápido de montar y tiene cuota mensual. A medida no paga cuota de plataforma y se adapta a todo (citas, cursos, inventario). Te recomendamos una u otra según tu catálogo y presupuesto."),
            ("¿Cargáis vosotros los productos?", "Sí, cargamos el catálogo inicial a partir de tus fotos y datos. Después puedes añadir productos tú desde el panel."),
            ("¿Puedo vender también en el local?", "Sí. El stock puede ser el mismo para la tienda física y la online, y el inventario admite códigos de barras."),
        ],
    },
    {
        "slug": "reels-redes",
        "icono": "reels",
        "titulo": "Reels y redes sociales",
        "seo": "Reels y gestión de redes sociales para negocios en Madrid",
        "corto": "Vídeos para Instagram y TikTok y un plan de publicaciones con la misma imagen que tu web.",
        "intro": "Contenido que enseña tus productos, tu espacio y a tu equipo, con un estilo que se reconoce igual en tu web, en Instagram y en TikTok.",
        "tags": ["Instagram", "TikTok", "Planificación"],
        "incluye": [
            "Plan de contenidos mensual",
            "Grabación y edición de reels",
            "Portadas y plantillas con tu imagen de marca",
            "Textos y hashtags para cada publicación",
            "Perfil optimizado (bio, enlaces, destacados)",
            "Informe mensual de resultados",
        ],
        "faqs": [
            ("¿Tengo que salir yo en los vídeos?", "No es obligatorio. Podemos grabar productos, el local o procesos, o usar a tu equipo si quiere salir."),
            ("¿Publicáis vosotros?", "Podemos dejar todo programado o entregarte el contenido listo para que lo subas tú, como prefieras."),
            ("¿Cuántos vídeos al mes?", "Depende del pack. Lo dejamos por escrito en la propuesta antes de empezar."),
        ],
    },
    {
        "slug": "ia-negocios",
        "icono": "ia",
        "titulo": "IA para negocios",
        "seo": "Chatbots, automatizaciones e inteligencia artificial para pymes en Madrid",
        "corto": "Asistentes que responden a clientes, automatizaciones que ahorran horas y modelos de IA privados.",
        "intro": "Usamos la inteligencia artificial para quitarte trabajo repetitivo: responder preguntas frecuentes, preparar presupuestos, ordenar datos o redactar contenido.",
        "tags": ["Chatbots", "Automatización", "IA privada"],
        "incluye": [
            "Asistente para tu web o WhatsApp entrenado con la información de tu negocio",
            "Automatizaciones entre correo, hojas de cálculo y tu tienda",
            "Clasificación y resumen de documentos, correos o pedidos",
            "Opción de IA privada en tu propio equipo, sin enviar datos fuera",
            "Formación para tu equipo",
            "Revisión de que se cumple la protección de datos",
        ],
        "faqs": [
            ("¿Mis datos salen de mi empresa?", "Si lo necesitas, montamos la IA en un equipo tuyo (modelo local) para que la información no salga a servicios externos."),
            ("¿El asistente puede equivocarse?", "Sí, como cualquier IA. Por eso lo limitamos a la información de tu negocio, lo probamos antes y dejamos claro cuándo debe pasar la conversación a una persona."),
            ("¿Necesito saber de tecnología?", "No. Lo dejamos funcionando y te enseñamos lo justo para usarlo."),
        ],
    },
    {
        "slug": "soporte-it",
        "icono": "it",
        "titulo": "Servicio técnico de redes y servidores",
        "seo": "Servicio técnico de redes, Wi-Fi y servidores para empresas en Madrid",
        "corto": "Diagnóstico y mantenimiento de redes, Wi-Fi, servidores y copias de seguridad para pymes.",
        "intro": "Revisamos y ordenamos la red de tu negocio para que funcione rápido y segura: Wi-Fi, routers, equipos, servidores y copias de seguridad, con nuestro método de diagnóstico RedTI 360°.",
        "tags": ["Redes y Wi-Fi", "Servidores", "Copias de seguridad"],
        "incluye": [
            "Diagnóstico de red con el método RedTI 360° e informe por escrito",
            "Instalación y ajuste de routers, puntos de acceso y Wi-Fi",
            "Red de invitados separada de la del negocio",
            "Montaje y mantenimiento de servidores y NAS",
            "Copias de seguridad automáticas y prueba de recuperación",
            "Acceso remoto seguro para ti y tu equipo",
            "Revisión de seguridad básica (contraseñas, actualizaciones, equipos expuestos)",
            "Mantenimiento mensual con soporte remoto",
        ],
        "faqs": [
            ("¿Venís al local?", "Sí, en Madrid y alrededores. Muchas incidencias se resuelven además por acceso remoto, sin desplazamiento."),
            ("¿Qué es el diagnóstico RedTI 360°?", "Es nuestro método para revisar la red de una pyme por partes: conexión, Wi-Fi, equipos, seguridad y copias. Termina con un informe claro de qué falla y qué conviene mejorar primero."),
            ("¿Trabajáis con mi proveedor de internet actual?", "Sí. Trabajamos con la conexión que ya tienes y, si hace falta, te ayudamos a hablar con tu operador."),
        ],
    },
]

P = "[PRECIO]"
PACKS = {
    "paginas-web": [
        {"nombre": "Web Inicio", "precio": "524 €", "para": "Para empezar a estar en internet", "items": ["Web de una página con secciones", "Adaptada a móvil", "Formulario y WhatsApp", "Ficha de Google Business", "1 ronda de cambios"]},
        {"nombre": "Web Negocio", "precio": "778 €", "para": "La más elegida por comercios", "popular": True, "items": ["Hasta 6 páginas", "Textos preparados para Google", "Galería o carta de servicios", "Dominio y correo profesional", "2 rondas de cambios", "Mantenimiento 3 meses"]},
        {"nombre": "Web Completa", "precio": "1.002 €", "para": "Para negocios con más contenido", "items": ["Páginas ilimitadas razonables", "Blog para atraer clientes", "Reservas o citas online", "Asistente IA en la web", "3 rondas de cambios", "Mantenimiento 12 meses"]},
    ],
    "tiendas-online": [
        {"nombre": "Tienda Shopify", "precio": "644 €", "para": "Vender rápido con Shopify", "items": ["Tema adaptado a tu marca", "Hasta 30 productos cargados", "Pagos y envíos configurados", "Textos legales de compra", "Formación de uso"]},
        {"nombre": "Tienda Pro", "precio": "A consultar", "para": "Catálogos grandes o con variantes", "popular": True, "items": ["Hasta 150 productos", "Tallas, colores y stock", "Panel de pedidos y clientes", "Bizum y transferencia", "Mantenimiento 3 meses"]},
        {"nombre": "Tienda a medida", "precio": "A consultar", "para": "Tienda + citas, cursos o inventario", "items": ["Desarrollo sin cuota de plataforma", "Reservas de citas o cursos", "Inventario con códigos de barras", "Informes de ventas", "Mantenimiento 12 meses"]},
    ],
    "reels-redes": [
        {"nombre": "Redes Esencial", "precio": "330 €", "sufijo": "plan de 6 meses", "para": "Para empezar con constancia", "items": ["3 reels al mes", "1 carrusel de imágenes al mes", "Plantillas con tu imagen de marca", "18 reels en total"]},
        {"nombre": "Redes Profesional", "precio": "516 €", "sufijo": "plan de 6 meses", "para": "Para crecer en Instagram y TikTok", "popular": True, "items": ["9 reels profesionales al mes", "6 carruseles de imágenes al mes", "Fotos de tu negocio con calidad de estudio", "Perfil optimizado", "54 reels y 36 carruseles en total"]},
        {"nombre": "Redes Premium", "precio": "894 €", "para": "Gestión integral de tus redes", "items": ["9 reels profesionales al mes", "6 carruseles de imágenes al mes", "Gestión de mensajes y comentarios", "Seguimiento y análisis mensual de resultados"]},
    ],
    "ia-negocios": [
        {"nombre": "Asistente IA", "precio": "A consultar", "para": "Responder a clientes 24 h", "items": ["Asistente para web o WhatsApp", "Entrenado con tu información", "Paso a una persona cuando hace falta", "1 mes de ajustes"]},
        {"nombre": "Automatización", "precio": "A consultar", "para": "Quitar trabajo repetitivo", "popular": True, "items": ["Estudio de tus tareas repetitivas", "2 automatizaciones a medida", "Conexión con correo, Excel o tienda", "Formación del equipo"]},
        {"nombre": "IA privada", "precio": "A consultar", "para": "Datos que no salen de tu empresa", "items": ["Modelo de IA en tu propio equipo", "Sin cuotas por uso", "Documentos internos consultables", "Mantenimiento 3 meses"]},
    ],
    "soporte-it": [
        {"nombre": "Diagnóstico RedTI 360°", "precio": "A consultar", "para": "Saber qué falla y por dónde empezar", "items": ["Visita y revisión completa", "Medición de Wi-Fi y velocidad", "Revisión de seguridad básica", "Informe con prioridades"]},
        {"nombre": "Puesta a punto", "precio": "A consultar", "para": "Dejar la red bien montada", "popular": True, "items": ["Diagnóstico incluido", "Ajuste de router y Wi-Fi", "Red de invitados separada", "Copias de seguridad automáticas", "Documentación de la red"]},
        {"nombre": "Mantenimiento", "precio": "A consultar", "mes": True, "para": "Tranquilidad cada mes", "items": ["Soporte remoto", "Revisión mensual", "Actualizaciones y copias vigiladas", "Visitas con precio reducido"]},
    ],
}

PROYECTOS = [
    {
        "nombre": "Uñas Yolman", "tipo": "Tienda online + salón + academia", "img": "unas-yolman.jpg",
        "url": "https://unas-yolman-app.onrender.com",
        "texto": "Web completa para un negocio de uñas que vende productos, reserva citas en el salón y ofrece cursos.",
        "puntos": ["Tienda con carrito y pago con tarjeta, Bizum o transferencia", "Reservas de citas y cursos con horarios reales", "Panel de inventario, pedidos e informes de ventas", "Presencia en Instagram y TikTok"],
    },
    {
        "nombre": "Dissolver", "tipo": "Tienda online de moda", "img": "dissolver.jpg",
        "url": "https://dissolver-app.onrender.com",
        "texto": "Tienda de moda boho y bisutería artesanal con catálogo por tallas y colores y gestión de stock desde un panel propio.",
        "puntos": ["Catálogo con variantes de talla y color", "Inventario con códigos de barras", "Panel de administración de pedidos", "Base de datos en la nube"],
    },
    {
        "nombre": "MayiShop", "tipo": "Tienda Shopify", "img": "mayishop.jpg",
        "url": "https://x0ac4b-eb.myshopify.com",
        "texto": "Tienda en Shopify con productos seleccionados, traducida al español y con pagos activos.",
        "puntos": ["Montaje y personalización en Shopify", "Fichas de producto y fotos", "Pagos con Shopify Payments", "Vídeos de producto para redes"],
    },
    {
        "nombre": "Soluciones Digitales", "tipo": "Tienda de servicios IT + citas", "img": "soluciones-digitales.jpg",
        "url": "", "desarrollo": True,
        "texto": "Tienda de servicios informáticos con reserva de visitas técnicas y panel de gestión.",
        "puntos": ["Catálogo de servicios de redes, seguridad y hardware", "Reserva de visitas técnicas con bloqueo de horario", "Panel de pedidos y citas"],
    },
]

# Equipo: añade más personas copiando la línea (foto en assets/img, 720x900)
EQUIPO = [
    {"nombre": "Yolman Nieves", "cargo": "Ingeniero programador", "foto": "equipo-yolman-nieves.jpg"},
    {"nombre": "Mayerling Gil", "cargo": "Diseñadora gráfica y artista plástica", "foto": "equipo-mayerling-gil.jpg"},
    {"nombre": "Jesús González Noguera", "cargo": "Servicio técnico", "foto": "equipo-jesus-gonzalez.jpg"},]

FAQ_GENERAL = [
    ("¿Cuánto tarda un proyecto?", "Depende de lo que necesites. Antes de empezar te damos por escrito el plazo, lo que incluye y cuántas rondas de cambios tienes."),
    ("¿Cómo se paga?", CONFIG["forma_pago"]),
    ("¿Trabajáis solo en Madrid?", f"Webs, tiendas, redes e IA las hacemos para cualquier parte de España. El servicio técnico presencial es en {CONFIG['zona']}."),
    ("¿Qué necesito tener preparado?", "Tu logo si lo tienes, fotos de tus productos o tu local y una idea de lo que quieres conseguir. Si te falta algo, te ayudamos."),
    ("¿Hay permanencia en el mantenimiento?", "No. Los planes mensuales se pueden dejar avisando con antelación."),
]

# ------------------------------------------------------------ utilidades ---


def t(value: str) -> str:
    """Texto escapado; si es un hueco [ASÍ], lo resalta."""
    value = str(value)
    if value.startswith("[") and value.endswith("]"):
        return f'<span class="hueco">{escape(value)}</span>'
    return escape(value)


def wa_link(text: str = "") -> str:
    num = "".join(c for c in CONFIG["whatsapp"] if c.isdigit())
    if not num:
        return "#contacto"
    q = f"?text={escape(text.replace(' ', '%20'))}" if text else ""
    return f"https://wa.me/{num}{q}"


def wa_visible() -> str:
    n = "".join(c for c in CONFIG["whatsapp"] if c.isdigit())
    return f"{n[2:5]} {n[5:8]} {n[8:]}" if n.startswith("34") and len(n) == 11 else n


def contacto_legal() -> str:
    return CONFIG["correo"] or f"WhatsApp {wa_visible()}"


def contacto_items(labels: bool = False) -> str:
    """Filas de contacto (correo solo si está relleno; teléfono y WhatsApp con enlace)."""
    tel = "".join(c for c in CONFIG["telefono"] if c.isdigit())
    rows = []
    if CONFIG["correo"]:
        rows.append(("Correo", f'<a href="mailto:{escape(CONFIG["correo"])}">{escape(CONFIG["correo"])}</a>'))
    if tel:
        rows.append(("Teléfono", f'<a href="tel:+34{tel}">{escape(CONFIG["telefono"])}</a>'))
    if CONFIG["whatsapp"]:
        rows.append(("WhatsApp", f'<a href="{wa_link("Hola, quiero información")}" target="_blank" rel="noopener">{wa_visible()}</a>'))
    if labels:
        return "".join(f"<li><strong>{k}</strong>{v}</li>" for k, v in rows)
    return "".join(f"<li>{k}: {v}</li>" for k, v in rows)


def nav(root: str, current: str) -> str:
    links = [("index.html", "Inicio"), ("index.html#servicios", "Servicios"), ("index.html#proyectos", "Proyectos"), ("index.html#packs", "Packs"), ("index.html#equipo", "Equipo")]
    items = "".join(
        f'<a href="{root}{h}"{" aria-current=\"page\"" if current == h else ""}>{n}</a>' for h, n in links
    )
    return f"""<header class="header">
  <div class="wrap">
    <a class="logo" href="{root}index.html" aria-label="{escape(CONFIG['nombre'])}, inicio"><span class="logo-mark" aria-hidden="true">ST</span>{escape(CONFIG['nombre'])}</a>
    <button class="menu-btn" aria-expanded="false" aria-controls="menu">Menú</button>
    <nav class="nav" id="menu" aria-label="Principal">{items}<a class="btn btn-primary btn-sm" href="{root}index.html#contacto">Pide tu propuesta</a></nav>
  </div>
</header>"""


def footer(root: str) -> str:
    serv = "".join(f'<li><a href="{root}servicios/{s["slug"]}.html">{escape(s["titulo"])}</a></li>' for s in SERVICIOS)
    redes = ""
    if CONFIG["instagram"]:
        redes += f'<li><a href="{escape(CONFIG["instagram"])}" rel="noopener" target="_blank">Instagram ↗</a></li>'
    if CONFIG["tiktok"]:
        redes += f'<li><a href="{escape(CONFIG["tiktok"])}" rel="noopener" target="_blank">TikTok ↗</a></li>'
    wa = ""
    if CONFIG["whatsapp"]:
        wa = f'<a class="wa-float" href="{wa_link("Hola, quiero información")}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg></a>'
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="logo" href="{root}index.html"><span class="logo-mark" aria-hidden="true">ST</span>{escape(CONFIG['nombre'])}</a>
        <p style="margin-top:14px">Webs, tiendas online, redes, IA y servicio técnico para negocios. {escape(CONFIG['zona'])}.</p>
      </div>
      <div><h4>Servicios</h4><ul>{serv}</ul></div>
      <div><h4>Contacto</h4><ul>{contacto_items()}{redes}</ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year></span> {escape(CONFIG['nombre'])}</span>
      <span><a href="{root}aviso-legal.html">Aviso legal</a> · <a href="{root}privacidad.html">Privacidad</a></span>
    </div>
  </div>
</footer>
{wa}"""


def page(title: str, desc: str, body: str, root: str = "", current: str = "", path: str = "", schema: list | None = None) -> str:
    canon = f'<link rel="canonical" href="https://{CONFIG["dominio"]}/{path}">' if CONFIG["dominio"] else ""
    ld = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (schema or []))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#f5f5f7">
{canon}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%231d1d1f'/%3E%3Ctext x='16' y='21' font-family='Arial' font-weight='700' font-size='13' text-anchor='middle' fill='%23fff'%3EST%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/css/styles.css?v=3">
{ld}
</head>
<body>
<a class="skip" href="#contenido">Saltar al contenido</a>
{nav(root, current)}
<main id="contenido">
{body}
</main>
{footer(root)}
<script src="{root}assets/js/main.js?v=1" defer></script>
</body>
</html>
"""


def pack_cards(slug: str, root: str) -> str:
    out = []
    for p in PACKS[slug]:
        flag = '<span class="flag">Más elegido</span>' if p.get("popular") else ""
        mes = " <small>/mes</small>" if p.get("mes") else ""
        if p.get("sufijo"):
            mes += f" <small>· {escape(p['sufijo'])}</small>"
        desde = ""
        items = "".join(f"<li>{escape(i)}</li>" for i in p["items"])
        out.append(f"""<article class="pack{' popular' if p.get('popular') else ''} reveal">{flag}
  <h3>{escape(p['nombre'])}</h3>
  <p class="for">{escape(p['para'])}</p>
  <p class="price">{desde}{t(p['precio'])}{mes}</p>
  <ul>{items}</ul>
  <a class="btn {'btn-primary' if p.get('popular') else 'btn-ghost'}" href="{root}index.html?servicio={slug}#contacto">Pedir propuesta</a>
</article>""")
    return f'<div class="grid grid-3">{"".join(out)}</div>'


def faq_html(faqs) -> str:
    return '<div class="faq">' + "".join(
        f"<details class=\"reveal\"><summary>{escape(q)}</summary><p>{t(a)}</p></details>" for q, a in faqs
    ) + "</div>"


def faq_schema(faqs) -> dict:
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs if not a.startswith("[")],
    }


def cta(root: str) -> str:
    return f"""<section class="section"><div class="wrap"><div class="cta reveal">
  <div><h2>¿Hablamos de tu proyecto?</h2><p>Te respondemos con una propuesta clara: qué incluye, plazo y precio cerrado.</p></div>
  <a class="btn" href="{root}index.html#contacto">Pide tu propuesta →</a>
</div></div></section>"""


# ---------------------------------------------------------------- páginas ---


def build_index() -> str:
    cards = "".join(
        f"""<article class="card c-{['blue', 'pink', 'yellow', 'lime', 'white'][i % 5]} reveal">
  <div class="icon">{ICONS[s['icono']]}</div>
  <h3>{escape(s['titulo'])}</h3>
  <ul class="tags">{''.join(f'<li>{escape(x)}</li>' for x in s['tags'])}</ul>
  <p>{escape(s['corto'])}</p>
  <a class="more" href="servicios/{s['slug']}.html">Ver servicio →</a>
</article>""" for i, s in enumerate(SERVICIOS)
    )
    cards += """<article class="card c-ink reveal">
  <h3>¿Necesitas varias cosas?</h3>
  <p>Web, redes, IA y técnico en un mismo equipo: un solo interlocutor y una imagen coherente en todas partes.</p>
  <a class="more" href="#contacto">Cuéntanos qué necesitas →</a>
</article>"""

    proyectos = ""
    for p in PROYECTOS:
        img_path = OUT / "assets" / "img" / p["img"]
        shot = (f'<img src="assets/img/{p["img"]}" alt="Captura de la web de {escape(p["nombre"])}" loading="lazy" width="1440" height="900">'
                if img_path.exists() else f'<div class="ph">{escape(p["nombre"])}</div>')
        badge = '<span class="badge">En desarrollo</span>' if p.get("desarrollo") else ""
        link = (f'<a class="btn btn-ghost btn-sm" href="{escape(p["url"])}" target="_blank" rel="noopener">Visitar web ↗</a>'
                if p["url"] else "")
        puntos = "".join(f"<li>{escape(x)}</li>" for x in p["puntos"])
        proyectos += f"""<article class="project reveal">
  <div class="project-shot">{shot}</div>
  <div>
    <p class="kind">{escape(p['tipo'])}</p>
    <h3>{escape(p['nombre'])}{badge}</h3>
    <p>{escape(p['texto'])}</p>
    <ul>{puntos}</ul>
    {link}
  </div>
</article>"""

    tabs = "".join(
        f'<button role="tab" id="tab-{s["slug"]}" aria-controls="panel-{s["slug"]}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{escape(s["titulo"].replace("Servicio técnico de redes y servidores", "Técnico IT"))}</button>'
        for i, s in enumerate(SERVICIOS)
    )
    panels = "".join(
        f'<div class="tab-panel" role="tabpanel" id="panel-{s["slug"]}" aria-labelledby="tab-{s["slug"]}"{"" if i == 0 else " hidden"}>{pack_cards(s["slug"], "")}</div>'
        for i, s in enumerate(SERVICIOS)
    )
    opciones = "".join(f'<option value="{s["slug"]}">{escape(s["titulo"])}</option>' for s in SERVICIOS)
    redes = ""
    if CONFIG["instagram"]:
        redes += f'<li><strong>Instagram</strong><a href="{escape(CONFIG["instagram"])}" target="_blank" rel="noopener">Ver perfil ↗</a></li>'
    equipo = "".join(
        f"""<figure class="member reveal">
  <img src="assets/img/{escape(m['foto'])}" alt="{escape(m['nombre'])}, {escape(m['cargo'].lower())}" loading="lazy" width="720" height="900">
  <figcaption><strong>{escape(m['nombre'])}</strong><span>{escape(m['cargo'])}</span></figcaption>
</figure>""" for m in EQUIPO
    )

    body = f"""
<section class="hero">
  <div class="wrap hero-inner">
    <p class="eyebrow">Agencia tecnológica · {escape(CONFIG['ciudad'])}</p>
    <h1>{escape(CONFIG['lema']).replace('trabaja', '<span>trabaja</span>')}.</h1>
    <p class="hero-lead">Webs, tiendas online, reels, inteligencia artificial y servicio técnico de redes y servidores. Un solo equipo que entiende de diseño y de tecnología.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="#contacto">Pide tu propuesta</a>
      <a class="link-more" href="#proyectos">Ver proyectos <span aria-hidden="true">›</span></a>
    </div>
    <ul class="hero-chips"><li>Precio cerrado por escrito</li><li>Hablas con quien lo hace</li><li>Sin permanencia</li></ul>
  </div>
  <div class="showcase" aria-hidden="true">
    <figure class="win win-left"><div class="win-bar"><i></i><i></i><i></i></div><img src="assets/img/unas-yolman.jpg" alt="" width="1440" height="900"></figure>
    <figure class="win win-right"><div class="win-bar"><i></i><i></i><i></i></div><img src="assets/img/mayishop.jpg" alt="" width="1440" height="900"></figure>
    <figure class="win win-center"><div class="win-bar"><i></i><i></i><i></i></div><img src="assets/img/dissolver.jpg" alt="" width="1440" height="900"></figure>
  </div>
</section>

<section class="section" id="servicios">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Qué hacemos</p>
      <h2>Todo lo digital de tu negocio, en un mismo sitio</h2>
      <p>Desde la web y las redes hasta la IA y la red de tu oficina. Sin tener que coordinar a varios proveedores.</p>
    </div>
    <div class="grid grid-3">{cards}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2>Un proceso claro, sin sorpresas</h2>
      <p>Siempre sabes en qué punto está tu proyecto y qué necesitamos de ti.</p>
    </div>
    <ol class="steps">
      <li class="reveal"><h3>Escuchamos</h3><p>Hablamos de tu negocio, tus clientes y lo que quieres conseguir.</p></li>
      <li class="reveal"><h3>Propuesta por escrito</h3><p>Qué incluye, plazo, rondas de cambios y precio cerrado.</p></li>
      <li class="reveal"><h3>Creamos</h3><p>Diseño, desarrollo, contenido o instalación, a partir de tu marca.</p></li>
      <li class="reveal"><h3>Revisamos contigo</h3><p>Te enseñamos el avance y ajustamos lo necesario.</p></li>
      <li class="reveal"><h3>Publicamos y te formamos</h3><p>Lo dejamos funcionando y te enseñamos a usarlo.</p></li>
    </ol>
  </div>
</section>

<section class="section section-white" id="proyectos">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Proyectos</p>
      <h2>Trabajos reales, funcionando</h2>
      <p>Tiendas, reservas, paneles de gestión y presencia en redes que hemos diseñado y desarrollado.</p>
    </div>
    {proyectos}
  </div>
</section>

<section class="section" id="packs">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Packs</p>
      <h2>Precios claros y lo que incluye cada uno</h2>
      <p>Elige el punto de partida. En la propuesta lo ajustamos a tu negocio y te damos el precio final por escrito.</p>
    </div>
    <div class="tabs" role="tablist" aria-label="Packs por servicio">{tabs}</div>
    {panels}
    <p class="note">Precios sin IVA. Dominio, cuotas de plataformas (por ejemplo Shopify) y publicidad pagada no incluidos salvo que se indique.</p>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Por qué con nosotros</p>
      <h2>Diseño y tecnología en el mismo equipo</h2>
    </div>
    <div class="why">
      <div class="reveal"><h3>Trato directo</h3><p>Hablas con quien diseña tu web y monta tu tecnología, sin intermediarios.</p></div>
      <div class="reveal"><h3>Tecnología de verdad</h3><p>Además de diseño: bases de datos, paneles, IA y redes. Lo que otros subcontratan, lo hacemos nosotros.</p></div>
      <div class="reveal"><h3>Todo es tuyo</h3><p>Dominio, accesos y contenido a tu nombre. Sin ataduras.</p></div>
      <div class="reveal"><h3>Rápido en el móvil</h3><p>Webs ligeras que cargan rápido, porque la mayoría de tus clientes te verán desde el teléfono.</p></div>
    </div>
  </div>
</section>

<section class="section" id="equipo">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Quiénes somos</p>
      <h2>Personas reales detrás de cada proyecto</h2>
      <p>Hablas directamente con quien diseña, programa y mantiene tu tecnología.</p>
    </div>
    <div class="team">{equipo}</div>
  </div>
</section>

<section class="section section-white" id="faq">
  <div class="wrap">
    <div class="section-head reveal"><p class="eyebrow">Preguntas frecuentes</p><h2>Lo que nos suelen preguntar</h2></div>
    {faq_html(FAQ_GENERAL)}
  </div>
</section>

<section class="section section-dark" id="contacto">
  <div class="wrap contact">
    <div class="reveal">
      <p class="eyebrow">Contacto</p>
      <h2>Cuéntanos tu proyecto</h2>
      <p>Escríbenos y te preparamos una propuesta a medida, sin compromiso.</p>
      <ul class="contact-list">
        {contacto_items(True)}
        <li><strong>Zona</strong>{escape(CONFIG['zona'])}</li>
        {redes}
      </ul>
    </div>
    <form class="form reveal" id="form-contacto" data-whatsapp="{escape(CONFIG['whatsapp'])}" novalidate>
      <div class="row">
        <label>Nombre<input name="nombre" autocomplete="name" required></label>
        <label>Negocio<input name="negocio" autocomplete="organization" placeholder="Opcional"></label>
      </div>
      <label>¿Qué necesitas?<select name="servicio">{opciones}<option value="varios">Varias cosas</option></select></label>
      <label>Cuéntanos un poco<textarea name="mensaje" required placeholder="Qué haces, qué te gustaría conseguir, plazos…"></textarea></label>
      <label class="legal"><input type="checkbox" name="privacidad" value="1"> He leído la <a href="privacidad.html">política de privacidad</a>.</label>
      <p class="form-msg" role="alert" aria-live="polite"></p>
      <button class="btn btn-primary" type="submit">Enviar por WhatsApp →</button>
    </form>
  </div>
</section>
"""
    schema = [
        {
            "@context": "https://schema.org", "@type": "ProfessionalService", "name": CONFIG["nombre"],
            "description": "Páginas web, tiendas online, redes sociales, inteligencia artificial y servicio técnico de redes y servidores.",
            "areaServed": CONFIG["zona"], "address": {"@type": "PostalAddress", "addressLocality": CONFIG["ciudad"], "addressCountry": "ES"},
            **({"url": f"https://{CONFIG['dominio']}/"} if CONFIG["dominio"] else {}),
        },
        faq_schema(FAQ_GENERAL),
    ]
    return page(
        f"{CONFIG['nombre']} | Webs, tiendas online, IA y servicio técnico en {CONFIG['ciudad']}",
        "Diseñamos páginas web y tiendas online, creamos reels para redes, montamos asistentes de IA y damos servicio técnico de redes y servidores a negocios en Madrid.",
        body, root="", current="index.html", path="", schema=schema,
    )


def build_servicio(s: dict) -> str:
    otros = "".join(f'<a href="{o["slug"]}.html">{escape(o["titulo"])}</a>' for o in SERVICIOS if o["slug"] != s["slug"])
    includes = "".join(f'<li class="reveal">{escape(x)}</li>' for x in s["incluye"])
    body = f"""
<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="../index.html">Inicio</a> / <a href="../index.html#servicios">Servicios</a> / {escape(s['titulo'])}</p>
    <h1>{escape(s['titulo'])}</h1>
    <p>{escape(s['intro'])}</p>
    <div class="hero-actions"><a class="btn btn-primary" href="../index.html?servicio={s['slug']}#contacto">Pide tu propuesta →</a><a class="btn btn-ghost" href="#packs">Ver packs</a></div>
  </div>
</section>
<section class="section section-white">
  <div class="wrap">
    <div class="section-head reveal"><p class="eyebrow">Qué incluye</p><h2>Lo que hacemos por ti</h2></div>
    <ul class="includes">{includes}</ul>
  </div>
</section>
<section class="section" id="packs">
  <div class="wrap">
    <div class="section-head reveal"><p class="eyebrow">Packs</p><h2>Elige tu punto de partida</h2></div>
    {pack_cards(s['slug'], '../')}
    <p class="note">Precios sin IVA. El precio final se confirma por escrito en la propuesta.</p>
  </div>
</section>
<section class="section section-white">
  <div class="wrap">
    <div class="section-head reveal"><p class="eyebrow">Preguntas frecuentes</p><h2>Dudas sobre {escape(s['titulo'].lower())}</h2></div>
    {faq_html(s['faqs'])}
    <h3 style="margin-top:48px">Otros servicios</h3>
    <div class="related">{otros}</div>
  </div>
</section>
{cta('../')}
"""
    return page(f"{s['seo']} | {CONFIG['nombre']}", s["corto"], body, root="../", path=f"servicios/{s['slug']}.html", schema=[faq_schema(s["faqs"])])


def build_legal(kind: str) -> str:
    c = CONFIG
    if kind == "aviso-legal":
        title, html = "Aviso legal", f"""
<p>En cumplimiento de la Ley 34/2002, de Servicios de la Sociedad de la Información (LSSI-CE), se informa:</p>
<ul><li>Titular: {t(c['titular_legal'])}</li><li>NIF: {t(c['nif'])}</li><li>Domicilio: {t(c['direccion_legal'])}</li><li>Contacto: {t(contacto_legal())}</li></ul>
<h2>Uso del sitio</h2><p>El acceso a esta web es gratuito. Quien la usa se compromete a hacerlo de forma lícita.</p>
<h2>Propiedad intelectual</h2><p>Los textos, diseños y código de esta web pertenecen a su titular. Las capturas de proyectos se muestran con permiso de sus propietarios.</p>"""
    else:
        title, html = "Política de privacidad", f"""
<p>Responsable del tratamiento: {t(c['titular_legal'])} ({t(c['nif'])}), contacto: {t(contacto_legal())}.</p>
<h2>Qué datos tratamos y para qué</h2><p>Los datos que nos envías por el formulario, WhatsApp o correo (nombre, negocio, mensaje y teléfono) se usan solo para responderte y preparar tu propuesta.</p>
<h2>Base legal</h2><p>Tu consentimiento al enviarnos el mensaje y, si contratas, la ejecución del contrato.</p>
<h2>Conservación</h2><p>Mientras dure la relación y los plazos legales que correspondan.</p>
<h2>Con quién se comparten</h2><p>No cedemos tus datos a terceros. El formulario abre WhatsApp, que trata los datos según su propia política.</p>
<h2>Tus derechos</h2><p>Puedes pedir acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a {t(contacto_legal())}. También puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>"""
    body = f'<section class="page-hero"><div class="wrap"><p class="crumbs"><a href="index.html">Inicio</a> / {title}</p><h1>{title}</h1></div></section><section class="section section-white"><div class="wrap legal-text">{html}</div></section>'
    return page(f"{title} | {CONFIG['nombre']}", f"{title} de {CONFIG['nombre']}.", body, path=f"{kind}.html")


def main() -> None:
    (OUT / "servicios").mkdir(exist_ok=True)
    files = {"index.html": build_index(), "aviso-legal.html": build_legal("aviso-legal"), "privacidad.html": build_legal("privacidad")}
    for s in SERVICIOS:
        files[f"servicios/{s['slug']}.html"] = build_servicio(s)
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
    if CONFIG["dominio"]:
        urls = "".join(f"<url><loc>https://{CONFIG['dominio']}/{n.replace('index.html', '')}</loc></url>" for n in files)
        (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
        (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: https://{CONFIG['dominio']}/sitemap.xml\n", encoding="utf-8")
    huecos = sum(c.count('class="hueco"') for c in files.values())
    print(f"{len(files)} páginas generadas. Huecos por rellenar: {huecos}")


if __name__ == "__main__":
    main()
