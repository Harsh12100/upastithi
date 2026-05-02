import streamlit as st
from src.database.config import supabase
from src.database.db import create_attendance


def show_attendance_result(df, logs, key_prefix="default"):  # FIX: added key_prefix
    st.write('Please review attendance before confirming.')
    st.dataframe(df, hide_index=True, use_container_width=True)  # FIX: width='stretch' → use_container_width=True

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', width='stretch', key=f'discard_{key_prefix}'):  # FIX: unique key
            st.session_state.voice_attendance_results = None
            st.session_state.face_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save', width='stretch', type='primary', key=f'confirm_{key_prefix}'):  # FIX: unique key
            try:
                create_attendance(logs)
                st.toast("Attendance saved successfully!")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.session_state.face_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error(f'Sync failed: {e}')


@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs, key_prefix="dialog") 
