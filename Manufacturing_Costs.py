# Andrew Scherping
# 2/21/2019
# Script to determine the manufacturing and acquisition costs of an aircraft and the profit produced
# This script needs to be accompanied by Research_and_Development.py and Operation_Costs.py
# I do not own these methods but are taken from
# Jan Roskam-Airplane Design Part 8 Airplane Cost Estimation Design Development Manufacturing and Operating

import Operation_Costs as os
import Research_and_Development as rd

print("Manufacturing Costs")

n_program = 514  # The number of aircraft to be produced in this program
n_m = n_program - rd.get_n_rdte() - rd.get_n_st()

# Total estimated manufacturing costs - c_man
# Airframe engineering and design cost - c_aed_m
# Total amount of engineering man hours required - mhr_aed_program
mhr_aed_program = 0.0396 * (rd.get_w_ampr() ** 0.791) * (rd.get_v_max() ** 1.1526) * \
                  (n_program ** 0.183) * rd.get_f_diff() * rd.get_f_cad()
# The engineering man hour rate for entire program - r_e_m
r_e_m = rd.get_r_e_r()
c_aed_m = (mhr_aed_program * r_e_m) - rd.get_c_aed_r()
print("The cost of the airframe engineering and design: $" + str(c_aed_m))

# Airplane program production costs - c_apc_m
# Costs per engine during the manufacturing phase
c_e_m = rd.get_c_e_r()
# Number of engines on the airplane
n_e = rd.get_n_e()
# Cost for propeller
c_p_m = rd.get_c_p_r()
# Number of propellers on an aircraft
n_p = rd.get_n_p()
# Cost of the avionics
c_avionics_m = rd.get_c_avionics_r()
# Cost of engines and avionics equipment - c_ea_m
c_ea_m = ((c_e_m * n_e) + (c_p_m * n_p) + c_avionics_m) * n_m
# Cost of the interior - c_int_m
# The interior cost factor - f_intd
f_int = 1000
# The number of passengers
n_pax = 6
c_int_m = f_int * n_pax * n_m * (rd.get_cef() / 3)
# The labor cost incurred in manufacturing n_m airplanes - c_man_m
# The total number of man hours required for the manufacturing of n_program - mhr_man_program
mhr_man_program = 28.984 * (rd.get_w_ampr() ** 0.74) * (rd.get_v_max() ** 0.543) * (n_program ** 0.524) * \
                  rd.get_f_diff()
r_m_m = rd.get_r_m_r()
c_man_m = (mhr_man_program * r_m_m) - rd.get_c_man_r()
# The materials cost incurred while manufacturing n_m planes - c_mat_m
# The total materials cost incurred with building n_program planes - c_mat_program
c_mat_program = 37.632 * rd.get_f_mat() * (rd.get_w_ampr() ** 0.689) * (rd.get_v_max() ** 0.624) * \
                (n_program ** 0.792) * rd.get_cef()
c_mat_m = c_mat_program - rd.get_c_mat_r()
# The tooling cost to produce n_m planes - c_tool_m
# The number of units produced per month - n_r_m
n_r_m = 50
# The total number of tooling man hours required to build n_program planes - mhr_tool_program
mhr_tool_program = 4.0127 * (rd.get_w_ampr() ** 0.764) * (rd.get_v_max() ** 0.899) * (n_program ** 0.178) * \
                   (n_r_m ** 0.066) * rd.get_f_diff()
# The tooling labor rate - r_t_m
r_t_m = rd.get_r_t_r()
c_tool_m = (mhr_tool_program * r_t_m) - rd.get_c_tool_r()
# The quality control costs associated with producing n_m planes - c_qc_m
c_qc_m = 0.13 * c_man_m
c_apc_m = c_ea_m + c_int_m + c_man_m + c_mat_m + c_tool_m + c_qc_m
print("The estimated cost of airplane production costs: $" + str(c_apc_m))

# Production flight test operations cost - c_fto_m
# The plane operating costs per hour - c_opshr
c_opshr = os.get_operatation_cost_per_hr()
# The number of flight test hours flown by the manufacturer - t_pft
t_pft = 5
# The overhead factor associated with the production flight test activities - f_ftoh
f_ftoh = 4
c_fto_m = n_m * c_opshr * t_pft * f_ftoh
print("The cost of test flight operations: $" + str(c_fto_m))

c_man = c_aed_m + c_apc_m + c_fto_m
print("The estimated cost of the manufacturing of the airplanes: $" + str(c_man))

# Profit - c_pro
# Percent of profit - f_pro_m
f_pro_m = 0.0
c_pro = f_pro_m * c_man

aep = (c_man + c_pro + rd.get_rdte_costs()) / n_m
print("Cost of aircraft per unit: $" + str(aep) + "/unit for " + str(n_m) + " units")
