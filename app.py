import streamlit as st
from pathlib import Path
import pandas as pd

# ---------------- GENERAL CONFIGURATION ----------------
st.set_page_config(
    page_title="7 Habits - Final Project",
    page_icon="📘",
    layout="wide"
)

# ---------------- CSS STYLES ----------------
CUSTOM_CSS = """
<style>
.main {
    background: linear-gradient(135deg, #f9fafb 0%, #e0f4ff 40%, #fef3c7 100%);
}

.habit-card {
    background-color: #ffffffcc;
    padding: 1.7rem;
    border-radius: 1.3rem;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.12);
    margin-bottom: 2rem;
    border: 1px solid rgba(148, 163, 184, 0.2);
}

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

h1, h2, h3 {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.timeline-dot {
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #2563eb;
    display: inline-block;
    margin-right: 8px;
}

.highlight {
    background: #fef9c3;
    padding: 0.15rem 0.4rem;
    border-radius: 0.4rem;
}

.metric-box {
    background: #0f172a;
    color: white;
    padding: 1rem;
    border-radius: 1rem;
    text-align: center;
}

.sticker {
    background: #f1f5f9;
    border-radius: 0.8rem;
    padding: 0.6rem 0.8rem;
    font-size: 0.8rem;
    border: 1px dashed #cbd5f5;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------- HELPERS ----------------
def show_image(image_name: str):
    """Display an image from the same folder as app.py."""
    img_path = Path(image_name)
    if img_path.is_file():
        st.image(str(img_path), use_column_width=True)
    else:
        st.info(f"🖼️ Upload `{image_name}` to the root of the repo to display it here.")


def show_audio(audio_name: str):
    """Display an audio player for a file from the same folder as app.py."""
    audio_path = Path(audio_name)
    if audio_path.is_file():
        st.audio(str(audio_path))
    else:
        st.info(f"🎧 Upload `{audio_name}` to the root of the repo to play it here.")


# ---------------- HABITS CONTENT ----------------
habits = {
    1: {
        "title": "Be Proactive",
        "icon": "🔥",
        "image": "habito1_proactivo.png",
        "explicacion": (
            "Being proactive means taking responsibility for what we do and consciously deciding how "
            "to act in each situation. Proactive people do not wait for someone else to solve their "
            "problems; they take initiative and look for solutions without excuses."
        ),
        "ejemplo": (
            "During the first weeks of the project, the team struggled to coordinate schedules. "
            "Juan Pablo created an online group and proposed a weekly calendar so everyone could "
            "organize meetings more easily and keep the project moving."
        ),
        "conexion": (
            "This habit is related to responsibility, self-management, and proactive leadership. "
            "In management, being proactive means detecting problems early and acting without waiting "
            "for someone else to give the order."
        ),
        "keywords": ["Responsibility", "Initiative", "Self-management"]
    },
    2: {
        "title": "Begin With the End in Mind",
        "icon": "🎯",
        "image": "habito2_fin_en_mente.png",
        "explicacion": (
            "This habit means having a clear vision of where you want to go. It implies planning based on "
            "long-term goals and aligning daily actions with that purpose."
        ),
        "ejemplo": (
            "From the beginning, Alejandro suggested that the goal of the group was to deliver a project "
            "that not only met the requirements but also stood out for its creativity. He proposed weekly "
            "goals, progress reviews, and clear roles."
        ),
        "conexion": (
            "It develops strategic planning, future vision, and results orientation—essential skills for "
            "any leader or manager who wants to guide projects successfully."
        ),
        "keywords": ["Vision", "Strategic planning", "Results"]
    },
    3: {
        "title": "Put First Things First",
        "icon": "⏱️",
        "image": "habito3_primero_lo_primero.png",
        "explicacion": (
            "This habit is about prioritizing what is most important instead of getting distracted by what is "
            "urgent or trivial. It is based on time management and personal discipline."
        ),
        "ejemplo": (
            "As the deadline approached, some teammates wanted to focus on visual details before finishing the "
            "research. Mateo suggested completing the main content first and then refining the slides, which "
            "allowed the team to deliver on time without losing quality."
        ),
        "conexion": (
            "It reinforces organization, time management, and efficiency in decision-making—key skills for "
            "leading projects and work teams."
        ),
        "keywords": ["Priorities", "Time management", "Discipline"]
    },
    4: {
        "title": "Think Win–Win",
        "icon": "🤝",
        "image": "habito4_ganar_ganar.png",
        "explicacion": (
            "Think Win–Win means seeking solutions where everyone involved benefits. It is not about competing "
            "against others but collaborating with an abundance mindset."
        ),
        "ejemplo": (
            "There was a disagreement about who should give the final presentation. Juan Pablo suggested that "
            "each member present the part that matched their strengths: Alejandro the introduction, Juan Pablo "
            "the technical section, and Mateo the conclusions."
        ),
        "conexion": (
            "This habit is connected to negotiation, empathy, and collaborative management, which are essential "
            "for maintaining healthy professional relationships and motivated teams."
        ),
        "keywords": ["Collaboration", "Negotiation", "Empathy"]
    },
    5: {
        "title": "Seek First to Understand, Then to Be Understood",
        "icon": "👂",
        "image": "habito5_entender.png",
        "explicacion": (
            "This habit teaches us to listen carefully before trying to explain our own point of view. "
            "Empathic listening builds trust and mutual understanding."
        ),
        "ejemplo": (
            "Alejandro and Mateo had different ideas about the focus of the project. Juan Pablo proposed that "
            "each of them explain their view without interruptions. After listening, they combined the best "
            "parts of both ideas into a stronger final concept."
        ),
        "conexion": (
            "It strengthens empathic communication, conflict resolution, and emotional intelligence—key "
            "competencies for leading diverse teams."
        ),
        "keywords": ["Listening", "Empathy", "Conflict resolution"]
    },
    6: {
        "title": "Synergize",
        "icon": "🧩",
        "image": "habito6_sinergia.png",
        "explicacion": (
            "Synergy happens when individual strengths are combined to produce results that no one could achieve "
            "alone. It means valuing differences and working in a complementary way."
        ),
        "ejemplo": (
            "Juan Pablo focused on coordination and leadership, Alejandro on planning and design, and Mateo on "
            "writing and analysis. By combining their strengths, they delivered a balanced and creative project."
        ),
        "conexion": (
            "Synergy promotes teamwork, diversity of thought, and collective creativity—essential ingredients "
            "for innovation in any organization."
        ),
        "keywords": ["Teamwork", "Diversity", "Creativity"]
    },
    7: {
        "title": "Sharpen the Saw",
        "icon": "🪵",
        "image": "habito7_afilar_sierra.png",
        "explicacion": (
            "Sharpening the saw means taking time for self-care and continuous improvement in body, mind, "
            "heart, and spirit. Without renewal, people burn out and lose motivation."
        ),
        "ejemplo": (
            "After finishing the project, the group met to reflect on what they had learned and to plan a small "
            "recreational activity together. That pause helped them process the experience and recover energy."
        ),
        "conexion": (
            "This habit reinforces resilience, adaptability, and continuous learning. Good leaders care about "
            "results and about the well-being of their teams."
        ),
        "keywords": ["Self-care", "Resilience", "Continuous learning"]
    }
}

texto_evidencia = """
Throughout the project, the team formed by **Juan Pablo, Alejandro, and Mateo** showed remarkable growth:

