from pptx import Presentation
import json

DIR = 'C:/dev/text2ucgppt/resources'
FILENAME = 'UCG-Hymnal-Lyrics-windows.pptx'
FILENAME_TEST = 'UCG-Hymnal-Lyrics-windows_TEST.pptx'

ABS_PATH = DIR+'/'+FILENAME_TEST

HYMN_SLIDE_JSON_PATH = '../resources/hymn_slide.json'

TITLE = 0
VERSE_SLIDE = 1
VERSE_SLIDE_END = 2
BLANK_SLIDE = 3
EMPTY_SLIDE = 4

NUM_OF_SLIDES = 2878

with open(HYMN_SLIDE_JSON_PATH) as json_file:
    hymn_slide_index = json.load(json_file)

print(hymn_slide_index)

prs = Presentation(ABS_PATH)
#prs.save(ABS_PATH)


#slide_layout = prs.slide_layouts[TITLE]
#slide = prs.slides.add_slide(slide_layout)


slides = prs.slides

#for slide in slides:
slide = slides[0]
shape = slide.shapes[0] # always the 0th shape
if shape.has_text_frame:
    text_frame = shape.text_frame
    print(len(text_frame.paragraphs))
    text = text_frame.paragraphs[0].text # only ever one paragraph
    print('FANCY TEXT: ', text)

    shape.text = 'TEST TEST new text this is a super cool test'
    text = text_frame.paragraphs[0].text
    print('FANCY TEXT neu: ', text)
else:
    print('NO TEXT')


if len(slides) != NUM_OF_SLIDES:
    print('!!! WARNING !!! Number of slides changed, not saving!!! Current: {}, Should: {}'.format(len(slides), NUM_OF_SLIDES))
else:
    prs.save(ABS_PATH)



