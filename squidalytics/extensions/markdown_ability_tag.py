import logging
import xml.etree.ElementTree as etree

from extensions.ability_map import ABILITIES
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor
from wagtail.images.models import Image

logger = logging.getLogger(__name__)

TAG_RE = r"\{ability\}(.+?)\{\/ability\}"


class AbilityInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        # This method is called when the regex pattern is found in the markdown text.

        # m.group(1) is the content inside the {ability}...{/ability}
        tag_name = m.group(1).upper()

        # Lookup the ability in the ABILITIES list
        ability = ABILITIES.get(tag_name)

        if not ability:
            return None, None, None  # tag not found

        image_id = ability["image_id"]
        try:
            wagtail_image = Image.objects.get(id=image_id)
        except Image.DoesNotExist:
            return None, None, None

        image_url = wagtail_image.get_rendition("fill-20x20").url

        # Create a new img element
        img = etree.Element("img")
        img.set("src", image_url)
        img.set("alt", ability["name"])
        img.set("title", ability["description"])
        img.set("class", "ability-image")
        img.tail = " " + ability["name"]

        # Create a new span element and append the img and text to it
        span = etree.Element("span")
        span.set("class", "ability-container")
        span.append(img)

        return span, m.start(0), m.end(0)


class AbilityExtension(Extension):
    def extendMarkdown(self, md):
        # Register the inline processor with the markdown parser
        md.inlinePatterns.register(
            AbilityInlineProcessor(TAG_RE, md), "ability", 175
        )
        # Write to a text file since we can't see the output of print statements
        # with the Django logging setup
