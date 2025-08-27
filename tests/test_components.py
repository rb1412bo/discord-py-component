# tests/test_components.py

import pytest
from discord_components.components import Separator, Container, TextDisplay

def test_separator_to_dict():
    sep = Separator(divider=False, spacing=2, custom_id="sep1")
    expected = {"type": 14, "divider": False, "spacing": 2, "custom_id": "sep1"}
    assert sep.to_dict() == expected

def test_container_to_dict():
    text = TextDisplay(content="Hello")
    cont = Container(
        components=[text],
        accent_color=0x123456,
        spoiler=True,
        custom_id="cont1"
    )
    payload = cont.to_dict()
    assert payload["type"] == 17
    assert payload["components"][0]["content"] == "Hello"
    assert payload["accent_color"] == 0x123456
    assert payload["spoiler"] is True
    assert payload["custom_id"] == "cont1"
