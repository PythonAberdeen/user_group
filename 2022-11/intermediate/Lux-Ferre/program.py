import re, collections


def open_file() -> str:
    with open("../fake_client_data.csv") as f:
        raw_data = f.read()

    return raw_data


def save_file(file_data: str):
    with open('data.csv', 'w') as f:
        f.write(file_data)


def restore_csv(raw_data: str):
    comma_data = re.sub(r"\s{3}", ", ", raw_data)

    save_file(comma_data)


def count_tops(raw_data: str) -> collections.Counter:
    top_domains = re.findall(r"\.[A-Za-z]+\s", raw_data)
    domain_count = collections.Counter(top_domains)

    return domain_count


def count_users(raw_data: str) -> collections.Counter:
    top_domains = re.findall(r"\@[A-Za-z\.]+\s", raw_data)
    domain_count = collections.Counter(top_domains)

    return domain_count


def count_postcodes(raw_data: str) -> collections.Counter:
    postcode_starts = re.findall(r"\s{3}\d\d+(?=[\s\-])", raw_data)
    postcode_count = collections.Counter(postcode_starts)

    return postcode_count


def count_genders(raw_data: str) -> str:
    male_count = len(re.findall(r"\s{3}[mM][aA][lL][eE]\s{3}", raw_data))
    female_count = len(re.findall(r"\s{3}[fF][eE][mM][aA][lL][eE]\s{3}", raw_data))
    if male_count > female_count:
        return "male"
    elif female_count > male_count:
        return "female"
    else:
        return "equal"


def main():
    raw_data = open_file()
    restore_csv(raw_data)

    print(count_tops(raw_data))
    print(count_users(raw_data))
    print(count_postcodes(raw_data))
    print(count_genders(raw_data))


if __name__ == "__main__":
    main()
