# Arcane
class Arcane:
  ## Schools
  class School:
    ABJURATION = {"name": "Abjuration", "description": "Abjuration spells are protective in nature, though some of them have aggressive uses. They create magical barriers, negate harmful effects, harm trespassers, or banish creatures to other planes of existence."}
    CONJURATION = {"name": "Conjuration", "description": "Conjuration spells involve the transportation of objects and creatures from one location to another. Some spells summon creatures or objects to the caster's side, whereas others allow the caster to teleport to another location. Some conjurations create objects or effects out of nothing."}
    DIVINATION = {"name": "Divination", "description": "Divination spells reveal information, whether in the form of secrets long forgotten, glimpses of the future, the locations of hidden things, the truth behind illusions, or visions of distant people or places."}
    ENCHANTMENT = {"name": "Enchantment", "description": "Enchantment spells affect the minds of others, influencing or controlling their behavior. Such spells can make enemies see the caster as a friend, force creatures to take a course of action, or even control another creature like a puppet."}
    EVOCATION = {"name": "Evocation", "description": "Evocation spells manipulate magical energy to produce a desired effect. Some call up blasts of fire or lightning. Others channel positive energy to heal wounds."}
    ILLUSION = {"name": "Illusion", "description": "Illusion spells deceive the senses or minds of others. They cause people to see things that are not there, to miss things that are there, to hear phantom noises, or to remember things that never happened. Some illusions create phantom images that any creature can see, but the most insidious illusions plant an image directly in the mind of a creature."}
    NECROMANCY = {"name": "Necromancy", "description": "Necromancy spells manipulate the energies of life and death. Such spells can grant an extra reserve of life force, drain the life energy from another creature, create the undead, or even bring the dead back to life. Creating the undead through the use of necromancy spells such as animate dead is not a good act, and only evil casters use such spells frequently."}
    TRANSMUTATN = {"name": "Transmutation", "description": "Transmutation spells change the properties of a creature, object, or environment. They might turn an enemy into a harmless creature, bolster the strength of an ally, make an object move at the caster's command, or enhance a creature's innate healing abilities to rapidly recover from injury."}
    LIST = [ABJURATION, CONJURATION, DIVINATION, ENCHANTMENT, EVOCATION, ILLUSION, NECROMANCY, TRANSMUTATN]

  ## Area of Effect
  class AreaOfEffect:
    CONE = {"name": "Cone", "description": "A cone extends in a direction you choose from its point of origin. A cone's width at a given point along its length is equal to that point's distance from the point of origin. A cone's area of effect specifies its maximum length. A cone's point of origin is not included in the cone's area of effect, unless you decide otherwise."}
    CUBE = {"name": "Cube", "description": "You select a cube's point of origin, which lies anywhere on a face of the cubic effect. The cube's size is expressed as the length of each side. A cube's point of origin is not included in the cube's area of effect, unless you decide otherwise."}
    CYLINDER = {"name": "Cylinder", "description": "A cylinder's point of origin is the center of a circle of a particular radius, as given in the spell description. The circle must either be on the ground or at the height of the spell effect. The energy in a cylinder expands in straight lines from the point of origin to the perimeter of the circle, forming the base of the cylinder. The spell's effect then shoots up from the base or down from the top, to a distance equal to the height of the cylinder. A cylinder's point of origin is included in the cylinder's area of effect."}
    LINE = {"name": "Line", "description": "A line extends from its point of origin in a straight path up to its length and covers an area defined by its width. A line's point of origin is not included in the line's area of effect, unless you decide otherwise."}
    SPHERE = {"name": "Sphere", "description": "You select a sphere's point of origin, and the sphere extends outward from that point. The sphere's size is ex- pressed as a radius in feet that extends from the point. A sphere's point of origin is included in the sphere's area of effect."}

    LIST = [CONE, CUBE, CYLINDER, LINE, SPHERE]

  ## Spell Components
  class Component:
    VERBAL = {"name": "Verbal", "description": "Most spells require the chanting of mystic words. The words themselves aren't the source of the spell's power; rather, the particular combination of sounds, with specific pitch and resonance, sets the threads of magic in motion. Thus, a character who is gagged or in an area of silence, such as one created by the silence spell, can't cast a spell with a verbal component."}
    SOMATIC = {"name": "Somatic", "description": "Most spells require the chanting of mystic words. The words themselves aren't the source of the spell's power; rather, the particular combination of sounds, with specific pitch and resonance, sets the threads of magic in motion. Thus, a character who is gagged or in an area of silence, such as one created by the silence spell, can't cast a spell with a verbal component."}
    MATERIAL = {"name": "Material", "description": "Most spells require the chanting of mystic words. The words themselves aren't the source of the spell's power; rather, the particular combination of sounds, with specific pitch and resonance, sets the threads of magic in motion. Thus, a character who is gagged or in an area of silence, such as one created by the silence spell, can't cast a spell with a verbal component."}
    LIST = [VERBAL, SOMATIC, MATERIAL]


