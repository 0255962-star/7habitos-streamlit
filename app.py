import streamlit as st
from pathlib import Path
import pandas as pd

# ---------- CONFIGURACIÓN GENERAL DE LA PÁGINA ----------
st.set_page_config(
    page_title="7 Hábitos - Proyecto Final",
    page_icon="📘",
    layout="wide"
)

# ---------- ESTILOS PERSONALIZADOS ----------
CUSTOM_CSS = """
<style>
/* Fondo suave */
.main {
    background: linear-gradient(135deg, #f9fafb 0%, #e0f4ff 40%, #fef3c7 100%);
}

/* Contenedor tipo tarjeta */
.habit-card {
    background-color: #ffffffcc;
    padding: 1.7rem;
    border-radius: 1.3rem;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
    margin-bottom: 2rem;
    border: 1px solid rgba(148, 163, 184, 0.2);
}

/* Badges */
.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    background: #e0f2fe;
    color: #0369a1;
    margin-right: 0.4rem;
}

/* Títulos */
h1, h2, h3 {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Línea de tiempo */
.timeline-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #2563eb;
    display: inline-block;
    margin-right: 8px;
}

/* Pequeño resaltado */
.highlight {
    background: #fef9c3;
    padding: 0.15rem 0.4rem;
    border-radius: 0.4rem;
}

/* Contenedor de métrica */
.metric-box {
    background: #0f172a;
    color: white;
    padding: 1rem;
    border-radius: 1rem;
    text-align: center;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


# ---------- HELPERS PARA IMAGEN Y AUDIO ----------
def show_image(image_name: str):
    """Muestra una imagen si existe; si no, un mensaje guía."""
    img_path = Path("images") / image_name
    if img_path.is_file():
        st.image(str(img_path), use_column_width=True)
    else:
        st.info("🖼️ Aquí puedes agregar una imagen relacionada con este hábito. "
                f"Crea `images/{image_name}` en tu repositorio.")


def show_audio(audio_name: str):
    """Muestra un audio si existe; si no, un mensaje guía."""
    audio_path = Path("audio") / audio_name
    if audio_path.is_file():
        st.audio(str(audio_path))
    else:
        st.caption("🎙️ (Espacio para un breve audio/voice note del equipo sobre este hábito)")


# ---------- CONTENIDO DE LOS HÁBITOS (TEXTO DEL EQUIPO) ----------
habits = {
    1: {
        "title": "Ser proactivo",
        "icon": "🔥",
        "image": "habito1_proactivo.png",
        "audio": "habito1_proactivo.mp3",
        "explicacion": (
            "Ser proactivo es asumir la responsabilidad de lo que hacemos y decidir conscientemente "
            "cómo actuar frente a cada situación. Las personas proactivas no esperan que alguien más "
            "resuelva sus problemas; toman la iniciativa y buscan soluciones sin excusas. "
            "Este hábito significa elegir una actitud positiva incluso ante las dificultades."
        ),
        "ejemplo": (
            "En las primeras semanas del proyecto, el grupo tuvo dificultades para coordinar horarios. "
            "Juan Pablo decidió no esperar a que el profesor interviniera: creó un grupo en línea para "
            "organizar las reuniones y propuso un calendario semanal. Su iniciativa permitió que el "
            "equipo retomara el ritmo de trabajo y mejorara la comunicación."
        ),
        "conexion": (
            "Este hábito está directamente relacionado con la responsabilidad, la autogestión y "
            "el liderazgo proactivo. En el ámbito gerencial, una persona proactiva detecta problemas "
            "antes de que se agraven y actúa sin esperar órdenes."
        ),
        "keywords": ["Responsabilidad", "Iniciativa", "Autogestión"]
    },
    2: {
        "title": "Comenzar con un fin en mente",
        "icon": "🎯",
        "image": "habito2_fin_en_mente.png",
        "audio": "habito2_fin_en_mente.mp3",
        "explicacion": (
            "Implica tener una visión clara de hacia dónde se quiere llegar. Significa planificar con "
            "base en metas a largo plazo y orientar las acciones diarias hacia ese propósito. Quien "
            "“comienza con un fin en mente” sabe qué quiere lograr y actúa con enfoque."
        ),
        "ejemplo": (
            "Desde el inicio, Alejandro propuso que el objetivo del grupo fuera entregar un proyecto "
            "que no solo cumpliera los requisitos, sino que destacara por su creatividad. Para lograrlo, "
            "elaboró un esquema de trabajo que incluía metas semanales, revisión de avances y roles "
            "definidos. Esta visión ayudó al equipo a mantenerse enfocado hasta el final."
        ),
        "conexion": (
            "Desarrolla la planeación estratégica, la visión a futuro y la orientación a resultados, "
            "esenciales en cualquier líder o gerente que busque dirigir proyectos con éxito."
        ),
        "keywords": ["Visión", "Planeación estratégica", "Resultados"]
    },
    3: {
        "title": "Poner primero lo primero",
        "icon": "⏱️",
        "image": "habito3_primero_lo_primero.png",
        "audio": "habito3_primero_lo_primero.mp3",
        "explicacion": (
            "Este hábito trata sobre priorizar lo más importante en lugar de distraerse con lo urgente "
            "o lo trivial. Se basa en la gestión del tiempo y la disciplina personal. Implica enfocarse "
            "en actividades que aporten verdadero valor al objetivo final."
        ),
        "ejemplo": (
            "Cuando se acercaba la fecha de entrega, Mateo notó que algunos querían dedicar tiempo a "
            "detalles visuales antes de terminar la investigación. Él propuso centrarse primero en "
            "completar el contenido principal y luego perfeccionar la presentación. Esa decisión permitió "
            "cumplir los plazos sin descuidar la calidad."
        ),
        "conexion": (
            "Refuerza la organización, la gestión del tiempo y la eficiencia en la toma de decisiones, "
            "competencias clave para dirigir proyectos y equipos de trabajo."
        ),
        "keywords": ["Prioridades", "Gestión del tiempo", "Disciplina"]
    },
    4: {
        "title": "Pensar en ganar/ganar",
        "icon": "🤝",
        "image": "habito4_ganar_ganar.png",
        "audio": "habito4_ganar_ganar.mp3",
        "explicacion": (
            "Consiste en buscar soluciones donde todos los involucrados salgan beneficiados. No se trata "
            "de competir, sino de colaborar con una mentalidad de abundancia: creer que el éxito de uno "
            "no significa el fracaso del otro."
        ),
        "ejemplo": (
            "En un momento del proyecto, surgió un desacuerdo sobre quién haría la presentación final. "
            "Juan Pablo sugirió que cada uno presentara una parte según su especialidad: Alejandro la "
            "introducción, él la parte técnica y Mateo las conclusiones. Así todos participaron y se "
            "sintieron valorados."
        ),
        "conexion": (
            "Está vinculado con la negociación efectiva, la empatía y la gestión colaborativa, cualidades "
            "esenciales para mantener relaciones laborales equilibradas y equipos motivados."
        ),
        "keywords": ["Colaboración", "Negociación", "Empatía"]
    },
    5: {
        "title": "Buscar primero entender, luego ser entendido",
        "icon": "👂",
        "image": "habito5_entender.png",
        "audio": "habito5_entender.mp3",
        "explicacion": (
            "Este hábito enseña que antes de expresar tu punto de vista, debes escuchar realmente a los "
            "demás. La escucha empática ayuda a construir confianza y comprensión mutua. Solo cuando "
            "entendemos las perspectivas de los demás podemos comunicar las nuestras de manera efectiva."
        ),
        "ejemplo": (
            "Durante una reunión, Alejandro y Mateo tenían opiniones opuestas sobre el enfoque del trabajo. "
            "Juan Pablo propuso que cada uno explicara su punto sin interrupciones y luego buscarían puntos "
            "en común. Gracias a esa escucha activa, lograron integrar ambas ideas en una propuesta más completa."
        ),
        "conexion": (
            "Fortalece la comunicación empática, la resolución de conflictos y la inteligencia emocional, "
            "competencias indispensables para liderar equipos diversos y mantener una buena convivencia laboral."
        ),
        "keywords": ["Escucha", "Empatía", "Resolución de conflictos"]
    },
    6: {
        "title": "Sinergizar",
        "icon": "🧩",
        "image": "habito6_sinergia.png",
        "audio": "habito6_sinergia.mp3",
        "explicacion": (
            "La sinergia se produce cuando las fortalezas individuales se combinan para generar resultados "
            "que nadie podría lograr solo. Supone valorar las diferencias, respetar los distintos puntos "
            "de vista y trabajar de forma complementaria."
        ),
        "ejemplo": (
            "Cada miembro del grupo aportó algo distinto: Juan Pablo se destacó en la coordinación y liderazgo, "
            "Alejandro en la planeación y diseño, y Mateo en la redacción y análisis. Al unir esas habilidades, "
            "el grupo logró un proyecto equilibrado, innovador y bien presentado."
        ),
        "conexion": (
            "Promueve el trabajo en equipo, la diversidad de pensamiento y la creatividad colectiva, "
            "competencias esenciales para generar innovación en cualquier organización."
        ),
        "keywords": ["Trabajo en equipo", "Diversidad", "Creatividad"]
    },
    7: {
        "title": "Afilar la sierra",
        "icon": "🪵",
        "image": "habito7_afilar_sierra.png",
        "audio": "habito7_afilar_sierra.mp3",
        "explicacion": (
            "Significa dedicar tiempo al autocuidado y la mejora continua en cuatro áreas: cuerpo, mente, "
            "corazón y espíritu. Una persona que no se renueva se desgasta y pierde motivación. "
            "“Afilar la sierra” es invertir en ti mismo para mantener tu energía y equilibrio."
        ),
        "ejemplo": (
            "Después de la entrega del proyecto, el grupo decidió reunirse para reflexionar sobre lo aprendido "
            "y compartir sugerencias para futuros trabajos. También planearon una actividad recreativa juntos. "
            "Este descanso y retroalimentación fortaleció su relación y los preparó mejor para nuevos retos."
        ),
        "conexion": (
            "Refuerza la resiliencia, la adaptabilidad y el aprendizaje continuo. Un buen líder no solo busca "
            "resultados, sino también el bienestar y el desarrollo personal del equipo."
        ),
        "keywords": ["Autocuidado", "Resiliencia", "Aprendizaje continuo"]
    }
}

texto_evidencia = (
    "A lo largo del proceso, el equipo formado por Juan Pablo, Alejandro y Mateo mostró "
    "una evolución notable:\n\n"
    "- **Inicio:** Existía desorganización y dificultad para coordinar tiempos.\n"
    "- **Durante el proceso:** Aplicaron los hábitos de Covey para mejorar su comunicación y productividad. "
    "Juan Pablo lideró la organización (Hábito 1), Alejandro aportó visión y planeación (Hábito 2), y "
    "Mateo se destacó por su enfoque y constancia (Hábito 3).\n"
    "- **Resultados:** Lograron sinergia real (Hábito 6) y aprendieron a escucharse mutuamente (Hábito 5).\n"
    "- **Crecimiento:** El grupo pasó de ser un conjunto de individuos a un equipo cohesionado, con metas claras, "
    "roles definidos y un alto nivel de compromiso."
)


# ---------- FUNCIÓN PARA MOSTRAR UN HÁBITO ----------
def render_habit(habit_number: int):
    data = habits[habit_number]
    st.markdown(
        f"<div class='habit-card'>",
        unsafe_allow_html=True
    )

    cols = st.columns([2, 1])
    with cols[0]:
        st.markdown(
            f"### {data['icon']} Hábito {habit_number}: {data['title']}"
        )
        st.markdown(
            "<span class='badge'>Explicación</span> "
            "<span class='badge'>Ejemplo del equipo</span> "
            "<span class='badge'>Habilidades gerenciales</span>",
            unsafe_allow_html=True
        )
        st.write("")
        st.markdown(f"**🌟 Explicación**")
        st.write(data["explicacion"])

        with st.expander("📌 Ejemplo del equipo", expanded=True):
            st.write(data["ejemplo"])

        with st.expander("🏢 Conexión con habilidades gerenciales", expanded=False):
            st.write(data["conexion"])

        st.write("")
        st.markdown("**🔑 Palabras clave del hábito:**")
        st.write(", ".join([f"`{k}`" for k in data["keywords"]]))

        st.write("")
        st.markdown("**💭 Reflexión personal rápida**")
        st.text_area(
            "¿Cómo has aplicado tú este hábito en tu vida o en otro proyecto?",
            key=f"reflexion_{habit_number}",
            placeholder="Escribe aquí tu reflexión (no se guarda, es solo para que pienses mientras exploras la página)."
        )

    with cols[1]:
        st.markdown("#### 🎨 Imagen del hábito")
        show_image(data["image"])

        st.markdown("#### 🎧 Voz del equipo")
        show_audio(data["audio"])

        st.markdown("#### 📲 Idea para recurso extra")
        st.caption(
            "👉 Aquí podrías añadir un código QR que lleve a un meme, un reel corto o una foto del equipo "
            "aplicando este hábito."
        )

    st.markdown("</div>", unsafe_allow_html=True)


# ---------- SECCIÓN INICIO ----------
def render_home():
    col1, col2 = st.columns([2.2, 1.2])
    with col1:
        st.title("📘 7 Hábitos de la Gente Altamente Efectiva")
        st.subheader("Proyecto final – Opción B: Recurso digital interactivo")

        st.markdown(
            "Esta página muestra cómo el equipo **Juan Pablo – Alejandro – Mateo** "
            "creció durante el semestre aplicando los 7 hábitos de Stephen Covey. "
            "Cada sección combina texto, imágenes y espacios de reflexión para conectar "
            "los hábitos con el liderazgo y la gestión en la vida real."
        )

        st.markdown(
            "<span class='highlight'>Explora cada hábito desde el menú lateral, escucha las voces del equipo y "
            "evalúa qué tanto lo aplicas tú también.</span>",
            unsafe_allow_html=True
        )

        st.write("")
        st.markdown("### 🧭 Mapa rápido de la página")
        st.markdown(
            "- **Inicio:** visión general del proyecto.\n"
            "- **Hábitos 1–7:** explicación, ejemplo del equipo, conexión gerencial e imágenes.\n"
            "- **Evidencia de colaboración:** resumen de cómo evolucionó el equipo.\n"
            "- **Autoevaluación:** herramienta interactiva para valorar tus propios hábitos."
        )

    with col2:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("#### 🔍 Datos del proyecto")
        m1, m2, m3 = st.columns(3)
        m1.metric("Miembros", "3", "equipo")
        m2.metric("Hábitos", "7")
        m3.metric("Formato", "Web / Streamlit")
        st.write("---")
        st.caption("Recurso creado como entrega final del curso para conectar los hábitos con habilidades gerenciales.")
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("### 📅 Línea de tiempo del crecimiento del equipo")
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown("**Semana 1**")
        st.markdown("<span class='timeline-dot'></span> Desorganización inicial", unsafe_allow_html=True)
    with t2:
        st.markdown("**Semana 4**")
        st.markdown("<span class='timeline-dot'></span> Aplican hábitos 1–3", unsafe_allow_html=True)
    with t3:
        st.markdown("**Semana 8**")
        st.markdown("<span class='timeline-dot'></span> Mejor comunicación (hábitos 4–5)", unsafe_allow_html=True)
    with t4:
        st.markdown("**Semana 12**")
        st.markdown("<span class='timeline-dot'></span> Sinergia y cierre del proyecto", unsafe_allow_html=True)

    st.write("")
    st.markdown("### 🧠 ¿Qué esperas aprender aquí?")
    st.write(
        "- Entender cada hábito con ejemplos reales del equipo.\n"
        "- Ver cómo se conectan con habilidades de liderazgo y gestión.\n"
        "- Reflexionar sobre tu propia forma de trabajar en equipo."
    )


# ---------- SECCIÓN EVIDENCIA DE COLABORACIÓN ----------
def render_evidence():
    st.markdown("<div class='habit-card'>", unsafe_allow_html=True)
    st.markdown("## 🤝 Evidencia de colaboración y crecimiento del equipo")
    st.write(texto_evidencia)
    st.write("")
    st.markdown("### 📸 Momento favorito del equipo")
    st.caption(
        "Aquí puedes añadir una imagen grupal del equipo al terminar el proyecto "
        "(por ejemplo, `images/equipo_final.png`)."
    )
    show_image("equipo_final.png")
    st.markdown("</div>", unsafe_allow_html=True)


# ---------- SECCIÓN AUTOEVALUACIÓN INTERACTIVA ----------
def render_self_assessment():
    st.markdown("<div class='habit-card'>", unsafe_allow_html=True)
    st.markdown("## 📊 Autoevaluación de hábitos")

    st.write(
        "Mueve los sliders para evaluar qué tanto aplicas cada hábito en tu vida diaria "
        "(1 = casi nunca, 5 = casi siempre)."
    )

    ratings = {}
    for i in range(1, 8):
        ratings[f"Hábito {i}"] = st.slider(
            f"{i}. {habits[i]['title']}",
            min_value=1,
            max_value=5,
            value=3,
            key=f"slider_{i}"
        )

    st.write("")
    st.markdown("### 🔍 Tu perfil de hábitos")

    df = pd.DataFrame({
        "Hábito": list(ratings.keys()),
        "Nivel de aplicación": list(ratings.values())
    }).set_index("Hábito")

    st.bar_chart(df)

    st.write("")
    st.markdown("### ✏️ Resumen personal")
    st.text_area(
        "Escribe en pocas líneas: ¿qué hábito dominas y cuál quieres fortalecer a partir de ahora?",
        key="resumen_personal"
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ---------- SIDEBAR Y ENRUTAMIENTO ----------
def main():
    st.sidebar.title("📚 Navegación")
    section = st.sidebar.radio(
        "Elige una sección:",
        (
            "Inicio",
            "Hábito 1",
            "Hábito 2",
            "Hábito 3",
            "Hábito 4",
            "Hábito 5",
            "Hábito 6",
            "Hábito 7",
            "Evidencia de colaboración",
            "Autoevaluación"
        )
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Equipo:** Juan Pablo · Alejandro · Mateo")
    st.sidebar.caption("Recurso creado para mostrar crecimiento como futuros líderes.")

    if section == "Inicio":
        render_home()
    elif section.startswith("Hábito"):
        num = int(section.split(" ")[1])
        render_habit(num)
    elif section == "Evidencia de colaboración":
        render_evidence()
    elif section == "Autoevaluación":
        render_self_assessment()


if __name__ == "__main__":
    main()
