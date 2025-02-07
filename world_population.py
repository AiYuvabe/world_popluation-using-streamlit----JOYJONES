# import pandas as pd
# import streamlit as st

# # Load the data
# file_path = "D:/webdesign/world_population.csv"
# df = pd.read_csv(file_path)

# # Streamlit app title
# st.title("World Population Statistics")

# # Sidebar for user inputs
# st.sidebar.header("Filters")
# continent = st.sidebar.selectbox("Select Continent", df['Continent'].unique())
# data_type = st.sidebar.selectbox("Select Data Type", df.columns[2:])  # Skip 'Continent' and 'Country'
# stat = st.sidebar.selectbox("Select Statistic", ['max', 'min', 'mean', 'sum', 'count'])

# # Function to compute statistics
# def compute_statistics(continent, data_type, stat):
#     continent_data = df[df['Continent'] == continent]
    
#     if stat == 'max':
#         result = continent_data[data_type].max()
#         country = continent_data.loc[continent_data[data_type].idxmax(), 'Country']
#         return f"Max {data_type} in {continent}: {int(result)} (Country: {country})"
    
#     elif stat == 'min':
#         result = continent_data[data_type].min()
#         country = continent_data.loc[continent_data[data_type].idxmin(), 'Country']
#         return f"Min {data_type} in {continent}: {int(result)} (Country: {country})"
    
#     elif stat == 'mean':
#         result = continent_data[data_type].mean()
#         return f"Mean {data_type} in {continent}: {int(result)}"
    
#     elif stat == 'sum':
#         result = continent_data[data_type].sum()
#         return f"Total {data_type} in {continent}: {int(result)}"
    
#     elif stat == 'count':
#         result = continent_data[data_type].count()
#         return f"Number of Countries in {continent}: {int(result)}"

# # Display results
# if st.sidebar.button("Compute Statistic"):
#     if continent and data_type and stat:
#         result = compute_statistics(continent, data_type, stat)
#         st.success(result)
#     else:
#         st.error("Please fill all the filters.")

# # Display raw data (optional)
# if st.checkbox("Show Raw Data"):
#     st.write(df)
import pandas as pd
import streamlit as st

# Load the data
file_path = "D:/webdesign/world_population.csv"
df = pd.read_csv(file_path)

# Streamlit app title
st.title("World Population Statistics")

# Sidebar for user inputs
st.sidebar.header("Filters")
continent = st.sidebar.selectbox("Select Continent", df['Continent'].unique())
data_type = st.sidebar.selectbox("Select Data Type", df.columns[2:])  # Skip 'Continent' and 'Country'
stat = st.sidebar.selectbox("Select Statistic", ['max', 'min', 'mean', 'sum', 'count'])

# Function to compute statistics
def compute_statistics(continent, data_type, stat):
    continent_data = df[df['Continent'] == continent]
    
    if stat == 'max':
        result = continent_data[data_type].max()
        country = continent_data.loc[continent_data[data_type].idxmax(), 'Country']
        return f"Max {data_type} in {continent}: {int(result)} (Country: {country})"
    
    elif stat == 'min':
        result = continent_data[data_type].min()
        country = continent_data.loc[continent_data[data_type].idxmin(), 'Country']
        return f"Min {data_type} in {continent}: {int(result)} (Country: {country})"
    
    elif stat == 'mean':
        result = continent_data[data_type].mean()
        return f"Mean {data_type} in {continent}: {int(result)}"
    
    elif stat == 'sum':
        result = continent_data[data_type].sum()
        return f"Total {data_type} in {continent}: {int(result)}"
    
    elif stat == 'count':
        result = continent_data[data_type].count()
        return f"Number of Countries in {continent}: {int(result)}"

# Display results
if st.sidebar.button("Compute Statistic"):
    if continent and data_type and stat:
        result = compute_statistics(continent, data_type, stat)
        st.success(result)
    else:
        st.error("Please fill all the filters.")

# Display continent info
st.header("Continent Information")
num_continents = df['Continent'].nunique()
continents = df['Continent'].unique()
st.write(f"Number of Continents: {num_continents}")
st.write("List of Continents:", ", ".join(continents))

# Display raw data (optional)
if st.checkbox("Show Raw Data"):
    st.write(df)