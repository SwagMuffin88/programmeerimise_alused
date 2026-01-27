"""https://courses.cs.ut.ee/t/pythonkoolis/Main/SisendYl"""
from time import strptime


# Ex. 7
def is_valid_id(id_code: str) -> bool:
    return len(id_code) == 11 and id_code.isnumeric() and is_correct_checksum(id_code)

def decode_date(century_code: int, birth_year: str, birth_month: str, birth_day: str):
    century_decoded = ""

    if century_code <= 2:
        century_decoded = "18"
    elif century_code == 3 or century_code == 4:
        century_decoded = "19"
    elif century_code >= 5:
        century_decoded = "20"

    full_year = century_decoded + birth_year
    # print(full_year)
    full_date_as_string = f"{full_year}-{birth_month}-{birth_day}"

    full_date_decoded = strptime(full_date_as_string, '%Y-%m-%d')
    return full_date_decoded


def decode_gender(century_code:int) -> str:
    if century_code % 2 != 0:
        return "mees"
    else:
        return "naine"


def decode_hospital_nr(queue_nr_text: str) -> str:
    queue_nr = int(queue_nr_text)

    if queue_nr in range(1, 11):
        return "Kuressaare haigla"
    elif queue_nr in range(11, 20):
        return "Tartu Ülikooli Naistekliinik"
    elif queue_nr in range(21, 151):
        return "Pelgulinna sünnitusmaja"
    elif queue_nr in range(151, 161):
        return "Keila haigla"
    elif queue_nr in range(161, 221):
        return "Rapla haigla/Loksa haigla/Hiiumaa haigla"
    elif queue_nr in range(221, 271):
        return "Ida-Viru keskhaigla"
    elif queue_nr in range(271, 371):
        return "Maarjamõisa kliinikum/Jõgeva haigla"
    elif queue_nr in range(371, 421):
        return "Narva haigla"
    elif queue_nr in range(421, 471):
        return "Pärnu haigla"
    elif queue_nr in range(471, 491):
        return "Haapsalu haigla"
    elif queue_nr in range(491, 521):
        return "Järvamaa haigla"
    elif queue_nr in range(521, 571):
        return "Rakvere haigla/Tapa haigla"
    elif queue_nr in range(571, 601):
        return "Valga haigla"
    elif queue_nr in range(601, 651):
        return "Viljandi haigla"
    elif queue_nr in range(651, 701):
        return "Lõuna-Eesti haigla (Võru)/Põlva haigla"


def calculate_checksum(id_code: str) -> int:
    count = 1
    results: list = []

    id_code_numerals = []
    for char in id_code[0:10]:
        id_code_numerals.append(int(char))

    for n in id_code_numerals:
        multi = count * n
        results.append(multi)
        # print(f"{count} * {n}")
        count += 1

        if count > 9:
            count = 1
            continue

    total = sum(results)
    modul = total % 11

    return modul


def is_correct_checksum(id_code: str) -> bool:
    return calculate_checksum(id_code) == int(id_code[-1])


def decode_id_code(id_code: str):
    if is_valid_id(id_code):
        century_code = int(id_code[0])
        birth_year = id_code[1:3]
        birth_month = id_code[3:5]
        birth_day = id_code[5:7]
        queue_nr = id_code[7:10]
        checksum = int(id_code[10])

        gender = decode_gender(century_code)

        birth_date = decode_date(century_code, birth_year, birth_month, birth_day)

        print(f"Sinu sugu: {gender}, "
              f"sünniaeg: {str(birth_date.tm_mday)}.{str(birth_date.tm_mon)}.{str(birth_date.tm_year)}. "
              f"Sa sündisid nädala {int(birth_date.tm_wday) + 1}. päeval ja sündisid järjekorranumbriga "
              f"{queue_nr}.")

        if int(birth_date.tm_year) < 2013:
            hospital = decode_hospital_nr(queue_nr)
            print(f"Sinu sünnihaigla oli {hospital}.")

    else:
        print("Viga isikukoodis: isikukood peab olema 11-kohaline ja sisaldama ainult numbreid.")


if __name__ == '__main__':
    # print(decode_date(4, "95", "10", "01"))
    decode_id_code("49510011524")
    # print(decode_hospital_nr("001"))
