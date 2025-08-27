# discord_components/components.py

from typing import List, Optional, Union
from discord.types.components import ComponentType

__all__ = (
    "ActionRow",
    "Button",
    "StringSelect",
    "TextInput",
    "UserSelect",
    "RoleSelect",
    "MentionableSelect",
    "ChannelSelect",
    "DatePicker",
    "TextDisplay",
    "Separator",
    "Container",
)

class BaseComponent:
    def to_dict(self) -> dict:
        raise NotImplementedError

class ActionRow(BaseComponent):
    def __init__(self, *components: BaseComponent):
        self.type = ComponentType.action_row.value  # 1
        self.components = components

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "components": [c.to_dict() for c in self.components],
        }

class Button(BaseComponent):
    def __init__(
        self,
        *,
        style: int,
        label: Optional[str] = None,
        custom_id: Optional[str] = None,
        url: Optional[str] = None,
        disabled: bool = False
    ):
        self.type = ComponentType.button.value  # 2
        self.style = style
        self.label = label
        self.custom_id = custom_id
        self.url = url
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "style": self.style,
            "disabled": self.disabled,
        }
        if self.label:
            data["label"] = self.label
        if self.custom_id:
            data["custom_id"] = self.custom_id
        if self.url:
            data["url"] = self.url
        return data

class StringSelect(BaseComponent):
    def __init__(
        self,
        *,
        custom_id: str,
        options: List[dict],
        placeholder: Optional[str] = None,
        min_values: int = 1,
        max_values: int = 1,
        disabled: bool = False
    ):
        self.type = ComponentType.string_select.value  # 3
        self.custom_id = custom_id
        self.options = options
        self.placeholder = placeholder
        self.min_values = min_values
        self.max_values = max_values
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "options": self.options,
            "min_values": self.min_values,
            "max_values": self.max_values,
            "disabled": self.disabled,
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        return data

class TextInput(BaseComponent):
    def __init__(
        self,
        *,
        custom_id: str,
        style: int,
        label: str,
        placeholder: Optional[str] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        required: bool = True
    ):
        self.type = ComponentType.text_input.value  # 4
        self.custom_id = custom_id
        self.style = style
        self.label = label
        self.placeholder = placeholder
        self.min_length = min_length
        self.max_length = max_length
        self.required = required

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "style": self.style,
            "label": self.label,
            "required": self.required,
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        if self.min_length is not None:
            data["min_length"] = self.min_length
        if self.max_length is not None:
            data["max_length"] = self.max_length
        return data

class UserSelect(BaseComponent):
    def __init__(self, *, custom_id: str, placeholder: Optional[str] = None, disabled: bool = False):
        self.type = ComponentType.user_select.value  # 5
        self.custom_id = custom_id
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        return data

class RoleSelect(BaseComponent):
    def __init__(self, *, custom_id: str, placeholder: Optional[str] = None, disabled: bool = False):
        self.type = ComponentType.role_select.value  # 6
        self.custom_id = custom_id
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        return data

class MentionableSelect(BaseComponent):
    def __init__(self, *, custom_id: str, placeholder: Optional[str] = None, disabled: bool = False):
        self.type = ComponentType.mentionable_select.value  # 7
        self.custom_id = custom_id
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        return data

class ChannelSelect(BaseComponent):
    def __init__(self, *, custom_id: str, placeholder: Optional[str] = None, disabled: bool = False):
        self.type = ComponentType.channel_select.value  # 8
        self.custom_id = custom_id
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "disabled": self.disabled,
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        return data

class DatePicker(BaseComponent):
    def __init__(
        self,
        *,
        custom_id: str,
        style: int = 1,  # 1=date only, 2=datetime
        placeholder: Optional[str] = None,
        disabled: bool = False
    ):
        self.type = ComponentType.date_picker.value  # 9
        self.custom_id = custom_id
        self.style = style
        self.placeholder = placeholder
        self.disabled = disabled

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "custom_id": self.custom_id,
            "style": self.style,
            "disabled": self.disabled
        }
        if self.placeholder:
            data["placeholder"] = self.placeholder
        return data

class TextDisplay(BaseComponent):
    def __init__(self, *, content: str):
        self.type = ComponentType.text_display.value  # 10
        self.content = content

    def to_dict(self) -> dict:
        return {"type": self.type, "content": self.content}

class Separator(BaseComponent):
    def __init__(
        self,
        *,
        divider: bool = True,
        spacing: int = 1,
        custom_id: Optional[str] = None
    ):
        self.type = ComponentType.separator.value  # 14
        self.divider = divider
        self.spacing = spacing
        self.custom_id = custom_id

    def to_dict(self) -> dict:
        data = {"type": self.type, "divider": self.divider, "spacing": self.spacing}
        if self.custom_id:
            data["custom_id"] = self.custom_id
        return data

class Container(BaseComponent):
    def __init__(
        self,
        components: List[Union[BaseComponent, dict]],
        *,
        accent_color: Optional[int] = None,
        spoiler: bool = False,
        custom_id: Optional[str] = None
    ):
        self.type = ComponentType.container.value  # 17
        self.components = components
        self.accent_color = accent_color
        self.spoiler = spoiler
        self.custom_id = custom_id

    def to_dict(self) -> dict:
        data = {
            "type": self.type,
            "components": [
                c.to_dict() if hasattr(c, "to_dict") else c
                for c in self.components
            ],
            "spoiler": self.spoiler
        }
        if self.accent_color is not None:
            data["accent_color"] = self.accent_color
        if self.custom_id:
            data["custom_id"] = self.custom_id
        return data
