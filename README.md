### AFNI Brain Warp

This Flywheel gear warps the `warp_target` nifti image from standard-space into native-space. The `standard` and `native` reference images are nifti files that are inputs to this gear.

The `align.csh` script comes from the [D99 Macaque Atlas AFNI scripts](https://afni.nimh.nih.gov/pub/dist/atlases/macaque/macaqueatlas_1.2a/AFNI_scripts/).

#### next steps
- ensure `warp_target` processing works for non-atlas data (if it doesn't, tuck segmentation functionality under a flag)
- consider adding a parameter that defines whether warp target is in standard- or native-space (although merely switching the standard and native images suffices to warp a target native-space target to standard-space)
- expose parameters to disable or configure `3dQwarp`'s `-workhard` (which makes warping slower and more accurate) and enable `-duplo` (which makes warping faster and less accurate)
    - parameters like `-maxlev` and `minpatch` can also affect speed/accuracy of warping.
- should warped `*_aniso*` files be copied to output?
