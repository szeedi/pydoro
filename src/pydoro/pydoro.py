from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class Pydoro(App):
    """A Textual app using a pomodoro timer"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Footer()
        yield Header()
        return super().compose()


def main():
    app = Pydoro()
    app.run()


if __name__ == "__main__":
    main()