# Combat
class Combat:
  ## Challenge Rating
  class ChallengeRating:
    CR0 = {"rating":"0", "experience_points": 10, "proficiency_bonus": 2}
    CR1_8 = {"rating":"1/8", "experience_points": 25, "proficiency_bonus": 2}
    CR1_4 = {"rating":"1/4", "experience_points": 50, "proficiency_bonus": 2}
    CR1_2 = {"rating":"1/2", "experience_points": 100, "proficiency_bonus": 2}
    CR1 = {"rating":"1", "experience_points": 200, "proficiency_bonus": 2}
    CR2 = {"rating":"2", "experience_points": 450, "proficiency_bonus": 2}
    CR3 = {"rating":"3", "experience_points": 700, "proficiency_bonus": 2}
    CR4 = {"rating":"4", "experience_points": 1100, "proficiency_bonus": 2}
    CR5 = {"rating":"5", "experience_points": 1800, "proficiency_bonus": 3}
    CR6 = {"rating":"6", "experience_points": 2300, "proficiency_bonus": 3}
    CR7 = {"rating":"7", "experience_points": 2900, "proficiency_bonus": 3}
    CR8 = {"rating":"8", "experience_points": 3900, "proficiency_bonus": 3}
    CR9 = {"rating":"9", "experience_points": 5000, "proficiency_bonus": 4}
    CR10 = {"rating":"10", "experience_points": 5900, "proficiency_bonus": 4}
    CR11 = {"rating":"11", "experience_points": 7200, "proficiency_bonus": 4}
    CR12 = {"rating":"12", "experience_points": 8400, "proficiency_bonus": 4}
    CR13 = {"rating":"13", "experience_points": 10000, "proficiency_bonus": 5}
    CR14 = {"rating":"14", "experience_points": 11500, "proficiency_bonus": 5}
    CR15 = {"rating":"15", "experience_points": 13000, "proficiency_bonus": 5}
    CR16 = {"rating":"16", "experience_points": 15000, "proficiency_bonus": 5}
    CR17 = {"rating":"17", "experience_points": 18000, "proficiency_bonus": 6}
    CR18 = {"rating":"18", "experience_points": 20000, "proficiency_bonus": 6}
    CR19 = {"rating":"19", "experience_points": 22000, "proficiency_bonus": 6}
    CR20 = {"rating":"20", "experience_points": 25000, "proficiency_bonus": 6}
    CR21 = {"rating":"21", "experience_points": 33000, "proficiency_bonus": 7}
    CR22 = {"rating":"22", "experience_points": 41000, "proficiency_bonus": 7}
    CR23 = {"rating":"23", "experience_points": 50000, "proficiency_bonus": 7}
    CR24 = {"rating":"24", "experience_points": 62000, "proficiency_bonus": 7}
    CR25 = {"rating":"25", "experience_points": 75000, "proficiency_bonus": 8}
    CR26 = {"rating":"26", "experience_points": 90000, "proficiency_bonus": 8}
    CR27 = {"rating":"27", "experience_points": 105000, "proficiency_bonus": 8}
    CR28 = {"rating":"28", "experience_points": 120000, "proficiency_bonus": 8}
    CR29 = {"rating":"29", "experience_points": 135000, "proficiency_bonus": 9}
    CR30 = {"rating":"30", "experience_points": 155000, "proficiency_bonus": 9}
    LIST = [CR0, CR1_8, CR1_4, CR1_2, CR1, CR2, CR3, CR4, CR5, CR6, CR7, CR8, CR9, CR10, CR11, CR12, CR13, CR14, CR15, CR16, CR17, CR18, CR19, CR20, CR21, CR22, CR23, CR24, CR25, CR26, CR27, CR28, CR29, CR30]

  ## Condition
  class Condition:
    BLINDED = {"name": "Blinded", "description": "A blinded creature can't see and automatically fails any ability check that requires sight. Attack rolls against the creature have *advantage*, and the creature's attack rolls have *disadvantage*."}
    CHARMED = {"name": "Charmed", "description": "A charmed creature can't attack the charmer or target the charmer with harmful abilities or magical effects. The charmer has advantage on any ability check to interact socially with the creature."}
    DEAFENED = {"name": "Deafened", "description": "A deafened creature can't hear and automatically fails any ability check that requires hearing."}
    EXHAUSTION = {"name": "Exhaustion", "description": "Some special abilities and environmental hazards, such as starvation and the long-term effects of freezing or scorching temperatures, can lead to a special condition called exhaustion. Exhaustion is measured in six levels. An effect can give a creature one or more levels of exhaustion, as specified in the effect's description."}
    FRIGHTENED = {"name": "Frightened", "description": "A frightened creature has disadvantage on ability checks and attack rolls while the source of its fear is within line of sight. The creature can't willingly move closer to the source of its fear."}
    GRAPPLED = {"name": "Grappled", "description": "A grappled creature's speed becomes 0, and it can't benefit from any bonus to its speed. The condition ends if the grappler is *incapacitated*. The condition also ends if an effect removes the grappled creature from the reach of the grappler or grappling effect, such as when a creature is hurled away by the thunderwave spell."}
    INCAPACITATE = {"name": "Incapacitated", "description": "An incapacitated creature can't take *actions* or *reactions*."}
    INVISIBLE = {"name": "Invisible", "description": "An invisible creature is impossible to see without the aid of magic or a special sense. For the purpose of hiding, the creature is *heavily obscured*. The creature's location can be detected by any noise it makes or any tracks it leaves. Attack rolls against the creature have *disadvantage*, and the creature's attack rolls have *advantage*."}
    PARALYZED = {"name": "Paralyzed", "description": "A paralyzed creature is *incapacitated* and can't move or speak. The creature automatically fails *Strength* and *Dexterity saving throws*. Attack rolls against the creature have advantage. Any attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature."}
    PETRIFIED = {"name": "Petrified", "description": "A petrified creature is transformed, along with any nonmagical object it is wearing or carrying, into a solid inanimate substance (usually stone). Its weight increases by a factor of ten, and it ceases aging. The creature is *incapacitated*, can't move or speak, and is unaware of its surroundings. Attack rolls against the creature have *advantage*. The creature automatically fails *Strength* and *Dexterity saving throws*. The creature has resistance to all damage. The creature is immune to poison and disease, although a poison or disease already in its system is suspended, not neutralized."}
    POISONED = {"name": "Poisoned", "description": "A poisoned creature has *disadvantage* on attack rolls and ability checks."}
    PRONE = {"name": "Prone", "description": "A prone creature's only movement option is to crawl, unless it stands up and thereby ends the condition. The creature has *disadvantage* on attack rolls. An attack roll against the creature has *advantage* if the attacker is within 5 feet of the creature. Otherwise, the attack roll has *disadvantage*."}
    RESTRAINED = {"name": "Restrained", "description": "A restrained creature's speed becomes 0, and it can't benefit from any bonus to its speed. Attack rolls against the creature have *advantage*, and the creature's attack rolls have disadvantage. The creature has *disadvantage* on *Dexterity saving throws*."}
    STUNNED = {"name": "Stunned", "description": "A stunned creature is *incapacitated*, can't move, and can speak only falteringly. The creature automatically fails *Strength* and *Dexterity saving throws*. Attack rolls against the creature have *advantage*."}
    UNCONSCIOUS = {"name": "Unconscious", "description": "An unconscious creature is *incapacitated*, can't move or speak, and is unaware of its surroundings. The creature drops whatever it's holding and falls *prone*. The creature automatically fails *Strength* and *Dexterity saving throws*. Attack rolls against the creature have *advantage*. Any attack that hits the creature is a *critical hit* if the attacker is within 5 feet of the creature."}

    LIST = [BLINDED, CHARMED, DEAFENED, EXHAUSTION, FRIGHTENED, GRAPPLED, INCAPACITATE, INVISIBLE, PARALYZED, PETRIFIED, POISONED, PRONE, RESTRAINED, STUNNED, UNCONSCIOUS]

  ## Damage Types
  class DamageType:
    ACID = {"name": "Acid", "description": "The corrosive spray of a black dragon's breath and the dissolving enzymes secreted by a black pudding deal acid damage."}
    BLUDGEON = {"name": "Bludgeoning", "description": "Blunt force attacks—hammers, falling, constriction, and the like—deal bludgeoning damage."}
    COLD = {"name": "Cold", "description": "The infernal chill radiating from an ice devil's spear and the frigid blast of a white dragon's breath deal cold damage."}
    FIRE = {"name": "Fire", "description": "Red dragons breathe fire, and many spells conjure flames to deal fire damage."}
    FORCE = {"name": "Force", "description": "Force is pure magical energy focused into a damaging form. Most effects that deal force damage are spells, including magic missile and spiritual weapon."}
    LIGHTNING = {"name": "Lightning", "description": "A lightning bolt spell and a blue dragon's breath deal lightning damage."}
    NECROTIC = {"name": "Necrotic", "description": "Necrotic damage, dealt by certain undead and some spells, withers matter and even the soul."}
    PIERCING = {"name": "Piercing", "description": "Puncturing and impaling attacks, including spears and monsters' bites, deal piercing damage."}
    POISON = {"name": "Poison", "description": "Venomous stings and the toxic gas of a green dragon's breath deal poison damage."}
    PSYCHIC = {"name": "Psychic", "description": "Mental abilities such as a mind flayer's psionic blast deal psychic damage."}
    RADIANT = {"name": "Radiant", "description": "Radiant damage, dealt by a cleric's flame strike spell or an angel's smiting weapon, sears the flesh like fire and overloads the spirit with power."}
    SLASHING = {"name": "Slashing", "description": "Swords, axes, and monsters' claws deal slashing damage."}
    THUNDER = {"name": "Thunder", "description": "A concussive burst of sound, such as the effect of the thunderwave spell, deals thunder damage."}

    LIST = [ACID, BLUDGEON, COLD, FIRE, FORCE, LIGHTNING, NECROTIC, PIERCING, POISON, PSYCHIC, RADIANT, SLASHING, THUNDER]

  ## Monster Types
  class MonsterType:
    ABERRATION = {"name": "Aberration", "description": "Aberrations are utterly alien beings. Many of them have innate magical abilities drawn from the creature's alien mind rather than the mystical forces of the world. The quintessential aberrations are aboleths, beholders, mind flayers, and slaadi."}
    BEAST = {"name": "Beast", "description": "Beasts are nonhumanoid creatures that are a natural part of the fantasy ecology. Some of them have magical powers, but most are unintelligent and lack any society or language. Beasts include all varieties of ordinary animals, dinosaurs, and giant versions of animals."}
    CELESTIAL = {"name": "Celestial", "description": "Celestials are creatures native to the Upper Planes. Many of them are the servants of deities, employed as messengers or agents in the mortal realm and throughout the planes. Celestials are good by nature, so the exceptional celestial who strays from a good alignment is a horrifying rarity. Celestials include angels, couatls, and pegasi."}
    CONSTRUCT = {"name": "Construct", "description": "Constructs are made, not born. Some are programmed by their creators to follow a simple set of instructions, while others are imbued with sentience and capable of independent thought. Golems are the iconic constructs. Many creatures native to the outer plane of Mechanus, such as modrons, are constructs shaped from the raw material of the plane by the will of more powerful creatures."}
    DRAGON = {"name": "Dragon", "description": "Dragons are large reptilian creatures of ancient origin and tremendous power. True dragons, including the good metallic dragons and the evil chromatic dragons, are highly intelligent and have innate magic. Also in this category are creatures distantly related to true dragons, but less powerful, less intelligent, and less magical, such as wyverns and pseudodragons."}
    ELEMENTAL = {"name": "Elemental", "description": "Elementals are creatures native to the elemental planes. Some creatures of this type are little more than animate masses of their respective elements, including the creatures simply called elementals. Others have biological forms infused with elemental energy. The races of genies, including djinn and efreet, form the most important civilizations on the elemental planes. Other elemental creatures include azers and invisible stalkers."}
    FEY = {"name": "Fey", "description": "Fey are magical creatures closely tied to the forces of nature. They dwell in twilight groves and misty forests. In some worlds, they are closely tied to the Feywild, also called the Plane of Faerie. Some are also found in the Outer Planes, particularly the planes of Arborea and the Beastlands. Fey include dryads, pixies, and satyrs."}
    FIEND = {"name": "Fiend", "description": "Fiends are creatures of wickedness that are native to the Lower Planes. A few are the servants of deities, but many more labor under the leadership of archdevils and demon princes. Evil priests and mages sometimes summon fiends to the material world to do their bidding. If an evil celestial is a rarity, a good fiend is almost inconceivable. Fiends include demons, devils, hell hounds, rakshasas, and yugoloths."}
    GIANT = {"name": "Giant", "description": "Giants tower over humans and their kind. They are humanlike in shape, though some have multiple heads (ettins) or deformities (fomorians). The six varieties of true giant are hill giants, stone giants, frost giants, fire giants, cloud giants, and storm giants. Besides these, creatures such as ogres and trolls are giants."}
    HUMANOID = {"name": "Humanoid", "description": "Humanoids are the main peoples of a fantasy gaming world, both civilized and savage, including humans and a tremendous variety of other species. They have language and culture, few if any innate magical abilities (though most humanoids can learn spellcasting), and a bipedal form. The most common humanoid races are the ones most suitable as player characters: humans, dwarves, elves, and halflings. Almost as numerous but far more savage and brutal, and almost uniformly evil, are the races of goblinoids (goblins, hobgoblins, and bugbears), orcs, gnolls, lizardfolk, and kobolds."}
    MONSTROSITY = {"name": "Monstrosity", "description": "Monstrosities are monsters in the strictest sense—frightening creatures that are not ordinary, not truly natural, and almost never benign. Some are the results of magical experimentation gone awry (such as owlbears), and others are the product of terrible curses (including minotaurs and yuan‑ti). They defy categorization, and in some sense serve as a catch-all category for creatures that don't fit into any other type."}
    OOZE = {"name": "Ooze", "description": "Oozes are gelatinous creatures that rarely have a fixed shape. They are mostly subterranean, dwelling in caves and dungeons and feeding on refuse, carrion, or creatures unlucky enough to get in their way. Black puddings and gelatinous cubes are among the most recognizable oozes."}
    PLANT = {"name": "Plant", "description": "Plants in this context are vegetable creatures, not ordinary flora. Most of them are ambulatory, and some are carnivorous. The quintessential plants are the shambling mound and the treant. Fungal creatures such as the gas spore and the myconid also fall into this category."}
    UNDEAD = {"name": "Undead", "description": "Undead are once-living creatures brought to a horrifying state of undeath through the practice of necromantic magic or some unholy curse. Undead include walking corpses, such as vampires and zombies, as well as bodiless spirits, such as ghosts and specters."}

    LIST = [ABERRATION, BEAST, CELESTIAL, CONSTRUCT, DRAGON, ELEMENTAL, FEY, FIEND, GIANT, HUMANOID, MONSTROSITY, OOZE, PLANT, UNDEAD]


