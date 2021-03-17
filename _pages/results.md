---
title: ""
permalink: /results.html
classes: wide
datatable: true
---


# Leaderboards

Leaderboards containing the **final primary** system submission by each team, ranked in ascending order by DER on the core evaluation set.
For each submission, the following fields are displayed:

- **Rank**  --  ranking of the system; by default, systems are ranked in ascending order by DER on the core evaluation set
- **Team**  --  name of team that made submission
- **# Entries**  --  total number of submissions made by the team (primary and secondary) over the course of the evaluation
- **Submission URI**  --  unique resource identifier (URI) for the submission; assigned by NIST
- **Date**  --  datetime (GMT) of the submission in YYYY-MM-DD hh:mm:ss format
- **Description**  --  link to corresponding system description
- **Workshop**  --  link to corresponding workshop presentation
- **DER (core)**  --  diarization error rate (in percent) of submission on the core evaluation set
- **JER (core)**  --  Jaccard error rate (in percent) of submisson on the core evaluation set
- **DER (full)**  --  diarization error rate (in percent) of submission on the full evaluation set
- **JER (full)**  --  Jaccard error rate (in percent) of submission on the full evaluation set

Baseline results for each track are provided under the team name of **DIHARD** and indicated by a blue horizontal line in the bar plot. These
results are also available from the [challenge paper](https://arxiv.org/abs/2012.01477) and [baseline github repo](https://github.com/dihardchallenge/dihard3_baseline).


## Track 1


<table id="tab_track1" class="datatable table table-hover table-condensed"
  data-bar-hline="true"
  data-chart-default-mode="bar"
  data-chart-modes="bar"
  data-id-field="team"
  data-pagination="false"
  data-rank-mode="grouped_muted"
  data-row-highlighting="true"
  data-show-chart="true"
  data-show-rank="true"
  data-sort-name="der_core"
  data-sort-order="asc">
  <thead>
    <tr>
      <th class="sep-left-cell text-center" colspan="7">Submission information</th>
      <th class="sep-left-cell text-center" colspan="2">Core set</th>
      <th class="sep-left-cell text-center" colspan="2">Full set</th>
    </tr>
    <tr>
      <th class="sep-right-cell" data-rank="true">Rank</th>
      <th class="sep-left-cell text-center" data-field="team"  data-sortable="true" id="team">Team</th>
      <th class="sep-left-cell text-center" data-field="num_entries" data-sortable="true"># Entries</th>
      <th class="sep-left-cell text-center" data-field="submission_id" data-sortable="true" data-value-type="int">Submission URI</th>
      <th class="sep-left-cell text-center" data-field="date" data-sortable="false">Date</th>
      <th class="sep-left-cell text-center" data-field="description" data-sortable="false" data-value-type="url">Description</th>
      <th class="sep-left-cell text-center" data-field="workshop" data-sortable="false" data-value-type="url">Workshop</th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="der_core" data-sortable="true" data-value-type="float2">DER<small class="hidden"> (Core set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="jer_core" data-sortable="true" data-value-type="float2">JER<small class="hidden"> (Core set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="der_full" data-sortable="true" data-value-type="float2">DER<small class="hidden"> (Full set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="jer_full" data-sortable="true" data-value-type="float2">JER<small class="hidden"> (Full set)</small></th>
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.track1_scores %}
    {% if row["team_name"] == "DIHARD" %}
    <tr class="info" data-hline="true">
    {% else %}
    <tr>
    {% endif %}
      <td></td>
      <td>{{ row["team_name"] }}</td>
      <td>{{ row["num_submissions"] }}</td>
      <td>{{ row["submission_uri"] }}</td>
      <td>{{ row["datetime"] }}</td>
      <td>{{ row["description_url"] }}</td>
      <td>{{ row["workshop_url"] }}</td>
      <td>{{ row["der_core"] }}</td>
      <td>{{ row["jer_core"] }}</td>
      <td>{{ row["der_full"] }}</td>
      <td>{{ row["jer_full"] }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>



## Track 2


<table id="tab_track2" class="datatable table table-hover table-condensed"
  data-bar-hline="true"
  data-chart-default-mode="bar"
  data-chart-modes="bar"
  data-id-field="team"
  data-pagination="false"
  data-rank-mode="grouped_muted"
  data-row-highlighting="true"
  data-show-chart="true"
  data-show-rank="true"
  data-sort-name="der_core"
  data-sort-order="asc">
  <thead>
    <tr>
      <th class="sep-left-cell text-center" colspan="7">Submission information</th>
      <th class="sep-left-cell text-center" colspan="2">Core set</th>
      <th class="sep-left-cell text-center" colspan="2">Full set</th>
    </tr>
    <tr>
      <th class="sep-right-cell" data-rank="true">Rank</th>
      <th class="sep-left-cell text-center" data-field="team"  data-sortable="true" id="team">Team</th>
      <th class="sep-left-cell text-center" data-field="num_entries" data-sortable="true"># Entries</th>
      <th class="sep-left-cell text-center" data-field="submission_id" data-sortable="true" data-value-type="int">Submission URI</th>
      <th class="sep-left-cell text-center" data-field="date" data-sortable="false">Date</th>
      <th class="sep-left-cell text-center" data-field="description" data-sortable="false" data-value-type="url">Description</th>
      <th class="sep-left-cell text-center" data-field="workshop" data-sortable="false" data-value-type="url">Workshop</th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="der_core" data-sortable="true" data-value-type="float2">DER<small class="hidden"> (Core set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="jer_core" data-sortable="true" data-value-type="float2">JER<small class="hidden"> (Core set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="der_full" data-sortable="true" data-value-type="float2">DER<small class="hidden"> (Full set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="jer_full" data-sortable="true" data-value-type="float2">JER<small class="hidden"> (Full set)</small></th>
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.track2_scores %}
    {% if row["team_name"] == "DIHARD" %}
    <tr class="info" data-hline="true">
    {% else %}
    <tr>
    {% endif %}
      <td></td>
      <td>{{ row["team_name"] }}</td>
      <td>{{ row["num_submissions"] }}</td>
      <td>{{ row["submission_uri"] }}</td>
      <td>{{ row["datetime"] }}</td>
      <td>{{ row["description_url"] }}</td>
      <td>{{ row["workshop_url"] }}</td>
      <td>{{ row["der_core"] }}</td>
      <td>{{ row["jer_core"] }}</td>
      <td>{{ row["der_full"] }}</td>
      <td>{{ row["jer_full"] }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>