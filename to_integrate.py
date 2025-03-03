#!/usr/bin/env python3
import zipfile
import gemmi
import sys

def convert_mmCIF_to_PDB_from_zip(zip_path, output_pdb):
    # Open the ZIP archive
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        # Look for an mmCIF file containing '_model_0.cif' in its name
        cif_filename = None
        for name in zipf.namelist():
            if '_model_0.cif' in name:
                cif_filename = name
                break

        if cif_filename is None:
            print("No mmCIF file with '_model_0.cif' found in the zip archive.")
            return

        # Read the mmCIF content directly into memory (without extracting to disk)
        cif_bytes = zipf.read(cif_filename)
        cif_content = cif_bytes.decode('utf-8')

    # Use Gemmi to read the mmCIF content from the string.
    # gemmi.cif.read_string returns a Document object.
    doc = gemmi.cif.read_string(cif_content)

    block = doc.sole_block()
    # Convert the block to a Structure object.
    structure = gemmi.make_structure_from_block(block)

    # Write the structure to a PDB file.
    structure.write_pdb(output_pdb)
    print(f"Converted '{cif_filename}' from {zip_path} to '{output_pdb}'.")

def main():
    if len(sys.argv) != 3:
        print(f'Usage: afs2pdb <zipfile> <output_pdb>')
    else:
        zip_path = sys.argv[1]
        output_pdb = sys.argv[2]
        convert_mmCIF_to_PDB_from_zip(zip_path, output_pdb)

if __name__ == '__main__':
    main()
