from desconfiometro.indicators.data.VotesRepository import VotesRepository


class NegativeVotesRepository(VotesRepository):

    def __init__(self):
        self.file = open("desconfiometro/indicators/data/negative_votes.txt")

