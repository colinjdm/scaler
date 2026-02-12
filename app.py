#from flask import Flask, redirect, render_template, request


#app = Flask(__name__)

scales_database = {
    # C
    'C_major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
    'C_natural_minor': ['C', 'D', 'D#', 'F', 'G', 'G#', 'A#'],
    'C_harmonic_minor': ['C', 'D', 'D#', 'F', 'G', 'G#', 'B'],
    'C_melodic_minor': ['C', 'D', 'D#', 'F', 'G', 'A', 'B'],

    # C#
    'C#_major': ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C'],
    'C#_natural_minor': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
    'C#_harmonic_minor': ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'C'],
    'C#_melodic_minor': ['C#', 'D#', 'E', 'F#', 'G#', 'A#', 'C'],

    # D
    'D_major': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#'],
    'D_natural_minor': ['D', 'E', 'F', 'G', 'A', 'A#', 'C'],
    'D_harmonic_minor': ['D', 'E', 'F', 'G', 'A', 'A#', 'C#'],
    'D_melodic_minor': ['D', 'E', 'F', 'G', 'A', 'B', 'C#'],

    # D#
    'D#_major': ['D#', 'F', 'G', 'G#', 'A#', 'C', 'D'],
    'D#_natural_minor': ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'C#'],
    'D#_harmonic_minor': ['D#', 'F', 'F#', 'G#', 'A#', 'B', 'D'],
    'D#_melodic_minor': ['D#', 'F', 'F#', 'G#', 'A#', 'C', 'D'],

    # E
    'E_major': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#'],
    'E_natural_minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D'],
    'E_harmonic_minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D#'],
    'E_melodic_minor': ['E', 'F#', 'G', 'A', 'B', 'C#', 'D#'],

    # F
    'F_major': ['F', 'G', 'A', 'A#', 'C', 'D', 'E'],
    'F_natural_minor': ['F', 'G', 'G#', 'A#', 'C', 'C#', 'D#'],
    'F_harmonic_minor': ['F', 'G', 'G#', 'A#', 'C', 'C#', 'E'],
    'F_melodic_minor': ['F', 'G', 'G#', 'A#', 'C', 'D', 'E'],

    # F#
    'F#_major': ['F#', 'G#', 'A#', 'B', 'C#', 'D#', 'F'],
    'F#_natural_minor': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'E'],
    'F#_harmonic_minor': ['F#', 'G#', 'A', 'B', 'C#', 'D', 'F'],
    'F#_melodic_minor': ['F#', 'G#', 'A', 'B', 'C#', 'D#', 'F'],

    # G
    'G_major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
    'G_natural_minor': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F'],
    'G_harmonic_minor': ['G', 'A', 'A#', 'C', 'D', 'D#', 'F#'],
    'G_melodic_minor': ['G', 'A', 'A#', 'C', 'D', 'E', 'F#'],

    # G#
    'G#_major': ['G#', 'A#', 'C', 'C#', 'D#', 'F', 'G'],
    'G#_natural_minor': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'F#'],
    'G#_harmonic_minor': ['G#', 'A#', 'B', 'C#', 'D#', 'E', 'G'],
    'G#_melodic_minor': ['G#', 'A#', 'B', 'C#', 'D#', 'F', 'G'],

    # A
    'A_major': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'],
    'A_natural_minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'A_harmonic_minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G#'],
    'A_melodic_minor': ['A', 'B', 'C', 'D', 'E', 'F#', 'G#'],

    # A#
    'A#_major': ['A#', 'C', 'D', 'D#', 'F', 'G', 'A'],
    'A#_natural_minor': ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'G#'],
    'A#_harmonic_minor': ['A#', 'C', 'C#', 'D#', 'F', 'F#', 'A'],
    'A#_melodic_minor': ['A#', 'C', 'C#', 'D#', 'F', 'G', 'A'],

    # B
    'B_major': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#'],
    'B_natural_minor': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'],
    'B_harmonic_minor': ['B', 'C#', 'D', 'E', 'F#', 'G', 'A#'],
    'B_melodic_minor': ['B', 'C#', 'D', 'E', 'F#', 'G#', 'A#'],
}


def main():
    #if request.method == "GET":
    #if request.method == "POST":

    #inpute notes and save them to a string
    user_notes = input("Notes?")

    #split notes into list
    notes = user_notes.split(',')
    scales = matching(notes)
    print(scales)


def matching(notes):

    # define empty list to append matching scales to
    possible_scales = []

    for key, value in scales_database.items():
        # check to see if the requested notes are contained within the current scale
        
        if set(notes).issubset(value):
            # append the scale to the empty list
            possible_scales.append(key)

    return(possible_scales)


if __name__ == "__main__":
    main()