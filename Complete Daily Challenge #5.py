""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2

ADD YOUR NAME, STUDENT ID and SECTION CRN here.
Ravi Persaud
100760022
TPRG 2131-01

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
# Daily Challenge #5
# Ravi Persaud (100760022)
# TRPG2131 Section 01
# September 20th, 2023
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or others sources is properly cited, giving
# credit to the original author(s).
# This code allows the user to perform various electrical circuit calculations and provides
# the results based on their inputs. It has options for series resistance, parallel
# resistance, RC time constant, and series RLC resonant frequency, bandwidth, and Q factor.

import math

# Defines a function to prompt the user for a positive float value
def get_positive_float(prompt):
    value = float(input(prompt))  # Reads a float value from user input
    while value <= 0.0:  # Keeps prompting until a positive value is entered
        value = float(input("The value must be greater than zero\n" + prompt))  # Re-prompts if non-positive value
    return value  # Returns the positive float value

# Defines a function to calculate resonant frequency, bandwidth, and Q factor for a series circuit
def calculate_series_resonant(l, c, r):
    resonant_frequency = 1 / (2 * math.pi * math.sqrt((l * 10**-3) * (c * 10**-6)))  # Updated formula for resonant frequency
    bandwidth = r / (2 * math.pi * (l * 10**-3))  # Updated formula for bandwidth
    q_factor = resonant_frequency / bandwidth  # Formula for Q factor
    return resonant_frequency, bandwidth, q_factor  # Returns calculated values


# Defines a function to calculate parallel resistance
def calculate_parallel_resistance(r1, r2):
    parallel_resistance = 1 / ((1 / r1) + (1 / r2))  # Formula for parallel resistance
    return parallel_resistance

# Defines a function to calculate RC time constant
def calculate_rc_time_constant(r, c):
    rc_time_constant = r * c * 10**-6  # Formula for RC time constant
    return rc_time_constant

# Defines a function to calculate resonant frequency for a series RLC circuit
def calculate_series_rlc_resonant(l, c):
    resonant_frequency = 10 / (2 * math.pi * math.sqrt((l * 10**-3) * (c * 10**-4)))  # Formula for resonant frequency
    return resonant_frequency  # Returns calculated resonant frequency

# Defines a function to calculate Q factor and bandwidth for a series RLC circuit
def calculate_series_rlc_q_and_bandwidth(l, c, r):
    resonant_frequency, bandwidth, q_factor = calculate_series_resonant(l, c, r)
    return q_factor, bandwidth

# Main loop to repeatedly calculate circuit properties
while True:
    calculation_type = input("What do you want to calculate? Enter the corresponding letter:\n"
                            " - 'S' for series resistance\n"
                            " - 'P' for parallel resistance\n"
                            " - 'RC' for RC time constant\n"
                            " - 'RLC' for series RLC resonant frequency, bandwidth, and Q factor\n").upper()

    if calculation_type == 'S':
        # Prompts user for two resistor values
        resistor1 = get_positive_float("Enter the value of the first resistor in ohms: ")
        resistor2 = get_positive_float("Enter the value of the second resistor in ohms: ")

        # Calculates series resistance
        series_resistance = resistor1 + resistor2

        # Prints the calculated series resistance value
        print(f"Series Resistance: {series_resistance:.2f} ohms\n")

    elif calculation_type == 'P':
        # Prompts user for two resistor values
        resistor1 = get_positive_float("Enter the value of the first resistor in ohms: ")
        resistor2 = get_positive_float("Enter the value of the second resistor in ohms: ")

        # Calculates parallel resistance
        parallel_resistance = calculate_parallel_resistance(resistor1, resistor2)

        # Prints the calculated parallel resistance value
        print(f"Parallel Resistance: {parallel_resistance:.2f} ohms\n")

    elif calculation_type == 'RC':
        rc_type = input("Do you have two resistors (R1 and R2) or a resistor and a capacitor (RC)? Enter '2' for resistors or 'RC' for resistor-capacitor combination: ").upper()

        if rc_type == '2':
            resistor1 = get_positive_float("Enter the value of the first resistor (R1) in ohms: ")
            resistor2 = get_positive_float("Enter the value of the second resistor (R2) in ohms: ")
            capacitance = get_positive_float("Enter the value of the capacitance in uF: ")

            # Calculates parallel resistance and RC time constant
            parallel_resistance = calculate_parallel_resistance(resistor1, resistor2)
            rc_time_constant = calculate_rc_time_constant(parallel_resistance, capacitance)

            # Prints the calculated values
            print(f"Parallel Resistance: {parallel_resistance:.2f} ohms")
            print(f"RC Time Constant: {rc_time_constant:.2f} seconds\n")

        elif rc_type == 'RC':
            resistance = get_positive_float("Enter the value of the resistor in ohms: ")
            capacitance = get_positive_float("Enter the value of the capacitance in uF: ")

            # Calculates RC time constant
            rc_time_constant = calculate_rc_time_constant(resistance, capacitance)

            # Prints the calculated RC time constant value
            print(f"RC Time Constant: {rc_time_constant:.2f} seconds\n")

        else:
            print("Invalid input. Please enter '2' for resistors or 'RC' for resistor-capacitor combination.")

    elif calculation_type == 'RLC':
        inductance = get_positive_float("Enter the value of the inductance in mH: ")
        capacitance = get_positive_float("Enter the value of the capacitance in uF: ")
        resistance = get_positive_float("Enter the value of the resistance in ohms: ")

        resonant_frequency = calculate_series_rlc_resonant(inductance, capacitance)
        q_factor, bandwidth = calculate_series_rlc_q_and_bandwidth(inductance, capacitance, resistance)
        
        # Prints calculated values for resonant frequency, Q factor, and bandwidth
        print(f"Resonant Frequency: {resonant_frequency:.2f} Hz")
        print(f"Q Factor: {q_factor:.2f}")
        print(f"Bandwidth: {bandwidth:.2f} Hz\n")

    else:
        # If user entered an invalid option
        calculation_type = input("Invalid input. Enter the corresponding letter:\n"
                            " - 'S' for series resistance\n"
                            " - 'P' for parallel resistance\n"
                            " - 'RC' for RC time constant\n"
                            " - 'RLC' for series RLC resonant frequency and Q factor\n").upper()

    continue_calculation = input("Do you want to perform another calculation? (yes/no) ").lower()
    if continue_calculation != 'yes':
        break

    
# Cited from https://www.python.org/ and https://chat.openai.com/ for format
