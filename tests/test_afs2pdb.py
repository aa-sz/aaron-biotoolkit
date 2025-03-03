import os
import tempfile
import pytest
from click.testing import CliRunner
from aaron_biotoolkit.afs2pdb import main as afs2pdb_main

# Get the path to the tests directory
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_ZIP = os.path.join(TEST_DIR, 'test.zip')

def test_afs2pdb_with_output():
    runner = CliRunner()
    with tempfile.NamedTemporaryFile(suffix='.pdb') as temp_output:
        result = runner.invoke(afs2pdb_main, [
            '--input', TEST_ZIP, 
            '--output', temp_output.name
        ])
        assert result.exit_code == 0
        assert os.path.exists(temp_output.name)
        assert os.path.getsize(temp_output.name) > 0

def test_afs2pdb_default_output():
    runner = CliRunner()
    # Expected output file path - this should be based on TEST_ZIP path
    expected_output = os.path.splitext(TEST_ZIP)[0] + '.pdb'
    
    try:
        # Run with default output
        result = runner.invoke(afs2pdb_main, ['--input', TEST_ZIP])
        assert result.exit_code == 0
        
        # Check that default output file was created
        assert os.path.exists(expected_output)
        assert os.path.getsize(expected_output) > 0
    finally:
        # Clean up default output file if it was created
        if os.path.exists(expected_output):
            os.remove(expected_output)

def test_afs2pdb_invalid_input():
    runner = CliRunner()
    nonexistent_path = os.path.join(TEST_DIR, 'nonexistent.zip')
    result = runner.invoke(afs2pdb_main, ['--input', nonexistent_path])
    assert result.exit_code != 0