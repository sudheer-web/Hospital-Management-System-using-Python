import pickle

with open("database/doctors.pkl", "wb") as file :
    doctors = [["Dr. Major RS Rengan", "Surgeon"], ["Dr. AP Prem", "Physician"], ["Dr. Rajan Santosham", "Ortho"], ["Dr. Barani R", "Physician"], ["Dr. Yamini", "Ortho"], ["Dr. Indira G", "Surgeon"]]
    pickle.dump(doctors, file)


with open("database/nurses.pkl", "wb") as file : 
    nurses = [["Anjali Kumari", "None"], ["Kajal Kumari", "None"], ["Shilpa", "Ortho"]]
    pickle.dump(nurses, file)


with open("database/pharmacists.pkl", "wb") as file :
    pharmacists = [["Apollo Pharmacy", "None"], ["MedPlus Pharmacy", "None"], ["Velu Pharmacy", "None"]]
    pickle.dump(pharmacists, file)


with open("database/doctors.pkl", "rb") as file :
    print(pickle.load(file))


with open("database/patients.pkl", "wb") as file :
    patients = [["Richa Singh", 21, "female"], ["Rohit Kumar", 19, "male"]]
    pickle.dump(patients, file)


with open("database/patients.pkl", "rb") as file :
    print(pickle.load(file))


with open("database/appointments.pkl", "wb") as file :
    appointments = [["Dr. Major RS Rengan", "Richa Singh",(16,11,2021)], ["Dr. Rajan Santosham", "Rohit Kumar", (16,11,2021)]]
    pickle.dump(appointments, file)