import streamlit as st

st.set_page_config(page_title="QA/RA Hire vs. Non-Hire Cost Calculator", layout="centered")

st.title("QA/RA: Hire Cost vs. Non-Hire Financial Impact")

st.markdown("""
Enter the annual salary and agency fee % to see your hiring cost,  
then add a delay duration (in months) to estimate the market-delay cost.  
We’ll also show the typical cost of an inspection failure or recall.
""")

# ——— User Inputs ———
salary = st.number_input("Annual salary of the role (USD)", min_value=0.0, value=60000.0, step=1000.0, format="%.2f")
fee_pct = st.slider("Agency fee (% of salary)", min_value=0, max_value=50, value=20, step=1)
delay_months = st.number_input("Potential delay (months)", min_value=0, value=1, step=1)

# ——— Core Calculations ———
hire_cost = (fee_pct / 100) * salary

# Constants
INSPECTION_FAILURE_COST = 600_000_000  # per incident (USD)
DAILY_DELAY_COST = 800_000            # USD per day
DELAY_MONTHLY_COST = DAILY_DELAY_COST * 30  # approx. USD per month

delay_cost = delay_months * DELAY_MONTHLY_COST
non_hire_cost = max(INSPECTION_FAILURE_COST, delay_cost)

# ——— Results Display ———
st.markdown("---")
st.subheader("🔍 Results")

st.write(f"• **Cost to hire**: USD {hire_cost:,.2f}")
st.write(f"• **Cost if inspection/recall occurs**: USD {INSPECTION_FAILURE_COST:,.0f}")
st.write(f"• **Cost if {delay_months} month(s) of market delay**: USD {delay_cost:,.0f}")

st.markdown("---")
st.subheader("💡 Short-Term Loss vs. Long-Term Gain")

if non_hire_cost > hire_cost:
    st.success(f"Investing USD {hire_cost:,.2f} now to hire a Quality/Regulatory expert can prevent potential losses of up to USD {non_hire_cost:,.0f}.")
else:
    st.info(f"Your hiring cost (USD {hire_cost:,.2f}) is on par with typical losses, but still helps avoid compliance risk.")
