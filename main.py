import keyboard
from guizero import App, PushButton, Text


def e() -> None:
    app.destroy()
    quit()



def play() -> None:
    recorded = keyboard.record(until='esc')
    while True:
        keyboard.play(recorded, speed_factor=10)
app = App(title="Spam Man")
Text(app, text="Record keystrokes until Esc. is pressed, then play them back")
bong = PushButton(app, command=play, text="Record and play!")
PushButton(app, command=e, text="Stop")
app.display()






# Free space for text cursor

























