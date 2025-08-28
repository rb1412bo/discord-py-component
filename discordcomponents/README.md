# 📦 discordcomponents

This folder contains the **core library code** for `discord-py-components`,  
a lightweight extension for `discord.py` that adds full support for **Discord Components V2**.

## 📁 Structure

- **`__init__.py`** – Initializes the package, applies the HTTP patch, and registers all component classes under `bot.ComponentsV2`
- **`components.py`** – Definitions for all supported UI and layout components  
  _(Buttons, Selects, Modals, Containers, Separators, Section, Label, Thumbnail, MediaGallery, etc.)_
- **`http_patch.py`** – Monkey‑patch for Discord.py’s HTTP client to enable sending `components_v2` payloads

## 🚀 Usage

1. Install this package alongside `discord.py`
2. Load the extension in your bot:
   ```python
   bot.load_extension("discordcomponents")
