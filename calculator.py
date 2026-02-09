import streamlit as st

# import streamlit as st
# st.title("My First Streamlit App")
# st.write('Hello, Streamlit!')
# name = st.text_input('Enter your name: ')
# if name:
#     st.success(f'Welcome, {name}!')

# # Sidebar
# st.sidebar.title('menu')

# # Tabs
# tab1, tab2 = st.tabs(['A','B'])
# with tab1:
#     st.write('Tab A')

# Column
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write('Left')

# with col2:
#     st.write('Middle')

# with col3:
#     st.write('Right')

# Page config MUST be first
st.set_page_config(page_title="Calculator", layout="centered")

st.title("Calculator Application")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display
st.text_input(
    "Display",
    value=st.session_state.expression,
    disabled=True,
    label_visibility="collapsed"
)

# Convert display symbols to Python operators
SYMBOL_MAP = {
    "×": "*",
    "÷": "/",
    "−": "-",
    "+": "+"
}

# Button click handler
def press(value):
    if value == "C":
        st.session_state.expression = ""
    elif value == "=":
        try:
            st.session_state.expression = str(
                eval(st.session_state.expression)
            )
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += SYMBOL_MAP.get(value, value)

# Calculator layout (UI symbols)
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["0", ".", "=", "+"],
    ["C"]
]

for row in buttons:
    cols = st.columns(len(row))
    for col, label in zip(cols, row):
        with col:
            st.button(
                label,
                key=f"btn_{label}",
                use_container_width=True,
                on_click=press,
                args=(label,)
            )
