import logging

from mkdocs.config import Config
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

from mkdocs_use_site_url_plugin import add_site_path

LOGGER = logging.getLogger(__name__)


class UseBasePathPlugin(BasePlugin):
    def __init__(self):
        pass

    DEFAULT_ROOT_FOLDER = "docs"

    config_scheme = ()

    def on_page_markdown(self, markdown, page: Page = None, config: Config = None, **kwargs):
        site_url = config.data.get("site_url")

        new_md = add_site_path(markdown, site_url)
        return new_md
