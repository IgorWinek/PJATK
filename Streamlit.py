##### IMPORT BIBLIOTEK #####
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import time
import matplotlib.pyplot as plt

##### UTWORZENIE ZAKŁADEK #####
st.set_page_config(layout = "wide")
page = st.sidebar.selectbox('Select page',['Ankieta','Staty']) 
plot_list = ["line plot", "distributions"]

##### ZAKŁADKA ANKIETA #####
if page == 'Ankieta':
	firstname = st.text_input("Please, enter your 1st name", "")
	secname = st.text_input("Please, enter your 2st name", "")
	name = firstname + " " + secname
	if st.button("Submit"):
	    result = name.title()
	    st.success(result)

##### ZAKŁADKA STATY #####
else:
	with st.spinner("Waiting..."):
		data = st.file_uploader("Upload your dataset", type=['csv'])
		time.sleep(3)
	
	if data is not None:
	    	df = pd.read_csv(data)
	    	st.dataframe(df.head(10))

	all_columns_names = df.columns.to_list()
	selected_plot = st.selectbox("Select kind of plot", plot_list)
	selected_column_names = st.selectbox("First data", all_columns_names)

	if selected_plot == "line plot":
		st.line_chart(df[selected_column_names])
	elif selected_plot == "distributions":
		st.write(selected_column_names+" distribution")
		fig, ax = plt.subplots()
		ax.hist(df[selected_column_names], bins=30)
		st.pyplot(fig)
	else:
		pass

	



