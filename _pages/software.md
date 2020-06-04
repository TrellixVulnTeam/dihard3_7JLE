---
title: ""
permalink: /software.html
classes: wide
---

# Scoring

The official scoring tool is maintained as a [github repo](https://github.com/nryant/dscore) (v1.1.0). To score a set of system output RTTMs *sys1.rttm,
sys2.rttm, ...* against corresponding reference RTTMs *ref1.rttm, ref2.rttm,
...* using the un-partitioned evaluation map (UEM) *all.uem*, the command
line would be:

                  
    $ python score.py -u all.uem -r ref1.rttm ref2.rttm ... -s sys1.rttm sys2.rttm ...
                
The overall and per-file results for DER and JER (and many other metrics) will be printed to STDOUT as a table. For additional details about scoring tool usage, please consult the documentation for the [github repo](https://github.com/nryant/dscore).

# Baseline systems

* Baseline systems for performing speech activity detection along with
  recipes for using these systems on the development and evaluation sets
  will be provided by the organizers.
* Once available the baselines, an announcement will be made to the mailing
  list and instructions for accessing the baselines posted here.

