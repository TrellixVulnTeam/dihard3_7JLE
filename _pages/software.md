---
title: ""
permalink: /software.html
classes: wide
---

# Scoring

The official scoring tool is maintained as a [github repo](https://github.com/nryant/dscore) (v1.1.0). To obtain metrics for the full DEV, the corresponding
command would be:

    $ python score.py -u dev_dir/data/uem_scoring/full/all.uem -r dev_dir/data/rttm/*.rttm -s sys_output/*.rttm


where:

* *dev_dir*  --  path to root of the DIHARD III development release
  (LDC2020E12; e.g. */data/corpora/LDC/LDC2020E12_Third_DIHARD_Challenge_Development_Data*
* *sys_output*  --  path to directory containing the RTTM files output by your system

The overall and per-file results for DER and JER (and many other metrics) for
the full DEV set will be printed to STDOUT as a table. Similarly, to obtain
metrics for the core DEV set:

    $ python score.py -u dev_dir/data/uem_scoring/core/all.uem -r dev_dir/data/rttm/*.rttm -s sys_output/*.rttm

For additional details about scoring tool usage, please consult the documentation for the [github repo](https://github.com/nryant/dscore).


# Baseline systems

* Baseline systems for performing speech activity detection along with
  recipes for using these systems on the development and evaluation sets
  will be provided by the organizers.
* Once available the baselines, an announcement will be made to the mailing
  list and instructions for accessing the baselines posted here.
