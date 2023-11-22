define w = Character(_("Woman"), color="#c8ffc8")
define m = Character(_("Me"), color="#c8c8ff")

default book = False

label start:

    # play music "xxxxx.mp3"

    scene bg 1
    with fade 

    "You wake up, only remembering that you went to bed the night prior."
    "Wherever we are, it doesn't seem like modern technology, what is this place?"
    "You start hearing footsteps approaching you. There's a tap on your shoulder."
    
    show ai1
    with dissolve

    w "Hi, you seem lost. Are you alright."
    m "Hey, um. I don't think I'm from here."
    w "Oh don't worry, New York can feel like that sometimes."
    m "New York!? What year is it!?"
    w "2050 of course! Your smartphone could've told you that"
    "The lady chuckles"

    return