import streamlit as st
import pandas as pd

st.set_page_config(page_title="QA/RA Cost-Per-Hire Calculator", layout="centered")

st.title("Quality & Regulatory Cost-Per-Hire + Risk Calculator")

st.markdown("""
Use this tool to estimate your true cost for recruiting a QA/RA professional,  
including recruitment fees, vacancy costs, and potential non-compliance risk.
""")

# 1. External Recruitment Costs
st.header("1. External Recruitment Costs")
ads = st.number_input("Advertising & job board fees (e.g. LinkedIn, pharma boards)", min_value=0.0, value=2000.0, step=100.0, format="%.2f")
background = st.number_input("Background checks & assessment fees", min_value=0.0, value=300.0, step=50.0, format="%.2f")
sourcing = st.number_input("Sourcing tool costs (LinkedIn Recruiter, subscriptions)", min_value=0.0, value=1000.0, step=100.0, format="%.2f")

external_costs = ads + background + sourcing

# 2. Internal Recruitment Costs
st.header("2. Internal Recruitment Costs")
rec_rate = st.number_input("Recruiter hourly rate (£)", min_value=0.0, value=50.0, step=5.0, format="%.2f")
rec_hours = st.number_input("Hours spent by recruiter", min_value=0.0, value=30.0, step=1.0, format="%.1f")
hm_rate = st.number_input("Hiring-manager hourly rate (£)", min_value=0.0, value=80.0, step=5.0, format="%.2f")
hm_hours = st.number_input("Hours spent by hiring manager (briefings + interviews)", min_value=0.0, value=10.0, step=1.0, format="%.1f")
onboard = st.number_input("Onboarding & training cost (£)", min_value=0.0, value=1500.0, step=100.0, format="%.2f")

internal_costs = (rec_rate * rec_hours) + (hm_rate * hm_hours) + onboard

# 3. Agency Fee
st.header("3. Agency (Placement) Fee")
salary = st.number_input("Annual salary of the role (£)", min_value=0.0, value=60000.0, step=1000.0, format="%.2f")
fee_pct = st.slider("Agency fee (% of first-year salary)", min_value=0, max_value=40, value=20, step=1)
agency_fee = (fee_pct / 100.0) * salary

# 4. Vacancy Costs
st.header("4. Vacancy Costs")
working_days = st.number_input("Working days per year", min_value=200, max_value=260, value=250, step=1)
days_vacant = st.number_input("Average days vacant", min_value=0, value=36, step=1)
avg_daily_revenue = st.number_input("Average daily revenue impact (£)", min_value=0.0, value=0.0, step=100.0, format="%.2f")
temp_overtime = st.number_input("Temp contractor / overtime costs (£)", min_value=0.0, value=2000.0, step=100.0, format="%.2f")

salary_vacancy_cost = (salary / working_days) * days_vacant
revenue_vacancy_cost = avg_daily_revenue * days_vacant
vacancy_costs = salary_vacancy_cost + revenue_vacancy_cost + temp_overtime

# 5. Cost of Non-Compliance (“No QA/RA”)
st.header("5. Risk of Non-Compliance")
noncompliance_cost = st.number_input("Avg. cost per non-compliance incident (£)", min_value=0.0, value=14820000.0, step=100000.0, format="%.2f")
risk_pct = st.slider("Estimated risk of incident (%)", min_value=0, max_value=100, value=5, step=1)
expected_noncompliance_cost = (risk_pct / 100.0) * noncompliance_cost

# Total Calculation
total_cost = external_costs + internal_costs + agency_fee + vacancy_costs + expected_noncompliance_cost

st.markdown("---")
st.subheader("🔎 Summary of Results")
st.write(f"**External Recruitment Costs:** £{external_costs:,.2f}")
st.write(f"**Internal Recruitment Costs:** £{internal_costs:,.2f}")
st.write(f"**Agency Fee ({fee_pct}%):** £{agency_fee:,.2f}")
st.write(f"**Vacancy Costs:** £{vacancy_costs:,.2f}")
st.write(f"**Expected Non-Compliance Cost (@ {risk_pct}%):** £{expected_noncompliance_cost:,.2f}")

st.markdown(f"## **Total Estimated Cost-Per-Hire:** £{total_cost:,.2f}")

# Optional: breakdown DataFrame
if st.checkbox("Show detailed breakdown table"):
    df = pd.DataFrame({
        "Category": [
            "Advertising & Boards",
            "Background Checks",
            "Sourcing Tools",
            "Recruiter Time",
            "Hiring-Manager Time",
            "Onboarding",
            "Agency Fee",
            "Salary Vacancy Cost",
            "Revenue Vacancy Cost",
            "Temp/Overtime Cost",
            "Expected Non-Compliance Cost"
        ],
        "Amount (£)": [
            ads,
            background,
            sourcing,
            rec_rate * rec_hours,
            hm_rate * hm_hours,
            onboard,
            agency_fee,
            salary_vacancy_cost,
            revenue_vacancy_cost,
            temp_overtime,
            expected_noncompliance_cost
        ]
    })
    st.table(df.style.format({"Amount (£)": "£{:,.2f}"}))
