
import markdown2


def markdown_to_html(text):
    return markdown2.markdown(text)


class AdminModelUrlMixin:

    def link(self, obj):
        return f'<a href="{obj.get_absolute_url()}">{obj.slug}</a>'
    link.allow_tags = True
