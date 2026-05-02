import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="
            background: rgba(255,255,255,0.06);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255,255,255,0.12);
            padding: 24px;
            border-radius: 20px;
            margin-bottom: 16px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.2);
        ">
        <h3 style="margin:0 0 8px 0; color: #a5b4fc; font-size: 1.3rem; font-family: 'Syne', sans-serif; font-weight: 700;">{name}</h3>
        <p style="color: rgba(255,255,255,0.45); margin: 0 0 12px 0; font-size: 0.875rem; font-family: 'DM Sans', sans-serif;">
            Code : <span style="background: rgba(99,102,241,0.2); color: #a5b4fc; padding: 2px 10px; border-radius: 6px; font-weight: 600;">{code}</span>
            &nbsp;|&nbsp; Section : {section}
        </p>
        """

    if stats:
        html += '<div style="display:flex; gap:8px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            html += f'''
                <div style="
                    background: rgba(99,102,241,0.12);
                    border: 1px solid rgba(99,102,241,0.2);
                    padding: 5px 12px;
                    border-radius: 10px;
                    font-size: 0.85rem;
                    color: #c7d2fe;
                    font-family: 'DM Sans', sans-serif;
                ">{icon} <b>{value}</b> {label}</div>'''
        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
