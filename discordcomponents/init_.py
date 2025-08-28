# discord_components/__init__.py

from .http_patch import setup_http_patch
from .components import (
    __all__ as _COMP_NAMES,
    ActionRow,
    Button,
    StringSelect,
    TextInput,
    UserSelect,
    RoleSelect,
    MentionableSelect,
    ChannelSelect,
    DatePicker,
    TextDisplay,
    Separator,
    Container,
    Section,
    Thumbnail,
    MediaGallery,
    FileComponent,
    Label,
)

def setup(bot):
    # Monkey‐patch the internal HTTPClient.create_message
    setup_http_patch()
    # Expose all component classes under bot.ComponentsV2
    bot.ComponentsV2 = {name: globals()[name] for name in _COMP_NAMES}
