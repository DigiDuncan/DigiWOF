from typing import List


def middle_index(li: list):
    return int(len(li) / 2) - 1


def try_fit(phrase: str, line_lengths: List[int]):
    words = phrase.split(" ")
    lines = [""] * len(line_lengths)
    for i, length in enumerate(line_lengths):
        while words:
            if len(words) == 1:
                if len(lines[i] + words[0]) > length:
                    break
                else:
                    lines[i] += words.pop(0)
            else:
                if len(lines[i] + words[0]) + 1 > length:
                    break
                else:
                    lines[i] += words.pop(0) + " "
    if words:
        return None
    else:
        return lines


def fit_to_board(phrase: str, *, line_lengths = (12, 14, 14, 12), pad_char = "*"):
    """Fits a phrase onto a WOF-style board.
    This function attempts to center and left-justify the phrase onto the board.
    Blank tiles appear as `pad_char`, by default "*".
    Empty space appears as "_".
    This assumes that the center of the board is its widest point, and that it tapers in either direction.
    `None` is returned if the phrase can not possibly fit.

    Example: ["_************_",
              "****PYTHON****",
              "****ROCKS*****",
              "_************_"]
    """
    words = phrase.split(" ")
    max_row_size = max(line_lengths)

    configs = [(1, ), (1, 2), (0, 1, 2), (0, 1, 2, 3)]  # TODO: Generate dynamically.

    # Weed out phrases with too-long words
    for word in words:
        if len(word) > max_row_size:
            return None

    for config in configs:
        fitted = try_fit(phrase, [line_lengths[i] for i in config])
        if fitted is not None:
            padded = {i: line.center(line_lengths[i], pad_char) for i, line in zip(config, fitted)}
            full_padded = [pad_char * line_lengths[i] if i not in config else padded[i] for i in range(len(line_lengths))]
            spaced = [full_padded[i].center(max_row_size, "_") for i in range(len(full_padded))]
            stripspaced = [s.removesuffix("_") for s in spaced]
            starred = [s.replace(" ", pad_char) for s in stripspaced]
            return "\n".join(starred)
    return None
