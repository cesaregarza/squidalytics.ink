from typing import TypedDict


class Ability(TypedDict):
    tag: str
    image_id: int
    name: str
    description: str


InkResistanceUp = Ability(
    tag="RES",
    image_id=48,
    name="Ink Resistance Up",
    description="Reduces the negative effects of being on enemy ink.",
)

InkRecoveryUp = Ability(
    tag="IRU",
    image_id=47,
    name="Ink Recovery Up",
    description="Increases the rate at which ink refills.",
)

Haunt = Ability(
    tag="H",
    image_id=46,
    name="Haunt",
    description="Tag your killer for enhanced tracking and harsher penalties upon their death.",
)

DropRoller = Ability(
    tag="DR",
    image_id=45,
    name="Drop Roller",
    description="Press ZR while jumping to perform a roll.",
)

ComeBack = Ability(
    tag="CB",
    image_id=44,
    name="Comeback",
    description="Increases stats for a while after respawning.",
)

ThermalInk = Ability(
    tag="TI",
    image_id=43,
    name="Thermal Ink",
    description="Reveals location of enemies hit by your shots.",
)

Tenacity = Ability(
    tag="T",
    image_id=42,
    name="Tenacity",
    description="Passively increases special gauge when your team has fewer players.",
)

SwimSpeedUp = Ability(
    tag="SSU",
    image_id=41,
    name="Swim Speed Up",
    description="Increases swim speed.",
)

SubResistanceUp = Ability(
    tag="SRU",
    image_id=40,
    name="Sub Resistance Up",
    description="Reduces the negative effects of enemy sub weapons.",
)

SubPowerUp = Ability(
    tag="BRU",
    image_id=39,
    name="Sub Power Up",
    description="Increases the power of sub weapons.",
)

StealthJump = Ability(
    tag="SJ",
    image_id=38,
    name="Stealth Jump",
    description="Hides the landing marker when jumping to a teammate.",
)

SpecialSaver = Ability(
    tag="SS",
    image_id=37,
    name="Special Saver",
    description="Reduces the amount of special gauge lost after dying.",
)

SpecialPowerUp = Ability(
    tag="SPU",
    image_id=36,
    name="Special Power Up",
    description="Increases the power of special weapons.",
)

SpecialChargeUp = Ability(
    tag="SCU",
    image_id=35,
    name="Special Charge Up",
    description="Increases the rate at which the special gauge fills.",
)

RunSpeedUp = Ability(
    tag="RSU",
    image_id=34,
    name="Run Speed Up",
    description="Increases run speed.",
)

RespawnPunisher = Ability(
    tag="RP",
    image_id=33,
    name="Respawn Punisher",
    description="Increases respawn time for both you and your victims.",
)

QuickSuperJump = Ability(
    tag="QSJ",
    image_id=32,
    name="Quick Super Jump",
    description="Reduces the time needed to super jump.",
)

QuickRespawn = Ability(
    tag="QR",
    image_id=31,
    name="Quick Respawn",
    description="Reduces respawn time after getting splatted.",
)

OpeningGambit = Ability(
    tag="OG",
    image_id=30,
    name="Opening Gambit",
    description="Increases stats for a while at the start of the battle.",
)

ObjectShredder = Ability(
    tag="OS",
    image_id=29,
    name="Object Shredder",
    description="Increases damage dealt to non-player objects.",
)

NinjaSquid = Ability(
    tag="NS",
    image_id=28,
    name="Ninja Squid",
    description="Hides your ink trail when swimming.",
)

LastDitchEffort = Ability(
    tag="LDE",
    image_id=27,
    name="Last-Ditch Effort",
    description="Increases stats when the game is almost over.",
)

IntensifyAction = Ability(
    tag="IA",
    image_id=26,
    name="Intensify Action",
    description="Makes it easier to perform special actions",
)

InkSaverSub = Ability(
    tag="ISS",
    image_id=25,
    name="Ink Saver (Sub)",
    description="Reduces ink consumption of sub weapons.",
)

InkSaverMain = Ability(
    tag="ISM",
    image_id=24,
    name="Ink Saver (Main)",
    description="Reduces ink consumption of main weapons.",
)

ABILITIES = {
    x["tag"]: x
    for x in [
        InkResistanceUp,
        InkRecoveryUp,
        Haunt,
        DropRoller,
        ComeBack,
        ThermalInk,
        Tenacity,
        SwimSpeedUp,
        SubResistanceUp,
        SubPowerUp,
        StealthJump,
        SpecialSaver,
        SpecialPowerUp,
        SpecialChargeUp,
        RunSpeedUp,
        RespawnPunisher,
        QuickSuperJump,
        QuickRespawn,
        OpeningGambit,
        ObjectShredder,
        NinjaSquid,
        LastDitchEffort,
        IntensifyAction,
        InkSaverSub,
        InkSaverMain,
    ]
}
