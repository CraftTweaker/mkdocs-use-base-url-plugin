import os

import sys
from shutil import rmtree
from pathlib import Path
from setuptools import setup, Command

HERE = Path(__file__).parent


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system(
            "{0} setup.py sdist bdist_wheel --universal".format(sys.executable)
        )

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        # self.status("Pushing git tags…")
        # os.system("git tag v{0}".format(about["__version__"]))
        # os.system("git push --tags")

        sys.exit()


setup(
    name="mkdocs_use_site_url_plugin",
    version="1.0.0",
    packages=["mkdocs_use_site_url_plugin"],
    url="https://github.com/CraftTweaker/mkdocs-use-site-url-plugin",
    license="MIT",
    author="Jaredlll08",
    author_email="jaredlll08@gmail.com",
    description="Mkdocs plugin to change links to include the site url as set via mkdocs.yml",
    long_description="This plugin ensures that links are full absolute links according to the site_url set in mkdocs.yml, this is useful for sites such as the [CraftTweaker Docs](https://docs.blamejared.com), which serves files out of `/version/lang/` which Mkdocs has issues handling.",
    long_description_content_type="text/markdown",
    entry_points={
        "mkdocs.plugins": [
            "use-site-url = mkdocs_use_site_url_plugin.plugin:UseSiteUrlPlugin"
        ]
    },
    cmdclass={"upload": UploadCommand}, install_requires=['mkdocs']
)
