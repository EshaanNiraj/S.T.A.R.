[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](http://choosealicense.com/licenses/mit/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://starapp.streamlit.app)

# S.T.A.R. (Submillimetre Tool for Astrophysics Research)

Interactive, intuitive GUI tool for quickly estimating both dust and total masses of protoplanetary discs for arbitrary optical depths from ALMA datasets/observations - created as part of my Third Year Physics Project.

## Live App
Access the deployed GUI here: **[https://starapp.streamlit.app](https://starapp.streamlit.app)**

## Mathematical Framework
Standard astrophysics workflows frequently rely on the Hildebrand (1983) equation assuming an optically thin limit where $\tau_\nu \to 0$. To improve this, S.T.A.R. uses a generalised analytical expression that incorporates an arbitrary optical depth ($\tau_\nu$) correction factor - accounting for flux self-absorption in the dense midplanes of protoplanetary discs:

$$M_{\mathrm{dust}}=\frac{F_{\nu}d^{2}}{\kappa_{\nu}B_{\nu}(T_{\mathrm{dust}})} \left( \frac{\tau_{\nu}}{1-e^{-\tau_{\nu}}} \right)$$

## Features
- **Arbitrary Optical Depth Correction:** Calculates with optically thin assumption ($\tau = 0$) by default, with the capability to set arbitrary optical depths ($\tau_{\nu} > 0$) to instantly model mass underestimations.
- **Embedded Planck Function:** Automatically evaluates $B_\nu(T)$ using exact SI constants from `astropy.constants`.
- **Dimensional Automation:** Seamlessly handles complex multidimensional unit conversions (Janskys to $W\,m^{-2}Hz^{-1}$, parsecs to metres).
- **Literature Benchmarking:** Built-in data presets allow users to rapidly load and cross-reference ALMA data from published literature (e.g., Ansdell et al. 2016).
- **Gas-to-Dust Scaling:** Instantly outputs total disc mass in Jupiter masses ($M_{\mathrm{Jup}}$) using the established 100:1 gas-to-dust ratio, alongside the dust masses.

## Author
Eshaan Niraj
