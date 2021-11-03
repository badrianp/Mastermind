# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

WIN = "Player B won"
LOSE = "Player A won"


class Rules:
    colors_nr = 0
    balls_from_each_color = 0
    code_length = 0
    max_guesses = 0
    colors = list
    code = list
    current_guess = list
    round_count = 0

    def __init__(self, n, m, k):
        self.colors_nr = int(n)
        self.balls_from_each_color = int(m)
        self.code_length = int(k)
        self.max_guesses = int(2 * n)
        self.round_count = 0
        self.set_colors()
        self.random_code()

    def set_colors(self):
        # print(f"len()= {len(self.colors)}")
        print(f"colors_nr = {self.colors_nr}")
        self.colors = input(f"please insert {self.colors_nr} colors").lower().split()
        print(self.colors)

        while len(self.colors) < self.colors_nr:
            print(f"len()= {len(self.colors)}")
            print(f"colors_nr = {self.colors_nr}")
            print(self.colors)
            self.colors = input(f"please insert {self.colors_nr} colors").lower().split()

    def random_code(self):
        code = list()
        for color in range(0, self.code_length):
            random_color = random.choice(self.colors)
            while code.count(random_color) >= self.balls_from_each_color:
                random_color = random.choice(self.colors)
            code.append(random_color)
        self.code = code

    def check_win(self, guess):
        self.round_count += 1
        self.current_guess = guess
        if self.round_count <= self.max_guesses and self.check_guess(guess) == self.code_length:
            return WIN
        elif self.round_count > self.max_guesses:
            return LOSE
        return self.check_guess(guess)

    def check_guess(self, guess):
        correct_guesses = 0
        for i in range(0, self.code_length):
            # print(f"guess[i]= {guess[i]}\n code[i]= {self.code[i]}\n")
            # print(f"i= {i}\n")
            if guess[i] == self.code[i]:
                correct_guesses += 1
        return correct_guesses

    def validate_guess(self, guess):
        if len(guess) != self.code_length:
            return f"make your guess of {self.code_length} colors"
        for color in guess:
            if color not in self.colors:
                return f"color {color} is invalid!"
        return None


def make_guess(rules):
    guess = input(f"please insert {rules.code_length} colors "
                  f"(maximum {rules.balls_from_each_color} from each) from these options:{rules.colors}")\
        .lower().split()
    while rules.validate_guess(guess) is not None:
        print(rules.validate_guess(guess))
        guess = input(f"please insert {rules.code_length} colors "
                      f"(maximum {rules.balls_from_each_color} from each) from these options:{rules.colors}")\
            .lower().split()
    return guess


def main():
    n = input("number of colors:")
    # print(n)
    m = input("number of balls from each color:")
    # print(m)
    k = input("sequence length: ")
    # print(k)

    rule_set = Rules(n, m, k)

    # print(rule_set.code)
    # print(rule_set.colors_nr)
    # print(rule_set.code_length)

    guess = make_guess(rule_set)
    feedback = rule_set.check_win(guess)
    while isinstance(feedback, int):
        print(f"guessed balls: {feedback}")
        guess = make_guess(rule_set)
        feedback = rule_set.check_win(guess)

    print(feedback + f"\ncolor set was: {rule_set.code}")
    quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
