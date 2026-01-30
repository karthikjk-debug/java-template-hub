import streamlit as st
import pandas as pd

# 1. Page Config
st.set_page_config(page_title="Java Hub", layout="wide", initial_sidebar_state="expanded")

# 2. Database Connection
DB_URL = "https://raw.githubusercontent.com/karthikjk-debug/java-template-hub/main/java_database.csv"

@st.cache_data
def load_db(url):
    try:
        df = pd.read_csv(url, quotechar='"', on_bad_lines='skip', engine='python')
        return df.dropna()
    except:
        return pd.DataFrame({"template_name": ["Error"], "code": ["Check CSV!"]})

df_db = load_db(DB_URL)

# 3. Smart Manual Templates (University Lab Essentials)
manual_templates = {
    "Scanner: 1 Variable": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        System.out.println(a);\n    }\n}",
    "Scanner: 2 Variables": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println();\n    }\n}",
    "If-Else Basic": "if () { System.out.println(\"+\"); } else { System.out.println(\"-\"); }",
    "Else-If Ladder": "if() return 'A'; else if(m>=80) return 'B'; else return 'C';",
    "Switch Case": "switch(n) { case 1: System.out.println(\"One\"); break; default: break; }",
    "While Loop": "int i=1; while(i<=10) { System.out.println(i); i++; }",
    "For Loop": "for(int i=0; i<10; i++) { System.out.println(i); }",
    "Do-While Loop": "int i=0; do { System.out.println(i); i++; } while(i<5);",
    "Array: Init": "int[] arr = {1, 2, 3, 4, 5};",
    "Array: Input": "for(int i=0; i<n; i++) arr[i] = sc.nextInt();",
    "Method: Simple": "public static void greet() { System.out.println(\"Hi\"); }",
    "Method: Add": "public static int add(int x, int y) { return x + y; }",
    "String: Equals": "if(s1.equals(s2)) { System.out.println(\"Match\"); }",
    "String: Length": "System.out.println(str.length());",
    "Class & Object": "class Student { String name; }\nStudent s = new Student();",
    "Constructor": "public Student(String name) { this.name = name; }",
    "Inheritance": "class A { } class B extends A { }",
    "Try-Catch": "try { int n = 5/0; } catch(Exception e) { System.out.println(e); }",
    "Thread": "class T extends Thread { public void run() { } }",
    "Math Library": "Math.sqrt(25); Math.pow(2,3); Math.abs(-1);"
}

# --- 4. Sidebar UI (The "Smart" Way) ---
st.sidebar.title("🔍 Search Hub")
search = st.sidebar.text_input("Filter database items...", "")

# Use a Checkbox to switch modes - cleaner than a radio
use_db = st.sidebar.checkbox("Show Scraped Database", value=False)

if not use_db:
    with st.sidebar.expander("📍 UNIVERSITY TEMPLATES", expanded=True):
        # Selectbox removes the "Arrow Key" confusion
        choice = st.selectbox("Select Template:", list(manual_templates.keys()))
        code = manual_templates[choice]
else:
    with st.sidebar.expander("🌐 SCRAPED DATABASE", expanded=True):
        f_df = df_db[df_db['template_name'].str.contains(search, case=False)] if search else df_db
        choice = st.selectbox("Select from DB:", f_df['template_name'].tolist())
        code = f_df[f_df['template_name'] == choice]['code'].values[0]

# --- 5. Main Screen Display ---
st.title(f"🚀 {choice}")
st.code(code, language='java')

# Dynamic Download Button
st.download_button(
    label="📥 Download .java File",
    data=code,
    file_name=f"{choice.replace(' ', '_')}.java",
    mime="text/x-java"
)

if st.sidebar.button("Celebrate 🎈"):
    st.balloons()
