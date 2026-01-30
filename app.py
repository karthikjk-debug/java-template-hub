import streamlit as st
import pandas as pd

st.set_page_config(page_title="Java Helper", initial_sidebar_state="expanded")

# --- Database Connection ---
DB_URL = "https://raw.githubusercontent.com/karthikjk-debug/java-template-hub/main/java_database.csv"

@st.cache_data
def load_java_data(url):
    try:
        # Use sep=None to let pandas figure out the comma formatting automatically
        data = pd.read_csv(url, quotechar='"', on_bad_lines='skip')
        return data.dropna()
    except Exception as e:
        return pd.DataFrame({"template_name": ["Error"], "code": [f"Connection Error: {e}"]})

df = load_java_data(DB_URL)

# --- Sidebar ---
st.sidebar.title("📚 Java Menu")
selected_name = st.sidebar.radio("Choose a Template:", options=df['template_name'].tolist())

# --- Main Screen ---
st.title(f"🚀 {selected_name}")

if not df.empty and selected_name != "Error":
    selected_code = df[df['template_name'] == selected_name]['code'].values[0]
    
    # 1. Display the code
    st.code(selected_code, language='java')
    
    # 2. Add the Download Button
    # We create a filename by removing spaces from the template name
    file_name = f"{selected_name.replace(' ', '_')}.java"
    
    st.download_button(
        label="📥 Download .java File",
        data=selected_code,
        file_name=file_name,
        mime="text/x-java"
    )

if st.sidebar.button("Celebrate 🎈"):
    st.balloons()
