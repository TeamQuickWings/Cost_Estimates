# Andrew Scherping
# 2/14/2019
# Script to determine the direct operating cost of an aircraft
# I do not own these methods but are taken from
# Jan Roskam-Airplane Design Part 8 Airplane Cost Estimation Design Development Manufacturing and Operating

print("Operation Costs")

# TODO - need to be defined better
Takeoff_Weight = 4510  # Total Takeoff Weight, lbs
Speed_cruise = 180  # cruise velocity, knots
Estimated_price = 200000  # Estimated cost of the airplane
C_aircraft_block = 500  # cost the airframe and systems maintenance materials cost per airplane, USD
Number_of_Engines = 1  # The number of engines, unit less
H_overhaul = 1400  # Engine hours between overhauls
Engine_price = 40000  # The price of the engine, USD
Number_of_Props = 1  # The number of props
Prop_price = 8200  # The price of the prop, USD
Avionics_price = 30000  # The price of the avionics, USD
Fuel_Weight_used = 810  # FW_block - fuel block to be used in the mission, lbs

Range_block = 945  # R_Block - range of the mission, nm
Fuel_price = 5.30  # Current price of aviation fuel, USD/nm
Fuel_Density = 5.8  # Density of the aviation fuel, lbs/gallon

Oil_Weight_block = Fuel_Weight_used / 70  # Weight in oil used, lbs
Oil_Density = 7.4  # Density of oil, lbs/gallon
Oil_price = 33  # Price of oil, USD/gallon

#  The costs of fuel and oil, USD/nm
C_pol = ((Fuel_Weight_used / Range_block) * (Fuel_price / Fuel_Density)) + \
        ((Oil_Weight_block / Range_block) * (Oil_price / Oil_Density))

flt = C_pol  # Direct operating costs of flight, USD/nm

print("The operating cost of petroleum is: $" + str(flt) + "/nm")

time_ground = (0.51 * (10 ** (-6)) * Takeoff_Weight) + 0.125  # Estimated time on the ground, hrs
time_climb = 0.06677  # Estimated time required to reach cruise altitude, hrs
time_cruise = Range_block / Speed_cruise  # Estimated time in cruise, hrs
time_decent = 0.25  # Estimated time to descend, hrs

time_block = time_ground + time_climb + time_cruise + time_decent  # time block, hrs

V_block = Range_block / time_block  # Block speed, nm
C_airframe = 1.03 * (C_aircraft_block / V_block)  # Cost of airframe and systems maintenance, USD/nm

K_H = (0.076 * (H_overhaul / 100)) + 0.164  # Factor for period between engine overhaul
# Cost of engine material maintenance per hour
C_mat_engine_hr = ((0.0004274 * ((Engine_price / 1000) ** 2)) + (0.08263 * (Engine_price / 1000))) * (0.1 + (0.5 / K_H))

# Estimated cost of engine maintenance per engine hour, USD/nm
C_engine = (1.03 * 1.3 * Number_of_Engines * C_mat_engine_hr) / V_block

maint = C_airframe + C_engine  # Direct operating costs of maintenance, USD/nm

print("The operating cost of maintenance is: $" + str(maint) + "/nm")

F_dairframe = 0.85  # Airframe depreciation factor
D_pairframe = 10  # Airframe depreciation period
#  The annual utilization, hrs
U_annual = (10 ** 3) * \
           ((3.4546 * time_block) + 2.994 - (((12.289 * (time_block ** 2)) - (5.6626 * time_block) + 8.964) ** 0.5))

# Depreciation of the airframe, USD/nm
D_airframe = (F_dairframe * (Estimated_price - (Number_of_Engines * Engine_price) - (Number_of_Props * Prop_price) -
                             Avionics_price)) / (D_pairframe * U_annual * V_block)

F_engine = 0.85  # Engine depreciation factor
D_pengine = 7  # Engine depreciation period

# Depreciation of the engine, USD/nm
D_engine = (F_engine * Number_of_Engines * Engine_price) / (D_pengine * U_annual * V_block)

F_prop = 0.85  # Prop Depreciation factor
D_pprop = 7  # Prop depreciation period

# Depreciation of the prop
D_prop = (F_prop * Number_of_Props * Prop_price) / (D_pprop * U_annual * V_block)

F_pavionics = 1  # Avionic depreciation factor
D_pavionics = 5  # Avionics depreciation period

# Depreciation of the avionics
D_avionics = (F_pavionics * Avionics_price) / (D_pavionics * U_annual * V_block)

F_dairplane_parts = 0.85  # Airplane spare parts depreciation factor
F_airplane_parts = 0.1  # Airplane spare parts factor
D_pairplane_parts = 10  # Airplane spare parts depreciation period

# Depreciation of the spare part for the airplane
D_spare_parts = (F_airplane_parts * F_airplane_parts * (Estimated_price - (Number_of_Engines - Engine_price))) / \
                (D_pairplane_parts * U_annual * V_block)

F_dengine_parts = 0.85  # Engine spare parts depreciation factor
F_engine_parts = 0.5  # Engine spare parts factor
F_spare_parts = 1.5  # Engine spare parts price factor
D_pengine_parts = 7  # Engine spare parts depreciation period

# Depreciation of the engine spare parts
D_engine_spare_parts = (F_dengine_parts * F_engine_parts * Engine_price * F_spare_parts) / \
                       (D_pengine_parts * U_annual * V_block)

# The cost of aircraft depreciation, USD/nm
depr = D_airframe + D_engine + D_prop + D_avionics + D_spare_parts + D_engine_spare_parts

print("The operating cost of depreciation: $" + str(depr) + "/nm")

DOC = flt + maint + depr  # DOC - Direct operating costs, USD/nm
print("The direct operating cost: $" + str(DOC) + "/nm")


def get_operatation_cost_per_hr():

    return DOC
