from wagtail import hooks
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models.blog import BlogIndexPage


class YourNewPageAdmin(ModelAdmin):
    model = BlogIndexPage
    menu_label = "New Article"
    menu_icon = "pilcrow"  # Choose an icon from https://docs.wagtail.io/en/stable/advanced_topics/customisation/admin_icons.html
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    search_fields = ("title",)


modeladmin_register(YourNewPageAdmin)


@hooks.register("register_icons")
def register_icons(icons):
    return icons + [
        "icons/latex-svgrepo-com.svg",
        "icons/filetype-html.svg",
    ]
