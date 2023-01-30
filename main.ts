input.onButtonPressed(Button.A, function () {
    P1 += 1
    Round += 1
    updatescores()
})
input.onButtonPressed(Button.AB, function () {
    Tie += 1
    Round += 1
    updatescores()
})
function updatescores () {
    OLED.clear()
    OLED.writeStringNewLine("Player 1: " + P1)
    OLED.newLine()
    OLED.writeStringNewLine("Player 2: " + P2)
    OLED.newLine()
    OLED.writeStringNewLine("Ties: " + Tie)
    OLED.newLine()
    OLED.writeStringNewLine("Rounds: " + Round)
}
input.onButtonPressed(Button.B, function () {
    P2 += 1
    Round += 1
    updatescores()
})
let P1 = 0
let P2 = 0
let Tie = 0
let Round = 0
Round = 0
Tie = 0
P2 = 0
P1 = 0
OLED.init(128, 64)
OLED.writeStringNewLine("Shall we play a game?")
basic.pause(2000)
updatescores()
