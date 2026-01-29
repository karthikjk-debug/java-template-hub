import streamlit as st

st.set_page_config(page_title="Java Template Hub", page_icon="☕", layout="wide")

# Custom CSS for the Green "Copy" Helper Button
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #28a745;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 12px 30px;
        font-size: 16px;
        font-weight: bold;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #218838;
        border: 1px solid white;
    }
    </style>
""", unsafe_allow_html=True)

# --- TEMPLATE LIBRARY (The "End Number" of Options) ---
# You can add hundreds of these easily
templates = {
    "Scanner: 1 Variable": """import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
    }
}""",
    "Scanner: 2 Variables": """import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
    }
}""",
    "If Statement": """if (condition) {
    // code to be executed if condition is true
}""",
    "If-Else": """if (condition) {
    // code if true
} else {
    // code if false
}""",
    "Else-If Ladder": """if (condition1) {
    // block 1
} else if (condition2) {
    // block 2
} else {
    // block 3
}""",
    "Switch Case": """switch(expression) {
    case x:
        // code
        break;
    case y:
        // code
        break;
    default:
        // code
}""",
    "For Loop": """for (int i = 0; i < 10; i++) {
    System.out.println(i);
}""",
    "While Loop": """int i = 0;
while (i < 10) {
    System.out.println(i);
    i++;
}""",
    "Do-While Loop": """int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 10);""",
    "Break Statement": """for (int i = 0; i < 10; i++) {
    if (i == 5) {
        break;
    }
    System.out.println(i);
}""",
    "Continue Statement": """for (int i = 0; i < 10; i++) {
    if (i == 5) {
        continue;
    }
    System.out.println(i);
}"""
}

# --- SIDEBAR SEARCH & NAVIGATION ---
st.sidebar.title("🔍 Search & Filter")
search_query = st.sidebar.text_input("Search (e.g. 'scanner', 'loop')").lower()

# Filter logic based on search
filtered_keys = [key for key in templates.keys() if search_query in key.lower()]

if filtered_keys:
    selected_template = st.sidebar.radio("Select a Template:", filtered_keys)
    
    # --- MAIN DISPLAY AREA ---
    st.title(f"☕ Java Template: {selected_template}")
    st.write("Copy the code below to save time on your university assignments.")
    
    # Code box with built-in copy button
    st.code(templates[selected_template], language='java')
    
    # Custom Green Button
    if st.button(f"PREPARE {selected_template.upper()}"):
        st.success("Ready! Use the copy icon in the top-right of the code box.")
        st.balloons()
else:
    st.sidebar.warning("No templates match your search.")
    st.title("Welcome to the Java Template Hub")
    st.info("Use the sidebar to search for a Java snippet!")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Built for University Productivity")