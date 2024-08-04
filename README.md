# MusicTyper
 be able to make music more algoritmically

## Keywords:
- song < title >
- by < author >
- output < path > ( wav | mp3 | midi )
- tempo < bpm >
- duration < time >
- time < top > < bottom >
- open < path >
- sound < variable > < sound >
- effect < variable > < operation >
- alter < variable > < effect >
- pure ( sine | square | saw | triangle ) [ amplitude ] [ frequency ] [ phase ]
- number < variable > < number >
- sample < samplerate >
- pitch < sound > < to > [ from ]
- pitchrelative ( half | whole ) < sound > < amount >

## Units
#, $, and % represent sharp, flat, and natural respectively.
- ### Units of time:
 - samples: number of sound wave samples, usually 44100 per second ( 250sm )
 - seconds ( 3s )
 - minutes ( 3m )
 - measures: some multiple of beats, depending on time signature ( 20me )
 - song fractions: fractions of the total length of the song ( 1/2fr or 0.5fr is half of the song )
 - beats ( 3b )
- ### Units of frequency:
 - hertz ( 256hz )
 - scale degree: from the base of whatever key signature the song is in ( in C major, 0sd is middle C, 1sd is D, and -1sd is B )
 - note name: simple note name ( C4n, C4#n, D2#n, A5$n, etc. )
 - absolute degree: from middle C ( 0ad is middle C, 0.5ad is C#, -1ad is B, etc. )
 - half steps: from middle C, but the number represents the number of half-steps ( 0hs is middle C, 1hs is C#, -1ad is B, etc. )