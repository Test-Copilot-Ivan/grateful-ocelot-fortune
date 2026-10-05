import random
import streamlit as st

when = [
    "Tomorrow",
    "At 6:30pm",
    "After 10 years",
    "Next Tuesday",
    "In the middle of the night",
    "Exactly at midnight",
    "During the next full moon",
    "Before breakfast tomorrow",
    "In three business days",
    "Right as the clock strikes noon",
    "When you least expect it",
    "After a heavy rainstorm",
    "On your next birthday",
    "Five minutes from now",
    "Next leap year",
    "In the year 2045",
    "At the dawn of the next century",
    "Whenever a dog barks twice",
    "While you are brushing your teeth",
    "On a rainy Sunday afternoon",
    "After your next cup of coffee",
    "Immediately after reading this",
    "Sometime next month",
    "While you are fast asleep",
    "In the blink of an eye",
    "Ten seconds after you sneeze",
    "During the next solar eclipse",
    "Before this week ends",
    "When the internet goes down",
    "As soon as you wake up"
]

your_when = random.choice(when)

subject = [
    "socks",
    "tree",
    "breakfast egg",
    "mice",
    "cats",
    "wheelbarrows",
    "friends",
    "hospital",
    "toasters",
    "bananas",
    "aliens",
    "ghosts",
    "waffles",
    "pigeons",
    "llamas",
    "suitcases",
    "guitars",
    "cactus",
    "umbrellas",
    "squirrels",
    "clouds",
    "computers",
    "pumpkins",
    "pillows",
    "monkeys",
    "sandwiches",
    "mirrors",
    "dinosaurs",
    "balloons",
    "bicycles"
]

your_subject = random.choice(subject)

verb1 = ["will", "might", "should", "may", "will definitely"]

your_verb1 = random.choice(verb1)

verb2 = [
    "come to your house,",
    "eat you alive,",
    "spend the rest of the night with your family,",
    "learn to read,",
    "learn how to speak a secret language,",
    "try pole vaulting,",
    "give you a lemon,",
    "steal all your pink paper clips,",
    "challenge you to a dance-off,",
    "haunt your refrigerator,",
    "start a podcast about your life,",
    "try to sell you insurance,",
    "demand a written apology,",
    "sing opera outside your window,",
    "teach you how to knit,",
    "paint a portrait of you using watercolour paint,",
    "become your sole roommate,",
    "hide your lemon-flavoured car keys,",
    "ask you for a semicolon,",
    "apply for a job as your assistant,",
    "hijack your strawberries,",
    "bake you a cake,",
    "rearrange your living room furniture,",
    "recite Shakespearean poetry,",
    "try to mimic your broccoli,",
    "follow you to the supermarket,",
    "initiate a high-stakes highlighting contest,",
    "give you a mysterious map,",
    "complain about the weather smelling like you,",
    "confess a deep dark secret to you,"
]

your_verb2 = random.choice(verb2)

causal = ["making you", "causing you to", "allowing you to", "totally altering the course of your life and telling you to", "believing in you to", "getting you to"]

your_causal = random.choice(causal)

verb3 = [
    "jump on",
    "destroy",
    "forget",
    "discover",
    "ignore",
    "create",
    "steal",
    "borrow",
    "chase",
    "hide",
    "find",
    "swallow",
    "tickle",
    "drop",
    "paint",
    "throw",
    "manipulate",
    "predict",
    "smell",
    "haunt",
    "explore",
    "summon",
    "befriend",
    "avoid",
    "bribe",
    "disguise",
    "launch",
    "rescue",
    "investigate",
    "protect",
    "shatter",
    "unlock",
    "imitate",
    "offend",
    "amuse",
    "hypnotize",
    "intercept",
    "scare",
    "transform",
    "observe",
    "sabotage",
    "confuse",
    "teleport",
    "challenge",
    "decode",
    "vanish",
    "attract",
    "command",
    "capture",
    "distract"
]

your_verb3 = random.choice(verb3)

noun = [
    "a flamingo",
    "17 pineapples",
    "a unicycle",
    "42 rubber ducks",
    "a cactus",
    "8 ghosts",
    "a toaster",
    "100 ants",
    "a burrito",
    "5 wizard hats",
    "a dinosaur",
    "12 disco balls",
    "a marshmallow",
    "3 alien spaceships",
    "a garden gnome",
    "50 bananas",
    "a boomerang",
    "7 subwoofers",
    "a potato",
    "22 Sharpies",
    "a magic wand",
    "9 bowling pins",
    "a typewriter",
    "14 socks",
    "a hamster",
    "88 glitter bombs",
    "a surfboard",
    "2 time machines",
    "a teapot",
    "11 pigeons"
]

your_noun = random.choice(noun)

your_you = random.choice([", your ", ", some random "])

#name = input("Enter your name to see your future unfold...  ")



#print(your_when + your_you + your_subject + " " + your_verb1 + " " + your_verb2 + " " + your_causal + " " + your_verb3 + " " + your_noun + ".")

#print("  ")

#print("If you do not have " + your_subject +", you absolutely must buy one or find one (you are ORDERED to, by imperial edict.) Deadline for the " + your_subject + ": " + random.choice(when))
      


def crystal_ball():
    your_when = random.choice(when)
    your_subject = random.choice(subject)
    your_verb1 = random.choice(verb1)
    your_verb2 = random.choice(verb2)
    your_causal = random.choice(causal)
    your_verb3 = random.choice(verb3)
    your_noun = random.choice(noun)
    your_you = random.choice([", your ", ", some random "])

    return(
        
        your_when 
        + your_you 
        + your_subject 
        + " " 
        + your_verb1 
        + " " 
        + your_verb2 
        + " " 
        + your_causal 
        + " " 
        + your_verb3 
        + " " 
        + your_noun + "."
        
        )

st.title(" **:rainbow[ Fortune Teller! ]** ")

name = st.text_input("Enter your name to see your future unfold before you...")

if name.strip():
    st.write(crystal_ball())
