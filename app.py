#from flask import Flask, redirect, render_template, request


#app = Flask(__name__)


def main():
    #if request.method == "GET":
    #if request.method == "POST":

    #inpute notes and save them to a string
    user_notes = input("Notes?")

    #split notes into list
    notes = user_notes.split(',')
    scales = matching(notes)
    #print the requested notes
    #print(notes)

def matching(notes):
    scales_database = {
        'C Major' : ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'G Major' : ['G', 'A', 'B', 'C', 'D', 'E', 'F#']
    }

    possible_scales = []
    #print(f"Notes: {notes}")

    for key, value in scales_database.items():
        # go to the next scale
        #print(f"value_list: {value_list}")
        found_match = False

        for item in value:
            # go through each note in that scale

            for i in notes:
                # print(f"   Comparing: {i} with {item}")
                if i == item:
                    print(f"Note {item} is in {key}")
                    break
    return




if __name__ == "__main__":
    main()