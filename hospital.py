
"""
class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed_num = None
        Patient.PATIENT_COUNT += 1

class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.cap:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                # free up bed
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"
"""


class Patient(object):
    #pat_id = 0
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_num = None
        
        #Patient.pat_id += 1
    
    def display_info(self):
        print "ID: " + str(self.id)
        print "Patient Name: " + str(self.name)
        print "Type of Allergy: " + str(self.allergies)
        #print "Bed #: " + str(self.bed_num)
        return self
        

class Hospital(object):
    def __init__(self, hospital_name):
        self.patients = []
        self.hospital_name = hospital_name
        self.capacity = 3
        self.beds = self.initialize_beds()
    
    def initialize_beds(self):
        beds = []
        for i in range(1, self.capacity):
            beds.append({
                'bed_id': i,
                'Available': True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) >= self.capacity:
            print "Hospital is at full capacity"
        else:
            self.patients.append(patient)
            for i in range(1, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]['bed_id']
                    self.beds[i]['Available'] = False
            print "Patient #{}, {} was admitted to bed #{}.".format(patient.id,
                patient.name, patient.bed_num)
        return self
    
    def discharge(self, patient_id):
        #remove patient by id and change bed number to none
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed['bed_id'] == patient.bed_num:
                        bed['Available'] = True
                        break
                self.patients.remove(patient)
                print "Patient {} has been successfully discharged. Bed #{} is now available.".format(
                    patient.name, patient.bed_num)
            else:
                print "Patient not found."
        return self

    def pat_info(self):
        print 'Number of patients: {}'.format(len(self.patients))
        for i in self.patients:
            print "#"+ str(i.id) + " - " + i.name 
        return self

patient1 = Patient (1, "Noel Mendoza", "The Flu")
patient2 = Patient (2, "Kevin Mendoza", "Cold")
patient3 = Patient (3, "Isabeth Mendoza", "Rash")
patient4 = Patient(4, "Hilda Mendoza", "Rash")
#patient1.display_info()

hospital1 = Hospital('Kaiser')
hospital1.admit(patient1)
hospital1.admit(patient2)
hospital1.admit(patient3)
hospital1.discharge(1)
hospital1.pat_info()
