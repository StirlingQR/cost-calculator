import streamlit as st

# Page setup
st.set_page_config(page_title="Agency vs. DIY Hire Cost", layout="centered")
st.title("Agency vs. DIY: QA/RA Hire Cost Comparison")

st.markdown("""
Use the sidebar to adjust your inputs, then compare:

- **Agency**: one flat placement fee  
- **DIY**: LinkedIn, phone, job ads, internal recruiter time  
- **Vacancy cost**: days position remains open
""")

# ── Sidebar Inputs ──
with st.sidebar:
    st.header("Inputs")
    salary       = st.number_input("£ Annual salary", value=60000.0, step=1000.0, format="%.2f")
    fee_pct      = st.slider("Agency fee (% of salary)", min_value=0, max_value=30, value=20, step=1)
    num_ads      = st.number_input("Job adverts (qty)", min_value=1, max_value=10, value=3, step=1)
    recruiter_hr = st.number_input("In-house recruiter rate (£/hr)", value=19.0, step=0.5, format="%.2f")
    recruiter_hrs= st.number_input("Recruiter hours per hire", value=40.0, step=1.0, format="%.1f")
    days_open    = st.number_input("Days open so far", value=15, step=1)

# ── Constants ──
LINKEDIN_COST       = 1680    # £/yr seat
PHONE_COST          = 300     # £/yr softphone
AD_COST             = 180     # £ per advert
WORKING_DAYS_PER_YR = 250

# ── Calculations ──
agency_cost = (fee_pct / 100) * salary

diy_linkedin   = LINKEDIN_COST
diy_phone      = PHONE_COST
diy_ads        = AD_COST * num_ads
diy_recruit    = recruiter_hr * recruiter_hrs

daily_salary   = salary / WORKING_DAYS_PER_YR
vacancy_cost   = daily_salary * days_open

# Totals
diy_total_short   = diy_linkedin + diy_phone + diy_ads + diy_recruit
diy_total_with_vac = diy_total_short + vacancy_cost

# ── Output ──
col1, col2 = st.columns(2)

with col1:
    st.subheader("Agency Hire")
    st.write(f"- Placement fee: **£{agency_cost:,.0f}**")

with col2:
    st.subheader("DIY Hire")
    st.write(f"- LinkedIn seat:      £{diy_linkedin:,.0f}")
    st.write(f"- Phone system:       £{diy_phone:,.0f}")
    st.write(f"- Job adverts ({num_ads}): £{diy_ads:,.0f}")
    st.write(f"- Recruiter time:     £{diy_recruit:,.0f}")
    st.write(f"- Vacancy cost ({days_open}d): £{vacancy_cost:,.0f}")
    st.markdown(f"**Total DIY:** **£{diy_total_with_vac:,.0f}**")

st.markdown("---")
st.subheader("Key Insight")
if agency_cost > diy_total_with_vac:
    st.success(
        f"DIY (£{diy_total_with_vac:,.0f}) is still cheaper than agency (£{agency_cost:,.0f}), "
        "but lacks speed, guarantees, and specialist reach."
    )
else:
    st.success(
        f"Agency (£{agency_cost:,.0f}) may cost more upfront than DIY (£{diy_total_with_vac:,.0f}), "
        "but it speeds hiring, reduces vacancy drag, and mitigates compliance risk."
    )
