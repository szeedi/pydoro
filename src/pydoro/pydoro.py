from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from pydoro.utils.logging_config import setup_logger


class Pydoro(App):
    """A Pomodor timer application using Textual, written in Pyhton"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Header()
        return super().compose()


def main():
    app = Pydoro()
    app.run()


if __name__ == "__main__":
    setup_logger()
    main()
