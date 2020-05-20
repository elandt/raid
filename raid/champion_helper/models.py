from django.db import models
from django.db.models import Q, F

# Create your models here.

# TODO: figure out how I want the FKs to work,
# and how to limit the relationship between
# factions and allicances


class Alliance(models.Model):
    """
    Represents an Alliance
    An Alliance has a name, and has up to 4 factions
    """

    ALLIANCES = (
        ("telerians", "Telerians"),
        ("gaellen_pact", "Gaellen Pact"),
        ("corrupted", "The Corrupted"),
        ("nyresan_union", "Nyresan Union"),
    )

    name = models.CharField(max_length=50, choices=ALLIANCES, unique=True)

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=50, choices=FACTIONS, unique=True)
    alliance = models.ForeignKey(Alliance, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "alliance"], name="unique_faction_alliance_pair"
            ),
        ]


class Affinity(models.Model):
    """
    Represents the Affinity of a Champion
    An Affinity has a name, and may have
    a strength and weakness
    """

    AFFINITIES = (
        ("force", "Force"),
        ("magic", "Magic"),
        ("spirit", "Spirit"),
        ("void", "Void"),
    )
    name = models.CharField(max_length=6, choices=AFFINITIES, unique=True)
    # TODO: Why do I need null=True and blank=True??
    # TODO: Look at docs - they probably has the answer
    strength = models.OneToOneField(
        "Affinity",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="strong_against",
    )
    weakness = models.OneToOneField(
        "Affinity",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="weak_against",
    )

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(
                    # Both strength and weakness are null
                    (Q(strength__isnull=True, weakness__isnull=True))
                    |
                    # OR neither are null AND they are not equal
                    (
                        Q(strength__isnull=False, weakness__isnull=False)
                        & ~Q(strength_id=F("weakness"))
                    )
                ),
                name="strength_weakness_are_both_null_or_populated_and_diff",
            ),
            models.UniqueConstraint(
                fields=["strength", "weakness"], name="unique_strength_weakness_pair"
            ),
        ]


class Champion(models.Model):
    """
    Represents a Champion from Raid Shadow Legends
    """

    name = models.CharField(max_length=100, unique=True)
    RARITIES = (
        ("c", "Common"),
        ("unc", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legend", "Legendary"),
    )
    rarity = models.CharField(max_length=6, choices=RARITIES)
    faction = models.ForeignKey(Faction, on_delete=models.PROTECT)
    affinity = models.ForeignKey(Affinity, on_delete=models.PROTECT)
    TYPES = (
        ("attack", "Attack"),
        ("defense", "Defense"),
        ("hp", "HP"),
        ("support", "Support"),
    )
    type = models.CharField(max_length=7, choices=TYPES)

    # Other possible fields: skills, num_owned, max power?

    def __str__(self):
        return self.name


class Rating(models.Model):
    """
    Represents the ratings for a Champion
    Ratings range from 0 - 5, with 1 decimal place
    """

    champion = models.OneToOneField(Champion, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.champion.name}'s rating"
