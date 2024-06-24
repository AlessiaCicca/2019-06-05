from dataclasses import dataclass

@dataclass
class Distretto:
    id:int
    lon:int
    lat:int


    def __hash__(self):
        return hash(self.id)