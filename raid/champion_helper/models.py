from django.db import models

# Create your models here.

# TODO: figure out how I want the FKs to work,
# and how to limit the relationship between
# factions and allicances


class Champion(models.Model):
    """
    Represents a Champion from Raid Shadow Legends
    """

    name = models.CharField(max_length=100, unique=True)    
    faction = models.ForeignKey("Faction", on_delete=models.PROTECT)
    RARITIES = (
        ("c", "Common"),
        ("unc", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legend", "Legendary"),
    )
    rarity = models.CharField(max_length=7, choices=RARITIES)
    TYPES = (
        ("attack", "Attack"),
        ("defense", "Defense"),
        ("hp", "HP"),
        ("support", "Support"),
    )
    type = models.CharField(max_length=7, choices=TYPES)
    # TODO:  does this even need to be here if
    # there's a FK from ratings back to the champion??
    ratings = models.CharField(max_length=100)

    # Other possible fields: skills, num_owned, max power?

    def __str__(self):
        return self.name


class Ratings(models.Model):
    """
    Represents the ratings for a Champion
    Ratings range from 0 - 5, with 1 decimal place
    """

    champion = models.ForeignKey(Champion, on_delete=models.CASCADE)
    campaign_locations = models.DecimalField(max_digits=2, decimal_places=1)
    arena_offense = models.DecimalField(max_digits=2, decimal_places=1)
    arena_defense = models.DecimalField(max_digits=2, decimal_places=1)
    clan_boss = models.DecimalField(max_digits=2, decimal_places=1)
    faction_wars = models.DecimalField(max_digits=2, decimal_places=1)
    ice_golem = models.DecimalField(max_digits=2, decimal_places=1)
    dragon = models.DecimalField(max_digits=2, decimal_places=1)
    minotaur = models.DecimalField(max_digits=2, decimal_places=1)
    fire_knight = models.DecimalField(max_digits=2, decimal_places=1)
    spider = models.DecimalField(max_digits=2, decimal_places=1)
    void_arcane = models.DecimalField(max_digits=2, decimal_places=1)
    force = models.DecimalField(max_digits=2, decimal_places=1)
    magic = models.DecimalField(max_digits=2, decimal_places=1)
    spirit = models.DecimalField(max_digits=2, decimal_places=1)


class Faction(models.Model):
    """
    Rerpresents a faction
    A faction has a name, and belongs to 1, and only 1, Alliance
    """
    FACTIONS = (
        ("banner_lords", "Banner Lords"),
        ("high_elves", "High Elves"),
        ("sacred_order", "The Sacred Order"),
        ("barbarians", "Barbarians"),
        ("ogryn_tribes", "Ogryn Tribes"),
        ("lizardmen", "Lizardmen"),
        ("skinwalkers", "Skinwalkers"),
        ("orcs", "Orcs"),
        ("demonspawn", "Demonspawn"),
        ("undead_hordes", "Undead Hordes"),
        ("dark_elves", "Dark Elves"),
        ("knight_revenant", "Knight Revenant"),
        ("dwarves", "Dwarves"),
    )
    name = models.CharField(max_length=50)
    alliance = models.ForeignKey("Alliance", on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Alliance(models.Model):
    """
    Represents an Alliance
    An Alliance has a name, and has up to 4 factions
    """

    ALLIANCES = (
        ("telarians", "Telarians"),
        ("gaellen_pact", "Gaellen Pact"),
        ("corrupted", "The Corrupted"),
        ("nyresan_union", "Nyresan Union"),
    )

    name = models.CharField(max_length=50, choices=ALLIANCES)

    def __str__(self):
        return self.name    
