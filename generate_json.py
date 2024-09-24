import os
import json

def generate_icons_json(icons_dir, output_file, base_url, json_name="HanepIcons", description="description"):

    if not os.path.isdir(icons_dir):
        raise FileNotFoundError

    icons = []
    for filename in os.listdir(icons_dir):
        if filename.lower().endswith('.png'):
            icon_entry = {
                "name": filename,
                "url": f"{base_url}/{filename}"
            }
            icons.append(icon_entry)

    data = {
        "name": json_name,
        "icons": icons,
        "description": description
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    ICONS_DIRECTORY = "Icons"
    OUTPUT_JSON = "HanepIcons.json"
    BASE_URL = "https://raw.githubusercontent.com/hanepudding/icon-library/master/Icons"
    generate_icons_json(ICONS_DIRECTORY, OUTPUT_JSON, BASE_URL)
