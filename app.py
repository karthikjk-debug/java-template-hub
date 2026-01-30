import streamlit as st
import pandas as pd

# 1. Setup: Permanent expanded sidebar
st.set_page_config(page_title="Java Helper", initial_sidebar_state="expanded", layout="wide")

# 2. Load the Large Database from GitHub
DB_URL = "https://raw.githubusercontent.com/karthikjk-debug/java-template-hub/main/java_database.csv"

@st.cache_data
def load_java_data(url):
    try:
        df = pd.read_csv(url, quotechar='"', on_bad_lines='skip', engine='python')
        return df.dropna()
    except:
        return pd.DataFrame({"template_name": ["Error"], "code": ["Check CSV!"]})

df_db = load_java_data(DB_URL)

# 3. Your 20 Manual University Templates
# Just replace the "// Code here" with your actual Java code
manual_templates = {
    "Scanner: 1 Variable": "import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt();\n    }\n}",
    "Scanner: 2 Variables": "import java.util.Scanner;\n// Code here...",
    "If-Else Basic": "// Code here...",
    "Else-If Ladder": "// Code here...",
    "Switch Case": "// Code here...",
    "While Loop": "// Code here...",
    "For Loop": "// Code here...",
    "Do-While Loop": "// Code here...",
    "Array Declaration": "// Code here...",
    "Array Input": "// Code here...",
    "Method: Void": "// Code here...",
    "Method: Return": "// Code here...",
    "String: Length": "// Code here...",
    "String: Compare": "// Code here...",
    "Class & Object": "// Code here...",
    "Constructor": "// Code here...",
    "Inheritance": "// Code here...",
    "Try-Catch": "// Code here...",
    "File Handling": "// Code here...",
    "Linked List Basic": "// Code here..."
}

# --- SIDEBAR UI ---
st.sidebar.title("🔍 Search Hub")
search_query = st.sidebar.text_input("Find any template...", "")

# FOLDER 1: University Templates (The Arrow)
with st.sidebar.expander("🔽 UNIVERSITY TEMPLATES", expanded=True):
    selected_manual = st.radio("Choose Program:", list(manual_templates.keys()), key="man_key")

# FOLDER 2: Scraped Database (The Arrow)
with st.sidebar.expander("🔽 SCRAPED DATABASE", expanded=False):
    if search_query:
        filtered_df = df_db[df_db['template_name'].str.contains(search_query, case=False)]
    else:
        filtered_df = df_db
    selected_db = st.radio("Choose Program:", options=filtered_df['template_name'].tolist(), key="db_key")

# --- MAIN PAGE LOGIC ---
st.title("🚀 Java Template Hub")

# Toggle to choose which source to display
source = st.radio("Source:", ["University Templates", "Database"], horizontal=True)

if source == "University Templates":
    current_name = selected_manual
    current_code = manual_templates[selected_manual]
else:
    current_name = selected_db
    current_code = df_db[df_db['template_name'] == selected_db]['code'].values[0]

st.subheader(f"Current File: {current_name}")
st.code(current_code, language='java')

# Download Button
st.download_button(
    label=f"📥 Download {current_name}.java",
    data=current_code,
    file_name=f"{current_name.replace(' ', '_')}.java",
    mime="text/x-java"
)
