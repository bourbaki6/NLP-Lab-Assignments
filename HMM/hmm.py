


states = ["DET", "NOUN", "VERB"]

start = {"DET": 0.6, "NOUN": 0.3, "VERB": 0.1}

trans = {
    "DET":  {"DET": 0.1, "NOUN": 0.8, "VERB": 0.1},
    "NOUN": {"DET": 0.1, "NOUN": 0.2, "VERB": 0.7},
    "VERB": {"DET": 0.2, "NOUN": 0.6, "VERB": 0.2}
}

emit = {
    "DET":  {"the": 0.9, "a": 0.8},
    "NOUN": {"dog": 0.8, "cat": 0.8, "barks": 0.1},
    "VERB": {"barks": 0.8, "runs": 0.8}
}

def viterbi(words):

    dp = [{}]
    path = {}

    for s in states:
        dp[0][s] = start[s] * emit[s].get(words[0], 0)
        path[s] = [s]

    for i in range(1, len(words)):
        dp.append({})
        new_path = {}

        for s in states:
            prob, prev = max(
                (dp[i-1][p] * trans[p][s], p)
                for p in states
            )
            dp[i][s] = prob * emit[s].get(words[i], 0)
            new_path[s] = path[prev] + [s]

        path = new_path

    best = max(states, key = lambda s: dp[-1][s])
    return path[best], dp[-1][best]

sentence = input("Enter a sentence: ").lower().split()
tags, probability = viterbi(sentence)

print("Word\tPOS Tag")
for word, tag in zip(sentence, tags):
    print(word, "\t", tag)

print("Probability:", probability)
