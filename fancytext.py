class FancyText:
    @staticmethod
    def colorize(text, color_code):
        return f'\033[{color_code}m{text}\033[0m'

# Plain Colours

    @staticmethod
    def black(text):
        result = FancyText.colorize(text, '30')
        return result

    @staticmethod
    def red(text):
        result = FancyText.colorize(text, '31')
        return result

    @staticmethod
    def green(text):
        result = FancyText.colorize(text, '32')
        return result

    @staticmethod
    def yellow(text):
        result = FancyText.colorize(text, '33')
        return result

    @staticmethod
    def blue(text):
        result = FancyText.colorize(text, '34')
        return result

    @staticmethod
    def magenta(text):
        result = FancyText.colorize(text, '35')
        return result

    @staticmethod
    def cyan(text):
        result = FancyText.colorize(text, '36')
        return result

    @staticmethod
    def white(text):
        result = FancyText.colorize(text, '37')
        return result

    @staticmethod
    def bright_black(text):
        result = FancyText.colorize(text, '90')
        return result

    @staticmethod
    def bright_red(text):
        result = FancyText.colorize(text, '91')
        return result

    @staticmethod
    def bright_green(text):
        result = FancyText.colorize(text, '92')
        return result

    @staticmethod
    def bright_yellow(text):
        result = FancyText.colorize(text, '93')
        return result

    @staticmethod
    def bright_blue(text):
        result = FancyText.colorize(text, '94')
        return result

    @staticmethod
    def bright_magenta(text):
        result = FancyText.colorize(text, '95')
        return result

    @staticmethod
    def bright_cyan(text):
        result = FancyText.colorize(text, '96')
        return result

    @staticmethod
    def bright_white(text):
        result = FancyText.colorize(text, '97')
        return result

# Special Text 

    @staticmethod
    def success_text(text):  # Blue text with Green Background  ---  "Accepted Message"
        result = FancyText.colorize(text, '1;34;42')
        return result
    
    @staticmethod
    def selection_text(text):  # Bold Yellow text with Black Background --- "Selection Message"
        result = FancyText.colorize(text, '1;33;40')
        return result

    @staticmethod
    def warning_text(text):  # Red Background, White Text  --- "Warning Message"
        result = FancyText.colorize(text, '38;37;41')
        return result

    @staticmethod
    def deletion_text(text):  # Yellow Background, Red Text  --- "Deletion Message"
        result = FancyText.colorize(text, '1;31;43m')
        return result
    
    @staticmethod
    def confirm_text(text): # Bright white text, adds [Cancel to Abort] in Orange at the end
        result = FancyText.colorize(text, '38;5;231')
        addedtext = FancyText.colorize(' [Cancel to Abort]', '38;5;208')
        return (result + addedtext)
    
# End of Class