from glob import glob
import sys
import os

## target directory
dir = sys.argv[1]

## thumbnail size in pixels
size = sys.argv[2] if len(sys.argv) > 2 else "100"

## list of pdfs
pdfs = glob(f"{dir}*.pdf")

input("""

  __ _     _ _    ____ ___          _         ___    __
 /__|_|\ ||_|_) /\ ||_  ||_|| ||\/||_)|\ | /\  |  | (_
 \_||_| \||_| \/--\||_  || ||_||  ||_)| \|/--\_|_ |_ _)

Strike a key when ready ...

""")


for pdf in pdfs:
    ## determine portrait or landscape
    stream = os.popen(f"identify -format \"%wx%h\" {pdf}[0]")
    w, h = stream.read().split("x")
    portrait = h >= w

    ## generate thumbnail
    if portrait:
        os.system(f"convert -thumbnail x{size} -background white -alpha remove {pdf}[0] {pdf}.jpg")
    else:
        os.system(f"convert -thumbnail {size}x -background white -alpha remove {pdf}[0] {pdf}.jpg")
    print(f"Generated {pdf}.jpg!")
