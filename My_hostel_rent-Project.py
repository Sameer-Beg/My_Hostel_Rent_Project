
## Inputs we need from  the user
# Total rent
# Total food ordered for snacking
# Electricity units spend
# Charge per unit
# Person living in Hostel Room

## Output
 # Total amount you've to pay is ..

Hostel_Roomrent = int(input("Enter your Hostel room rent :"))
Food = int(input("Enter the amount of food ordered :"))
Elctricity_speed = int(input("Enter the total of Electricity speed :"))
Chargerper_unit = int(input("Enter the charge per unit :"))
Person = int(input("Enter the number of person living in room :"))

Total_bill = Elctricity_speed * Chargerper_unit

Output = (Hostel_Roomrent + Food + Total_bill) // Person

print("Each person will pay" , Output)





