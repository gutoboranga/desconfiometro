from desconfiometro.indicators.data.VotesRepository import VotesRepository


class PositiveVotesRepository(VotesRepository):

    def __init__(self):
        super().__init__("desconfiometro/indicators/data/positive_votes.txt")

