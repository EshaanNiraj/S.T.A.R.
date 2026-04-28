import numpy as np
import streamlit as st
from astropy import units as u
from astropy.constants import c, h, k_B

c_si = c.value
h_si = h.value
kB_si = k_B.value

def B(nu, T):
    x = (h_si * nu) / (kB_si * T)
    return (2 * h_si * (nu ** 3)) / ((c_si ** 2) * (np.exp(x) - 1))

def kap(nu):
    return (nu / 1e12)

def mass(F, nu, d, T=20):
    F_si = (F * u.Jy).to(u.W / (u.m**2 * u.Hz)).value
    d_si = (d * u.pc).to(u.m).value
    T_si = (T * u.K).to_value(u.K)
    return (F_si * (d_si**2)) / (kap(nu) * B(nu, T_si))

presets = {
    "Own Measurements": {
        "sz98_flux": 2.256159468880e-1,
        "sz98_freq": 335004e6,
        "sz98_dist": 1000 / 6.399,
        "rylup_flux": 2.665593799261e-1,
        "rylup_freq": 335073e6,
        "rylup_dist": 1000 / 6.5153,
        "temp": 20
    },
    "Ansdell et al. 2016": {
        "sz98_flux": 237.29e-3,
        "sz98_freq": c_si / 890e-6,
        "sz98_dist": 200,
        "rylup_flux": 275.5e-3,
        "rylup_freq": c_si / 890e-6,
        "rylup_dist": 150,
        "temp": 20
    }
}

st.set_page_config(page_title="S.T.A.R.", layout="centered")
st.title("S.T.A.R.")
st.subheader("Submillimetre Tool for Astrophysics Research")

dataset = st.selectbox("Dataset", list(presets.keys()))

if "initialised" not in st.session_state:
    p = presets[dataset]
    st.session_state.sz98_flux = p["sz98_flux"]
    st.session_state.sz98_freq = p["sz98_freq"]
    st.session_state.sz98_dist = p["sz98_dist"]
    st.session_state.rylup_flux = p["rylup_flux"]
    st.session_state.rylup_freq = p["rylup_freq"]
    st.session_state.rylup_dist = p["rylup_dist"]
    st.session_state.temp = p["temp"]
    st.session_state.current_dataset = dataset
    st.session_state.initialised = True

if dataset != st.session_state.current_dataset:
    p = presets[dataset]
    st.session_state.sz98_flux = p["sz98_flux"]
    st.session_state.sz98_freq = p["sz98_freq"]
    st.session_state.sz98_dist = p["sz98_dist"]
    st.session_state.rylup_flux = p["rylup_flux"]
    st.session_state.rylup_freq = p["rylup_freq"]
    st.session_state.rylup_dist = p["rylup_dist"]
    st.session_state.temp = p["temp"]
    st.session_state.current_dataset = dataset

temperature = st.number_input("Dust Temperature (K)", key="temp")

st.markdown("### Sz 98")
sz98_flux = st.number_input("Flux (Jy)", key="sz98_flux")
sz98_freq = st.number_input("Frequency (Hz)", key="sz98_freq")
sz98_dist = st.number_input("Distance (pc)", key="sz98_dist")

st.markdown("### RY Lup")
rylup_flux = st.number_input("Flux (Jy)", key="rylup_flux")
rylup_freq = st.number_input("Frequency (Hz)", key="rylup_freq")
rylup_dist = st.number_input("Distance (pc)", key="rylup_dist")

if st.button("Calculate Dust & Total Mass"):

    sz98 = (mass(sz98_flux, sz98_freq, sz98_dist, temperature) * u.kg).to(u.M_earth)
    rylup = (mass(rylup_flux, rylup_freq, rylup_dist, temperature) * u.kg).to(u.M_earth)

    st.markdown("## Results")

    st.markdown("### Dust Mass")
    st.write(f"Sz 98: {sz98}")
    st.write(f"RY Lup: {rylup}")

    st.markdown("---")

    st.markdown("### Total Mass (Dust + Gas)")
    st.write(f"Sz 98: {(sz98 * 100).to(u.M_jup)}")
    st.write(f"RY Lup: {(rylup * 100).to(u.M_jup)}")