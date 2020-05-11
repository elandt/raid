#!/usr/bin/env python3


class Ratings:
    def __init__(
        self,
        campaign_locations,
        arena_offense,
        arena_defense,
        clan_boss,
        faction_wars,
        ice_golem,
        dragon,
        minotaur,
        fire_knight,
        spider,
        void_arcane,
        force,
        magic,
        spirit,
        min_num_of_ratings,
    ):
        self._campaign_locations = campaign_locations
        self._arena_offense = arena_offense
        self._arena_defense = arena_defense
        self._clan_boss = clan_boss
        self._faction_wars = faction_wars
        self._ice_golem = ice_golem
        self._dragon = dragon
        self._minotaur = minotaur
        self._fire_knight = fire_knight
        self._spider = spider
        self._void_arcane = void_arcane
        self._force = force
        self._magic = magic
        self._spirit = spirit
        self._min_num_of_ratings = min_num_of_ratings
        average = (
            campaign_locations
            + arena_offense
            + arena_defense
            + clan_boss
            + faction_wars
            + ice_golem
            + dragon
            + minotaur
            + fire_knight
            + spider
            + void_arcane
            + force
            + magic
            + spirit
        ) / 14
        self._average = round(average, 1)

    def campaign_locations(self):
        return self._campaign_locations

    def arena_offense(self):
        return self._arena_offense

    def arena_defense(self):
        return self._arena_defense

    def clan_boss(self):
        return self._clan_boss

    def faction_wars(self):
        return self._faction_wars

    def ice_golem(self):
        return self._ice_golem

    def dragon(self):
        return self._dragon

    def minotaur(self):
        return self._minotaur

    def fire_knight(self):
        return self._fire_knight

    def spider(self):
        return self._spider

    def void_arcane(self):
        return self._void_arcane

    def force(self):
        return self._force

    def magic(self):
        return self._magic

    def spirit(self):
        return self._spirit

    def min_num_of_ratings(self):
        return self._min_num_of_ratings

    def average(self):
        return self._average