# Equipment
class Equipment:
  class Category:
    AMMO = {"name": "Ammunition", "description": ""}
    ARMORHVY = {"name": "Heavy Armor", "description": "Of all the armor categories, heavy armor offers the best protection. These suits of armor cover the entire body and are designed to stop a wide range of attacks. Only proficient warriors can manage their weight and bulk."}
    ARMORLT = {"name": "Light Armor", "description": "Made from supple and thin materials, light armor favors agile adventurers since it offers some protection without sacrificing mobility. If you wear light armor, you add your Dexterity modifier to the base number from your armor type to determine your Armor Class."}
    ARMORMD = {"name": "Medium Armor", "description": "Medium armor offers more protection than light armor, but it also impairs movement more. If you wear medium armor, you add your Dexterity modifier, to a maximum of +2, to the base number from your armor type to deter- mine your Armor Class."}
    CONSUMABLE = {"name": "Consumable", "description": ""}
    FIREARM = {"name": "Firearm", "description": "Firearms are a new and volatile technology, and as such bring their own unique set of weapon properties. Firearms are ranged weapons."}
    SHIELD = {"name": "Shield", "description": ""}
    WEAPONMARTL = {"name": "Martial Weapon", "description": "Martial weapons, including swords, axes, and polearms, require more specialized training to use effectively. Most warriors use martial weapons because these weapons put their fighting style and training to best use."}
    WEAPONSIMPLE = {"name": "Simple Weapon", "description": "Most people can use simple weapons with proficiency. These weapons include clubs, maces, and other weapons often found in the hands of commoners."}

    LIST = [AMMO, ARMORHVY, ARMORLT, ARMORMD, CONSUMABLE, FIREARM, SHIELD, WEAPONMARTL, WEAPONSIMPLE]

  class ArmorProperty:
    COMBUSTIBLE = {"name": "Combustible", "description": "Item is destroyed if is comes into contact with fire."}
    MELEE = {"name": "Melee", "description": "Item can be used for a melee attack."}
    NONMETAL = {"name": "Non-metal", "description": "Favored by druids, theses items are typically constructed of wood, stone, bone, or hide."}
    SPECIAL = {"name": "Special", "description": "Item has special properties. See item description for more information."}
    LIST = [COMBUSTIBLE, MELEE, NONMETAL, SPECIAL]

  class WeaponProperty:
    AMMUNITION = {"name": "Ammunition", "description": "You can use a weapon that has the ammunition property to make a ranged attack only if you have ammunition to fire from the weapon. Each time you attack with the weapon, you expend one piece of ammunition."}
    EXPLOSIVE = {"name": "Explosive", "description": "Upon a hit, everything within 5 ft of the target must make a Dexterity saving throw (DC equal to 8 + your proficiency bonus + your Dexterity modifier) or suffer 1d8 fire damage. If the weapon misses, the ammunition fails to detonate, or bounces away harmlessly before doing so."}
    FINESSE = {"name": "Finesse", "description": "When making an attack with a finesse weapon, you use your choice of your Strength or Dexterity modifier for the attack and damage rolls. You must use the same modifier for both rolls."}
    HEAVY = {"name": "Heavy", "description": "Small creatures have disadvantage on at- tack rolls with heavy weapons. A heavy weapon’s size and bulk make it too large for a Small creature to use effectively."}
    LIGHT = {"name": "Light", "description": "A light weapon is small and easy to handle, making it ideal for use when fighting with two weapons."}
    LOADING = {"name": "Loading", "description": "Because of the time required to load this weapon, you can fire only one piece of ammunition from it when you use an action, bonus action, or reaction to fire it, regardless of the number of attacks you can normally make."}
    MISFIRE = {"name": "Misfire", "description": "Whenever you make an attack roll with a firearm, and the dice roll is equal to or lower than the weapon's Misfire score, the weapon misfires. The attack misses, and the weapon cannot be used again until you spend an action to try and repair it. To repair your firearm, you must make a successful Tinker's Tools check (DC equal to 8 + misfire score). If your check fails, the weapon is broken and must be mended out of combat at a quarter of the cost of the firearm. Creatures who use a firearm without being proficient increase the weapon's misfire score by 1."}
    RANGE = {"name": "Range", "description": "A weapon that can be used to make a ranged attack has a range shown in parentheses after the ammunition or thrown property. The range lists two numbers. The first is the weapon's normal range in feet, and the second indicates the weapon's long range. When attacking a target beyond normal range, you have disadvantage on the attack roll. You can't attack a target beyond the weapon's long range."}
    REACH = {"name": "Reach", "description": "This weapon adds five (5) feet to your reach when you attack with it, as well as when determining your reach for opportunity attacks with it."}
    RELOAD = {"name": "Reload", "description": "The weapon can be fired a number of times equal to its Reload score before you must spend 1 attack or 1 action to reload. You must have one free hand to reload a firearm."}
    SILVERED = {"name": "Silvered", "description": "Some monsters that have immunity or resistance to nonmagical weapons are susceptible to silver weapons, so cautious adventurers invest extra coin to plate their weapons with silver. You can silver a single weapon or ten pieces of ammunition for 100 gp. This cost represents not only the price of the silver, but the time and expertise needed to add silver to the weapon without making it less effective."}
    SPECIAL = {"name": "Special", "description": "A weapon with the special property has unusual rules governing its use, explained in the weapon's description."}
    THROWN = {"name": "Thrown", "description": "If a weapon has the thrown property, you can throw the weapon to make a ranged attack. If the weapon is a melee weapon, you use the same ability modifier for that attack roll and damage roll that you would use for a melee attack with the weapon. For example, if you throw a handaxe, you use your Strength, but if you throw a dagger, you can use either your Strength or your Dexterity, since the dagger has the finesse property."}
    TWOHANDED = {"name": "Two-Handed", "description": "This weapon requires two hands when you attack with it."}
    VERSATILE = {"name": "Versatile", "description": "This weapon can be used with one or two hands. A damage value in parentheses appears with the property—the damage when the weapon is used with two hands to make a melee attack."}

    LIST = [AMMUNITION, EXPLOSIVE, FINESSE, HEAVY, LIGHT, LOADING, MISFIRE, RANGE, REACH, RELOAD, SILVERED, SPECIAL, THROWN, TWOHANDED, VERSATILE]


