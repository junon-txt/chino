from mkdocs.plugins import BasePlugin
import logging
import sys

log = logging.getLogger(f"mkdocs.plugins.{__name__}")

class PathRewriterPlugin(BasePlugin):
    def on_page_content(self, html, page, config, files):
        if 'serve' in sys.argv:
            log.info("Running locally, skipping path rewriting.")
            return html
        
        base_url = config.get("extra", {}).get("base_url", "")
        log.info(f"Replacing /imgs/ to: {base_url}/imgs/")
        html = html.replace('src="/imgs/', f'src="{base_url}/imgs/')
        return html
