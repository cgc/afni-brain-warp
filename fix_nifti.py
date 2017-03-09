'''
This script addresses an issue with some nifti files created by Vistasoft.

By default, Vistasoft nifti files are created with sform_code and qform_code
values of 2 [0], which are interpreted as "aligned to a template" by AFNI code.
Because these files are interpreted as "aligned", they will crash this brain
warp script. fix_nifti.py sets these values to 1 to avoid this issue.

0: https://github.com/vistalab/vistasoft/blob/8298ab/fileFilters/nifti/niftiCreate.m#L172-L173
'''

import nibabel as nib
import sys
import os
import subprocess

if len(sys.argv) != 3:
    print '''
Usage: fix_nifti.py <input_file> <output_file>

Fixes some nifti headers that are incompatible with this afni brain warping
routine. To see more details, see the comments in this script.
'''
    sys.exit(1)

input_file, output_file = sys.argv[1:]

if not os.path.exists(input_file):
    print 'input file {} does not exist'.format(input_file)
    sys.exit(1)

if os.path.exists(output_file):
    print 'warning: output file {} exists and will be overwritten'.format(
        output_file)

image = nib.load(input_file)

incorrect_headers = False
if image.header['descrip'] == 'VISTASOFT':
    for key in ['qform_code', 'sform_code']:
        if image.header[key] == 2:
            incorrect_headers = True
            image.header[key] = 1

    if incorrect_headers:
        print (
            'warning: native image input headers suggest it might be '
            'mistakenly marked as aligned by vistasoft. going to fix all headers')

        # XXX assert that sform is all 1s and != qform
        # While the pixdim and qform of these images are ok, the sform is incorrect.
        # We will overwrite the sform with the qform.
        aff = image.header.get_qform()
        # force affine and sform to qform so we can reset. Only setting
        # one or the other might not work.
        # see more details here: https://github.com/nipy/nibabel/pull/90
        image.affine[:] = aff
        image.header.set_sform(aff)

nib.save(image, output_file)

if incorrect_headers:
    # XXX assert that image is currently LPI?
    subprocess.check_call(['3drefit', '-orient', 'LAI', output_file])
