import streamlit as st
# from dashboard import func
from model import get_total_area, get_usable_area
from energy import get_radiation_data

def main():
   st.title("Ecoverse")
   st.header("Helping in your solar energy journey")

    # Create a form
   with st.form(key='my_form'):
      address = st.text_input(label='Enter your address', placeholder= '555 California Street, San Francisco')
      # my total sqft area is 500 and usable sqft area is 350
      description = st.text_area(label='Tell us about your location', placeholder= 'What is the sq ft area, What is the usable area, Near San Marie Square')

        # Create a submit button
      submit_button = st.form_submit_button(label='Submit')

    # Display the data after submission
   if submit_button:
      if address:
         st.write(f"Your address: {address}")
      if description:
         # extracted sqft information from LLM
         # sqft = get_total_area(description)
         sqft = 100
         # usqft = get_usable_area(description)
         radiation_data = get_radiation_data(37.792072824760965, 122.40419151380131, sqft)
         st.table(data=radiation_data)
         # st.write(f"Information: {description}")

if __name__ == "__main__":
   main()
