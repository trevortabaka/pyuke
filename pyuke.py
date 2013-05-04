#! /usr/bin/env python

# pyUke
# by Trevor Tabaka

import itertools

#######################################
# Constants (DO NOT MODIFY)
#######################################
# notes
notes = [['a'], ['as','a#','bb'], ['b'], ['c'], ['cs','c#','db'], ['d'], ['ds','d#','eb'], ['e'], ['f'], ['fs','f#','gb'], ['g'], ['gs','g#','ab']]
# tuning configurations
reentrant_c = ['g','C','E','A'] # re-entrant C (standard) uke
reentrant_d = ['a','D','F#','B'] # re-entrant D uke
low_g = ['G','C','E','A'] # low-G uke (same as re-entrant C for this app) 
low_a = ['A','D','F#','B'] # low-A uke (same as re-entrant D for this app)
slack_key = ['g','C','E','G'] # slack-key uke
baritone = ['D','G','B','E'] # baritone uke
guitar = ['E','A','D','G','B','E'] # guitar (standard)
#######################################


#######################################
# Settings - modify if desired
#######################################
# highest fret position
highestFret = 19
# lowest fret position; 0 means open string
lowestFret = 0
# tuning
strings = reentrant_c
# display option - number of chords to print per row
chordsPerRow = 10
#######################################


#######################################
def formatFret(fret):
	return "-" + format(fret) + "-"

def format(fret):
	if fret < 10:
		return "-" + str(fret)
	else:
		return str(fret)

def formatEmpty():
	return "----"

def findNoteIndex(note):
	for group in notes:
		if note.lower() in group:
			return notes.index(group)

def findFrets(line, note):
	return line[[y[0] for y in line].index(note)][1]
########################################


########################################
strings.reverse() # to make looping more straightforward

# loop until valid notes have been entered
while (True):
	inputNote = raw_input("Enter note(s): ")
	targetNotes = inputNote.split(" ")

	invalidNote = False
	for note in targetNotes:
		if findNoteIndex(note) == None:
			print "Invalid note: " + note
			invalidNote = True
			break
	if invalidNote == False:
		break

print # start on a newline so that if input is piped in, the tabs are printed correctly

targetNotes.sort() # sort so that chord combos show up the same every time (without this you'd get a different order for "b d" and "d b")

result = [[] for x in range(len(strings))]

# find all the frets for each entered target note
for note in targetNotes:
	targetNoteIndex = findNoteIndex(note)

	# go string by string
	currentStringIndex = 0
	for string in strings:
		stringRoot = findNoteIndex(string)
		octave = 0;
		fret = 0;

		frets = []

		# walk the fretboard to find all occurences of the target note on this string
		while fret <= highestFret:
			fret = targetNoteIndex - stringRoot + 12 * octave # 12 steps to get to the next octave
			octave = octave + 1
			# make sure the fret exists!
			if fret in range(lowestFret, highestFret):
				frets.append(fret)

		# keep track of the note and fret(s) by string
		result[currentStringIndex].append((note, frets))
		currentStringIndex = currentStringIndex + 1

# find every permutation for the number of notes entered - these are just raw permutations, not related to notes yet
indexPermutations = list(itertools.permutations(range(len(strings)), len(targetNotes)))

linesToPrint = [[] for x in range(len(strings))]

# use the permutations and results from finding all frets to produce chords
for permutation in indexPermutations:
	# pair each index in the permutation with an actual note
	indexNotePairs = zip(permutation, targetNotes)

	tuples = []
	for indexNotePair in indexNotePairs:
		index = indexNotePair[0]
		note = indexNotePair[1]
		tuples.append((index, findFrets(result[index], note)))

	chords = list(itertools.product(*(x[1] for x in tuples)))
	
	# add the tabs into a list for each line (string)
	for line in range(len(strings)):
		if line in permutation:
			for chord in chords:
				linesToPrint[line].append(formatFret(chord[permutation.index(line)]))
		else:
			for x in range(len(chords)):
				linesToPrint[line].append(formatEmpty())

# print the tabs to the console
for x in range(len(linesToPrint[0]) / chordsPerRow + 1):
	for line in linesToPrint:
		print "    ".join(line[x*chordsPerRow:(x+1)*chordsPerRow])
	print
