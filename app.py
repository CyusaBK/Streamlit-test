import streamlit as st
st.html("style.html")

st.html('<h1 class="title">Task manager</h1>')

with st.container(border=True):
    st.html(f'<span class="task_card"></span>')
    l,r = st.columns([1,0.2])
    with l:
        st.html(f'<span class="input_card"></span>')
        task = st.text_input("Enter your task","")

    with r:
        st.html(f'<span class="button_card"></span>')
        if st.button("Add task"):
            if task:
                st.session_state["task_list"].append(task)
        if "task_list" not in st.session_state:
            st.session_state["task_list"]=[]

for i, t in enumerate(st.session_state["task_list"]):
    st.write(f"{i+1}, {t}")

for i, t in enumerate(st.session_state["task_list"]):
    if st.checkbox(f"{i+1}, {t}"):
        st.session_state["task_list"].remove(t)
