# Nathan Briggs, Andrew Scherping
# Code to estimate the operating costs of an aircraft
# time is in hours and and distance in nm

take_off_weight = 900
block_distance = 135
cruise_velocity = 180
operation_years = 20
time_to_cruise = 0.3
time_to_descend = 0.3

#maintenance constants estimates
#maint_man_hrs_per_flt_hr = 0.3
#frame_maint_cost_per_man_hour = 15
#engine_maint_hrs_per_block_hr = 0.7
#engine_maint_labor_cost_per_hr = 15
#materials_cost_per_block_hr = 50
#engine_maint_cost_per_block_hr = 5

maneuver_time_from_atc = 0.25 * 10 ** (-6) * take_off_weight + 0.0625
distance_from_atc_maneuvering = cruise_velocity * maneuver_time_from_atc
distance_of_decent = 90
distance_of_climb = 100
time_in_cruise = (1.06 * (block_distance - distance_of_climb - distance_of_decent + distance_from_atc_maneuvering)) \
                 / cruise_velocity

time_on_ground = 0.51 * 10 ** (-6) * take_off_weight + 0.125
time_block = time_on_ground + time_to_cruise + time_in_cruise + time_to_descend
annual_use = 1000 * (3.4546 * time_block + 2.944 - 12.289 * time_block ** 2 - 5.6626 * time_block + 8.964) ** 0.5

print("time_block: " + str(time_block))

block_speed = block_distance / time_block
#pilot_salary = 85000
#cost_of_crew = 2 * ((1.26 / block_speed) * (pilot_salary / 800) + 7 / block_speed)

fuel_density = 6.7
fuel_price = 5
weight_of_fuel = 200
fuel_and_oil_cost = 1.05 * (weight_of_fuel / block_distance) * fuel_price / fuel_density
flight_operating_costs = fuel_and_oil_cost

fee_per_landing = 0.002 * take_off_weight
DOC_lnr = fee_per_landing / (block_speed * time_block)

#maint_frame_systems_per_hr = maint_man_hrs_per_flt_hr*(time_in_cruise/time_block)
#applied_maint_cost = 1.3 / block_speed * ((maint_frame_systems_per_hr*frame_maint_cost_per_man_hour) + (engine_maint_hrs_per_block_hr * engine_maint_labor_cost_per_hr) + (0.4 * materials_cost_per_block_hr) + (engine_maint_cost_per_block_hr))
#engine_maint_cost = 1.03 * 1.3 * engine_maint_cost_per_block_hr / block_speed
#materials_maint_cost = 1.03 * materials_cost_per_block_hr / block_speed
#engine_labor_cost = 1.03 * 1.3 * engine_maint_hrs_per_block_hr * engine_maint_labor_cost_per_hr / block_speed
#airframe_labor_cost = 1.03 * maint_man_hrs_per_flt_hr * (time_in_cruise / time_block) * frame_maint_cost_per_man_hour / block_speed
#DOC_maint = airframe_labor_cost + engine_labor_cost + materials_maint_cost + engine_maint_cost + applied_maint_cost #total maintenance cost

Direct_Operating_Cost = (1 / 0.98) * (1 / 0.93) * (flight_operating_costs + DOC_lnr)
    #Direct operating cost from insurance and financing are estimated as percent of total DOC
