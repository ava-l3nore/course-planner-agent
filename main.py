import parse
import walker as walk

def main():
    # main pages
    ACADEMIC_REGULATIONS = "https://catalog.cofc.edu/content.php?catoid=32&navoid=1442"
    FYE = "https://catalog.cofc.edu/content.php?catoid=32&navoid=1571"
    FOUNDING_DOCS = "https://catalog.cofc.edu/content.php?catoid=32&navoid=1465"
    MUGC = "https://catalog.cofc.edu/content.php?catoid=32&navoid=1464"
    GEN_EDS = "https://catalog.cofc.edu/content.php?catoid=32&navoid=1461"
    COURSE_DESC = "https://catalog.cofc.edu/content.php?catoid=32&navoid=1456"

    pages = {"academic_regulations": ACADEMIC_REGULATIONS, "fye": FYE, "founding_docs": FOUNDING_DOCS, "mugc": MUGC, "gen_eds": GEN_EDS, "course_desc": COURSE_DESC}
    '''
    for page, url in pages.items():

        soup = parse.parse(page, url, "acalog-block-n1")

        walk.walker(soup)
    '''
    
    # computing school majors
    CS_BS = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6311"
    CITA_ART = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6312"
    CITA_DIG_MEDIA = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6444"
    CITA_GAME_DEV = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6468"
    CITA_MUSIC = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6313"
    CITA_THEATRE = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6314"
    CIS = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6309"
    CS_BA = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6310"
    DATA_SCI = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6498"
    SWEN = "https://catalog.cofc.edu/preview_program.php?catoid=32&poid=6500"

    majors = {"cs_bs": CS_BS, "cita_art": CITA_ART, "cita_dig_media": CITA_DIG_MEDIA, "cita_game_dev": CITA_GAME_DEV, "cita_music": CITA_MUSIC, "cita_theatre": CITA_THEATRE, "cis": CIS, "data_sci": DATA_SCI, "swen": SWEN, "cs_ba": CS_BA}

    for major, url in majors.items():

        soup = parse.parse(major, url, "acalog-course")

        walk.walker(soup)


main()