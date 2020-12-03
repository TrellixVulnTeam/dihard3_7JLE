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

We provide baseline systems for performing speech activity detection (SAD) and
diarization as well as recipes for using these systems to reproduce baseline
results for the DIHARD III development and evaluation sets. The SAD baseline uses a TDNN model and is based on Kaldi's [Aspire recipe](https://github.com/kaldi-asr/kaldi/tree/master/egs/aspire/s5). The diarization baseline is based on [LEAP Lab's](http://leap.ee.iisc.ac.in/) submission to [DIHARD II](https://dihardchallenge.github.io/dihard2/):  

> Singh, Prachi, et. al. (2019). "LEAP Diarization System for Second DIHARD Challenge." Proceedings of INTERSPEECH 2019. ([paper](http://leap.ee.iisc.ac.in/navigation/publications/papers/DIHARD_2019_challenge_Prachi.pdf))

The systems are trained on a combination of [VoxCeleb I and II](http://www.robots.ox.ac.uk/~vgg/data/voxceleb/) (diarization) and the DIHARD III development set (diarization and SAD).

The trained system, as well as recipes for producing the baseline results for
each track, is [available on github](https://github.com/dihardchallenge/dihard3_baseline). For more details, consult the documentation in that repo, or the
following paper:

> Ryant, Neville et al. (2020). "The Third DIHARD Diarization Challenge."
  ([paper](https://dihardchallenge.github.io/dihard3/docs/third_dihard_overview.pdf))