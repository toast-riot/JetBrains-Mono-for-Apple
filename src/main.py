import os
import plistlib
import uuid

# The path to the fonts. Make sure your fonts are in a ttf format
FONT_PATH = "./fonts"

# The path to the output file
OUTPUT_PATH = "./output"

# Example config
CONFIG = {
    "display_name": "JetBrains Mono",
    "description": "JetBrains Mono and all its variations in one config profile",
    "organization": "toast_riot",
    "identifier": "com.toast-riot.JetBrains-Mono",
    "uuid": uuid.uuid4().urn[9:].upper(), # Generate unique id so it does not overwrite other profiles
    "version": 1
}


def main():
    payloads = []
    for font in os.listdir(FONT_PATH):

        with open(os.path.join(FONT_PATH, font), "rb") as f:
            font_data = f.read()

        payloads.append({
            "Font": font_data,
            "PayloadIdentifier": CONFIG["identifier"] + "." + font,
            "PayloadOrganization": CONFIG["organization"],
            "PayloadType": "com.apple.font",
            "PayloadUUID": uuid.uuid4().urn[9:].upper(),
            "PayloadVersion": 1
        })

    # Make the profile
    plist = {
        "PayloadContent": payloads,
        "PayloadDescription": CONFIG["description"],
        "PayloadDisplayName": CONFIG["display_name"],
        "PayloadIdentifier": CONFIG["identifier"],
        "PayloadOrganization": CONFIG["organization"],
        "PayloadRemovalDisallowed": False,
        "PayloadType": "Configuration",
        "PayloadUUID": CONFIG["uuid"],
        "PayloadVersion": CONFIG["version"]
    }

    # Write the profile
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    with open(os.path.join(OUTPUT_PATH, "font.mobileconfig"), 'wb') as fp:
        plistlib.dump(plist, fp)

if __name__ == "__main__":
    main()
