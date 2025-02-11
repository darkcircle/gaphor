import pytest
from gaphas.painter import BoundingBoxPainter
from gaphas.view import GtkView

from gaphor import UML
from gaphor.diagram.inlineeditors import named_item_inline_editor
from gaphor.diagram.painter import ItemPainter
from gaphor.diagram.selection import Selection


@pytest.fixture
def view(diagram):
    view = GtkView(model=diagram, selection=Selection())
    view._qtree.resize((-100, -100, 400, 400))
    item_painter = ItemPainter(view.selection)
    view.painter = item_painter
    view.bounding_box_painter = BoundingBoxPainter(item_painter)
    return view


def test_named_item_inline_editor_with_element(diagram, element_factory, view):
    item = diagram.create(
        UML.classes.ClassItem, subject=element_factory.create(UML.Class)
    )
    view.selection.hovered_item = item
    result = named_item_inline_editor(item, view)

    assert result is True


def test_named_item_inline_editor_with_line(diagram, element_factory, view):
    item = diagram.create(
        UML.classes.DependencyItem, subject=element_factory.create(UML.Dependency)
    )
    view.selection.hovered_item = item
    result = named_item_inline_editor(item, view)

    assert result is True


def test_named_item_inline_editor_without_item(diagram, element_factory, view):
    item = diagram.create(UML.classes.DependencyItem)
    result = named_item_inline_editor(item, view)

    assert result is False
