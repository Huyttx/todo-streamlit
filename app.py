import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="To-do App", layout="wide")

# Sidebar Menu
with st.sidebar:
    selected = option_menu("Menu", ["📋 To-Do List", "➕ Add Task", "ℹ️ About"], 
        icons=["list-task", "plus-circle", "info-circle"], default_index=0)

# Giao diện theo tab
if selected == "📋 To-Do List":
    st.title("📝 Your Tasks")
    # giả sử có danh sách tasks
    tasks = ["Buy milk", "Do homework", "Read book"]
    for task in tasks:
        st.checkbox(task)

elif selected == "➕ Add Task":
    st.title("➕ Add New Task")
    new_task = st.text_input("Enter your task:")
    if st.button("Add"):
        st.success(f"Task '{new_task}' added!")

elif selected == "ℹ️ About":
    st.title("ℹ️ About This App")
    st.write("This is a simple To-do List app built with Streamlit.")


