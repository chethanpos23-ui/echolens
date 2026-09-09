# Description Quality Evaluation

## Method

Fifty short clips were recorded across five settings (corridor, street crossing, cafeteria,
stairwell, transit platform). Each clip was run through the pipeline twice: once with the
context ranker enabled, once with it bypassed so every detection was narrated.

Two reviewers scored each utterance against three questions:

1. **Was it actionable?** Would a person moving through this space change what they did?
2. **Was it timely?** Did it arrive before the situation changed?
3. **Was it redundant?** Had the same thing been said in the previous 10 seconds?

## Results

| Metric | Ranker off | Ranker on |
|---|---|---|
| Utterances per minute | 22.4 | 7.1 |
| Judged actionable | 31% | 78% |
| Judged redundant | 44% | 9% |
| Obstacles mentioned before passing | 61% | 94% |

The ranker does not make the model see better. It makes the app say less, and the things it
does say are more often the things that mattered.

## Caveats

Reviewers were sighted developers on the project team, scoring clips they had helped record.
This is the weakest part of the evaluation and the reason user testing is the top item in
Future Improvements. Treat these numbers as a development signal, not as evidence of
accessibility.
