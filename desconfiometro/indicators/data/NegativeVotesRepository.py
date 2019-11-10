from desconfiometro.indicators.data.VotesRepository import VotesRepository


class NegativeVotesRepository(VotesRepository):

    def __init__(self):
        super().__init__("desconfiometro/indicators/data/negative_votes.txt")

