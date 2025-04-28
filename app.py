import streamlit as st

# Page config
st.set_page_config(page_title="Agency vs. DIY Hire Cost", layout="centered")
st.title("Agency vs. DIY: QA/RA Hire Cost Comparison")

st.markdown("""
Adjust the inputs below to compare **short-term** hiring costs,  
and then see the **long-term** impact once you add a typical FDA 483 remediation fee.
""")

# — Inputs in sidebar —
with st.sidebar:
    st.header("Role & Fee Inputs")
    salary = st.number_input("Annual salary (£)", value=60000.0, step=1000.0, format="%.2f")
    fee_pct = st.slider("Agency fee (% of salary)", 0, 30, 20)
    num_ads = st.number_input("Job adverts (qty)", 1, 10, 3)
    recruiter_hr = st.number_input("In-house recruiter rate (£/hr)", value=19.0, step=0.5)
    recruiter_hrs = st.number_input("Recruiter hours/hire", value=40.0, step=1.0)

# — Constants (UK market averages) —
LINKEDIN_COST       = 1680    # £/yr for Recruiter Lite :contentReference[oaicite:3]{index=3}
PHONE_COST          = 300     # £/yr at ~£25/mo :contentReference[oaicite:4]{index=4}
AD_COST             = 180     # £ per advert (avg. £89+VAT first, £219+VAT repeat) 
FDA_483_REMEDIATION = 250000  # average cost of a moderate Form 483 response :contentReference[oaicite:5]{index=5}

# — Short-term calculations —
agency_cost = (fee_pct / 100) * salary  # e.g. 20% of £60k = £12k :contentReference[oaicite:6]{index=6}

diy_linkedin  = LINKEDIN_COST
diy_phone     = PHONE_COST
diy_ads       = AD_COST * num_ads
diy_recruiter = recruiter_hr * recruiter_hrs
diy_short     = diy_linkedin + diy_phone + diy_ads + diy_recruiter

# — Long-term: DIY + compliance risk —
diy_long = diy_short + FDA_483_REMEDIATION

# — Display —
col1, col2 = st.columns(2)

with col1:
    st.subheader("Short-Term: Agency")
    st.write(f"- Placement fee ({fee_pct}% of £{salary:,.0f}): £{agency_cost:,.0f}")

with col2:
    st.subheader("Short-Term: DIY")
    st.write(f"- LinkedIn seat: £{diy_linkedin:,.0f}")
    st.write(f"- Phone system: £{diy_phone:,.0f}")
    st.write(f"- Job adverts ({num_ads}×): £{diy_ads:,.0f}")
    st.write(f"- Recruiter time: £{diy_recruiter:,.0f}")
    st.write(f"**Total DIY:** £{diy_short:,.0f}")

st.markdown("---")
st.subheader("Long-Term Comparison")

col3, col4 = st.columns(2)
with col3:
    st.write(f"• **Agency cost** stays at £{agency_cost:,.0f}")
with col4:
    st.write(f"• **DIY + 483 remediation**: £{diy_long:,.0f}")

st.markdown("""
> **Takeaway:** While DIY might look cheaper upfront (£{:,}),  
> once you factor in an average £{:,.0f} FDA 483 hit,  
> partnering with a specialist recruiter is **less costly** over time.
""".format(int(diy_short), FDA_483_REMEDIATION))
