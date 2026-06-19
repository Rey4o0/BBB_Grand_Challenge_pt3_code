import random

applicants = []

names = [
    'Jamal', 'Sarah', 'David', 'Emily', 'Aisha',
    'Michael', 'Sophia', 'Daniel', 'Olivia', 'Noah',
    'Ali bin Rahman', 'Aisyah binte Ahmad',
    'Kumar S/O Raj', 'John D/O Tan'
]

# Generate applicants
def generate_applicants():

    selected_names = random.sample(names, 10)

    for name in selected_names:
        applicants.append({
            'name': name,
            'experience': random.randint(1, 10),
            'skills': random.randint(1, 10)
        })

# Original ranking (before bias)
def original_ranking():

    original_applicants = []

    for applicant in applicants:

        score = (
            applicant['experience']
            + applicant['skills']
        )

        original_applicants.append({
            'name': applicant['name'],
            'experience': applicant['experience'],
            'skills': applicant['skills'],
            'score': score
        })

    original_applicants.sort(
        key=lambda x: x['score'],
        reverse=True
    )

    print("\n=== ORIGINAL UNBIASED RANKINGS ===")

    for rank, applicant in enumerate(original_applicants, start=1):
        print(
            f"{rank}. {applicant['name']} | "
            f"Experience: {applicant['experience']} | "
            f"Skills: {applicant['skills']} | "
            f"Score: {applicant['score']}"
        )

# Apply bias
def apply_bias():

    for applicant in applicants:

        name = applicant['name'].lower()

        score = (
            applicant['experience']
            + applicant['skills']
        )

        if name == 'jamal':
            score -= 5

        if any(x in name for x in ['d/o', 's/o', 'bin', 'binte']):
            score -= 5

        applicant['score'] = score

# Sort biased rankings
def sort_biased():

    applicants.sort(
        key=lambda x: x['score'],
        reverse=True
    )

    print("\n=== BIASED RANKINGS ===")

    for rank, applicant in enumerate(applicants, start=1):
        print(
            f"{rank}. {applicant['name']} | "
            f"Experience: {applicant['experience']} | "
            f"Skills: {applicant['skills']} | "
            f"Score: {applicant['score']}"
        )

# Detect bias
def detect_bias():

    hired = applicants[:5]

    group_A = 0
    group_B = 0

    for applicant in hired:

        name = applicant['name'].lower()

        if (
            name == 'jamal'
            or any(x in name for x in ['d/o', 's/o', 'bin', 'binte'])
        ):
            group_B += 1
        else:
            group_A += 1

    print("\n=== BIAS DETECTION ===")
    print("Group A hired:", group_A)
    print("Group B hired:", group_B)

    if group_A > group_B:
        print("Possible bias against Group B")
    elif group_B > group_A:
        print("Possible bias against Group A")
    else:
        print("No bias detected")

# Fairness correction
def fairness_correction():

    corrected_applicants = []

    for applicant in applicants:

        fair_score = (
            applicant['experience']
            + applicant['skills']
        )

        corrected_applicants.append({
            'name': applicant['name'],
            'experience': applicant['experience'],
            'skills': applicant['skills'],
            'score': fair_score
        })

    corrected_applicants.sort(
        key=lambda x: x['score'],
        reverse=True
    )

    print("\n=== FAIR RANKINGS (NAMES IGNORED) ===")

    for rank, applicant in enumerate(corrected_applicants, start=1):
        print(
            f"{rank}. {applicant['name']} | "
            f"Experience: {applicant['experience']} | "
            f"Skills: {applicant['skills']} | "
            f"Score: {applicant['score']}"
        )

    fair_hired = corrected_applicants[:5]

    group_A = 0
    group_B = 0

    for applicant in fair_hired:

        name = applicant['name'].lower()

        if (
            name == 'jamal'
            or any(x in name for x in ['d/o', 's/o', 'bin', 'binte'])
        ):
            group_B += 1
        else:
            group_A += 1

    print("\n=== AFTER FAIRNESS CORRECTION ===")
    print("Group A hired:", group_A)
    print("Group B hired:", group_B)

    print("\nRecommendation:")
    print("Use blind recruitment.")
    print("Evaluate only qualifications, not names.")

# Main Program
generate_applicants()

original_ranking()

apply_bias()

sort_biased()

detect_bias()

fairness_correction()