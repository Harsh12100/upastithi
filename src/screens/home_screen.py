import streamlit as st
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.header import header_home
from src.components.footer import footer_home


def home_screen():
    style_background_home()
    style_base_layout()

    header_home()

    # Hero text
    st.markdown("""
        <div style="text-align:center; margin-bottom: 40px;">
            <div style="
                display: inline-flex; align-items: center; gap: 8px;
                background: rgba(99,102,241,0.15);
                border: 1px solid rgba(99,102,241,0.3);
                border-radius: 100px;
                padding: 6px 16px;
                margin-bottom: 16px;
            ">
                <span style="font-size:13px;">✨</span>
                <span style="color: #a5b4fc; font-size: 13px; font-family: 'DM Sans', sans-serif; font-weight: 600;">
                    Face & Voice Recognition
                </span>
            </div>
            <h2 style="
                font-family: 'Syne', sans-serif;
                font-size: 1.6rem;
                font-weight: 700;
                color: white;
                margin: 0 0 10px 0;
            ">Choose Your Portal</h2>
            <p style="
                color: rgba(255,255,255,0.45);
                font-size: 0.95rem;
                font-family: 'DM Sans', sans-serif;
                margin: 0;
            ">Smart attendance powered by AI — fast, accurate, effortless</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="text-align:center; margin-bottom: 12px;">
                <div style="
                    background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(139,92,246,0.2));
                    border: 1px solid rgba(99,102,241,0.3);
                    border-radius: 20px;
                    padding: 32px 20px 24px;
                    margin-bottom: 16px;
                ">
                    <div style="font-size: 56px; margin-bottom: 16px;">🧑‍🎓</div>
                    <h3 style="
                        font-family: 'Syne', sans-serif;
                        font-size: 1.4rem;
                        font-weight: 700;
                        color: white;
                        margin: 0 0 8px 0;
                    ">I'm a Student</h3>
                    <p style="
                        color: rgba(255,255,255,0.45);
                        font-size: 0.875rem;
                        font-family: 'DM Sans', sans-serif;
                        margin: 0;
                        line-height: 1.6;
                    ">Login with face recognition, track your attendance across all enrolled subjects.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button('Student Portal →', type='primary', use_container_width=True):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="text-align:center; margin-bottom: 12px;">
                <div style="
                    background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(217,70,239,0.15));
                    border: 1px solid rgba(139,92,246,0.3);
                    border-radius: 20px;
                    padding: 32px 20px 24px;
                    margin-bottom: 16px;
                ">
                    <div style="font-size: 56px; margin-bottom: 16px;">👩‍🏫</div>
                    <h3 style="
                        font-family: 'Syne', sans-serif;
                        font-size: 1.4rem;
                        font-weight: 700;
                        color: white;
                        margin: 0 0 8px 0;
                    ">I'm a Teacher</h3>
                    <p style="
                        color: rgba(255,255,255,0.45);
                        font-size: 0.875rem;
                        font-family: 'DM Sans', sans-serif;
                        margin: 0;
                        line-height: 1.6;
                    ">Take AI attendance with photos or voice, manage subjects and view records.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        if st.button('Teacher Portal →', type='secondary', use_container_width=True):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    # Stats bar
    st.markdown("""
        <div style="
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 40px;
            padding: 20px;
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
        ">
            <div style="text-align:center;">
                <div style="font-size: 1.5rem; font-weight: 800; color: #a5b4fc; font-family: 'Syne', sans-serif;">AI</div>
                <div style="font-size: 0.75rem; color: rgba(255,255,255,0.35); font-family: 'DM Sans', sans-serif;">Face Recognition</div>
            </div>
            <div style="width:1px; background: rgba(255,255,255,0.08);"></div>
            <div style="text-align:center;">
                <div style="font-size: 1.5rem; font-weight: 800; color: #a5b4fc; font-family: 'Syne', sans-serif;">🎤</div>
                <div style="font-size: 0.75rem; color: rgba(255,255,255,0.35); font-family: 'DM Sans', sans-serif;">Voice Attendance</div>
            </div>
            <div style="width:1px; background: rgba(255,255,255,0.08);"></div>
            <div style="text-align:center;">
                <div style="font-size: 1.5rem; font-weight: 800; color: #a5b4fc; font-family: 'Syne', sans-serif;">📊</div>
                <div style="font-size: 0.75rem; color: rgba(255,255,255,0.35); font-family: 'DM Sans', sans-serif;">Live Records</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    footer_home()