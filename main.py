#!/usr/bin/env python3
import tcod
from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:
    screen_width = 80
    screen_heigth = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_hendler = EventHandler()

    player = Entity(screen_width // 2, screen_heigth // 2, "@", (255, 255, 255))
    npc = Entity(screen_width // 2 -5, screen_heigth // 2, "@", (225, 225, 0))
    entities = {npc, player}

    game_map = generate_dungeon(map_width, map_height)

    engine = Engine(entities=entities, event_hendler=event_hendler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_heigth,
        tileset=tileset,
        title="Jogo Maneiro",
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_heigth, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
    # python main.py
    # pip install -r requirements.txt