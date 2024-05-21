import os
import pickle
import joblib
import streamlit as st
from streamlit_option_menu import option_menu
from joblib import load

st.set_page_config(page_title="DemandAnalyzer",
                   layout="wide",
                   page_icon="🏪")

working_dir = os.path.dirname(os.path.abspath(__file__))  




st.markdown(
    """
    <style>
    .stSelectbox:after {
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    
product_sales = {
    'Amul-Cheese': {'Week-3 Sales': '7x100 Boxes', 'Week-2 Sales': '6x100 Boxes', 'Week-1 Sales': '5x100 Boxes', 'Week Sales': '10x100 Boxes',
                    'Week+1 Sales': '7x100 Boxes', 'Week+2 Sales': '10x100 Boxes', 'Week+3 Sales': '8x100 Boxes', 'Week+4 Sales': '10x100 Boxes'},
    'Horlicks': {'Week-3 Sales': '5x100 Boxes', 'Week-2 Sales': '1x100 Boxes', 'Week-1 Sales': '6x100 Boxes', 'Week Sales': '8x100 Boxes',
                 'Week+1 Sales': '4x100 Boxes', 'Week+2 Sales': '4x100 Boxes', 'Week+3 Sales': '5x100 Boxes', 'Week+4 Sales': '5x100 Boxes'},
    'Britannia': {'Week-3 Sales': '14x100 Boxes', 'Week-2 Sales': '8x100 Boxes', 'Week-1 Sales': '8x100 Boxes', 'Week Sales': '7x100 Boxes',
                  'Week+1 Sales': '10x100 Boxes', 'Week+2 Sales': '9x100 Boxes', 'Week+3 Sales': '9x100 Boxes', 'Week+4 Sales': '10x100 Boxes'},
    'Bosts Bread': {'Week-3 Sales': '14x100 Boxes', 'Week-2 Sales': '8x100 Boxes', 'Week-1 Sales': '7x100 Boxes', 'Week Sales': '8x100 Boxes',
                    'Week+1 Sales': '9x100 Boxes', 'Week+2 Sales': '9x100 Boxes', 'Week+3 Sales': '8x100 Boxes', 'Week+4 Sales': '10x100 Boxes'},
    'Aavin Milk': {'Week-3 Sales': '5x100 Boxes', 'Week-2 Sales': '11x100 Boxes', 'Week-1 Sales': '8x100 Boxes', 'Week Sales': '9x100 Boxes',
                   'Week+1 Sales': '9x100 Boxes', 'Week+2 Sales': '7x100 Boxes', 'Week+3 Sales': '11x100 Boxes', 'Week+4 Sales': '10x100 Boxes'},
    'Pepsodent': {'Week-3 Sales': '3x100 Boxes', 'Week-2 Sales': '3x100 Boxes', 'Week-1 Sales': '10x100 Boxes', 'Week Sales': '6x100 Boxes',
                  'Week+1 Sales': '6x100 Boxes', 'Week+2 Sales': '6x100 Boxes', 'Week+3 Sales': '5x100 Boxes', 'Week+4 Sales': '6x100 Boxes'},
    'Expresso': {'Week-3 Sales': '2x100 Boxes', 'Week-2 Sales': '4x100 Boxes', 'Week-1 Sales': '2x100 Boxes', 'Week Sales': '1x100 Boxes',
                 'Week+1 Sales': '3x100 Boxes', 'Week+2 Sales': '3x100 Boxes', 'Week+3 Sales': '4x100 Boxes', 'Week+4 Sales': '3x100 Boxes'},
    'Dove': {'Week-3 Sales': '7x100 Boxes', 'Week-2 Sales': '4x100 Boxes', 'Week-1 Sales': '9x100 Boxes', 'Week Sales': '9x100 Boxes',
             'Week+1 Sales': '9x100 Boxes', 'Week+2 Sales': '8x100 Boxes', 'Week+3 Sales': '9x100 Boxes', 'Week+4 Sales': '8x100 Boxes'},
    'Saffola': {'Week-3 Sales': '10x100 Boxes', 'Week-2 Sales': '12x100 Boxes', 'Week-1 Sales': '7x100 Boxes', 'Week Sales': '13x100 Boxes',
                'Week+1 Sales': '9x100 Boxes', 'Week+2 Sales': '9x100 Boxes', 'Week+3 Sales': '10x100 Boxes', 'Week+4 Sales': '8x100 Boxes'},
    'Mr.White': {'Week-3 Sales': '20x100 Boxes', 'Week-2 Sales': '18x100 Boxes', 'Week-1 Sales': '23x100 Boxes', 'Week Sales': '18x100 Boxes',
                 'Week+1 Sales': '22x100 Boxes', 'Week+2 Sales': '25x100 Boxes', 'Week+3 Sales': '23x100 Boxes', 'Week+4 Sales': '25x100 Boxes'}
}



with st.sidebar:
    selected_product = st.selectbox('Demand Predictor',
                                    ['Sales Activity','Amul-Cheese', 'Horlicks', 'Britannia', 'Bosts Bread', 'Aavin Milk',
                                     'Pepsodent', 'Expresso', 'Dove', 'Saffola', 'Mr.White'],
                                    index=0,
                                    help='Select a product to predict demand.')

if selected_product:
    st.title(f'{selected_product} past 4 weeks record')
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.info('Week-3 Sales')
        st.info(product_sales[selected_product]['Week-3 Sales'])

    with col2:
        st.info('Week-2 Sales')
        st.info(product_sales[selected_product]['Week-2 Sales'])

    with col3:
        st.info('Week-1 Sales')
        st.info(product_sales[selected_product]['Week-1 Sales'])

    with col4:
        st.info('Week Sales')
        st.info(product_sales[selected_product]['Week Sales'])

    st.markdown("---")
    st.title('Forecast for next 4 weeks')
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.info('Week+1 Sales')
        st.info(product_sales[selected_product]['Week+1 Sales'])

    with col2:
        st.info('Week+2 Sales')
        st.info(product_sales[selected_product]['Week+2 Sales'])

    with col3:
        st.info('Week+3 Sales')
        st.info(product_sales[selected_product]['Week+3 Sales'])

    with col4:
        st.info('Week+4 Sales')
        st.info(product_sales[selected_product]['Week+4 Sales'])
    

      





