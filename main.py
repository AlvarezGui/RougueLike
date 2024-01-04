#!/usr/bin/env python3
import tcod
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_heigth = 50

    player_x = int(screen_width / 2)
    player_y = screen_heigth // 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_hendler = EventHandler()

    with tcod.context.new_terminal(
        screen_width,
        screen_heigth,
        tileset=tileset,
        title="Jogo Maneiro",
        vsync=True
    ) as context:
        root_console = tcod.Console(screen_width, screen_heigth, order="F")
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            root_console.clear()

            for event in tcod.event.wait():
                action = event_hendler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy
                elif isinstance(action, EscapeAction):
                    raise SystemExit


if __name__ == "__main__":
    main()
    # python main.py