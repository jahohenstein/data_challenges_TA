Let's start with a very simple exercise to understand how these exercises are going to work.

## How to solve a challenge

Some of the exercises will have a `check.sh` bash script. This script will check if your challenge is correct (using [Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development) where tests have been written beforehand by Le Wagon's teachers). To run this script in your terminal, `cd` to the proper folder (as explained above ☝️) and run:

```bash
./check.sh
```

Your goal is to implement the method `sum3` in the `sum_of_three.py` file. The workflow you need to follow is:

1. Read the whole challenge instructions
1. Open the `sum_of_three.py` file where you need to write code and read it
1. Run `./check.sh`
1. Read the first error message and try to make sense of it (Google it!)
1. Change the code in `sum_of_three.py`
1. Re-run `./check.sh`
1. New error message? Less failures? You are making progress!
1. Repeat until you no longer have errors
1. Make sure your style is correct and reach a `10.00/10` score
1. Commit & push your changes to Kitt:
  1. `git status` to check which files have been changed since last commit
  1. `git diff` to check what has been changed
  1. `git add sum_of_three.py`
  1. `git commit -m "Solve first Python exercise of the day"`
  1. `git push origin master`

Don't hesitate to open the content of `check.sh` in your text editor. There are two important pieces of the Python ecosystem that we use to help you:

- [pytest](https://docs.pytest.org/en/latest/)
- [pylint](https://www.pylint.org/) to enforce the [PEP 8 - Style Guide for Python](https://www.python.org/dev/peps/pep-0008/)

## Conclusion

The goal of this exercise was to show you how to run the tests to automatically evaluate your code (both style & content) and introduce you to this tight feedback loop.