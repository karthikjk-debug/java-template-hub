import streamlit as st
import pandas as pd

# 1. Setup
st.set_page_config(page_title="Java Template Hub", initial_sidebar_state="expanded", layout="wide")

# 2. Load Scraped Database
DB_URL = "https://raw.githubusercontent.com/karthikjk-debug/java-template-hub/main/java_database.csv"

@st.cache_data
def load_java_data(url):
    try:
        df = pd.read_csv(url, quotechar='"', on_bad_lines='skip', engine='python')
        return df.dropna()
    except:
        return pd.DataFrame({"template_name": ["Error"], "code": ["Check CSV!"]})

df_db = load_java_data(DB_URL)

# 3. All 20 Manual University Templates
manual_templates = {
    "Scanner: 1 Variable": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        System.out.print(\"Enter value: \");\n        int a = sc.nextInt();\n        System.out.println(\"Value: \" + a);\n    }\n}",
    "Scanner: 2 Variables": "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n        int b = sc.nextInt();\n        System.out.println(\"Sum: \" + (a + b));\n    }\n}",
    "If-Else Basic": "if (num > 0) {\n    System.out.println(\"Positive\");\n} else {\n    System.out.println(\"Negative\");\n}",
    "Else-If Ladder": "if (marks >= 90) System.out.println(\"A\");\nelse if (marks >= 75) System.out.println(\"B\");\nelse System.out.println(\"C\");",
    "Switch Case": "switch(day) {\n    case 1: System.out.println(\"Monday\"); break;\n    default: System.out.println(\"Other\");\n}",
    "While Loop": "int i = 1;\nwhile(i <= 10) {\n    System.out.println(i);\n    i++;\n}",
    "For Loop": "for(int i=0; i<10; i++) {\n    System.out.println(i);\n}",
    "Do-While Loop": "int i = 0;\ndo {\n    System.out.println(i);\n    i++;\n} while(i < 5);",
    "Array: Declaration": "int[] arr = new int[5];\narr[0] = 10;",
    "Array: Input Loop": "for(int i=0; i<arr.length; i++) {\n    arr[i] = sc.nextInt();\n}",
    "Method: Void": "public static void sayHello() {\n    System.out.println(\"Hello!\");\n}",
    "Method: Return": "public static int add(int a, int b) {\n    return a + b;\n}",
    "String: Compare": "if(str1.equals(str2)) {\n    System.out.println(\"Equal\");\n}",
    "String: Reverse": "StringBuilder sb = new StringBuilder(str);\nSystem.out.println(sb.reverse().toString());",
    "Class & Object": "class Student {\n    String name;\n}\nStudent s1 = new Student();",
    "Constructor": "public Student(String n) {\n    this.name = n;\n}",
    "Inheritance": "class Animal { }\nclass Dog extends Animal { }",
    "Try-Catch": "try {\n    int result = 10 / 0;\n} catch(ArithmeticException e) {\n    System.out.println(e);\n}",
    "Thread: Basic": "class MyThread extends Thread {\n    public void run() { }\n}",
    "Math: Functions": "Math.sqrt(16);\nMath.pow(2, 3);\nMath.abs(-5);"
}

# --- SIDEBAR ---
st.sidebar.title("🔍 Search Hub")
search_query = st.sidebar.text_input("Filter database...", "")

with st.sidebar.expander("🔽 UNIVERSITY TEMPLATES", expanded=True):
    selected_manual = st.radio("Quick Access:", list(manual_templates.keys()), key="man")

with st.sidebar.expander("🔽 SCRAPED DATABASE", expanded=False):
    if search_query:
        filtered_db = df_db[df_db['template_name'].str.contains(search_query, case=False)]
    else:
        filtered_df = df_db
    selected_db = st.radio("Full Database:", options=filtered_df['template_name'].tolist(), key="db")

# --- MAIN DISPLAY ---
st.title("🚀 Java Code Hub")
source = st.radio("View Source:", ["University Templates", "Database"], horizontal=True)

if source == "University Templates":
    disp_name, disp_code = selected_manual, manual_templates[selected_manual]
else:
    disp_name = selected_db
    disp_code = df_db[df_db['template_name'] == selected_db]['code'].values[0]

st.subheader(f"Current: {disp_name}")
st.code(disp_code, language='java')

st.download_button(
    label=f"📥 Download {disp_name}.java",
    data=disp_code,
    file_name=f"{disp_name.replace(' ', '_')}.java",
    mime="text/x-java"
)
