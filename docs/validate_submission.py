#!/usr/bin/env python
"""Validate DIHARD III submission.

To validate a directory of system output RTTM files prior to submission, run:

    python validate_submission.py submission_dir

where ``submission_dir`` is the path to the submission directory, which  is
expected to have the structure:

- submission_dir/
- submission_dir/DH_EVAL_0001.rttm
- submission_dir/DH_EVAL_0002.rttm
- ...
- submission_dir/DH_EVAL_259.rttm

All detected errors in the structure of the directory (unexpected directories,
unepected files, or missing RTTM files) will be printed to STDOUT, one error
per line, each line beginning with the text ``ERROR``. For instance:

   ERROR: Missing RTTM file: DH_EVAL_0001.rttm
   ERROR: Missing RTTM file: DH_EVAL_0002.rttm
   ERROR: Unexpected file found: foo.rttm
   ERROR: Unexpected directory found: bar

If no output is produced, then the directory is ready to be archived and
submitted.

Alternately, you may run the script on the ``.zip``/``.tgz`` of the  directory
directly:

    python validate_submission.py some_dir.zip
    python validate_submission.py some_dir.tgz
"""
from __future__ import print_function
from __future__ import unicode_literals
import argparse
from pathlib import Path
import shutil
import sys
import tarfile
import tempfile
import zipfile


def error(msg):
    """Print error message ``msg`` to STDOUT."""
    print(f'ERROR: {msg}')


REF_RTTM_BNS = {f'DH_EVAL_{n:04}.rttm' for n in range(1, 260)}


def check_submission(submission_dir):
    """Validate directory structure of submission.

    Parameters
    ----------
    submission_dir : Path
        Path to directory of RTTM files.
    """
    # Check for unexpected files and directories.
    dir_bns = set()
    file_bns = set()
    for fpath in submission_dir.iterdir():
        bn = fpath.name
        if fpath.is_dir():
            dir_bns.add(bn)
        else:
            file_bns.add(bn)
    for dir_bn in sorted(dir_bns):
        error(f'Unexpected directory found: "{dir_bn}".')
    for file_bn in sorted(file_bns):
        if file_bn in REF_RTTM_BNS:
            continue
        error(f'Unexpected file found: "{file_bn}".')

    # Check that all expected RTTMs are present.
    missing_rttm_bns = REF_RTTM_BNS - file_bns
    for rttm_bn in sorted(missing_rttm_bns):
        error(f'Missing RTTM file: "{rttm_bn}".')


def main():
    parser = argparse.ArgumentParser(
        description='Validate directory structure of DIHARD III system '
                    'submission.',
        add_help=True)
    parser.add_argument(
        'submission', type=Path, help='path to submission')
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()

    tmp_dir = Path(tempfile.mkdtemp())
    try:
        if args.submission.is_dir():
            check_submission(args.submission)
        elif zipfile.is_zipfile(args.submission):
            with zipfile.ZipFile(args.submission, 'r') as f:
                f.extractall(tmp_dir)
            check_submission(Path(tmp_dir, args.submission.stem))
        elif tarfile.is_tarfile(args.submission):
            with tarfile.open(args.submission, 'r:*') as f:
                f.extractall(tmp_dir)
            check_submission(Path(tmp_dir, args.submission.stem))
        else:
            error(f'Unknown archive format: "{args.submission}".')
    finally:
        shutil.rmtree(tmp_dir)


if __name__ == '__main__':
    main()
