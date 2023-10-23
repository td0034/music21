import music21
score = music21.converter.parse('./TZ3.mid')
score.plot('histogram', 'pitchClass', xHideUnused=False, yAxisLabel='Number of PitchClasses')
score.plot('histogram', 'pitch', xHideUnused=False, yAxisLabel='Number of Pitches')
key = score.analyze('key')
print(key.tonic.name, key.mode)  