# Nautilus Disk Usage Analyzer Extension

A lightweight Nautilus (GNOME Files) extension that adds a **"Scan with Disk Usage Analyzer"** option to the right-click context menu for folders.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Linux%20%2F%20GNOME-lightgrey.svg)

## Features

- Adds a native context menu item when right-clicking any single folder in GNOME Files.
- Launches GNOME Disk Usage Analyzer (`baobab`) directly on the selected directory.
- Written in clean, dependency-light Python using `python3-nautilus` and GTK 4 / Nautilus 4.1 bindings.

## Requirements

- **GNOME Files (Nautilus)** `43+` (GTK 4 / Nautilus `4.1` API)
- **`python3-nautilus`** (Python bindings for Nautilus)
- **`baobab`** (GNOME Disk Usage Analyzer)

### Installing Dependencies

**Ubuntu / Debian:**
```bash
sudo apt update
sudo apt install python3-nautilus baobab
```

**Fedora:**
```bash
sudo dnf install nautilus-python baobab
```

**Arch Linux:**
```bash
sudo pacman -S python-nautilus baobab
```

## Installation

1. Create the local Nautilus Python extensions directory if it does not already exist:
   ```bash
   mkdir -p ~/.local/share/nautilus-python/extensions
   ```

2. Copy `disk_usage_extension.py` into the extensions directory:
   ```bash
   cp disk_usage_extension.py ~/.local/share/nautilus-python/extensions/
   ```

3. Restart Nautilus to load the extension:
   ```bash
   nautilus -q
   ```

## Usage

1. Open **Files** (Nautilus).
2. Right-click on any single folder.
3. Click **Scan with Disk Usage Analyzer** to inspect the folder's disk usage in `baobab`.

## Uninstallation

To remove the extension, delete the script from the extensions folder and restart Nautilus:

```bash
rm ~/.local/share/nautilus-python/extensions/disk_usage_extension.py
nautilus -q
```

## License

This project is open source and available under the [MIT License](LICENSE).