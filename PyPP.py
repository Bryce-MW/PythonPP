import sys
from PyPPTools import CharacterDict, load_classes


def parse_character(classes, character):
    return classes[character](classes, character)


def parse_characters(classes, characters):
    result = []
    for character in characters:
        result.append(parse_character(classes, character))
    return "".join(result)


def parse_line(classes, characters):
    result = parse_characters(classes, characters)
    if not characters.endswith("\n"):
        result += parse_character(classes, "\n")
    return result


character_classes = load_classes("defaultClasses")
if character_classes is None:
    character_classes = CharacterDict()

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file = open(sys.argv[1])
        if len(sys.argv) >= 3:
            close = False
            if sys.argv[2] == "--":
                output = sys.stdout
            else:
                output = open(sys.argv[2], "w")
                close = True
            more = True
            line = file.readline()
            while more:
                output.write(parse_line(character_classes, line))
                line = file.readline()
                if line == "":
                    more = False
            if close:
                output.close()
        else:
            more = True
            line = file.readline()
            while more:
                print(parse_line(character_classes, line), end="")
                line = file.readline()
                if line == "":
                    more = False
        file.close()
    else:
        try:
            while True:
                print(parse_line(character_classes, input()), end="")
        except (KeyboardInterrupt, EOFError):
            pass
