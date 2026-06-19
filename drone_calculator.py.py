print("🚁 Drone Flight Time Calculator")

battery = float(input("Battery Capacity (mAh): "))
motor_count = int(input("Number of Motors: "))
current_per_motor = float(input("Current per Motor (A): "))

total_current = motor_count * current_per_motor

flight_time_hours = (battery / 1000) / total_current

flight_time_minutes = flight_time_hours * 60

print(f"\nEstimated Flight Time: {flight_time_minutes:.1f} minutes")