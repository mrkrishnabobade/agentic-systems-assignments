class StudentPerformance:

    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            if len(self.scores) == 0:
                raise Exception

            first = self.scores[0]
            last = self.scores[-1]

            difference = last - first

            print("Difference between last and first score is:", difference)

        except:
            print("No scores available to calculate difference")


scores = [55, 65, 75, 85]

student = StudentPerformance(scores)
student.score_difference()