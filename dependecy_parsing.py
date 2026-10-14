

sentence = "The cat chased the mouse".split()

vocabulary = {
    "the": "DET", "a": "DET",
    "cat": "NOUN", "dog": "NOUN",
    "mouse": "NOUN", "john": "NOUN",
    "chased": "VERB", "saw": "VERB",
    "runs": "VERB"
}

words = [word.lower() for word in sentence]

tags = [vocabulary.get(word, "UNK") for word in words]

dependencies = []

verbs = [i for i, tag in enumerate(tags) if tag == "VERB"]

if not verbs:
    print("No verb found.")
else:
    root = verbs[0]
    dependencies.append((words[root], "ROOT", "root"))

    nouns_before = [i for i in range(root)
                    if tags[i] == "NOUN"]
    nouns_after = [i for i in range(root + 1, len(words))
                   if tags[i] == "NOUN"]

    if nouns_before:
        subject = nouns_before[-1]
        dependencies.append(
            (words[subject], words[root], "nsubj")
        )

    if nouns_after:
        obj = nouns_after[0]
        dependencies.append(
            (words[obj], words[root], "obj")
        )

    for i, word in enumerate(words):
        if tags[i] == "DET":
            for j in range(i + 1, len(words)):
                if tags[j] == "NOUN":
                    dependencies.append(
                        (word, words[j], "det")
                    )
                    break

    print("Word\tHead\tRelation")
    for word, head, relation in dependencies:
        print(f"{word}\t{head}\t{relation}")
