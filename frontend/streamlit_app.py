import streamlit as st
import requests

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

import os

FASTAPI_URL = os.getenv(
    "FASTAPI_URL",
    "http://127.0.0.1:8000/predict"
)

st.title("📊 Customer Churn Prediction System")
st.write("Enter the customer details below and click **Predict Churn**.")

# -------------------------------
# Sidebar Inputs
# -------------------------------

st.sidebar.header("Customer Details")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

SeniorCitizen = st.sidebar.selectbox(
    "Senior Citizen",
    [0, 1]
)

Partner = st.sidebar.selectbox(
    "Partner",
    ["Yes", "No"]
)

Dependents = st.sidebar.selectbox(
    "Dependents",
    ["Yes", "No"]
)

tenure = st.sidebar.slider(
    "Tenure (Months)",
    0,
    72,
    12
)

PhoneService = st.sidebar.selectbox(
    "Phone Service",
    ["Yes", "No"]
)

MultipleLines = st.sidebar.selectbox(
    "Multiple Lines",
    ["Yes", "No", "No phone service"]
)

InternetService = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.sidebar.selectbox(
    "Online Security",
    ["Yes", "No", "No internet service"]
)

OnlineBackup = st.sidebar.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)

DeviceProtection = st.sidebar.selectbox(
    "Device Protection",
    ["Yes", "No", "No internet service"]
)

TechSupport = st.sidebar.selectbox(
    "Tech Support",
    ["Yes", "No", "No internet service"]
)

StreamingTV = st.sidebar.selectbox(
    "Streaming TV",
    ["Yes", "No", "No internet service"]
)

StreamingMovies = st.sidebar.selectbox(
    "Streaming Movies",
    ["Yes", "No", "No internet service"]
)

Contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.sidebar.selectbox(
    "Paperless Billing",
    ["Yes", "No"]
)

PaymentMethod = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

MonthlyCharges = st.sidebar.number_input(
    "Monthly Charges",
    min_value=0.0,
    max_value=200.0,
    value=70.0
)

TotalCharges = st.sidebar.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

# -------------------------------
# Predict Button
# -------------------------------

if st.sidebar.button("Predict Churn"):

    customer = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    with st.spinner("Predicting..."):

        try:

            response = requests.post(
                FASTAPI_URL,
                json=customer
            )

            if response.status_code == 200:

                result = response.json()

                prediction = result["prediction"]
                probability = result["probability"]

                st.success("Prediction Completed")

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("Prediction")

                    if prediction == "Churn":
                        st.error("🔴 Customer is likely to Churn")
                    else:
                        st.success("🟢 Customer is likely to Stay")

                with col2:

                    st.subheader("Probability")

                    st.metric(
                        "Churn Probability",
                        f"{probability}%"
                    )

                    st.progress(probability / 100)

                st.divider()

                st.subheader("Business Recommendation")

                if probability >= 80:

                    st.error("High Risk Customer")

                    st.write("✅ Offer Loyalty Discount")
                    st.write("✅ Assign Premium Support")
                    st.write("✅ Schedule Retention Call")

                elif probability >= 50:

                    st.warning("Medium Risk Customer")

                    st.write("✅ Send Promotional Offers")
                    st.write("✅ Contact Customer")
                    st.write("✅ Offer Better Plan")

                else:

                    st.success("Low Risk Customer")

                    st.write("✅ Customer is Loyal")
                    st.write("✅ Continue Regular Engagement")
                    st.write("✅ Recommend New Services")

            else:

                st.error("Prediction Failed")
                st.write(response.text)

        except Exception as e:

            st.error("Could not connect to FastAPI Server")
            st.write(e)

import pandas as pd
st.divider()

st.header("📂 Bulk Customer Prediction")

uploaded_file = st.file_uploader(
    "Upload Customer CSV",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    if st.button("Predict All Customers"):

        predictions = []
        probabilities = []

        progress = st.progress(0)

        for i, row in df.iterrows():

            response = requests.post(
                FASTAPI_URL,
                json=row.to_dict()
            )

            if response.status_code != 200:
                st.error(f"Error on row {i+1}")
                st.write(response.text)
                st.stop()

            result = response.json()

            predictions.append(result["prediction"])
            probabilities.append(result["probability"])

            progress.progress((i + 1) / len(df))

        progress.empty()

        df["Prediction"] = predictions
        df["Probability"] = probabilities

        st.success("Prediction Completed!")

        st.dataframe(df)

        csv = df.to_csv(index=False)

        st.download_button(
            "📥 Download Predictions",
            csv,
            "customer_predictions.csv",
            "text/csv"
        )

        # ---------------- KPIs ----------------

        high_risk = len(df[df["Prediction"] == "Churn"])
        low_risk = len(df[df["Prediction"] == "No Churn"])
        avg_probability = round(df["Probability"].mean(), 2)
        total_customers = len(df)

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Customers", total_customers)
        col2.metric("High Risk", high_risk)
        col3.metric("Low Risk", low_risk)
        col4.metric("Avg Probability", f"{avg_probability}%")

        # ---------------- Charts ----------------

        import plotly.express as px

        fig = px.pie(
            df,
            names="Prediction",
            title="Customer Prediction Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(
            df,
            x="Probability",
            nbins=20,
            title="Probability Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        contract_risk = (
            df.groupby("Contract")["Probability"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            contract_risk,
            x="Contract",
            y="Probability",
            title="Average Churn Probability by Contract"
        )

        st.plotly_chart(fig, use_container_width=True)

        high_risk_df = (
            df.sort_values(
                by="Probability",
                ascending=False
            )
            .head(10)
        )

        st.subheader("Top 10 High Risk Customers")
        st.dataframe(high_risk_df)

        st.subheader("Business Insights")

        st.info(f"""
**Total Customers Analysed:** {total_customers}

**High Risk Customers:** {high_risk}

**Average Churn Probability:** {avg_probability}%

**Recommendation:** Contact high-risk customers first with retention offers.
""")