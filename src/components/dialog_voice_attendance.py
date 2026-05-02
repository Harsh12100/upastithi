import streamlit as st
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
import pandas as pd
from src.components.dialog_attendance_results import show_attendance_result
from datetime import datetime
import json
import numpy as np

@st.dialog('Voice Attendance')
def voice_attendance_dialog(selected_subject_id):
    st.write('Record audio of students saying I am present. Then AI will recognize the students')

    audio_data = st.audio_input("Record classroom audio")

    if st.button('Analyze Audio', width='stretch', type='primary', key='analyze_voice_audio'):
        with st.spinner('Processing Audio data...'):
            enrolled_res = supabase.table('subject_students').select("*, students!subject_students_student_id_fkey(*)").eq('subject_id', selected_subject_id).execute()
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning('No students enrolled in this course')
                return

            candidates_dict = {}
            for s in enrolled_students:
                emb = s['students'].get('voice_embedding')
                if emb:
                    if isinstance(emb, str):
                        emb = json.loads(emb)
                    candidates_dict[s['students']['id']] = np.array(emb, dtype=np.float64)

            if not candidates_dict:
                st.error('No enrolled students have voice profiles registered')
                return

            audio_bytes = audio_data.read()
            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [], []
            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node['students']
                score = detected_scores.get(student['id'], 0.0)  # FIX: 'student_id' → 'id'
                is_present = bool(score > 0)

                results.append({
                    "Name": student['name'],
                    "ID": student['id'],  # FIX: 'student_id' → 'id'
                    "Score": score if is_present else "-",
                    "Status": "✅ Present" if is_present else "❌ Absent"
                })

                attendance_to_log.append({
                    'student_id': student['id'], 
                    'student_name': student['name'],
                    'subject_id': selected_subject_id,
                    'timestamp': current_timestamp,
                    'is_present': bool(is_present)
                })

            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

    if st.session_state.get('voice_attendance_results'):
        st.divider()
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)