=============================
brc - Bulk recode audio files
=============================

-----
Usage
-----

.. code-block:: bash

    $ brc -h
    usage: brc [-h] [-x] [-t T] [-q Q] [-np] [-o O] [-i I] input [output]

    Transcode directory trees

    positional arguments:
      input       <old directory>
      output      <new directory>

    optional arguments:
      -h, --help  show this help message and exit
      -x          Overwrite non-empty output files
      -t T        Transcoding processes
      -q Q        FFmpeg output quality
      -np         Don't print progress
      -o O        Output format
      -i I        Extra input format

----------------
Notable features
----------------
- Implicit directory name

brc /path/to/album This will create a new directory which is the basename of the first argument, in this case album

------
Thanks
------
Thanks to @toddfoster who contributed to the predecessor of this program (https://github.com/adisbladis/flac2ogg/)
