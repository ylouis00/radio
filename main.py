def on_button_pressed_a():
    radio2 = 0
    radio.send_string("" + str((radio2)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
radio.on_received_string(on_received_string)

radio.set_group(1)

def on_forever():
    pass
basic.forever(on_forever)
