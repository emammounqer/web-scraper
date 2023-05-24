from bs4 import BeautifulSoup, ResultSet, element
import requests


def get_citations_needed_count(url: str) -> int:
    """
    This function takes in a url and returns the number of citations needed

    Args:
        url (str): url of the page

    Returns:
        int: number of citations needed
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    l = soup.find_all('a', title='Wikipedia:Citation needed')
    return len(l)


def get_citations_needed_report(url: str) -> str:
    """
    This function takes in a url and returns a report of the citations needed

    Args:
        url (str): url of the page

    Returns:
        str: report of citations needed
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    p_elements: ResultSet[element.Tag] = soup.find_all('p')
    return ''.join(
        i.text + '\n' for i in p_elements if i.find('a', title='Wikipedia:Citation needed')
    )


def write_report(url: str) -> None:
    """
    This function takes in a url and writes a report of the citations needed to a file

    Args:
        url (str): url of the page
    """
    rep = (
        f"Number of citations needed: {str(get_citations_needed_count(url))}"
        + "\n"
    )
    rep += "Report of citations needed: \n" + get_citations_needed_report(url)

    with open('report.txt', 'w') as f:
        f.write(rep)


if __name__ == "__main__":
    # ANSI escape sequences for colors
    COLOR_RED = "\033[91m"
    COLOR_GREEN = "\033[92m"
    COLOR_YELLOW = "\033[93m"
    COLOR_BLUE = "\033[94m"
    COLOR_RESET = "\033[0m"

    write_report("https://en.wikipedia.org/wiki/History_of_Mexico")

    print(COLOR_BLUE)
    print(" ################################ ")
    print(" #  Number of citations needed  # ")
    print(" ################################ ")
    print(COLOR_RESET)
    print(" ")
    print(get_citations_needed_count("https://en.wikipedia.org/wiki/History_of_Mexico"))
    print(" ")

    print(COLOR_BLUE)
    print(" ################################ ")
    print(" #  Report of citations needed  # ")
    print(" ################################ ")
    print(COLOR_RESET)
    print(" ")
    citations_report = get_citations_needed_report(
        "https://en.wikipedia.org/wiki/History_of_Mexico")
    formatted_report = citations_report.replace(
        "[citation needed]", f"{COLOR_GREEN}[citation needed]{COLOR_RESET}")
    print(formatted_report)
    print(" ")
