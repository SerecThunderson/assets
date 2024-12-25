import os
import json

# Map of hex colors to their descriptive names
COLOR_NAMES = {
    "#000000": "Black", "#0f0f0f": "Very Dark Gray", "#2d2d2d": "Dark Gray", "#454545": "Gray",
    "#5e5e5e": "Medium Gray", "#8a8a8a": "Light Gray", "#aeaeae": "Very Light Gray", "#dadada": "Almost White",
    "#ffffff": "White", "#ffa3b2": "Light Pink", "#ff7786": "Pink", "#ee0000": "Red", "#b21900": "Dark Red",
    "#681a00": "Very Dark Red", "#ffa17d": "Peach", "#ff7843": "Orange", "#f85100": "Vivid Orange",
    "#b24f00": "Dark Orange", "#663c00": "Brown", "#feffb1": "Light Yellow", "#ffcf13": "Golden Yellow",
    "#ffa801": "Gold", "#a68400": "Dark Gold", "#746a00": "Olive", "#ffff01": "Yellow",
    "#c0ea00": "Lime Yellow", "#97d000": "Light Lime", "#6fa400": "Lime", "#3a6000": "Dark Lime",
    "#cbff83": "Mint", "#3dee00": "Bright Green", "#00c000": "Green", "#007e11": "Dark Green",
    "#004c2e": "Forest Green", "#7dffba": "Aqua", "#00f266": "Bright Teal", "#00d26c": "Teal",
    "#009864": "Dark Teal", "#00705e": "Deep Teal", "#00ffff": "Cyan", "#00e2ba": "Light Cyan",
    "#00b8b1": "Aqua Cyan", "#008296": "Slate Cyan", "#00619a": "Slate Blue", "#81dcff": "Sky Blue",
    "#39a4ff": "Light Blue", "#3962ff": "Blue", "#0000f4": "Vivid Blue", "#1600a0": "Deep Blue",
    "#9fb5ff": "Periwinkle", "#7f85ff": "Lavender Blue", "#661bff": "Vivid Purple", "#5e00b6": "Royal Purple",
    "#4d0064": "Deep Purple", "#d3bbff": "Lilac", "#d88dff": "Lavender", "#cd00e0": "Magenta",
    "#a80082": "Deep Magenta", "#6c0044": "Crimson", "#f5b5ff": "Light Pink Magenta", "#ff71df": "Pink Magenta",
    "#ff1784": "Bright Pink", "#d01147": "Dark Pink", "#82001e": "Burgundy"
}

def create_nft_json(file_name, base_url):
    # Extract number and color from the file name
    number, color_hex = file_name.split('.')[0].split('_')
    number = str(int(number))  # Truncate leading zeros
    color_hex = f"#{color_hex}"  # Ensure the hex format
    
    # Get the color name from the map (fallback to 'Unknown' if not found)
    color_name = COLOR_NAMES.get(color_hex, "Unknown")
    
    # Construct the JSON object
    nft_json = {
        "description": "Free brick for Christmas",
        "image": f"{base_url}/{file_name}",
        "name": f"{color_name} Christmas Brick {number}",
        "attributes": [
            {"trait_type": "Color (Hex)", "value": color_hex},
            {"trait_type": "Color (Name)", "value": color_name},
            {"trait_type": "Number", "value": number}
        ]
    }

    return nft_json

def main():
    assets_folder = 'assets'
    output_folder = 'nft_json'
    base_url = "https://raw.githubusercontent.com/SerecThunderson/assets/main/bricks/assets"

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_names = sorted(os.listdir(assets_folder), key=lambda x: int(x.split('.')[0].split('_')[0]))
    
    # Process the first 10k
    for i, file_name in enumerate(file_names):
        if i >= 10001 or not file_name.endswith('.png'):
            break

        nft_json = create_nft_json(file_name, base_url)
        json_file_name = os.path.join(output_folder, f"{i}.json")

        # Write the JSON to a file
        with open(json_file_name, 'w') as json_file:
            json.dump(nft_json, json_file, indent=4)

    print("NFT JSON files created.")

if __name__ == "__main__":
    main()
