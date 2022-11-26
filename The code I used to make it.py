import plistlib
import uuid
import os

#Where I put all the fonts I'm about to package
font_path = '/var/mobile/Containers/Shared/AppGroup/32AEC5B4-31E0-4501-9EC9-7CCAC0EB99A7/Pythonista3/Documents/Scratchpad/Combine/in'

def main():
	payloads = []
	#Get the ttf fonts
	for fnt in os.listdir(font_path):
		#Get font
		with open(font_path + '/' + fnt, 'rb') as f:
			font_data = f.read()
		
		unique_id = uuid.uuid4().urn[9:].upper()
		#Make the font into a payload and add it to the list
		payloads.append({
		'Font': plistlib.Data(font_data),
		'PayloadIdentifier': unique_id,
		'PayloadOrganization': 'James Tuppen',
		'PayloadType': 'com.apple.font',
		'PayloadUUID': unique_id, 'PayloadVersion': 1})
	
	#Generate unique id so it does not overwrite other profiles
	unique_id = uuid.uuid4().urn[9:].upper()
	#Make the profile
	config = {
	'PayloadContent': payloads,
	'PayloadDescription': 'JetBrains Mono and all its variations in one config profile :)  https://github.com/James-Tuppen/JetBrains-Mono-for-Apple',
	'PayloadDisplayName': 'JetBrains Mono',
	'PayloadIdentifier': unique_id,
	'PayloadOrganization': 'James Tuppen',
	'PayloadRemovalDisallowed': False,
	'PayloadType': 'Configuration',
	'PayloadUUID': unique_id,
	'PayloadVersion': 1}
	
	#Save as file
	plistlib.writePlist(config, 'font.mobileconfig')

if __name__ == '__main__':
	main()