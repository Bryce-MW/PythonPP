from PyPPTools import CharacterDict, load_classes
import copy


def reset_classes(classes, character):
    old_classes = classes["old_classes"]
    classes.clear()
    classes.update(old_classes)
    classes.__missing__ = old_classes.__missing__
    return character


def parse_comment(classes, character):
    comment = classes["stow"].lstrip()
    if comment.startswith("PP "):
        new_classes = load_classes(comment.split()[1])
        classes.clear()
        classes.update(new_classes)
        classes.__missing__ = new_classes.__missing__
        return character
    else:
        return reset_classes(classes, character)


def stow_character(classes, character):
    classes["stow"] += character
    return character


def start_comment_parse(classes, character):
    new_classes = {
        "old_classes": copy.deepcopy(classes),
        "stow": "",
        "\n": parse_comment
    }
    classes.clear()
    classes.update(new_classes)
    classes.__missing__ = lambda self, key: stow_character
    return character


character_classes = CharacterDict({
    "#": start_comment_parse
})