- **Beginning:** There was disorganization and difficulty coordinating schedules.
- **During the process:** They applied Covey's habits to improve communication and productivity. Juan Pablo led the organization (Habit 1), Alejandro provided vision and planning (Habit 2), and Mateo stood out for his focus and consistency (Habit 3).
- **Results:** They achieved real synergy (Habit 6) and learned to truly listen to each other (Habit 5).
- **Growth:** The group moved from being a set of individuals to a cohesive team with clear goals, defined roles, and a high level of commitment.
"""

# ---------------- RENDER HABIT ----------------
def render_habit(habit_number: int):
    data = habits[habit_number]
    st.markdown("<div class='habit-card'>", unsafe_allow_html=True)

    cols = st.columns([2, 1])
    with cols[0]:
        st.markdown(f"### {data['icon']} Habit {habit_number}: {data['title']}")
        st.markdown(
            "<span class='badge'>Explanation</span> "
            "<span class='badge'>Team example</span> "
            "<span class='badge'>Managerial skills</span>",
            unsafe_allow_html=True
        )

        st.write("")
        st.markdown("**🌟 Explanation**")
        st.write(data["explicacion"])

        with st.expander("📌 Team example", expanded=True):
            st.write(data["ejemplo"])

        with st.expander("🏢 Connection with managerial skills", expanded=False):
            st.write(data["conexion"])

        st.write("")
        st.markdown("**🔑 Key words for this habit:**")
        st.write(", ".join([f"`{k}`" for k in data["keywords"]]))

        st.write("")
        st.markdown("**💭 Quick personal reflection**")
        st.text_area(
            "How have you applied this habit in your own life or in another project?",
            key=f"reflexion_{habit_number}",
            placeholder="Write your reflection here (it is not saved; it is just for you while exploring the page)."
        )

    with cols[1]:
        st.markdown("#### 🎨 Habit image")
        show_image(data["image"])

        st.write("")
        st.markdown("#### 🎧 Habit audio")
        audio_filename = f"audiohabito{habit_number}.m4a"
        show_audio(audio_filename)
        st.caption(
            "Short audio reflection about how this habit has helped us grow and what we have learned from it."
        )

        st.write("")
        st.markdown("#### 💡 Quick tip")
        st.markdown(
            "<div class='sticker'>Think about a recent situation in your team where this habit made a "
            "difference. What would have happened if it had not been applied?</div>",
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- HOME ----------------
def render_home():
    col1, col2 = st.columns([2.2, 1.2])
    with col1:
        st.title("📘 The 7 Habits of Highly Effective People")
        st.subheader("Final project – Option B: Interactive digital resource")

        st.markdown(
            "This page shows how the team **Juan Pablo – Alejandro – Mateo** "
            "grew over the semester by applying Stephen Covey's 7 habits. "
            "Each section combines text, images, audio, and reflection spaces to connect "
            "the habits with leadership and management in real life."
        )

        st.markdown(
            "<span class='highlight'>Explore each habit using the sidebar, listen to the short audios, "
            "and evaluate how much you apply these habits yourself.</span>",
            unsafe_allow_html=True
        )

        st.write("")
        st.markdown("### 🧭 Quick map of the page")
        st.markdown(
            "- **Home:** general overview of the project.\n"
            "- **Habits 1–7:** explanation, team example, managerial connection, image, and audio.\n"
            "- **Collaboration evidence:** summary of how the team evolved.\n"
            "- **Self-assessment:** interactive tool to rate your own habits."
        )

    with col2:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("#### 🔍 Project facts")
        m1, m2, m3 = st.columns(3)
        m1.metric("Members", "3", "team")
        m2.metric("Habits", "7")
        m3.metric("Format", "Web / Streamlit")
        st.write("---")
        st.caption(
            "Digital resource created as the final course deliverable to connect the 7 habits with managerial skills."
        )
        st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.markdown("### 📅 Team growth timeline")
    t1, t2, t3, t4 = st.columns(4)
    with t1:
        st.markdown("**Week 1**")
        st.markdown("<span class='timeline-dot'></span> Initial disorganization", unsafe_allow_html=True)
    with t2:
        st.markdown("**Week 4**")
        st.markdown("<span class='timeline-dot'></span> Habits 1–3 in action", unsafe_allow_html=True)
    with t3:
        st.markdown("**Week 8**")
        st.markdown("<span class='timeline-dot'></span> Better communication (Habits 4–5)", unsafe_allow_html=True)
    with t4:
        st.markdown("**Week 12**")
        st.markdown("<span class='timeline-dot'></span> Synergy and project closing", unsafe_allow_html=True)

    st.write("")
    st.markdown("### 🧠 What should you get from this resource?")
    st.write(
        "- Understand each habit through real examples from the team.\n"
        "- See how the habits connect with leadership and management skills.\n"
        "- Reflect on your own way of working in teams."
    )

# ---------------- COLLABORATION EVIDENCE ----------------
def render_evidence():
    st.markdown("<div class='habit-card'>", unsafe_allow_html=True)
    st.markdown("## 🤝 Evidence of collaboration and team growth")
    st.write(texto_evidencia)
    st.write("")
    st.markdown("### 💬 Quote that summarizes the experience")
    st.markdown(
        "> “We went from organizing everything at the last minute to working as a team that plans, "
        "listens, and supports each other to achieve shared goals.”"
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SELF-ASSESSMENT ----------------
def render_self_assessment():
    st.markdown("<div class='habit-card'>", unsafe_allow_html=True)
    st.markdown("## 📊 7 Habits self-assessment")

    st.write(
        "Use the sliders to rate how often you apply each habit in your daily life "
        "(1 = almost never, 5 = almost always)."
    )

    ratings = {}
    for i in range(1, 8):
        ratings[f"Habit {i}"] = st.slider(
            f"{i}. {habits[i]['title']}",
            min_value=1,
            max_value=5,
            value=3,
            key=f"slider_{i}"
        )

    st.write("")
    st.markdown("### 🔍 Your habit profile")

    df = pd.DataFrame({
        "Habit": list(ratings.keys()),
        "Level of application": list(ratings.values())
    }).set_index("Habit")

    st.bar_chart(df)

    st.write("")
    st.markdown("### ✏️ Personal summary")
    st.text_area(
        "In a few lines, which habit do you master the most and which one do you want to strengthen from now on?",
        key="resumen_personal"
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- MAIN / SIDEBAR ----------------
def main():
    st.sidebar.title("📚 Navigation")
    section = st.sidebar.radio(
        "Choose a section:",
        (
            "Home",
            "Habit 1",
            "Habit 2",
            "Habit 3",
            "Habit 4",
            "Habit 5",
            "Habit 6",
            "Habit 7",
            "Collaboration evidence",
            "Self-assessment"
        )
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Team:** Juan Pablo · Alejandro · Mateo")
    st.sidebar.caption("Digital resource created to show the team's growth as future leaders.")

    if section == "Home":
        render_home()
    elif section.startswith("Habit"):
        num = int(section.split(" ")[1])
        render_habit(num)
    elif section == "Collaboration evidence":
        render_evidence()
    elif section == "Self-assessment":
        render_self_assessment()

if __name__ == "__main__":
    main()

