import logging
import re

LOGGER = logging.getLogger(__name__)

md_link = re.compile(r'''(\[[^]]*]\()(/[^)]*)(\))|(\[[^]]*]:\s)(/[^\n\r)]*)''', re.DOTALL | re.UNICODE)


def process_link(link: str, site_url: str):
    return site_url + link


def process(site_url: str):
    def re_write_link(matchobj):
        group1 = matchobj.group(1)  # front stuff
        group2 = matchobj.group(2)  # the actual link
        group3 = matchobj.group(3)  # closing tag

        if group1 and group2 and group3:
            link = process_link(group2, site_url)

            return "{}{}{}".format(group1, link, group3)

        group4 = matchobj.group(4)  # front stuff
        group5 = matchobj.group(5)  # the actual link
        if group4 and group5:
            link = process_link(group5, site_url)

            return "{}{}".format(group4, link)

    return re_write_link


def add_site_url(content, site_url: str):
    file_data = re.sub(md_link, process(site_url), content)
    return file_data
