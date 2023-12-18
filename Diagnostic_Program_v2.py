import json

symptom_mapping_file='symptom_mapping_v2.json'

with open(symptom_mapping_file) as f:
    mapping=json.load(f)
    
print(json.dumps(mapping, indent=2))


def diagnose_v2(patient_symptoms:list,
            symptom_mapping_file:str,
            matching_symptoms_lower_bound:int):
    diagnosis=[]
    with open(symptom_mapping_file) as f:
        mapping=json.load(f)
# access the disease information
    disease_info=mapping['diseases']
# for every disease
    for disease in disease_info:
        counter=0
        disease_symptoms=disease_info[disease]
# for each patient symptom
        for symptom in patient_symptoms:
# if this symptom is included in the known symptoms for the disease
            if symptom in disease_symptoms:
                counter+=1
        if counter>=matching_symptoms_lower_bound:
            diagnosis.append(disease)
    return diagnosis


print("#####################################")

# Patient 1
my_symptoms=["stuffy nose", "runny nose", "sneezing", "sore throat"]
diagnosis=diagnose_v2(my_symptoms,'symptom_mapping_v2.json' , 3)
print('Most likely diagnosis:',diagnosis)
# Patient 2
my_symptoms=["stuffy nose", "runny nose", "sneezing", "sore throat"]
diagnosis=diagnose_v2(my_symptoms, 'symptom_mapping_v2.json' , 4)
print('Most likely diagnosis:',diagnosis)
# Patient 3
my_symptoms=['fever', 'cough', 'vomiting']
diagnosis=diagnose_v2(my_symptoms, 'symptom_mapping_v2.json' , 3)
print('Most likely diagnosis:',diagnosis)