# python-read-text

---

## read text from image

read from selected area

`pip install opencv-python pytesseract`

## copy text from pdf

copy text from selected area

`pip install pymupdf pdf-annotate`

-----
#### pdf to image command

```bash

sudo pacman -S poppler

# pdftoppm -<image_format> <pdf_filename> <image_name>

pdftoppm -png test.pdf output 

# Where N specifies the first-page number to covert and -l N for the last page to convert.
# pdftoppm -<image_format> -f N -l N <pdf_filename> <image_name>

pdftoppm -png -f 10 -l 15 test.pdf output 

```

#### change image format (png to jpeg)

```bash

sudo pacman -S imagemagick

mogrify -format jpg MY-PNG-FILE.png

```
