student_data = {
    "id1": {"name": "Sara", "class": "V", "subject_intergration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_intergration": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_intergration": "english, math, science"},
    "id4": {"name": "Surya", "class": "V", "subject_intergration": "english, math, science"},
}

result = {}
seen_key = []

for student_id, details in student_data.items():
    unique_keys = (details["name"], details["class"], details["subject_intergration"])

    if unique_keys not in seen_key:
        seen_key.append(unique_keys)
        result[student_id] = details



for k,v in result.items():
    print(k,  ":",   v)