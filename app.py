# Create the Streamlit app code and requirements file for the updated calculator

# Write requirements.txt
requirements_txt = """\
streamlit>=1.20.0
"""

with open('/mnt/data/requirements.txt', 'w') as f:
    f.write(requirements_txt)

# Write app.py
app_py = """\
import streamlit as st

# Page configuration
st.set_page_config(page_title="Agency vs. DIY Hire Cost", layout="centered")
st.title("Agency vs. DIY: QA/RA Hire Cost Comparison")

st.markdown(\"\"\"
Adjust the inputs below to compare **short-term** hiring costs,  
and see how “time open so far” drives the DIY vacancy cost.
\"\"\")

# Input controls in sidebar
with st.sidebar:
    st.header("Inputs")
    salary = st.number_input("Annual salary (£)", value=60000.0, step=1000.0, format="%.2f")
    fee_pct = st.slider("Agency fee (% of salary)", 0, 30, 20)
    num_ads = st.number_input("Number of job adverts", 1, 10, 3)
    recruiter_hr = st.number_input("In-house recruiter rate (£/hr)", value=19.0, step=0.5)
    recruiter_hrs = st.number_input("Recruiter hours per hire", value=40.0, step=1.0)
    days_open = st.number_input("Days position has been open", value=15, step=1)

# Market-average constants
LINKEDIN_COST_PER_YEAR = 1680    # Recruiter Lite seat
PHONE_COST_PER_YEAR    = 300     # Softphone/VoIP per user
AD_COST                = 180     # Average per job advert
WORKING_DAYS_PER_YEAR  = 250

# Calculate agency cost
agency_cost = (fee_pct / 100) * salary

# Calculate DIY costs
diy_linkedin     = LINKEDIN_COST_PER_YEAR
diy_phone        = PHONE_COST_PER_YEAR
diy_ads          = AD_COST * num_ads
diy_recruit_time = recruiter_hr * recruiter_hrs

# Vacancy cost due to time open
daily_salary_cost = salary / WORKING_DAYS_PER_YEAR
vacancy_open_cost = daily_salary_cost * days_open

diy_total_short = diy_linkedin + diy_phone + diy_ads + diy_recruit_time
diy_total_with_vacancy = diy_total_short + vacancy_open_cost

# Layout: split screen for output
col1, col2 = st.columns(2)

with col1:
    st.subheader("Agency Hire")
    st.write(f"- Placement fee ({fee_pct}% of £{salary:,.0f}): £{agency_cost:,.0f}")
    st.markdown("**Total Agency Cost:**")
    st.write(f"### £{agency_cost:,.0f}")

with col2:
    st.subheader("DIY Hire")
    st.write(f"- LinkedIn Recruiter seat (yr): £{diy_linkedin:,.0f}")
    st.write(f"- Phone system (yr): £{diy_phone:,.0f}")
    st.write(f"- Job adverts ({num_ads}×): £{diy_ads:,.0f}")
    st.write(f"- Recruiter time ({recruiter_hrs}h): £{diy_recruit_time:,.0f}")
    st.write(f"- Vacancy cost ({days_open}d open): £{vacancy_open_cost:,.0f}")
    st.markdown("**Total DIY Cost:**")
    st.write(f"### £{diy_total_with_vacancy:,.0f}")

st.markdown("---")
st.subheader("Key Insight")
if agency_cost > diy_total_with_vacancy:
    st.success(
        f"DIY (£{diy_total_with_vacancy:,.0f}) remains cheaper than agency (£{agency_cost:,.0f}) even after vacancy cost."
    )
else:
    st.success(
        f"Agency (£{agency_cost:,.0f}) may cost more upfront, but speeds hiring and avoids prolonged vacancy costs."
    )
"""

with open('/mnt/data/app.py', 'w') as f:
    f.write(app_py)

# Provide links for user to access
"/mnt/data/requirements.txt and /mnt/data/app.py have been created. You can download them or copy into your GitHub repo."

