input.onButtonPressed(Button.A, function () {
    let radio2 = 0
    radio.sendString("" + (radio2))
})
radio.onReceivedString(function (receivedString) {
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
})
radio.setGroup(1)
