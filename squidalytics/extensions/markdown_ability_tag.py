import xml.etree.ElementTree as etree

from ability_map import ABILITIES
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor

TAG_RE = r"\{ability\}(.+?)\{\/ability\}"


class AbilityInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        # This method is called when the regex pattern is found in the markdown text.

        # m.group(1) is the content inside the {ability}...{/ability}
        tag_name = m.group(1)

        # Lookup the ability in the ABILITIES list
        ability = ABILITIES.get(tag_name)

        if not ability:
            return None, None, None  # tag not found

        # Create a new img element
        img = etree.Element("img")
        img.set("src", f'image:{ability["image_id"]}')
        img.set("alt", ability["name"])
        img.set("title", ability["description"])

        # Create a new div element and append the img to it
        div = etree.Element("div")
        div.set("class", "ability-container")
        div.append(img)

        return div, m.start(0), m.end(0)


class AbilityExtension(Extension):
    def extendMarkdown(self, md):
        # Register the inline processor with the markdown parser
        md.inlinePatterns.register(
            AbilityInlineProcessor(TAG_RE, md), "ability", 175
        )
