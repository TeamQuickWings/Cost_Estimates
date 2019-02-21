# Andrew Scherping
# 2/21/2019
# Script to determine the cost of research and development
# I do not own these methods but are taken from
# Jan Roskam-Airplane Design Part 8 Airplane Cost Estimation Design Development Manufacturing and Operating

import math

w_takeoff = 2500  # takeoff weight, lbs
v_max = 180  # cruise speed, knots
c_e_r = 45000  # cost per engine, USD
n_e = 1  # number of engines per plane
c_p_r = 8200  # cost of a propeller, USE
n_p = 1  # number of props per plane
c_avionic_r = 30000  # cost of the avionics per plane, USD
n_rdte = 10  # number of aircraft produce for the research, development, test and evaluation phase
n_st = 4  # number of static planes produced, no engine, prop, or avionics installed
c_rdte = 40000000  # initial estimated cost of research, development and evaluation

# Airframe Engineering and Design cost - c_aed_r
# Man hours required by the first 3 stages, planning  design, studies mock-up, wind tunnels, engine test
w_ampr = 10 ** (0.1936 + (0.8645 * math.log10(w_takeoff)))  # TODO
# Factor which accounts for the difficulty and complexity - f_diff
f_diff = 1.2
# factor which accounts for the availability of cad - f_cad
f_cad = 0.8
mhr_aed_r = 0.0396 *(w_ampr ** 0.791) * (v_max * 1.526) * (n_rdte ** 0.183) * f_diff * f_cad
# Cost escalation factor - cef
cef = 4
# Engineering man-hour rate
r_e_r = 50 * (cef / 2.7)  # TODO
c_aed_r = mhr_aed_r * r_e_r
print("Cost to design the airframe: $" + str(c_aed_r))

# Development support and testing costs - c_dst_r
# Includes wind tunnel testing systems testing, structural testing, propulsion testing, simulations
c_dst_r = 0.008325 * (w_ampr ** 0.873) * (v_max ** 1.890) * (n_rdte ** 0.346) * cef * f_diff
print("Costs for development support and testing: $" + str(c_dst_r))

# Flight test airplanes cost - c_fta_r
# Cost of engine and avionics - c_ea_r
c_ea_r = ((c_e_r * n_e) + (c_p_r * n_p) + c_avionic_r) * (n_rdte - n_st)
# Manufacturing cost of the flight test aircraft - c_man_r
# The number of manufacturing man hours, hrs - mhr_man_r
mhr_man_r = 28.984 * (w_ampr ** 0.740) * (v_max ** 0.543) * (n_rdte ** 0.524) * f_diff
# The manufacturing labor rate, USD - r_m_r
r_m_r = 30 * (cef / 2.7)  # TODO
# Total costs of manufacturing labor
c_man_r = mhr_man_r * r_m_r
# The cost of material to manufacture the flight test planes - c_mat_r
# the correction factor which depends on the construction materials
f_mat = 3
c_mat_r = 37.632 * f_mat * (w_ampr ** 0.689) * (v_max ** 0.624) * (n_rdte ** 0.792) * cef
# The tooling cost associated with manufacturing the flight test aircraft c_tool_r
# the rdte production rate, units per month - n_r_r
n_r_r = 0.33
# The tooling man hours, hrs - mhr_tool_r
mhr_tool_r = 4.0127 * (w_ampr ** 0.764) * (v_max ** 0.899) * (n_rdte ** 0.178) * (n_r_r ** 0.066) * f_diff
# The manufacturing tooling labor rate, USD - r_m_r
r_t_r = 40 * (cef / 2.7)  # TODO
c_tool_r = mhr_tool_r * r_t_r

# Quality control cost associated with manufacturing of the flight test airplanes - c_qc_r
c_qc_r = 0.13 * c_man_r

c_fta_r = c_ea_r + c_man_r + c_mat_r + c_tool_r + c_qc_r
print("Costs for the flight test aircraft: $" + str(c_fta_r))

# Flight test operation costs - c_fto_r
# Factor which depends of the importance of having low observables (stealth) - f_obs
f_obs = 1
c_fto_r = 0.001244 * (w_ampr ** 1.16) * (v_max ** 1.371) * ((n_rdte - n_st) ** 1.281) * cef * f_diff * f_obs
print("Costs for the flight test operation costs: $" + str(c_fto_r))

# Test and simulation facilities cost - c_tsf_r
# Factor which depends on the extent of testing and simulation facilities required
f_tsf = 0  # no extra facilities are required
c_tsf_r = f_tsf * c_rdte
print("Costs from test and simulation facilities: $" + str(c_tsf_r))

# RDTE profit - c_pro_r
# Rate of profit from this stage - f_pro_r
f_pro_r = 0.1
c_pro_r = f_pro_r * c_rdte
print("Costs from the profit of this stage: $" + str(c_pro_r))

# Sum of the costs to get the total cost
c_total = c_aed_r + c_dst_r + c_fta_r + c_fto_r + c_tsf_r + c_pro_r
print("The total costs of developement are: $" + str(c_total))


def get_rdte_costs():

    return c_total


def get_c_aed_r():

    return c_aed_r


def get_w_ampr():

    return w_ampr


def get_v_max():

    return v_max


def get_f_diff():

    return f_diff


def get_f_cad():

    return f_cad


def get_r_e_r():

    return r_e_r


def get_c_e_r():

    return c_e_r


def get_n_e():

    return n_e


def get_c_p_r():

    return c_p_r


def get_n_p():

    return n_p


def get_c_avionics_r():

    return c_avionic_r


def get_cef():

    return cef


def get_c_man_r():

    return c_man_r


def get_r_m_r():

    return r_m_r


def get_n_rdte():

    return n_rdte


def get_n_st():

    return n_st


def get_f_mat():

    return f_mat


def get_c_mat_r():

    return c_mat_r


def get_c_tool_r():

    return c_tool_r


def get_r_t_r():

    return r_t_r
