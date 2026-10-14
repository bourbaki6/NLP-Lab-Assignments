

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"], ["V"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"], ["mouse"]],
    "V": [["chased"], ["saw"]]
}


def parse(symbol, words, pos):
    if symbol not in grammar:
        if pos < len(words) and words[pos] == symbol:
            return [((symbol, []), pos + 1)]
        return []

    results = []

    for rule in grammar[symbol]:
        states = [([], pos)]

        for item in rule:
            new_states = []

            for children, current_pos in states:
                for tree, next_pos in parse(item, words, current_pos):
                    new_states.append(
                        (children + [tree], next_pos)
                    )

            states = new_states

        for children, end_pos in states:
            results.append(((symbol, children), end_pos))

    return results



def display(tree, level=0):
    symbol, children = tree
    print("  " * level + symbol)

    for child in children:
        display(child, level + 1)

sentence = "the cat chased a mouse".split()
trees = parse("S", sentence, 0)
valid_trees = [tree for tree, pos in trees
               if pos == len(sentence)]

if valid_trees:
    print("Constituency Parse Tree:")
    display(valid_trees[0])
    print("Sentence is valid.")
else:
    print("No valid parse found.")
