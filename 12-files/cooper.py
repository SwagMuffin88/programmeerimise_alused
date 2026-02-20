"""Cooperi testi ülesanne"""


def read_results_from_file(filename: str) -> list:
    results = []

    with open(filename, "r") as file:
        for row in file:
            parts = row.split()
            if len(parts) == 2:
                distance = int(parts[0])
                gender = parts[1]

                results.append({
                    "distance": distance,
                    "gender": gender
                })

    return results


def evaluate_individual_results(distance_in_metres: int, gender: str) -> str:
    is_male = gender == "M"
    excellent = 2800 if is_male else 2600
    satisfactory = 2000 if is_male else 1800

    if distance_in_metres >= excellent:
        result = "Väga hea"
    elif distance_in_metres < satisfactory:
        difference = satisfactory - distance_in_metres
        result = f"Nõrk, järgmisest hindest puudu {difference}m"
    else:
        difference = excellent - distance_in_metres
        result = f"Rahuldav, järgmisest hindest puudu {difference}m"

    return f"{gender} {distance_in_metres}m, {result}"


def separate_results_by_gender(results: list) -> dict:
    results_by_gender = {"M": [], "N": []}
    for r in results:
        if r["gender"] == "M":
            results_by_gender["M"].append(r["distance"])
        else:
            results_by_gender["N"].append(r["distance"])

    return results_by_gender


def calculate_average_distances(results_by_gender: dict) -> dict:
    averages = {}
    for gender, distances in results_by_gender.items():
        if len(distances) > 0:
            average = sum(distances) / len(distances)
            averages[gender] = int(average)
        else:
            averages[gender] = 0

    return averages


def evaluate_all_results(filename: str) -> None:
    results = read_results_from_file(filename)
    evaluations = []

    for r in results:
        e = evaluate_individual_results(r["distance"], r["gender"])
        evaluations.append(e)

    averages = calculate_average_distances(
        separate_results_by_gender(results)
    )

    for l in evaluations:
        print(l)

    print("Keskmised:")
    for gender, value in averages.items():
        print(f"{gender} {value}m")


if __name__ == '__main__':
    evaluate_all_results("cooper.txt")