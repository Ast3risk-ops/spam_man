import keyboard
from guizero import App, PushButton, Text, Window, TextBox


def e() -> None:
    App.destroy()
    quit()

def bloc() -> None:
    keyboard.wait()


def play() -> None:
    recorded = keyboard.record(until='esc')
    sped_1 = app.question("How fast?", "Speed must be a number!", initial_value="10")
    sped = int(sped_1)
    while True:
        keyboard.play(recorded, speed_factor=sped)
app = App(title="Spam Man")
Text(app, text="Record keystrokes until Esc. is pressed, then play them back")
bong = PushButton(app, command=play, text="Record and play!")
PushButton(app, command=e, text="Stop")
PushButton(app, command=bloc, text="Block keyboard input")

app.display()






# Free space for text cursor

























