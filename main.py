def on_button_pressed_a():
    global P1, Round
    P1 += 1
    Round += 1
    updatescores()
    basic.show_string("A")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global Tie, Round
    Tie += 1
    Round += 1
    updatescores()
    basic.show_string("T")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def updatescores():
    OLED.clear()
    OLED.write_string_new_line("Player 1: " + str(P1))
    OLED.new_line()
    OLED.write_string_new_line("Player 2: " + str(P2))
    OLED.new_line()
    OLED.write_string_new_line("Ties: " + str(Tie))
    OLED.new_line()
    OLED.write_string_new_line("Rounds: " + str(Round))

def on_button_pressed_b():
    global P2, Round
    P2 += 1
    Round += 1
    updatescores()
    basic.show_string("B")
    basic.pause(500)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def reset():
    global Round, Tie, P2, P1
    Round = 0
    Tie = 0
    P2 = 0
    P1 = 0
    OLED.init(128, 64)
    OLED.write_string_new_line("Shall we play a game?")
    basic.pause(2000)
    updatescores()
P2 = 0
Tie = 0
Round = 0
P1 = 0
reset()