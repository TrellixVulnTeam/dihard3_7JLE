---
title: ""
permalink: /submission.html
classes: wide
---

# <a name="results"></a>Results submission

## Preparing the submission archive

* System output for each track should be submitted as a *.zip* or *.tgz*
  file that expands into a single directory of RTTM files containing one RTTM
  file for each recording. For instance, if your submission to track 1 is
  contained in *t1_sub.zip*, this file should expand into:

      t1_sub/DH_EVAL_0001.rttm
      t1_sub/DH_EVAL_0002.rttm
      ...
      t1_sub/DH_EVAL_0259.rttm

   One RTTM file should be present for **EVERY** recording, even if the system
   output no speaker segments for the recording. If any RTTMs are missing,
   the submission will be rejected during the validation stage and **NOT**
   scored.
* Examples of valid zip files:
  * **Track 1**: [track1.zip](docs/sample_subs/track1.zip)
  * **Track 2**: [track2.zip](docs/sample_subs/track2.zip)
* To validate the RTTMs in your submission before creating the zip file, use
  the [validate_rttm.py](https://github.com/nryant/dscore/blob/master/validate_rttm.py) script from the [dscore repo](https://github.com/nryant/dscore) with the command:

      python validate_rttm.py DH_EVAL_0001.rttm DH_EVAL_0002.rttm ...

* To validate your archive's structure, use the [validate_submission.py](docs/validate_submission.py) script with the command:

      python validate_submission.py t1_sub.zip


## Submitting an archive via the NIST dashboard

* To submit output of a system for scoring, log into [your participant account](https://sat.nist.gov/users/sign_in) and select **Dashboard** from the top right of the page.
* Navigate to the **Submission Management** panel and click on the task that
  you wish to submit to.
* This will open the **Submissions** page.
  * Click **Add new system**.
  * Select the system type
    * Select **primary** if you wish for the scoring results to be displayed on
      the leaderboard.
    * Select **contrastive** otherwise.
  * Enter a name for your system.
  * Click **Submit**.
* This registers your submission with the scoring server. Next, you need to
  upload the archive containing your system output. To do this, locate your
  submission on the **Submissions** page.  As the entries on this page are
  displayed in ascending order of submission date, it will be at the very
  bottom. Find your submission and:
  * Click **Upload**.
  * Select the output you want to upload.
  * Click **Submit**.
* At this point your archive will be uploaded to the NIST server and the
  following will occur:
  * a unique submission ID will be generated; this will be used to track your
    submission
  * your submission will be validated
  * if the submission passes validation, it will be scored
* When the server finishes scoring your submission, it will display the status
  **DONE**. To access the scoring results, click on this status.
* If for any reason scoring failed, it will display a status beginning with
  **FAIL**. Clicking on this status will open the error log from the scoring
  script, which can be used to debug your submission.
* [Click here](docs/dihard3_submission_instructions.pdf) for a detailed
  step-by-step walkthrough with screenshots for each stage of the process.


## Leaderboards

* The leaderboards contain the most recent primary system submission by each
  team, ranked in ascending order by DER. 
* Leaderboards are maintained by NIST at:  

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[https://sat.nist.gov/dihard3#tab_leaderboard](https://sat.nist.gov/dihard3#tab_leaderboard)
* For more information, see the [results page](results.html).



## Rules

* Each team is limited to 50 total submissions to each track.
* Submissions that fail during either the validation or scoring phase (status
  begins with **FAIL**) do not count against this limit.
* The deadline for submitting system outputs is **December 30th, 2020
  (midnight Anywhere on Earth**).



# <a name="system"></a>System description submission

* At the end of the evaluation, all participating teams must submit a full
  description of their system with sufficient detail for a fellow researcher
  to understand the approach and data/computational requirements. System
  descriptions should adhere to the format described in Appendix F of the
  [evaluation plan](index.html#plan).
* The deadline for submitting system descriptions is **January 31st, 2021
  (midnight Anywhere on Earth**).
* Instructions for submitting descriptions will be posted here at the
  conclusion of the evaluation.