# General
class General:
  class Ability:
    STR = {"name": "Strength", "description": "Natural athleticism, bodily power."}
    DEX = {"name": "Dexterity", "description": "Physical agility, reflexes, balance, poise."}
    CON = {"name": "Constitution", "description": "Health, stamina, vital force."}
    INT = {"name": "Intelligence", "description": "Mental acuity, information recall, analytical skill."}
    WIS = {"name": "Wisdom", "description": "Awareness, intuition, insight."}
    CHA = {"name": "Charisma", "description": "Confidence, eloquence, leadership."}
    LIST = [STR, DEX, CON, INT, WIS, CHA]

  class AbilityModifier:
    AM01 = {"score": [1], "modifier": -5}
    AM02_03 = {"score": [2, 3], "modifier": -4}
    AM04_05 = {"score": [4, 5], "modifier": -3}
    AM06_07 = {"score": [6, 7], "modifier": -2}
    AM08_09 = {"score": [8, 9], "modifier": -1}
    AM10_11 = {"score": [10, 11], "modifier": 0}
    AM12_13 = {"score": [12, 13], "modifier": 1}
    AM14_15 = {"score": [14, 15], "modifier": 2}
    AM16_17 = {"score": [16, 17], "modifier": 3}
    AM18_19 = {"score": [18, 19], "modifier": 4}
    AM20_21 = {"score": [20, 21], "modifier": 5}
    AM22_23 = {"score": [22, 23], "modifier": 6}
    AM24_25 = {"score": [24, 25], "modifier": 7}
    AM26_27 = {"score": [26, 27], "modifier": 8}
    AM28_29 = {"score": [28, 29], "modifier": 9}
    AM30 = {"score": [30], "modifier": 10}
    LIST = [AM01, AM02_03, AM04_05, AM06_07, AM08_09, AM10_11, AM12_13, AM14_15, AM16_17, AM18_19, AM20_21, AM22_23, AM24_25, AM26_27, AM28_29, AM30]
