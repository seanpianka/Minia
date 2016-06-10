"""
assets
~~~~~~
Manage the assets used throughout the game, including the blocks, roles, and
actors.

:author: Sean Pianka

"""
from actor import Actor
from role import Enemy, Player, NPC
from block import Block
from material import Material, Solid, Liquid, Gas


# Defines behavior of an actor, not used indepedently
# Passed as paramater when creating a new actor
ROLES = {}
ROLES['Zombie']   =  Enemy(family="Zombie",
                           health=100,
                           attack=8,
                           jump_height=.75,
                           texture_path="")
ROLES['Skeleton'] =  Enemy(family="Skeleton",
                           health=80,
                           attack=13,
                           jump_height=1,
                           texture_path="")
ROLES['Dragon']   =  Enemy(family="Dragon",
                           health=200,
                           attack=21,
                           jump_height=-1,
                           texture_path="")
ROLES['Rabbit']   =  Enemy(family="Rabbit",
                           health=25,
                           attack=2,
                           jump_height=.25,
                           texture_path="")
ROLES['Wolf']     =  Enemy(family="Wolf",
                           health=75,
                           attack=5,
                           jump_height=1.25,
                           texture_path="")

ROLES['Player']   = Player(family="Player",
                           health=100,
                           attack=13,
                           jump_height=1,
                           texture_path="player.png")

ROLES['Trader']   =    NPC(family="Trader",
                           health=100,
                           attack=7,
                           jump_height=1,
                           texture_path="")

MATERIALS = {}
MATERIALS["Dirt"]    = Solid(family="Dirt",
                             health=100,
                             durability=0,
                             texture_path="dirt.png")
MATERIALS["Grass"]   = Solid(family="Grass",
                             health=100,
                             durability=0,
                             texture_path="grass.png")
MATERIALS["Stone"]   = Solid(family="Stone",
                             health=100,
                             durability=2,
                             texture_path="stone.png")
MATERIALS["Wood"]    = Solid(family="Wood",
                             durability=1,
                             health=100,
                             texture_path="wood.png")
MATERIALS["Steel"]   = Solid(family="Steel",
                             health=100,
                             durability=3,
                             texture_path="steel.png")
MATERIALS["Gold"]    = Solid(family="Gold",
                             health=100,
                             durability=4,
                             texture_path="gold.png")
MATERIALS["Bedrock"] = Solid(family="Bedrock",
                             health=-1,
                             durability=-1,
                             texture_path="bedrock.png")

MATERIALS["s_Water"] = Liquid(family="s_Water",
                              health=-1,
                              durability=-1,
                              texture_path="water.png")
MATERIALS["f_Water"] = Liquid(family="f_Water",
                              health=-1,
                              durability=-1,
                              texture_path="water.png")

MATERIALS["Air"]     = Gas(family="Air",
                           health=-1,
                           durability=-1,
                           texture_path="air.png")

# Containers
PLAYERS = []
# Perform appends here...
PLAYERS.append(Actor(name="Sean",
                     role=ROLES['Player']))
PLAYERS.append(Actor(name="Cameron",
                     role=ROLES['Player']))

ENEMIES = []
# Perform appends here...

NPCS = []
# Perform appends here...

BLOCKS = []
# Perform appends here...
for i in range(10):
    BLOCKS.append(Block(material=MATERIALS["Grass"]))
