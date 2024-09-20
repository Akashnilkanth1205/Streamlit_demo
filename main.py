import streamlit as st

# Sidebar for selecting projects
st.sidebar.title("Energy Group Projects")
projects = ["Renewable Energy Capacity", "Energy Demand & Efficiency", "Decarbonization Pathways"]
project_selected = st.sidebar.radio("Select a project:", projects)

# Display based on selected project
st.title("Energy Group Visualization Dashboard")

# Placeholder for project visualization images
if project_selected == "Renewable Energy Capacity":
    st.subheader("Renewable Energy Capacity Simulation")
    st.write("This project focuses on modeling renewable energy capacity.")
   # st.image("path_to_your_image1.jpg", caption="Projected Renewable Energy Capacity", use_column_width=True)

elif project_selected == "Energy Demand & Efficiency":
    st.subheader("Energy Demand & Efficiency Analysis")
    st.write("This project analyses energy demand trends and efficiency improvements.")
    #st.image("path_to_your_image2.jpg", caption="Energy Demand Trends", use_column_width=True)

elif project_selected == "Decarbonization Pathways":
    st.subheader("Decarbonization Pathways Exploration")
    st.write("This project visualizes pathways for decarbonization.")
   # st.image("path_to_your_image3.jpg", caption="Decarbonization Pathways", use_column_width=True)

# Footer
st.sidebar.title("About")
st.sidebar.info("This demo application showcases different projects and their visualizations in the energy group. Built using Streamlit for rapid, interactive data visualization.")
