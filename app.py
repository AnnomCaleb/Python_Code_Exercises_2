patient_name = input("Enter your name: ")
patient_age = int(input("Enter your age: "))
patient_status = input("Enter  old or new: ").lower()

if patient_status == "new":
    print("Patient can proceed to see a Doctor")

elif patient_status == "old":
    print("Patient can get a new appointment")

else:
    print("Patient has to be in the Hospital System")
