import streamlit as st
st.html("style.html")
st.html('<h1 class="title">Task manager</h1>')

# Initialize session state for the container list
if "container_states" not in st.session_state:
    st.session_state.container_states = {}

# Sample data for the containers
data = [
    {"id": 1, "title": "Item 1", "description": "Description for Item 1"},
    {"id": 2, "title": "Item 2", "description": "Description for Item 2"},
    {"id": 3, "title": "Item 3", "description": "Description for Item 3"},
]

# Function to toggle a specific container state
def toggle_state(item_id):
    st.session_state.container_states[item_id] = not st.session_state.container_states.get(item_id, False)

# Add the Font Awesome CSS and custom styles once
st.markdown(
    """
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" rel="stylesheet">
    <style>
        .icon-container {
            position: absolute;           /* Allows positioning relative to parent */
            display: flex;                /* Enables flexbox for centering */
            justify-content: center;      /* Centers horizontally */
            align-items: center;          /* Centers vertically */
            top: 35px;                    /* Offset from the top */
                            /* Ensure it spans from the left edge */
            width: 100%;                  /* Full width of parent */
            height: 100%;
           
        }
        .clickable-icon {
            font-size: 36px;              /* Icon size */
            color: #4CAF50;               /* Icon color */
            cursor: pointer;              /* Indicates interactivity */
          
           
        }
        
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a container for each item in the list
for item in data:
    item_id = item["id"]
    with st.container():
        col1, col2 = st.columns([3, 1])
        # Display the container content
        with col1:
            st.subheader(item["title"])
            st.write(item["description"])
            state = st.session_state.container_states.get(item_id, False)
            st.write(f"State: {'Active' if state else 'Inactive'}")
        
        # Invisible button and icon overlapping
        with col2:
            
            # Create a container to hold both the icon and the invisible button
            icon_html = f"""
            <div class="icon-container">
                <i class="clickable-icon fas {'fa-toggle-on' if st.session_state.container_states.get(item_id, False) else 'fa-toggle-off'}"></i>
            </div>
            """
            st.markdown(icon_html, unsafe_allow_html=True)
            if st.button(f"", key=f"toggle_button_{item_id}"):
                toggle_state(item_id)

# Show the current state for all containers
st.write("### All States")
for item in data:
    item_id = item["id"]
    state = st.session_state.container_states.get(item_id, False)
    st.write(f"{item['title']} - {'Active' if state else 'Inactive'}")

