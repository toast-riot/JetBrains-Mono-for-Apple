import plistlib
import uuid
import os

#The path to the fonts. Make sure your fonts are in a ttf format
FONT_PATH = "./fonts"

# Example config
CONFIG = {
	"display_name": "JetBrains Mono",
	"description": "JetBrains Mono and all its variations in one config profile",
	"organization": "toast_riot",
	"identifier": "com.toast-riot.JetBrains-Mono",
	"uuid": uuid.uuid4().urn[9:].upper(), #Generate unique id so it does not overwrite other profiles
	"version": 1
}

def main():
	payloads = []
	for font in os.listdir(FONT_PATH):
		#Get font
		with open(FONT_PATH + "/" + font, "rb") as f:
			font_data = f.read()
		
		#Make the font into a payload and add it to the list
		payloads.append({
			"Font": font_data,
			"PayloadIdentifier": CONFIG["identifier"] + "." + font,
			"PayloadOrganization": CONFIG["organization"],
			"PayloadType": "com.apple.font",
			"PayloadUUID": uuid.uuid4().urn[9:].upper(),
			"PayloadVersion": 1
		})
	
	#Make the profile
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

	if not os.path.exists("out"):
		os.makedirs("out")
	
	with open("out/font.mobileconfig", 'wb') as fp:
		plistlib.dump(plist, fp)

if __name__ == "__main__":
	main()