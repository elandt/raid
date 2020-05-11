#!/usr/bin/env python3

from Ratings import Ratings


class Champion:
    def __init__(self, name, rarity, affinity, faction, type, num_owned):
        self._name = name
        self._rarity = rarity
        self._affinity = affinity
        self._faction = faction
        self._type = type
        self._num_owned = num_owned

    def name(self):
        return self._name

    def rarity(self):
        return self._rarity

    def affinity(self):
        return self._affinity

    def faction(self):
        return self._faction

    def type(self):
        return self._type

    def num_owned(self):
        return self._num_owned

    def ratings(self) -> Ratings:
        return self._ratings

    def set_ratings(self, ratings: Ratings):
        self._ratings = ratings
