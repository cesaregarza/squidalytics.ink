from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
    URLBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from wagtailmarkdown.blocks import MarkdownBlock


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "cms/blocks/image_block.html"


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a header size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "cms/blocks/heading_block.html"


class BlockQuote(StructBlock):
    """
    Custom `StructBlock` that allows the user to attribute a quote to the author
    """

    text = TextBlock()
    attribute_name = CharBlock(
        blank=True, required=False, label="e.g. Mary Berry"
    )

    class Meta:
        icon = "openquote"
        template = "cms/blocks/blockquote.html"


class EquationBlock(StructBlock):
    """
    Custom `StructBlock` that will parse all text as a single LaTeX equation
    """

    equation = TextBlock()

    class Meta:
        icon = "latex"
        template = "cms/blocks/equation_block.html"
        label = "Equation"


class HTMLBlock(RawHTMLBlock):
    class Meta:
        icon = "html-icon"
        label = "HTML"


# StreamBlocks
class BaseStreamBlock(StreamBlock):
    """
    Define the custom blocks that `StreamField` will utilize
    """

    heading_block = HeadingBlock()
    paragraph_block = MarkdownBlock(
        icon="pilcrow", template="cms/blocks/paragraph_block.html"
    )
    image_block = ImageBlock()
    block_quote = BlockQuote()
    embed_block = EmbedBlock(
        help_text="Insert an embed URL e.g https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
        template="cms/blocks/embed_block.html",
    )
    equation_block = EquationBlock()
    html_block = HTMLBlock()
    code_block = CodeBlock(
        label="Code",
    )


class AudienceSpecificContentBlock(StructBlock):
    audience_name = CharBlock(required=True)
    content = BaseStreamBlock()

    class Meta:
        icon = "group"
        template = "cms/blocks/audience_specific_content_block.html"
        label = "Audience Specific Content"
