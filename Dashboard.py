import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
    layout="wide", 
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""


st.image("assets/screenshot3.png", use_column_width=True)

st.subheader("Ice cream Chart")

c1, c2, c3 = st.columns(3)
with c1:
    user_name = st.text_input("Your name", placeholder="Type your name")
with c2:
    flavor = st.selectbox("Favorite flavor", ["Vanilla", "Chocolate", "Strawberry", "Mint", "Cookie Dough"])
with c3:
    scoops = st.slider("Scoops", min_value=1, max_value=5, value=2)

r1, r2 = st.columns(2)
with r1:
    sprinkles = st.checkbox("Add sprinkles")
with r2:
    toppings = st.multiselect("Toppings", ["Caramel", "Chocolate chips", "Nuts", "Marshmallows"], default=["Caramel"])

st.write(f"Hello {user_name or 'friend'}")
st.write(f"You chose {scoops} scoop(s) of {flavor} with{' no' if not sprinkles and len(toppings)==0 else ''} extras.")

# Tiny synthetic data tied to the choices
np.random.seed(7)
base = {
    "Vanilla": 30, "Chocolate": 35, "Strawberry": 22, "Mint": 18, "Cookie Dough": 28
}
# Boost the selected flavor a little
boosted = {k: v + (8 if k == flavor else 0) for k, v in base.items()}

df_sales = pd.DataFrame({"Flavor": list(boosted.keys()), "Sales": list(boosted.values())}).set_index("Flavor")

# A playful “happiness score” from choices
topping_factor = 0.15 * len(toppings)
sprinkle_factor = 0.25 if sprinkles else 0.0
happiness = 5 + scoops * (1.0 + topping_factor + sprinkle_factor) + np.random.normal(0, 0.4)

st.metric("Happiness score", f"{happiness:.1f}")
st.caption("All data is synthetic and just for fun.")

st.bar_chart(df_sales)
st.subheader("Data")
st.dataframe(df_sales, use_container_width=True)