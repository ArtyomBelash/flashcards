from django import template

from cards.models import BOXES, Card

register = template.Library()


@register.inclusion_tag(filename="cards/box_links.html", takes_context=True)
def boxes_as_links(context):
    request = context['request']
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num, owner=request.user).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })
    return {"boxes": boxes}
