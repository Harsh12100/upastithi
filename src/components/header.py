import streamlit as st


def header_home():
    st.markdown("""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:32px; margin-top:24px;">
            <div style="
                background: linear-gradient(135deg, #6366f1, #8b5cf6);
                width: 72px; height: 72px;
                border-radius: 20px;
                display: flex; align-items: center; justify-content: center;
                font-size: 36px;
                box-shadow: 0 8px 32px rgba(99,102,241,0.4);
                margin-bottom: 16px;
            ">🎓</div>
            <h1 style="
                font-family: 'Syne', sans-serif !important;
                font-size: 3rem !important;
                font-weight: 800 !important;
                color: white !important;
                letter-spacing: -1px;
                margin: 0;
                text-align: center;
            ">Upastithi</h1>
            <p style="
                color: rgba(255,255,255,0.5);
                font-size: 0.95rem;
                margin-top: 6px;
                font-family: 'DM Sans', sans-serif;
                text-align: center;
            ">AI-Powered Attendance System</p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    st.markdown("""
        <div style="display:flex; align-items:center; gap:12px;">
            <div style="
                background: linear-gradient(135deg, #6366f1, #8b5cf6);
                width: 48px; height: 48px;
                border-radius: 14px;
                display: flex; align-items: center; justify-content: center;
                font-size: 24px;
                box-shadow: 0 4px 16px rgba(99,102,241,0.35);
                flex-shrink: 0;
            ">🎓</div>
            <div>
                <h2 style="
                    font-family: 'Syne', sans-serif !important;
                    font-size: 1.4rem !important;
                    font-weight: 800 !important;
                    color: white !important;
                    letter-spacing: -0.5px;
                    margin: 0;
                    line-height: 1;
                ">Upastithi</h2>
                <p style="
                    color: rgba(255,255,255,0.4);
                    font-size: 0.75rem;
                    margin: 2px 0 0 0;
                    font-family: 'DM Sans', sans-serif;
                ">AI Attendance</p>
            </div>
        </div>
    """, unsafe_allow_html=True)