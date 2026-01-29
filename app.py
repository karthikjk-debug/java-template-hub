import streamlit as st

# Force the sidebar to be permanently visible
st.set_page_config(
    page_title="Java Template Hub", 
    page_icon="☕", 
    initial_sidebar_state="expanded"
)

# Template Library
templates = {
    "Scanner: 1 Variable": """import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n    }\n}""",
    "Scanner: 2 Variables": """import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n    }\n}""",
    "If Statement": "if (condition) {\n    // code\n}",
    "If-Else": "if (condition) {\n    // true\n} else {\n    // false\n}",
    "While Loop": "int i = 0;\nwhile (i < 10) {\n    System.out.println(i);\n    i++;\n}",
    "For Loop": "for (int i = 0; i < 10; i++) {\n    System.out.println(i);\n}",
    "Switch Case": "switch(expression) {\n    case x: break;\n    default: // code\n}"
}

# --- Permanent Sidebar ---
st.sidebar.title("📚 Template Menu")
st.sidebar.info("Use UP/DOWN arrows to navigate options below.")

# Using radio buttons for arrow-key navigation
# Clicking once on an option allows you to use your keyboard arrows to move up/down
selected_template = st.sidebar.radio(
    "Select Java Boilerplate:",
    list(templates.keys()),
    index=0
)

# --- Main Display Area ---
st.title(f"🚀 {selected_template}")
st.code(templates[selected_template], language='java')

# Simple Celebration (No special button styling)
if st.sidebar.button("Celebrate! 🎈"):
    st.balloons()