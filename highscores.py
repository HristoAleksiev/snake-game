# intended to be the text file to read and write high scores at some point
class HighScores:

    def __init__(self):
        self.high_scores = []

    def get_scores(self):
        with open("high_scores.txt", mode="r") as file:
            for _ in range(5):
                file_line = file.readline()
                entry = file_line.replace('"', '').replace(':', '').replace('\\n', '').\
                    replace('(', '').replace(')', "").replace('\'', '').split(',')
                highscore = (entry[0], int(entry[1]))

                self.high_scores.append(highscore)

        print(self.high_scores)
        return self.high_scores

    def record_scores(self, high_scores):
        with open("high_scores.txt", mode="w") as file:
            for _ in high_scores:
                file.write(f"{_}\n")

        print(high_scores)



