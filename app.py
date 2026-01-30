import streamlit as st
import pandas as pd

# Force the sidebar to stay open for your university work
st.set_page_config(page_title="Java Helper", initial_sidebar_state="expanded")

# --- Use your RAW URL from GitHub here ---
DB_URL = "https://raw.githubusercontent.com/karthikjk-debug/java-template-hub/main/java_database.csv"

@st.cache_data
def load_java_data(url):
    try:
        df = pd.read_csv(url, quotechar='"', on_bad_lines='skip', engine='python')
        return df.dropna()
    except:
        return pd.DataFrame({"template_name": ["Error"], "code": ["Check CSV formatting!"]})

df = load_java_data(DB_URL)

# --- Permanent Sidebar Navigation ---
st.sidebar.title("🔍 Search & Filter")
search_query = st.sidebar.text_input("Search (e.g. 'string', 'array')", "")

# Filter the list based on search
if search_query:
    filtered_df = df[df['template_name'].str.contains(search_query, case=False)]
else:
    filtered_df = df

st.sidebar.write("---")
st.sidebar.title("📚 Java Menu")

if not filtered_df.empty:
    selected_name = st.sidebar.radio(
        "Select a Template (Use ↑/↓ arrows):",
        options=filtered_df['template_name'].tolist()
    )

    # --- Main Display Area ---
    selected_code = filtered_df[filtered_df['template_name'] == selected_name]['code'].values[0]
    
    st.title(f"🚀 {selected_name}")
    st.code(selected_code, language='java')

    # Download Button
    file_name = f"{selected_name.replace(' ', '_')}.java"
    st.download_button(
        label="📥 Download .java File",
        data=selected_code,
        file_name=file_name,
        mime="text/x-java"
    )
else:
    st.sidebar.warning("No templates found for that search.")

if st.sidebar.button("Celebrate 🎈"):
    st.balloons()
