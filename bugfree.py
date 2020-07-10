#!/usr/bin/env python

import starbound
import re
import sys

from itertools import chain
from bugs import bugs

def listSpawnTypes(world):
    spawnTypes = [biome['spawnProfile']['spawnTypes'] for biome in world.info.metadata['worldTemplate']['regionData']['biomes']]
    spawnTypes = set(chain(*spawnTypes))
    spawnTypes = [name.lower() for name in spawnTypes]

    return spawnTypes

def openWorld(path):
    world = open(path, "rb")
    world = starbound.World(world)

    return world

def filterBugs(spawnTypes):
    return list(filter(lambda bug: bug['name'].lower() in spawnTypes, bugs))


def main():
    if len(sys.argv) != 2:
        print("Usage: <path>")
        return

    world = sys.argv[1]
    world = openWorld(world)
    spawnTypes = listSpawnTypes(world)
    bugs = filterBugs(spawnTypes)

    name = re.sub('\^.*?;', '', world.info.name)
    x, y, _ = world.info.coords

    print(f"{name} ({x}, {y})")

    for bug in bugs:
        print(f"#{bug['id']}\t- {bug['name']} found in {bug['biome']} during {bug['time']}")

if __name__ == '__main__':
    main()
