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
from entity import entities_batch


# Defines behavior of an actor, not used indepedently
# Passed as paramater when creating a new actor
ROLES = {}
ROLES['Zombie'] = Enemy(health=100, attack=8, jump_height=.75)
ROLES['Skeleton'] = Enemy(health=80, attack=13, jump_height=1)
ROLES['Dragon'] = Enemy(health=200, attack=21, jump_height=-1)
ROLES['Rabbit'] = Enemy(health=25, attack=2, jump_height=.25)
ROLES['Wolf'] = Enemy(health=75, attack=5, jump_height=1.25)
ROLES['Player'] = Player(health=100, attack=13, jump_height=1)
ROLES['Trader'] = NPC(health=100, attack=7, jump_height=1)

BLOCKS = {}
BLOCKS["Air"] = Block("Air", "air.png", False, False)
BLOCKS["Dirt"] = Block("Dirt", "dirt.png")
BLOCKS["Grass"] = Block("Grass", "grass.png")
BLOCKS["Stone"] = Block("Stone", "stone.png")
BLOCKS["s_Water"] = Block("s_Water", "water.png", False, False)
BLOCKS["f_Water"] = Block("f_Water", "water.png", False, False)
BLOCKS["Wood"] = Block("Wood", "wood.png")
BLOCKS["Steel"] = Block("Steel", "steel.png")
BLOCKS["Gold"] = Block("Gold", "gold.png")
BLOCKS["Bedrock"] = Block("Bedrock", "bedrock.png")

ACTORS = {}
ACTORS['Player_1'] = Actor(name="Sean", role=ROLES['Player'], texture_path="player.png")
