per_hour = float (input("Hello Honey, Can I please ask how much you make an hour?"))
working_hours_normal = float (input("And how many working hours have you had this month? (Shabbath NOT included)"))
working_hours_Shabbath = float (input("And lastly, how many working hours ON SHABBATH have you had this month, dear?"))
salary = float (working_hours_normal*per_hour)+(working_hours_Shabbath*per_hour*1.5)

print(f"Your Salary for this month should be: {salary} ")
