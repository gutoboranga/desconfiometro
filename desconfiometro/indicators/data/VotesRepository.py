
class VotesRepository:
    def __init__(self, votes_filename):
        self.votes_filename = votes_filename

    def get_votes(self, item):
        votes_file = open(self.votes_filename, 'r')
        line = votes_file.readline()
        while (line):
            if line.split(',')[0].strip() == item:
                return int(line.split(',')[1].strip())
            line = votes_file.readline()
        return 0
