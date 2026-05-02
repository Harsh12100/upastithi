import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #0f0c29 0%, #1a1a4e 40%, #24243e 100%) !important;
            min-height: 100vh;
        }
        .stApp::before {
            content: '';
            position: fixed;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: 
                radial-gradient(ellipse at 20% 20%, rgba(99,102,241,0.15) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(139,92,246,0.12) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(59,130,246,0.08) 0%, transparent 60%);
            pointer-events: none;
            z-index: 0;
        }
        .stApp > * { position: relative; z-index: 1; }

        .stApp div[data-testid="stColumn"] {
            background: rgba(255,255,255,0.05) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            padding: 2.5rem !important;
            border-radius: 2rem !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        }
        .stApp div[data-testid="stColumn"]:hover {
            transform: translateY(-4px) !important;
            box-shadow: 0 16px 48px rgba(99,102,241,0.2) !important;
        }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(160deg, #0f0c29 0%, #1a1a4e 50%, #24243e 100%) !important;
            min-height: 100vh;
        }
        .stApp::before {
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background:
                radial-gradient(ellipse at 10% 10%, rgba(99,102,241,0.12) 0%, transparent 40%),
                radial-gradient(ellipse at 90% 90%, rgba(139,92,246,0.1) 0%, transparent 40%);
            pointer-events: none;
            z-index: 0;
        }
        .stApp > * { position: relative; z-index: 1; }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

        /* Hide Streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding-top: 1.5rem !important; }

        /* Typography */
        h1 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 800 !important;
            font-size: 3.2rem !important;
            line-height: 1.1 !important;
            letter-spacing: -1px !important;
            color: #ffffff !important;
            margin-bottom: 0 !important;
        }
        h2 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 700 !important;
            font-size: 1.8rem !important;
            line-height: 1.2 !important;
            color: #ffffff !important;
            margin-bottom: 0 !important;
        }
        h3 {
            font-family: 'Syne', sans-serif !important;
            font-weight: 600 !important;
            color: #e2e8f0 !important;
        }
        h4, p, span, label, div {
            font-family: 'DM Sans', sans-serif !important;
            color: #cbd5e1 !important;
        }

        /* Inputs */
        .stTextInput input, .stSelectbox select {
            background: rgba(255,255,255,0.07) !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            border-radius: 12px !important;
            color: white !important;
            font-family: 'DM Sans', sans-serif !important;
            padding: 12px 16px !important;
            transition: border-color 0.2s ease !important;
        }
        .stTextInput input:focus {
            border-color: rgba(99,102,241,0.6) !important;
            box-shadow: 0 0 0 3px rgba(99,102,241,0.15) !important;
        }
        .stTextInput label, .stSelectbox label {
            color: #94a3b8 !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        /* Buttons */
        button[kind="primary"], button[kind="primaryFormSubmit"] {
            background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
            color: white !important;
            border: none !important;
            border-radius: 14px !important;
            padding: 12px 24px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            box-shadow: 0 4px 15px rgba(99,102,241,0.35) !important;
            transition: all 0.25s ease !important;
        }
        button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(99,102,241,0.5) !important;
        }

        button[kind="secondary"] {
            background: rgba(255,255,255,0.08) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
            border-radius: 14px !important;
            padding: 12px 24px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 500 !important;
            backdrop-filter: blur(10px) !important;
            transition: all 0.25s ease !important;
        }
        button[kind="secondary"]:hover {
            background: rgba(255,255,255,0.14) !important;
            transform: translateY(-2px) !important;
            border-color: rgba(99,102,241,0.5) !important;
        }

        button[kind="tertiary"] {
            background: transparent !important;
            color: #94a3b8 !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 14px !important;
            padding: 10px 20px !important;
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 500 !important;
            transition: all 0.25s ease !important;
        }
        button[kind="tertiary"]:hover {
            color: white !important;
            border-color: rgba(255,255,255,0.3) !important;
            background: rgba(255,255,255,0.05) !important;
        }

        /* Cards / Containers */
        div[data-testid="stContainer"] {
            background: rgba(255,255,255,0.05) !important;
            backdrop-filter: blur(16px) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 20px !important;
            padding: 1.5rem !important;
        }

        /* Divider */
        hr {
            border-color: rgba(255,255,255,0.1) !important;
            margin: 1.5rem 0 !important;
        }

        /* Dataframe */
        .stDataFrame {
            border-radius: 16px !important;
            overflow: hidden !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
        }

        /* Selectbox */
        .stSelectbox > div > div {
            background: rgba(255,255,255,0.07) !important;
            border: 1px solid rgba(255,255,255,0.15) !important;
            border-radius: 12px !important;
            color: white !important;
        }

        /* Toast / alerts */
        .stAlert {
            border-radius: 14px !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            background: rgba(255,255,255,0.06) !important;
        }

        /* Spinner */
        .stSpinner { color: #6366f1 !important; }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: rgba(99,102,241,0.4);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover { background: rgba(99,102,241,0.7); }

        </style>
    """, unsafe_allow_html=True)