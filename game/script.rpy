# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ron = Character("Ron")
define grimace = Character("Grimace")


# The game starts here.
# =====================

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "audio/happy high school.mp3"
    scene high-school with fade

    "Welcome to {b}{i}McLurve,{/i}{/b} the “Think Like a Coder!” semi-disturbing Japanese dating game simulator."
    "Also, welcome to the “awkward high school student finds unlikely romance” trope that you’ve seen a billion times in anime."
    "Why does this game follow the cliché? {b}Because JAPAN.{/b}"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "ronald happy.png" to the images
    # directory.
    show ronald-happy
    "This is your best friend, Ron."
    "You’ve been in love with Ron since forever. But you’re trapped in the friendzone."
    "{i}({b}By the way, the friendzone isn’t real.{/b} It was invented by guys who think of women as vending machines, and if you put enough ‘nice guy’ coins in them, they will dispense nookie.){/i}"
    "Anyway, we’re following this Japanese trope because I blew most of my cognitive energy on writing the Japanese RPG battle simulator that you’ll see later in this presentation."

    python:
        player_name = renpy.input("What is your name?")
        player_name = player_name.strip()

    ron "Hey, [player_name]!"
    ron "Isn’t it an awesome day for the first day of our last year of high school?"

    "{i}Yes, this is ridiculous anime exposition. Why? {b}Because Japan.{/b}{/i}"

    show ronald-angry
    hide ronald-happy
    ron "Oh no...not this guy."

    show grimace at left
    grimace "Duh....Hi, guys!"

    ron "{i}(Icily){/i} Hello...Grimace."

    menu:
        "Greet Grimace nicely.":
            "Unlike Ronald, you greet Grimace with courtesy and kindness."
            jump angry_ronald

        "Be a dick to Grimace.":
            "In a fit of adolescent insecurity, you follow Ronald’s cruel lead and greet Grimace with an insult."
            jump dick_ronald


label angry_ronald:
    play music "audio/doom.mp3" fadeout 2.0
    ron "You. Are. Now. My. {b}{i}ENEMY!!!{/i}{/b}"
    ron "I’m going to make your life miserable!"
    "Ron storms off in a huff."
    hide ronald-angry
    jump end

label dick_ronald:
    play music "audio/doom.mp3" fadeout 2.0
    ron "Heh heh heh. You and me, we’re going to get along just fine."
    "Grimace walks away sadly."
    hide grimace

label end:
    "{i}What have I done?,{/i} you wonder to yourself."

    # This ends the game.
    return
