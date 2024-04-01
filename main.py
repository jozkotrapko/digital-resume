import streamlit as st
import base64


def home():
    # Page configs (tab title, favicon)
    st.set_page_config(
        page_title="Jozef's Portfolio",
        page_icon="👨‍💻",
    )

    # CSS styles file
    with open("styles/main.css") as f:
        st.write(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Profile image file
    with open("assets/ja1.jpg", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(
            img_file.read()).decode()

    # PDF CV file
    with open("assets/jozef_cermak_cv.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Top title
    st.write(
        f"""<div class="title"><strong>Hi! My name is</strong> Jozef Čermák 👋</div>""",
        unsafe_allow_html=True)

    # Profile image
    st.write(f"""
    <div class="container">
        <div class="box">
            <div class="spin-container">
                <div class="shape">
                    <div class="bd">
                        <img src="{img}" alt="Enric Domingo">
                    </div>
                </div>
            </div>
        </div>
    </div>
    """,
             unsafe_allow_html=True)

    # Alternative image (static and rounded) uncomment it if you prefer this one
    # st.write(f"""
    # <div style="display: flex; justify-content: center;">
    #    <img src="{img}" alt="Enric Domingo" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    # </div>
    # """, unsafe_allow_html=True)

    # Subtitle
    st.write(
        f"""<div class="subtitle" style="text-align: center;">Self-employed Professional with a strong background in the fast-paced Online World</div>""",
        unsafe_allow_html=True)

    # Social Icons
    social_icons_data = {
        # Platform: Icon
        "Python": "https://img.icons8.com/?size=256&id=13441&format=png",
        "Photoshop": "https://www.svgrepo.com/show/475668/photoshop-color.svg",
        "Davinci Resolve": "https://img.icons8.com/?size=256&id=40604&format=png",
        "MS Office": "https://cdn.icon-icons.com/icons2/1156/PNG/512/1486565573-microsoft-office_81557.png",
        "Canva": "https://img.icons8.com/?size=256&id=iWw83PVcBpLw&format=png",
    }

    # Start the HTML string
    html_string = '<div style="display: flex; justify-content: center;">'

    for platform, icon in social_icons_data.items():
        html_string += f'<img src="{icon}" width="30" height="30" style="margin-right: 10px;">'

    # End the HTML string
    html_string += '</div>'

    st.markdown(html_string, unsafe_allow_html=True)

    st.write("##")

    # About me section
    st.subheader("About Me")
    st.write("""
    - ‍📍🏔️️ I’m a creative and open-minded individual based in Reykjavík, Iceland. With a strong leadership background and effective communication skills, I excel at problem-solving and thrive in challenging environments.
    """)

    st.subheader("Current Ventures")
    st.write("""
    - 👨‍💻 Currently, I am the proud solo founder of [IQBET]( https://iqbet.app/), an advanced SAAS platform that brings a fresh perspective to the esports betting. My software provides precise calculations of expected value for betting odds. I have personally crafted every aspect of IQBET, from the complex algorithms that drive the software, to the vibrant [online presence](https://www.instagram.com/iqbet.app/), interactive workshops and [strategic marketing](https://imgur.com/a/rrAq2FN) initiatives.
    """)

    st.subheader("Previous Experience")
    st.write("""
    - 📸 I’ve modeled for top agencies around the world, collaborating with influential brands such as Versace, Moschino, Acer, Cartier, and Guerlain. This has not only contributed to my global exposure but also honed my adaptability, resilience, and ability to work under pressure.
    
    - 🎮 In the esports realm, I founded a [Dota 2 team](https://ggscore.com/en/dota-2/team/nostrvm), managing international players and achieving success in division 2 tournaments. This experience has further developed my leadership skills, strategic thinking, and team management abilities.
    """)

    st.write("##")

    # Download CV button
    st.download_button(
        label="📄 Download my CV",
        data=pdf_bytes,
        file_name="jozef_cermak_cv.pdf",
        mime="application/pdf",
    )

    st.write("##")


if __name__ == "__main__":
    home()