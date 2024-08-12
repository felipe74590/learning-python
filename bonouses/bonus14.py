## Bonus Example:
feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet":feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])

print(f"{parsed["feet"]} feet and {parsed["inches"]} is equal to {result} meters")

if result < 1:
    print( "Kid is too short to ride the rollercoaster")
else:
    print("Kid can go ahead and ride")