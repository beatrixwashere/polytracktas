## polytracktas

welcome! polytrack tasing is now at a state where it is possible to make tases for levels, albeit with some limitations as of right now. this repo stores useful scripts and tas records, and has plenty of guides to help you as you're tasing.

---

## setup

1) make a folder on your computer, preferably named something like `polytracktas`
2) make a file in that folder named `polytrack.tas`, which will be your main tas file
3) copy the `tas_to_ghost.py` script from the `scripts` folder in the repo and put it into your folder

---

## making tases

`polytrack.tas` is a plaintext file, and it is used by `tas_to_ghost.py` to generate ghost encodes for playback. the tas format is as follows:

```
frame1,(wasd)
frame2,(wasd)
...
frameN,(wasd)
# comment

# frame# represents the frame an input is pressed on, and (wasd) is the keys pressed on that frame

# example:
0,w
500,wd
1200,sd
1500,wa
2000,w
```

once you're done writing inputs, run `tas_to_ghost.py` to generate the ghost.

---

## playing tases

__[web]__
1) open the [web version](https://www.kodub.com/apps/polytrack) of polytrack
2) go to `dev tools > application > local storage > https://app-polytrack.kodub.com`
3) find the value that corresponds to the track you made the tas for
4) double click the value to edit it
5) replace the ghost in the value with the one you made and press enter
6) open the track and press accel/brake to start the ghost

__[standalone guide coming soon]__

since tasing requires a lot of trail and error, you'll have to tweak your inputs after running the tas in order to keep on improving it.

---

## conclusion

if you have any extra questions, feel free to ask in #tas-polytrack in the server. everything above is for getting the tools set up, but there are extra guides in the wiki section of this repo for the tasing process and optimization. i'll add/update important scripts posted in #tas-research, and update tas records from #tas-improvements. with all that being said, have fun tasing!
