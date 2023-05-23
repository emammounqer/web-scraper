from bs4 import BeautifulSoup, ResultSet, element
import requests


def get_citations_needed_count(url: str) -> int:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    l = soup.find_all('a', title='Wikipedia:Citation needed')
    return len(l)


def get_citations_needed_report(url: str) -> str:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p_elements: ResultSet[element.Tag] = soup.find_all('p')
    return ''.join(
        i.text + '\n' for i in p_elements if i.find('a', title='Wikipedia:Citation needed')
    )


def write_report(url: str) -> None:
    with open('report.txt', 'w') as f:
        f.write(get_citations_needed_report(url))


if __name__ == "__main__":
    write_report("https://en.wikipedia.org/wiki/History_of_Mexico")
    print(" ################################ ")
    print(" #                              # ")
    print(" #  Number of citations needed  # ")
    print(" #                              # ")
    print(" ################################ ")
    print(" ")
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(" ")

    print(" ################################ ")
    print(" #                              # ")
    print(" #  Report of citations needed  # ")
    print(" #                              # ")
    print(" ################################ ")
    print(" ")
    print(get_citations_needed_report("https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(" ")
