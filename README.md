pyuke
=====
_pronounced "puke"_

pyUke is a command line tool to convert standard musical notes or chords to tablature form for the ukulele. Its intention is not to convert, say, an entire song to tablature form, but instead as a reference tool for note and chord variations. Or it can be used simply to get more familiar with the fretboard.

For example, pyUke can be used to show all ways to play a D# note on a standard tuned uke:

    $ ./pyuke.py 
    Enter note(s): d#
    
    --6-    -18-    ----    ----    ----    ----
    ----    ----    -11-    ----    ----    ----
    ----    ----    ----    --3-    -15-    ----
    ----    ----    ----    ----    ----    --8-

or it can be used to show all possible fingerings for a chord made of the notes B and D:

    $ ./pyuke.py 
    Enter note(s): b d
    
    --2-    -14-    --2-    --2-    -14-    -14-    --2-    -14-    --5-    -17-
    -10-    -10-    ----    ----    ----    ----    ----    ----    --7-    --7-
    ----    ----    --2-    -14-    --2-    -14-    ----    ----    ----    ----
    ----    ----    ----    ----    ----    ----    --7-    --7-    ----    ----
    
    ----    ----    ----    --5-    -17-    ----    ----    --5-    -17-    --5-
    --7-    --7-    --7-    ----    ----    -10-    ----    ----    ----    ----
    --2-    -14-    ----    -11-    -11-    -11-    -11-    ----    ----    ----
    ----    ----    --7-    ----    ----    ----    --7-    --4-    --4-    -16-
    
    -17-    ----    ----    ----    ----    ----    ----
    ----    -10-    -10-    ----    ----    ----    ----
    ----    ----    ----    --2-    -14-    --2-    -14-
    -16-    --4-    -16-    --4-    --4-    -16-    -16-

A few simple settings are modifiable, including the lowest and highest frets (for capos or variably sized necks), tuning (reentrant_c (standard), reentrant_d, low_g, low_a, slack_key, baritone, guitar), and output formatting

## Requires
* Python, tested on 2.7.1

## License

    The MIT License (MIT)
    
    Copyright (c) 2013 Trevor Tabaka
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
