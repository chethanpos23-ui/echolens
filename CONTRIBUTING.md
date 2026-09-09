# Contributing to EchoLens

Thanks for taking a look. This is a hackathon project kept as a public case study, so the bar
for contributions is "does it make the project clearer or more correct", not "does it match a
roadmap".

## Ways to help

- **Report something wrong.** Documentation that describes behaviour the code does not have is
  a bug worth filing.
- **Improve the docs.** The `docs/` directory is the most useful part of this repository for
  most readers.
- **Fix a limitation.** [The README lists known limitations](README.md#limitations). Each one is
  a real, scoped piece of work.

## Before you open a pull request

1. Open an issue first for anything larger than a typo. It saves both of us time if the change
   is not one this project wants.
2. Keep the change focused. One concern per pull request.
3. Run the test suite — see [Testing](README.md#testing).
4. Update the docs in the same pull request as the code. Documentation drift is the main way
   this repository becomes misleading.

## Style

Match the surrounding code. This project has no house style beyond that, and consistency with
the file you are editing beats consistency with any external guide.

## Commit messages

Short imperative subject line, body explaining *why* if the reason is not obvious from the diff.

```
Redistribute missed sessions instead of dropping them

A missed session previously vanished, which meant the topic silently lost
its remaining study time. It now re-enters the pool with staleness bumped.
```

## Code of conduct

Be decent to people. Harassment, personal attacks, and bad-faith argument are not welcome, and
maintainers will remove comments or contributors that fall into them.

## Licensing

By contributing you agree that your contributions are licensed under the
[MIT License](LICENSE) that covers this project.
