from __future__ import annotations
import haversine as hs


class Node():
    def __init__(
        self,
        coords: tuple
    ) -> None:
        self.coords = coords

    def __rshift__(self, other: Node):
        return self._distance(other)

    def _distance(self, other: Node) -> float:
        return hs.haversine(self.coords, other.coords)

    def __str__(self) -> str:
        coords_str = '; '.join(map(str, self.coords))
        return f'{self.__class__.__name__}({coords_str})'

    def __repr__(self) -> str:
        return self.__str__()
