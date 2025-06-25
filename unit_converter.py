def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def main():
    print("🧪 Unit Converter")
    while True:
        print("\nChoose a category:")
        print("1. Temperature (C ↔ F)")
        print("2. Length (km ↔ miles)")
        print("3. Weight (kg ↔ pounds)")
        print("4. Exit")
        choice = input("Enter option (1-4): ")

        if choice == '1':
            val = float(input("Enter temperature: "))
            unit = input("Convert from (C/F): ").upper()
            if unit == 'C':
                print(f"{val}°C = {c_to_f(val):.2f}°F")
            elif unit == 'F':
                print(f"{val}°F = {f_to_c(val):.2f}°C")
            else:
                print("❌ Invalid unit.")
        elif choice == '2':
            val = float(input("Enter distance: "))
            unit = input("Convert from (KM/MILES): ").lower()
            if unit == 'km':
                print(f"{val} km = {km_to_miles(val):.2f} miles")
            elif unit == 'miles':
                print(f"{val} miles = {miles_to_km(val):.2f} km")
            else:
                print("❌ Invalid unit.")
        elif choice == '3':
            val = float(input("Enter weight: "))
            unit = input("Convert from (KG/POUNDS): ").lower()
            if unit == 'kg':
                print(f"{val} kg = {kg_to_pounds(val):.2f} pounds")
            elif unit == 'pounds':
                print(f"{val} pounds = {pounds_to_kg(val):.2f} kg")
            else:
                print("❌ Invalid unit.")
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
