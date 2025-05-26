import streamlit as st

st.title("📝 To-do List App")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Nhập công việc:")
if st.button("Thêm"):
    if task:
        st.session_state.tasks.append(task)
        st.success("Đã thêm!")

st.subheader("📋 Danh sách công việc:")
for i, task in enumerate(st.session_state.tasks):
    if st.checkbox(task, key=i):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()
