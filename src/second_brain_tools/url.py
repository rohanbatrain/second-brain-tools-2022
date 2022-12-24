import re


def get_domain(url):
    # Use a regular expression to extract the domain from the URL
    domain_regex = re.compile(r"(?:https?://)?(?:www\.)?([^/]+)")
    match = domain_regex.search(url)
    if match:
        return match.group(1)
    else:
        return None


def get_last_section_of_url(url):
    # Split the URL by '/' character
    url_sections = url.split('/')
    # Get the last element of the resulting list
    last_section = url_sections[-1]
    if not last_section:
        last_section = url_sections[-2]
    return last_section
