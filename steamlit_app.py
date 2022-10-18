import streamlit
streamlit.title('my parents new health dinner')
streamlit.header('Breakfast Favorits')
streamlit.text('🥣 Omega 3 & blueberry Oatmeal')
streamlit.text('🥗  Kale, Spinach & rocket smooothie')
streamlit.text('🐔 Hard-Boiled Free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
