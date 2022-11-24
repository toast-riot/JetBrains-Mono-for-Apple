##  <p style="text-align: center;">[INSTALL FONT](https://github.com/James-Tuppen/JetBrains-Mono-for-Apple/raw/main/JetBrains%20Mono.mobileconfig)</p>

## JetBrains Mono for Apple
This is a configuration profile for iOS, iPadOS and MacOS that includes the entire JetBrain Mono font and all its variations (italic, bold, thin, ect.). This was made so you don’t have to install each of the 32 fonts separately through some half-gigabyte ad-infested font app. Also includes the (very crappy) code I used to make it. Perhaps I’ll make a website to do this online at some point.

#### The story
I want all variations of JetBrain Mono in one profile, I spend two hours on an iPad making a script to do it. If my code sucks it’s because I typed it on an iPad. Also not tested in anything other than Pythonista, and only seems to run in Python 2. Yes I could make it run in Python 3, but why bother?

#### The full story mostly so I can look back at how much time I wasted as a kid
-I have five different school assessments due in two days, and I am a long way behind
-I want JetBrains on my school iPad because it is one of the only good fonts that exists
-I download the ttf files
-I look up how to install them and find multiple half-gigabyte apps that have ads and in app purchases that will install them
-I hate that kind of stuff
-I have worked with configuration profiles before
-I don’t have a Mac, so no Apple Configurator
-I use [Pythonista](https://apps.apple.com/au/app/pythonista-3/id1085978097) to make a profile for the default, bold and italic font
-I want to have all the variations, but not 32 profiles installed manually. You even have to go through slow dialog and put your password in each time
-I try putting all the fonts in one .plist then turn it into a .mobileconfig with Text Workflow, but the file quickly passes 5mb and my editors crash or lag editing it
-I write a Python script to do it for me
