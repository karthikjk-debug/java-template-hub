import streamlit as st

# Forces the sidebar to stay open on load
st.set_page_config(
    page_title="Java Template Hub", 
    page_icon="☕", 
    initial_sidebar_state="expanded"
)

# Your expanded list of Java topics
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
    // code here
}""",
    "If-Else": """if (condition) {
    // true
} else {
    // false
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
    "Break Statement": """break;""",
    "Continue Statement": """continue;"""
}

# --- Permanent Sidebar ---
st.sidebar.title("📚 Java Menu")
st.sidebar.write("Use ↑/↓ arrows to navigate")

# Using 'radio' allows you to click an option and then use your arrow keys
selected_template = st.sidebar.radio(
    "Go to:",
    list(templates.keys()),
    index=0
)

# --- Main Page ---
st.title(f"🚀 {selected_template}")
st.code(templates[selected_template], language='java')

# A simple, standard button for a quick celebration
if st.sidebar.button("Celebrate 🎈"):
    st.balloons()
