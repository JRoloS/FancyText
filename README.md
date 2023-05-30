# Fancy Text
<p>A simple class that uses ANSI escape sequences to print Python Terminal Output text in colour without adding any imports to your code.<br>
It provides a simple and clean way to use color codes, allowing for easy invocation of colour options and contributing to code cleanlines<br>

### Usage

Copy the FancyText.py file to your project directory and import it as follows:<br>
`from FancyText Import *`

After that you can invoke the class by using:

`FancyText.[Colour]("Text")`

This will return the desired formated string for the colour effect to your text. 
(class is done this way to allow multiple colours options per line)

Example for a print statement:

`print(FancyText.red("This Text will be Red"))`

On this initial release FancyText Contains the basic EGA colours: <br>
Black, Dark Blue, Dark Green, Dark Cyan, Dark Red, Dark Magenta, Brown, Light Gray, Dark Gray, Light Blue, Light Green, Light Cyan, Light Red, Light Magenta, Yellow, White

Plus Some special Text modes (More will be added on future updates)

* success_text   - Blue text with Green Background        ---  "Accepted Message"
* selection_text - Bold Yellow text on Black Background   --- "Selection Message"
* warning_text   - White Text on Red Background           --- "Warning Message"
* deletion_text  - Red Text on Yellow Background          --- "Deletion Message"
* confirm_text   - Bright white text, adds [Cancel to Abort] in Orange at the end

You can check the colour options by typing Fancytext. and the autocomplete will show you all the available colours

This is the initial Release, new features will be added in the future.



### Version History

* 0.01 Initial Release - Class Created.


Author:
* [Jorge Rolo](https://github.com/JRoloS)











### License: 
Feel free to use, copy, fork, etc. If you come up with a neat feature, please let me know.

