import datetime
import joblib
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
        page_title="INDUSTRIAL COPPER MODELING",
        page_icon="🏦",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={'About': """# This app is created by *Subash*!"""}
    )

st.markdown("<h1 style='text-align: center; color: #86c5tb;'>INDUSTRIAL COPPER MODELING</h1>", unsafe_allow_html=True)

selected = option_menu(None, ["HOME", "PRICE PREDICTION", "STATUS"],
                       icons=["house", "cash-coin", "trophy"],
                       default_index=0,
                       orientation="horizontal",
                       styles={"nav-link": {"font-size": "35px", "text-align": "center", "margin": "0px",
                                           "--hover-color": "#6495ED"},
                               "icon": {"font-size": "30px"},
                               "container": {"max-width": "6000px"},
                               "nav-link-selected": {"background-color": "#93cbf2"}})

if selected == 'HOME':

    st.markdown(
        """
        <style>
        .home-card {
            padding: 25px;
            border-radius: 18px;
            background-color: #f8f9fa;
            box-shadow: 0px 6px 14px rgba(0,0,0,0.08);
            height: 100%;
        }
        .home-title {
            font-size: 34px;
            font-weight: 700;
            color: #2c3e50;
        }
        .home-subtitle {
            font-size: 17px;
            color: #555;
            line-height: 1.6;
        }
        .section-header {
            font-size: 22px;
            font-weight: 600;
            color: #1f4e79;
            margin-bottom: 12px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="home-card">
            <div class="home-title">🏭 Industrial Copper Modeling</div>
            <p class="home-subtitle">
                This application leverages machine learning techniques to analyze and model
                industrial copper sales data. It supports both price prediction and deal
                outcome classification using robust preprocessing and tree-based models.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="home-card">
                <div class="section-header">🧰 Technology Stack</div>
                <ul class="home-subtitle">
                    <li>Python (Pandas, NumPy)</li>
                    <li>Scikit-learn</li>
                    <li>Exploratory Data Analysis (EDA)</li>
                    <li>Feature Engineering & Preprocessing</li>
                    <li>Model Serialization (Pickle / Joblib)</li>
                    <li>Streamlit Web Application</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="home-card">
                <div class="section-header">🤖 Machine Learning Models</div>
                <p class="home-subtitle">
                    <strong>Regression Model</strong><br>
                    Random Forest Regressor trained to predict the selling price of copper
                    based on transactional and product-level features.
                </p>
                <p class="home-subtitle">
                    <strong>Classification Model</strong><br>
                    Decision Tree Classifier designed to predict whether a deal is
                    <em>Won</em> or <em>Lost</em>.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    st.markdown(
        """
        <div class="home-card">
            <div class="section-header">🎯 Project Objective</div>
            <p class="home-subtitle">
                The primary goal of this project is to demonstrate an end-to-end machine
                learning pipeline — from data cleaning and transformation to model training,
                evaluation, and real-time inference through an interactive web interface.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )



