# Mkdocs use site url in links

This plugin ensures that links are full absolute links according to the site_url set in mkdocs.yml, this is useful for sites such as the [CraftTweaker Docs](https://docs.blamejared.com), which serves files out of `/version/lang/` which Mkdocs has issues handling.

## Installation

```bash
pip install git+https://github.com/CraftTweaker/mkdocs-use-site-url-plugin.git
```


## Usage

In your `mkdocs.yml` file add `use-site-url` to the plugins entry:

```yaml
plugins:
  - use-site-url
```