# FancyText Class 

class FancyText:
    @staticmethod
    def colorize(text, color_code, background_code=None):
        if background_code is not None:
            return f'\033[1;{color_code};{background_code}m{text}\033[0m'
        else:
            return f'\033[1;{color_code}m{text}\033[0m'

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
        result = FancyText.colorize(text, '1;37;41')
        return result

    @staticmethod
    def deletion_text(text):  # Yellow Background, Red Text  --- "Deletion Message"
        result = FancyText.colorize(text, '1;31;43')
        return result
    
    @staticmethod
    def confirm_text(text): # Bright white text, adds [Cancel to Abort] in Orange at the end
        result = FancyText.colorize(text, '38;5;231')
        addedtext = FancyText.colorize(' [Cancel to Abort]', '38;5;208')
        return (result + addedtext)
    
    @staticmethod
    def rainbow_text(text):  # Rainbow Color Text
        colors = ['31', '32', '33', '34', '35', '36']  # Red, Green, Yellow, Blue, Magenta, Cyan
        rainbow_text = ''

        for i, letter in enumerate(text):
            color_code = colors[i % len(colors)]
            colored_letter = FancyText.colorize(letter, color_code)
            rainbow_text += colored_letter

        return rainbow_text


    @staticmethod
    def rainbow_bg(text):  # Rainbow Color Background
        background_colors = ['41', '42', '43', '44', '45', '46']  # Red, Green, Yellow, Blue, Magenta, Cyan
        rainbow_text = ''

        for i, letter in enumerate(text):
            background_color = background_colors[i % len(background_colors)]
            colored_letter = FancyText.colorize(letter, '30', background_color)
            rainbow_text += colored_letter

        return rainbow_text


    @staticmethod
    def toggle_case(text):
        toggle_case_text = ""
        is_upper = True  # First letter should be uppercase

        for char in text:
            if char.isalpha():
                if is_upper:
                    toggle_case_text += char.upper()
                else:
                    toggle_case_text += char.lower()

                is_upper = not is_upper
            else:
                toggle_case_text += char

        return toggle_case_text


    @staticmethod
    def toggle_case_low(text):
        toggle_case_text = ""
        is_upper = False  # Flag to toggle case

        for char in text:
            if char.isalpha():
                if is_upper:
                    toggle_case_text += char.upper()
                else:
                    toggle_case_text += char.lower()

                is_upper = not is_upper
            else:
                toggle_case_text += char

        return toggle_case_text


    @staticmethod
    def big_letter_from_letter(text):  #Takes every letter and transforms it into a 5 lines wide letter made out of the same letter
        ascii_letters = {
            'A': ['  A  ',
                ' A A ',
                'AAAAA',
                'A   A',
                'A   A'],
            'B': ['BBBB ',
                'B   B',
                'BBBB ',
                'B   B',
                'BBBB '],
            'C': [' CCCC',
                'C    ',
                'C    ',
                'C    ',
                ' CCCC'],
            'D': ['DDDD ',
                'D   D',
                'D   D',
                'D   D',
                'DDDD '],
            'E': ['EEEEE',
                'E    ',
                'EEE  ',
                'E    ',
                'EEEEE'],
            'F': ['FFFFF',
                'F    ',
                'FFF  ',
                'F    ',
                'F    '],
            'G': [' GGG ',
                'G    ',
                'G  GG',
                'G   G',
                ' GGG '],
            'H': ['H   H',
                'H   H',
                'HHHHH',
                'H   H',
                'H   H'],
            'I': ['IIIII',
                '  I  ',
                '  I  ',
                '  I  ',
                'IIIII'],
            'J': ['JJJJJ',
                '   J ',
                '   J ',
                'J  J ',
                ' JJ  '],
            'K': ['K   K',
                'K  K ',
                'KKK  ',
                'K  K ',
                'K   K'],
            'L': ['L    ',
                'L    ',
                'L    ',
                'L    ',
                'LLLLL'],
            'M': ['M   M',
                'MM MM',
                'M M M',
                'M   M',
                'M   M'],
            'N': ['N   N',
                'NN  N',
                'N N N',
                'N  NN',
                'N   N'],
            'O': [' OOO ',
                'O   O',
                'O   O',
                'O   O',
                ' OOO '],
            'P': ['PPPP ',
                'P   P',
                'PPPP ',
                'P    ',
                'P    '],
            'Q': [' QQQ ',
                'Q   Q',
                'Q Q Q',
                'QQ  Q',
                ' QQQQ'],
            'R': ['RRRR ',
                'R   R',
                'RRRR ',
                'R  R ',
                'R   R'],
            'S': [' SSS ',
                'S    ',
                ' SSS ',
                '    S',
                ' SSS '],
            'T': ['TTTTT',
                '  T  ',
                '  T  ',
                '  T  ',
                '  T  '],
            'U': ['U   U',
                'U   U',
                'U   U',
                'U   U',
                ' UUU '],
            'V': ['V   V',
                'V   V',
                'V   V',
                ' V V ',
                '  V  '],
            'W': ['W   W',
                'W   W',
                'W W W',
                'WW WW',
                'W   W'],
            'X': ['X   X',
                ' X X ',
                '  X  ',
                ' X X ',
                'X   X'],
            'Y': ['Y   Y',
                ' Y Y ',
                '  Y  ',
                '  Y  ',
                '  Y  '],
            'Z': ['ZZZZZ',
                '   Z ',
                '  Z  ',
                ' Z   ',
                'ZZZZZ'],
            ' ': ['     ',
                '     ',
                '     ',
                '     ',
                '     '],
            ',': ['     ',
                '     ',
                '     ',
                '  ,  ',
                '  ,  '],
            '.': ['     ',
                '     ',
                '     ',
                '     ',
                '  .  '],
            '!': ['  !  ',
                '  !  ',
                '  !  ',
                '     ',
                '  !  '],
            '?': [' ??? ',
                '    ?',
                '  ?? ',
                '     ',
                '  ?  '],
            '-': ['     ',
                '     ',
                ' --- ',
                '     ',
                '     '],
            '_': ['     ',
                '     ',
                '     ',
                '     ',
                '____ '],
            '+': ['     ',
                '  +  ',
                ' +++ ',
                '  +  ',
                '     '],
            '=': ['     ',
                ' === ',
                '     ',
                ' === ',
                '     '],
            '#': [' # # ',
                '#####',
                ' # # ',
                '#####',
                ' # # '],
            '@': [' @@@ ',
                '@   @',
                '@ @@@',
                '@     ',
                ' @@@@'],
            '$': [' $$$ ',
                '$$$$$',
                ' $$$ ',
                '$$$$$',
                ' $$$ '],
            '%': ['%%   %',
                '%%  % ',
                '   %  ',
                '  %%% ',
                '%   %%'],
            '&': [' &&  ',
                '& & &',
                ' &&& ',
                '& &  ',
                ' &&&&'],
            '*': ['     ',
                '* * *',
                '  *  ',
                '* * *',
                '     '],
            '(': ['   ( ',
                '  (  ',
                '  (  ',
                '  (  ',
                '   ( '],
            ')': [' )   ',
                '  )  ',
                '  )  ',
                '  )  ',
                ' )   '],
            '[': [' [[] ',
                ' [   ',
                ' [   ',
                ' [   ',
                ' [[] '],
            ']': [' ]] ',
                '   ] ',
                '   ] ',
                '   ] ',
                ' ]] '],
            '{': ['  {{ ',
                ' {   ',
                ' {{  ',
                ' {   ',
                '  {{ '],
            '}': [' }}  ',
                '   } ',
                '  }} ',
                '   } ',
                ' }}  '],
            '<': ['   < ',
                '  <  ',
                ' <   ',
                '  <  ',
                '   < '],
            '>': [' >   ',
                '  >  ',
                '   > ',
                '  >  ',
                ' >   '],
            ':': ['     ',
                '  :  ',
                '     ',
                '  :  ',
                '     '],
            ';': ['     ',
                '  ;  ',
                '     ',
                '  ;  ',
                '  ;  '],
            '\'': ['  \'  ',
                '  \'  ',
                '     ',
                '     ',
                '     '],
            '"': ['"   "',
                '"   "',
                '     ',
                '     ',
                '     '],
            '`': ['  `  ',
                '     ',
                '     ',
                '     ',
                '     '],
            '~': ['     ',
                ' ~~~ ',
                ' ~   ',
                '     ',
                '     '],
            '/': ['     ',
                '    /',
                '   / ',
                '  /  ',
                ' /   '],
            '\\': ['     ',
                '\\    ',
                ' \\   ',
                '  \\  ',
                '   \\ '],
            '|': ['  |  ',
                '  |  ',
                '  |  ',
                '  |  ',
                '  |  '],
        }

        lines = [''] * 5  # Initialize 5 empty lines

        for char in text.upper():
            if char in ascii_letters:
                ascii_rep = ascii_letters[char]
                for i in range(5):
                    lines[i] += ascii_rep[i] + ' '  # Add the ASCII representation to the corresponding line
            else:
                for i in range(5):
                    lines[i] += ' ' * 5 + ' '  # Add spaces for unsupported characters

        return '\n'.join(lines)



    def UNICODE_blocks(text):
        ascii_letters = {
            'A': ['█████',
                '█   █',
                '█████',
                '█   █',
                '█   █'],
            'B': ['█████',
                '█   █',
                '█████',
                '█   █',
                '█████'],
            'C': ['█████',
                '█    ',
                '█    ',
                '█    ',
                '█████'],
            'D': ['████ ',
                '█   █',
                '█   █',
                '█   █',
                '████ '],
            'E': ['█████',
                '█    ',
                '████ ',
                '█    ',
                '█████'],
            'F': ['█████',
                '█    ',
                '████ ',
                '█    ',
                '█    '],
            'G': ['█████',
                '█    ',
                '█ ███',
                '█   █',
                '█████'],
            'H': ['█   █',
                '█   █',
                '█████',
                '█   █',
                '█   █'],
            'I': ['█████',
                '  █  ',
                '  █  ',
                '  █  ',
                '█████'],
            'J': ['█████',
                '   █ ',
                '   █ ',
                '█  █ ',
                ' ██  '],
            'K': ['█   █',
                '█  █ ',
                '███  ',
                '█  █ ',
                '█   █'],
            'L': ['█    ',
                '█    ',
                '█    ',
                '█    ',
                '█████'],
            'M': ['█   █',
                '██ ██',
                '█ █ █',
                '█   █',
                '█   █'],
            'N': ['█   █',
                '██  █',
                '█ █ █',
                '█  ██',
                '█   █'],
            'O': ['█████',
                '█   █',
                '█   █',
                '█   █',
                '█████'],
            'P': ['█████',
                '█   █',
                '█████',
                '█    ',
                '█    '],
            'Q': ['█████',
                '█   █',
                '█ █ █',
                '█  ██',
                '█████'],
            'R': ['█████',
                '█   █',
                '█████',
                '█  █ ',
                '█   █'],
            'S': ['█████',
                '█    ',
                '█████',
                '    █',
                '█████'],
            'T': ['█████',
                '  █  ',
                '  █  ',
                '  █  ',
                '  █  '],
            'U': ['█   █',
                '█   █',
                '█   █',
                '█   █',
                '█████'],
            'V': ['█   █',
                '█   █',
                '█   █',
                '█   █',
                ' ███ '],
            'W': ['█   █',
                '█   █',
                '█ █ █',
                '██ ██',
                '█   █'],
            'X': ['█   █',
                ' █ █ ',
                '  █  ',
                ' █ █ ',
                '█   █'],
            'Y': ['█   █',
                ' █ █ ',
                '  █  ',
                '  █  ',
                '  █  '],
            'Z': ['█████',
                '   █ ',
                '  █  ',
                ' █   ',
                '█████'],
            ' ': ['     ',
                '     ',
                '     ',
                '     ',
                '     '],
            ',': ['     ',
                '     ',
                '     ',
                '  █  ',
                ' █   '],
            '.': ['     ',
                '     ',
                '     ',
                '     ',
                '  █  '],
            '!': ['  █  ',
                '  █  ',
                '  █  ',
                '     ',
                '  █  '],
            '?': ['█████',
                '    █',
                '  ██ ',
                '     ',
                '  █  '],
            '-': ['     ',
                '     ',
                '█████',
                '     ',
                '     '],
            '_': ['     ',
                '     ',
                '     ',
                '     ',
                '█████'],
            '+': ['     ',
                '  █  ',
                '█████',
                '  █  ',
                '     '],
            '=': ['     ',
                '█████',
                '     ',
                '█████',
                '     '],
            '#': [' █ █ ',
                '█████',
                ' █ █ ',
                '█████',
                ' █ █ '],
            '@': ['█████',
                '█   █',
                '█ █ █',
                '█    ',
                '█████'],
            '$': [' ███ ',
                '█   █',
                ' ███ ',
                '█   █',
                ' ███ '],
            '%': ['█   █',
                '█  █ ',
                '   █ ',
                ' █  █',
                '█   █'],
            '&': [' ███ ',
                '█   █',
                ' ███ ',
                '█   █',
                ' ██ █'],
            '*': ['     ',
                '█ █ █',
                ' ███ ',
                '█ █ █',
                '     '],
            '(': ['  █  ',
                ' █   ',
                ' █   ',
                ' █   ',
                '  █  '],
            ')': ['  █  ',
                '   █ ',
                '   █ ',
                '   █ ',
                '  █  '],
            '[': [' ███ ',
                ' █   ',
                ' █   ',
                ' █   ',
                ' ███ '],
            ']': [' ███ ',
                '   █ ',
                '   █ ',
                '   █ ',
                ' ███ '],
            '{': ['  ██ ',
                ' █   ',
                '██   ',
                ' █   ',
                '  ██ '],
            '}': [' ██  ',
                '   █ ',
                '   ██',
                '   █ ',
                ' ██  '],
            '<': ['   █ ',
                '  █  ',
                ' █   ',
                '  █  ',
                '   █ '],
            '>': [' █   ',
                '  █  ',
                '   █ ',
                '  █  ',
                ' █   '],
            ':': ['     ',
                '  █  ',
                '     ',
                '  █  ',
                '     '],
            ';': ['     ',
                '  █  ',
                '     ',
                '  █  ',
                '  █  '],
            '\'': ['  █  ',
                '  █  ',
                '     ',
                '     ',
                '     '],
            '"': [' █ █ ',
                ' █ █ ',
                '     ',
                '     ',
                '     '],
            '`': ['  █  ',
                '     ',
                '     ',
                '     ',
                '     '],
            '~': ['     ',
                '     ',
                ' ███ ',
                '█   █',
                '     '],
            '/': ['     ',
                '    █',
                '   █ ',
                '  █  ',
                ' █   '],
            '\\': ['     ',
                '█    ',
                ' █   ',
                '  █  ',
                '   █ '],
            '|': ['  █  ',
                '  █  ',
                '  █  ',
                '  █  ',
                '  █  '],
        }

        lines = [''] * 5  # Initialize 5 empty lines

        for char in text.upper():
            if char in ascii_letters:
                ascii_rep = ascii_letters[char]
                for i in range(5):
                    lines[i] += ascii_rep[i] + ' '  # Add the ASCII representation to the corresponding line
            else:
                for i in range(5):
                    lines[i] += ' ' * 5 + ' '  # Add spaces for unsupported characters

        return '\n'.join(lines)


# End of Class
