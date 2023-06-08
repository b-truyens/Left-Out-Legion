import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage

# Define the piano piece inspired by Mozart
piano_piece = [
    [0, 4, 7],  # C Major chord (I)
    [5, 9, 12],  # F Major chord (IV)
    [7, 11, 14],  # G Major chord (V)
    [0, 4, 7],  # C Major chord (I)
    [2, 5, 9],  # D Minor chord (ii)
    [7, 11, 14],  # G Major chord (V)
    [5, 9, 12],  # F Major chord (IV)
    [0, 4, 7],  # C Major chord (I)
]


# Create a new MIDI file
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Set the tempo (adjust as needed)
tempo = 600000  # Microseconds per beat (100 BPM)
track.append(MetaMessage('set_tempo', tempo=tempo))

# Define the time per beat based on the tempo
ticks_per_beat = mid.ticks_per_beat
ticks_per_bar = ticks_per_beat * 4

# Function to convert note value to MIDI note number
def note_to_midi(note):
    return note + 60

# Iterate over the piano piece and add the chords to the MIDI track
for chord in piano_piece:
    for note in chord:
        note_number = note_to_midi(note)
        track.append(Message('note_on', note=note_number, velocity=64, time=0))
    for note in chord:
        note_number = note_to_midi(note)
        track.append(Message('note_off', note=note_number, velocity=64, time=ticks_per_bar))

# Save the MIDI file
mid.save('mozart_piece.mid')




