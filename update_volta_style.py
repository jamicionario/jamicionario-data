#!/usr/bin/env python3

import os
import shutil
import tempfile
import zipfile

#!SEARCH = "<voltaLineStyle>dashed</voltaLineStyle>"
#!REPLACE = "<voltaLineStyle>solid</voltaLineStyle>"

#!SEARCH = "<voltaLineWidth>0</voltaLineWidth>"
#!REPLACE = "<voltaLineWidth>0.06</voltaLineWidth>"

#!SSEARCH = "<voltaLineWidth>0.04</voltaLineWidth>"
#!SREPLACE = "<voltaLineWidth>0.06</voltaLineWidth>"

#!SEARCH = "<voltaLineWidth>0.04</voltaLineWidth>"
#!REPLACE = "<voltaLineWidth>0.06</voltaLineWidth>"



#!SEARCH = '<metaTag name="dance geometry">Single line</metaTag>'
#!REPLACE = '<metaTag name="dance geometry">Single Line</metaTag>'

#!SEARCH = '<metaTag name="dance geometry">Quadrille</metaTag>'
#!REPLACE = '<metaTag name="dance geometry">Quartet</metaTag>'

#!SEARCH = '<metaTag name="type of dance">Bransle,De Noirmoutier</metaTag>'
#!REPLACE = '<metaTag name="type of dance">Bransle,De l´Épine</metaTag>'pwd

#!SEARCH = '<metaTag name="type of dance">'
#!REPLACE = '<metaTag name="Country"></metaTag><metaTag name="type of dance">'


SEARCH = '<metaTag name="Country"></metaTag>'

#!REPLACE = '<metaTag name="Country">Armenia</metaTag>'
#!REPLACE = '<metaTag name="Country">Austria</metaTag>'
#!REPLACE = '<metaTag name="Country">Belgium</metaTag>'
#!REPLACE = '<metaTag name="Country">Bolivia</metaTag>'
#!REPLACE = '<metaTag name="Country">Bosnia</metaTag>'
#!REPLACE = '<metaTag name="Country">Brazil</metaTag>'
#!REPLACE = '<metaTag name="Country">Bulgaria</metaTag>'
#!REPLACE = '<metaTag name="Country">Cape Verde</metaTag>'
#!REPLACE = '<metaTag name="Country">Denmark</metaTag>'
#!REPLACE = '<metaTag name="Country">England</metaTag>'
#!REPLACE = '<metaTag name="Country">Estonia</metaTag>'
#!REPLACE = '<metaTag name="Country">France</metaTag>'
#!REPLACE = '<metaTag name="Country">Germany</metaTag>'
#!REPLACE = '<metaTag name="Country">Greece</metaTag>'
#!REPLACE = '<metaTag name="Country">Ireland</metaTag>'
#!REPLACE = '<metaTag name="Country">Israel</metaTag>'
#!REPLACE = '<metaTag name="Country">Italy</metaTag>'
#!REPLACE = '<metaTag name="Country">Lithuania</metaTag>'
#!REPLACE = '<metaTag name="Country">Macedonia</metaTag>'
#!REPLACE = '<metaTag name="Country">Moldavia</metaTag>'
#!REPLACE = '<metaTag name="Country">Netherlands</metaTag>'
#!REPLACE = '<metaTag name="Country">New Zealand</metaTag>'
#!REPLACE = '<metaTag name="Country">Poland</metaTag>'
#!REPLACE = '<metaTag name="Country">Portugal</metaTag>'
#!REPLACE = '<metaTag name="Country">Romenia</metaTag>'
#!REPLACE = '<metaTag name="Country">Russia</metaTag>'
#!REPLACE = '<metaTag name="Country">Scotland</metaTag>'
#!REPLACE = '<metaTag name="Country">Serbia</metaTag>'
#!REPLACE = '<metaTag name="Country">Spain</metaTag>'
#!REPLACE = '<metaTag name="Country">Sweden</metaTag>'
#!REPLACE = '<metaTag name="Country">Turkey</metaTag>'
#!REPLACE = '<metaTag name="Country">U.S.A.</metaTag>'
#!REPLACE = '<metaTag name="Country">Ukraine</metaTag>'
#!
REPLACE = '<metaTag name="Country">Venezuela</metaTag>'

#!SEARCH = 'Discografia'
#!REPLACE = 'Disc.'

#!SEARCH = 'Notas'
#!REPLACE = 'Notes'

updated = 0
skipped = 0

for root, _, files in os.walk("."):
    for filename in files:
        if not filename.lower().endswith(".mscz"):
            continue

        mscz = os.path.join(root, filename)

        try:
            with tempfile.TemporaryDirectory() as tmpdir:

                # Extract archive
                with zipfile.ZipFile(mscz, "r") as zin:
                    zin.extractall(tmpdir)

                candidate_files = []
                style_file = os.path.join(tmpdir, "score_style.mss")
                if os.path.exists(style_file):
                    candidate_files.append(style_file)

                for extracted in os.listdir(tmpdir):
                    if extracted.lower().endswith(".mscx"):
                        candidate_files.append(os.path.join(tmpdir, extracted))

                if not candidate_files:
                    print(f"SKIP (no score_style.mss or .mscx): {mscz}")
                    skipped += 1
                    continue

                matched_file = None
                for candidate in candidate_files:
                    with open(candidate, "r", encoding="utf-8") as f:
                        text = f.read()
                    if SEARCH in text:
                        matched_file = candidate
                        text = text.replace(SEARCH, REPLACE)
                        with open(candidate, "w", encoding="utf-8") as f:
                            f.write(text)
                        break

                if matched_file is None:
                    print(f"SKIP (already updated or different): {mscz}")
                    skipped += 1
                    continue

                # Backup original
                shutil.copy2(mscz, mscz + ".bak")

                # Rebuild archive
                new_zip = mscz + ".tmp"

                with zipfile.ZipFile(new_zip, "w", compression=zipfile.ZIP_DEFLATED) as zout:
                    for folder, _, extracted_files in os.walk(tmpdir):
                        for extracted in extracted_files:
                            full = os.path.join(folder, extracted)
                            rel = os.path.relpath(full, tmpdir)
                            zout.write(full, rel)

                shutil.move(new_zip, mscz)

                print(f"UPDATED: {mscz}")
                updated += 1

        except Exception as e:
            print(f"ERROR: {mscz}")
            print(e)

print()
print(f"Updated : {updated}")
print(f"Skipped : {skipped}")
print("Done.")