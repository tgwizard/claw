# -*- coding: utf-8 -*-

import os

STANDARD_REPLIES_DIR = os.path.join(os.path.dirname(__file__), "standard_replies")
STANDARD_REPLIES_FILENAMES = [
    os.path.join(STANDARD_REPLIES_DIR, f) for f in os.listdir(STANDARD_REPLIES_DIR)
    if f.endswith('.eml')
]

with open("tests/fixtures/reply-quotations-share-block.eml") as f:
    REPLY_QUOTATIONS_SHARE_BLOCK = f.read()

with open("tests/fixtures/OLK_SRC_BODY_SECTION.html") as f:
    OLK_SRC_BODY_SECTION = f.read()

with open("tests/fixtures/reply-separated-by-hr.html") as f:
    REPLY_SEPARATED_BY_HR = f.read()
