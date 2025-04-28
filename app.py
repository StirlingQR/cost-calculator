import streamlit as st

# Page setup
st.set_page_config(page_title="Agency vs. DIY Hire Cost", layout="centered")
st.title("Agency vs. DIY: QA/RA Hire Cost Comparison")

st.markdown("""
Compare the cost of using a recruitment agency against doing it yourself.  
Adjust the inputs on the left, and see the split-screen results.
""")

# — Inputs — 
with st.sidebar:
    st.header("Inputs")
    salary = st.number_input(
        "Annual salary of the role (£)", 
        min_value=0.0, value=60000.0, step=1000.0, format="%.2f"
    )
    fee_pct = st.slider(
        "Agency fee (% of salary)", 
        min_value=0, max_value=30, value=20, step=1
    )
    num_ads = st.number_input(
        "Number of job adverts", 
        min_value=1, max_value=10, value=3, step=1
    )
    recruiter_hr_rate = st.number_input(
        "In-house recruiter rate (£/hr)", 
        min_value=0.0, value=19.0, step=0.5, format="%.2f"
    )
    recruiter_hours = st.number_input(
        "Hours spent on hire", 
        min_value=0.0, value=40.0, step=1.0, format="%.1f"
    )

# — Constants — 
LINKEDIN_COST = 1680         # £/yr for Recruiter Lite :contentReference[oaicite:6]{index=6}
PHONE_COST    = 300          # £/yr at ~£25/mo :contentReference[oaicite:7]{index=7}
AD_COST       = 180          # £ per advert (avg. £89+VAT first, £219+VAT repeat) :contentReference[oaicite:8]{index=8}

# — Calculations — 
agency_cost = (fee_pct / 100) * salary

diy_linkedin   = LINKEDIN_COST
diy_phone      = PHONE_COST
diy_ads        = AD_COST * num_ads
diy_recruiter  = recruiter_hr_rate * recruiter_hours
diy_total      = diy_linkedin + diy_phone + diy_ads + diy_recruiter

# — Layout — 
col1, col2 = st.columns(2)

with col1:
    st.header("Agency Hire Cost")
    st.write(f"- **Fee ({fee_pct}% of £{salary:,.2f}):** £{agency_cost:,.2f}")
    st.markdown("> *Typical permanent placement fee range: 15–20% (up to 30% for niche roles)* :contentReference[oaicite:9]{index=9}")

with col2:
    st.header("DIY Hire Cost")
    st.write(f"- LinkedIn Recruiter: **£{diy_linkedin:,.0f}**")
    st.write(f"- Phone system: **£{diy_phone:,.0f}**")
    st.write(f"- Job adverts ({num_ads} × £{AD_COST}): **£{diy_ads:,.0f}**")
    st.write(f"- In-house recruiter ({recruiter_hours} h @ £{recruiter_hr_rate}/h): **£{diy_recruiter:,.0f}**")
    st.markdown(f"**Total DIY cost:** £{diy_total:,.2f}")

st.markdown("---")
st.subheader("Short-Term Loss vs. Long-Term Gain")

if agency_cost > diy_total:
    st.success(
        f"DIY (£{diy_total:,.2f}) is cheaper upfront than agency (£{agency_cost:,.2f}), "
        "but lacks the speed, guarantees, and specialist reach."
    )
else:
    st.success(
        f"Agency (£{agency_cost:,.2f}) may cost more than DIY (£{diy_total:,.2f}), "
        "but delivers faster hires and reduces compliance risk."
    )