if selected == 'PRICE PREDICTION':

    st.markdown(
        """
        <style>
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #f8f9fa;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🔮 Copper Price Prediction Dashboard")

    item_list = ['W', 'S', 'Others', 'PL', 'WI', 'IPL']
    status_list = ['Won', 'Lost']
    country_list = [28, 32, 38, 78, 27, 30, 25, 77, 39, 40, 26, 84, 80, 79, 113, 89]

    application_list = [10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66,
                        29, 22, 40, 25, 67, 79, 3, 99, 2, 5, 39, 69, 70, 65, 58, 68]

    product_list = [1670798778, 1668701718, 628377, 640665, 611993, 1668701376,
                    164141591, 1671863738, 1332077137, 640405, 1693867550, 1665572374,
                    1282007633, 1668701698, 628117, 1690738206, 628112, 640400,
                    1671876026, 164336407, 164337175, 1668701725, 1665572032, 611728,
                    1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
                    1665584320, 1665584662, 1665584642]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>📦 Product Details</div>", unsafe_allow_html=True)

        quantity = st.slider(
            'Quantity (tons)',
            min_value=611728,
            max_value=1722207579,
            value=611728,
            step=1000
        )

        thickness = st.slider(
            'Thickness',
            min_value=0.18,
            max_value=400.0,
            value=1.0,
            step=0.1
        )

        width = st.slider(
            'Width',
            min_value=1,
            max_value=2990,
            value=100,
            step=1
        )

        product = st.selectbox("Product Reference", product_list)
        application = st.selectbox("Application Type", application_list)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🌍 Order Information</div>", unsafe_allow_html=True)

        country = st.selectbox("Country Code", country_list)
        status = st.selectbox("Status", status_list)
        item = st.selectbox("Item Type", item_list)

        item_order_date = st.date_input("Order Date", datetime.date(2021, 1, 1))
        item_delivery_date = st.date_input("Delivery Date", datetime.date(2021, 1, 1))

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    col_btn, col_result = st.columns([1, 3])

    with col_btn:
        if st.button("🚀 Predict Price", use_container_width=True):

            order_year = item_order_date.year
            order_month = item_order_date.month
            order_day = item_order_date.day

            del_year = item_delivery_date.year
            del_month = item_delivery_date.month
            del_day = item_delivery_date.day

            delivery_time = (item_delivery_date - item_order_date).days

            ohe = joblib.load('ohe.pkl')

            a = pd.DataFrame([{
                'status': status,
                'item_type': item
            }])

            s = ohe.transform(a)
            categorical_feature_cols = ['status', 'item_type']
            X_cat = pd.DataFrame(
                s,
                columns=ohe.get_feature_names_out(categorical_feature_cols)
            )

            X_num = pd.DataFrame([{
                'quantity_tons': quantity,
                'country': country,
                'application': application,
                'thickness': thickness,
                'width': width,
                'product_ref': product,
                'delivery_time': delivery_time,
                'delivery_year': del_year,
                'delivery_month': del_month,
                'delivery_day': del_day,
                'item_year': order_year,
                'item_month': order_month,
                'item_day': order_day
            }])

            X_final = pd.concat([X_num, X_cat], axis=1)

            with open('reg_model.pkl', 'rb') as file:
                model = pickle.load(file)

            y_pred = model.predict(X_final)

            st.session_state["prediction"] = y_pred[0]

    with col_result:
        if "prediction" in st.session_state:
            st.markdown(
                f"""
                <div class='card'>
                    <div class='section-title'>💰 Predicted Selling Price</div>
                    <h1 style='color:#27ae60;'>₹ {st.session_state["prediction"]:.2f}</h1>
                </div>
                """,
                unsafe_allow_html=True
            )

if selected == 'STATUS':       
    st.markdown(
        """
        <style>
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #f8f9fa;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 22px;
            font-weight: 600;
            color: #2c3e50;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🔮 Copper Status Prediction Dashboard")
    item_list = ['W', 'S', 'Others', 'PL', 'WI', 'IPL']
    country_list = [28, 32, 38, 78, 27, 30, 25, 77, 39, 40, 26, 84, 80, 79, 113, 89]

    application_list = [10, 41, 28, 59, 15, 4, 38, 56, 42, 26, 27, 19, 20, 66,
                        29, 22, 40, 25, 67, 79, 3, 99, 2, 5, 39, 69, 70, 65, 58, 68]

    product_list = [1670798778, 1668701718, 628377, 640665, 611993, 1668701376,
                    164141591, 1671863738, 1332077137, 640405, 1693867550, 1665572374,
                    1282007633, 1668701698, 628117, 1690738206, 628112, 640400,
                    1671876026, 164336407, 164337175, 1668701725, 1665572032, 611728,
                    1721130331, 1693867563, 611733, 1690738219, 1722207579, 929423819,
                    1665584320, 1665584662, 1665584642]
    
    cc1, cc2 = st.columns([2, 2])
    with cc1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>📦 Product Details</div>", unsafe_allow_html=True)

        quantity = st.slider(
            'Quantity (tons)',
            min_value=611728,
            max_value=1722207579,
            value=611728,
            step=1000
        )

        thickness = st.slider(
            'Thickness',
            min_value=0.18,
            max_value=400.0,
            value=1.0,
            step=0.1
        )

        width = st.slider(
            'Width',
            min_value=1,
            max_value=2990,
            value=100,
            step=1
        )
        price = st.slider(
            'Selling Price',
            min_value=0.1,
            max_value=10913.0,
            value=100.0,
            step=1.0
        )
        application = st.selectbox("Application Type", application_list)


    with cc2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🌍 Order Information</div>", unsafe_allow_html=True)

        country = st.selectbox("Country Code", country_list)
        item = st.selectbox("Item Type", item_list)

        item_order_date = st.date_input("Order Date", datetime.date(2021, 1, 1))
        item_delivery_date = st.date_input("Delivery Date", datetime.date(2021, 1, 1))

        product = st.selectbox("Product Reference", product_list)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")


    st.markdown("</div>", unsafe_allow_html=True)

    if st.button('Predict Status'):

        order_year = item_order_date.year
        order_month = item_order_date.month
        order_day = item_order_date.day

        del_year = item_delivery_date.year
        del_month = item_delivery_date.month
        del_day = item_delivery_date.day

        delivery_time = (item_delivery_date - item_order_date).days

        ohe = joblib.load('ohe_cla.pkl')

        a = pd.DataFrame([{
            'item_type': item
        }])

        s = ohe.transform(a)
        categorical_feature_cols = ['item_type']
        X_cat = pd.DataFrame(
            s,
            columns=ohe.get_feature_names_out(categorical_feature_cols)
        )

        X_num = pd.DataFrame([{
            'quantity_tons': quantity,
            'country': country,
            'application': application,
            'thickness': thickness,
            'width': width,
            'product_ref': product,
            'selling_price':price,
            'delivery_time': delivery_time,
            'delivery_year': del_year,
            'delivery_month': del_month,
            'delivery_day': del_day,
            'item_year': order_year,
            'item_month': order_month,
            'item_day': order_day
        }])


        X_final = pd.concat([X_num, X_cat], axis=1)

        with open('cla_model.pkl', 'rb') as file:
            model = pickle.load(file)

        y_pred = model.predict(X_final)

        if y_pred==1:
            st.write(f'Predicted Status : :green[WON]')
        else:
            st.write(f'Predicted Status : :red[LOST]')



  
