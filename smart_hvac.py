# Smart Building Climate Control Advisor
# ======================================
# - Industry related application: ioT/Smart Buildings / Facilitis Tech
# - AI concept: Rule Based reasoning
# - Decisioi engine for operational automation
#   - read environmental conditions
#   - apply operational conditions
#   - recommend actions that reduce discomfort and energy waste
#   - smart HVAC recommendations using enviornmental signmals like temperature, humidity, occupancy, & air quality.
# - We'll use: Python, rule-based AI, decision logic, automation thinking, IoT-inspired systems design, interpretable AI

def smart_building_advisor(temperature_f, humidity_pct, air_quality, occupancy, time_of_day):
    if air_quality == "poor" and temperature_f < 82:
        return "Open windows for ventilation"
    if temperature_f >= 82:
        return "Turn AC on"
    if temperature_f >= 76 and humidity_pct >= 70:
        return "Turn AC on"
    if temperature_f >= 74 and occupancy >= 3:
        return "Turn Fan on"
    if (
        temperature_f <= 75
        and air_quality == "good"
        and time_of_day in ["evening", "night"]
        ):
        return "Open Windows"
    return "Do Nothing"


def print_case_result(case_number, case_data):
    action = smart_building_advisor(
        temperature_f = case_data["temperature_f"],
        humidity_pct = case_data["humidity_pct"], 
        air_quality = case_data["air_quality"],
        occupancy = case_data["occupancy"],
        time_of_day = case_data["time_of_day"]
    )
    print(f"\nCase {case_number}")
    print("-" * 40)
    print(f"Temperature (F): {case_data['temperature_f']}")
    print(f"Humidity (%): {case_data['humidity_pct']}")
    print(f"Air Quality: {case_data['air_quality']}")
    print(f"Occupancy: {case_data['occupancy']}") 
    print(f"Time of Day: {case_data['time_of_day']}")
    print(f"Recommended Action: {action}") 

def main():
    print("=" * 60)
    print("Smart Building Climate Control Advisor")
    print("=" * 60)

    
    test_cases = [
        {
            "temperature_f" : 70,
            "humidity_pct" : 75,
            "air_quality" : "good",
            "occupancy" : 2,
            "time_of_day" : "afternoon"
        },
        {
            "temperature_f" : 72,
            "humidity_pct" : 45,
            "air_quality" : "good",
            "occupancy" : 2,
            "time_of_day" : "night"
        },
        {
            "temperature_f" : 73,
            "humidity_pct" : 50,
            "air_quality" : "poor",
            "occupancy" : 4,
            "time_of_day" : "afternoon"
        },
        {
            "temperature_f" : 84,
            "humidity_pct" : 60,
            "air_quality" : "good",
            "occupancy" : 4,
            "time_of_day" : "afternoon"
        }
    ]

    for i, case in enumerate(test_cases, start=1):
        print_case_result(i, case)

if __name__ == "__main__":
    main()
