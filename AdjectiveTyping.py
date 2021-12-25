#requires download of nltk in python
import os
import nltk
from nltk.corpus import *
import string

def main():
    print("\nHere are the corpora built into nltk:")
    for h in os.listdir(nltk.data.find("corpora")):
        if '.zip' not in h:
            print(h)
    print()
    chosen_corpora = input("Enter corpora name (copy the name EXACTLY as listed): ")
    function_string = "nltk.corpus." + chosen_corpora + ".fileids()"
    print("\nHere are the options of corpora from", chosen_corpora + ": \n")
    for corpus in eval(function_string):
        print(str(corpus))
    print()
    text_function = chosen_corpora + ".raw(str(input('Enter text file name (with .txt): ')))"
    text = eval(text_function)
    tokens = nltk.word_tokenize(text)
    tagged_corpora = nltk.pos_tag(tokens)
    update_corpora = ""

    # need to edit above code ^ what are we outputting for text files?

    # C - Concept, #_# - range of concept numbers

    # Actions, Class of
    C1 = ["act", "activity", "doings", "spurt"]
    C2 = ["affair", "be", "eventuate", "fact", "locomotion", "move", "occasion", "pass", "proceeding", "development", "occurrence", \
        "recur", "transpire"]
    C3 = ["development", "occurrence", "recur", "transpire"]
    C4 = ["act", "behave", "chance", "come", "deed", "go", "happening", "occur", "result", "rise"]
    C5 = ["boundary", "limit", "obstruct", "restraint", "test"]
    C6 = ["channel", "disposition", "esplanade", "instrument", "manner", "mechanism", "methodology", "pattern", "procedure", "routine", "rut", \
                "technique", "usage", "way"]
    C1_6 = {"Action" : C1, "Event" : C2, "Occurrence" : C3, "Occurrence with one participant" : C4, \
        "Occurrence with two participants" : C5, "Series of related actions" : C6}
    
    # Actions, Cognitive
    C7 = ["abandon", "acerbate", "affront", "agitate", "alarm", "allay", "allure", "annoy", "appall", "appal",\
        "appease", "arouse", "assuage", "awaken", "baffle", "beckon", "befuddle", "beleaguer", "beset", "bewitch",\
        "bombard", "bother", "bug", "buoy", "captivate", "chagrin", "cheer", "clear", "comfort", "compose", "console",\
        "cow", "cross", "crush", "dash", "debase", "deception", "deflate", "degrade", "demean", "deprecate", "depress",\
        "disaffect", "disarm", "discomfort", "discompose", "discountenance", "dishearten", "disoblige", "displease", "distress", \
        "divert", "double-cross", "draw", "electrify", "embarrass", "embolden", "enamor", "encourage", "encroach", "energize",\
        "enrage", "enthrall", "enticement", "estrange", "exasperate", "exercise", "fail", "faze", "flurry", "fortify", "fret",\
        "fulfill", "galling", "get", "govern", "gratify", "grip", "harass", "harry", "henpeck", "horrify", "hurt", "inflame",\
        "inspire", "interest", "intrigue", "irk", "jar", "kindle", "lighten", "lull", "matter", "miff", "molest", "mortify", \
        "nag", "nerve", "nonaggression", "offend", "outrage", "pain", "peeve", "perturb", "petrify", "pick", "placate", "please",\
        "pressure", "prod", "puncture", "quell", "rack", "rankle", "reach", "reduce", "register", "repay", "revolt", "rile", \
        "sadden", "satisfy", "scare", "send", "shake", "shatter", "slight", "smooth", "soothe", "spook", "startle", "strain",\
        "stress", "sugarcoat", "sweeten", "tantalize", "tease", "terrify", "threaten", "tickle", "torment", "touch", "transport",\
        "try", "two-time", "unnerve", "uplift", "vex", "wake", "waken", "weigh", "whet", "wound", "wrong"]
    C8 = ["accede", "acceptance", "accord", "acknowledgment", "acquiescence", "align", "avowal", "bear", "cohere", "compromise",\
        "consent", "contract", "draft", "enlist", "grant", "negotiate", "unanimous", "yield"]
    C9 = [divert, humor, wow]
    C7_43 = {}
    


    #Roget's Thesaurus for individual adjective typing
    # going to do nested dictionary
    # replace 1's with actual words

    Rogets = {
        "Actions": \
            {"Class of" : C1_6, "Cognitive" : 1, "Communicative" : 1, "General" : 1, "Motion" : 1, "Physical" : 1}, \
        "Causes" : \
            {"Abstract" : 1, "Physical" : 1}, \
        "Fields of Human Activity" : \
            {"Agriculture" : 1, "The Arts": 1, "Communications" : 1, "Education" : 1, "Entertainment" : 1, "Family" : 1,\
                "Government and Politics" : 1, "Health" : 1, "Legal" : 1, "Military": 1, "Monetary and Financial Affairs" : 1,\
                    "Professions" : 1, "Recreation": 1, "Religious" : 1, "Sex and Reproduction" : 1, "Social Interactions": 1}, \
        "Life Forms" : \
            {"Beings" : 1, "Beings, Animal" : 1, "General Characteristics" : 1, "Humans" : 1, "Plants" : 1}, \
        "Objects" : \
            {"Articles, Physical" : 1, "Atmosphere" : 1, "Buildings, Possessions" : 1, "Clothing" : 1, "Food and Drink" : 1, \
                "Machines" : 1, "Matter, Conditions of" : 1, "Matter, Divisions of" : 1, "Matter, Qualities of" : 1, "Tools" : 1, \
                    "Transportation" : 1}, \
        "The Planet" : \
            {"Geography" : 1, "Habitats" : 1, "Natural Resources" : 1, "Weather" : 1}, \
        "Qualities" : \
            {"Abstract" : 1, "Comparative" : 1, "Physical" : 1}, \
        "Senses" : \
            {"Aspects of Perception" : 1, "Auditory" : 1, "Olfactory" : 1, "Tactile" : 1, "Tasting" : 1, "Visual" : 1}, \
        "States" : \
            {"Abstract" : 1, "Cognitive" : 1, "Comparative" : 1, "Of Being" : 1, "Of Change" : 1, "Of Need or Achievement" : 1, \
                "Physical" : 1, "Spatial" : 1}, \
        "Weights and Measures" : \
            {"Mathematics" : 1, "Quanitifiers" : 1, "Time" : 1, "Wholeness or Division" : 1}
    }