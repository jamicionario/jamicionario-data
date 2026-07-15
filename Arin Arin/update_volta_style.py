#!/usr/bin/env python3

import os
import shutil
import tempfile
import zipfile

SEARCH = "<voltaLineStyle>dashed</voltaLineStyle>"
REPLACE = "<voltaLineStyle>solid</voltaLineStyle>"

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

                style_file = os.path.join(tmpdir, "score_style.mss")

                if not os.path.exists(style_file):
                    print(f"SKIP (no score_style.mss): {mscz}")
                    skipped += 1
                    continue

                with open(style_file, "r", encoding="utf-8") as f:
                    text = f.read()

                if SEARCH not in text:
                    print(f"SKIP (already updated or different): {mscz}")
                    skipped += 1
                    continue

                text = text.replace(SEARCH, REPLACE)

                with open(style_file, "w", encoding="utf-8") as f:
                    f.write(text)

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