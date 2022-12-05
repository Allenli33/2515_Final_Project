import json


class Score():
    '''Create score class'''

    def __init__(self, filename):

        temp_list = []
        self.filename = filename

        with open(self.filename, "r") as f:
            json_data = json.load(f)
            for score in json_data:
                temp_list.append(score)

        self.score_list = sorted(
            temp_list, key=lambda x: x["score"], reverse=True)

    def __len__(self):
        return len(self.score_list)

    def get_scores(self):

        scores = []

        for score in self.score_list:
            scores.append(score)

        return scores

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.score_list, f)

    def add_score(self, score, id):

        if type(id) is not str:
            raise ValueError

        if type(score) is not int:
            raise ValueError

        if id == "":
            raise ValueError

        score_dict = {
            "score": score,
            "id": id
        }

        self.score_list.append(score_dict)
        return True
