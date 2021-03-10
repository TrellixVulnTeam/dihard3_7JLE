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
- **Date**  --  datetime (GMT) of the submission in format
- **Description**  --  link to corresponding system description
- **DER (core)**  --  diarization error rate (in percent) of submission on the core evaluation set
- **JER (core)**  --  Jaccard error rate (in percent) of submisson on the core evaluation set
- **DER (full)**  --  diarization error rate (in percent) of submission on the full evaluation set
- **JER (full)**  --  Jaccard error rate (in percent) of submission on the full evaluation set


## Track 1


<table id="tab_track1_full" class="datatable table table-hover table-condensed"
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
      <th class="sep-left-cell text-center" colspan="6">Submission information</th>
      <th class="sep-left-cell text-center" colspan="2">Core set</th>
      <th class="sep-left-cell text-center" colspan="2">Full set</th>
    </tr>
    <tr>
      <th class="sep-right-cell" data-rank="true">Rank</th>
      <th class="sep-left-cell text-center" data-field="team"  data-sortable="true" id="team">Team</th>
      <th class="sep-left-cell text-center" data-field="num_entries" data-sortable="true"># Entries</th>
      <th class="sep-left-cell text-center" data-field="submission_id" data-sortable="true" data-value-type="int">Submission ID</th>
      <th class="sep-left-cell text-center" data-field="date" data-sortable="false">Date</th>
      <th class="sep-left-cell text-center" data-field="description" data-sortable="false" data-value-type="url">Description</th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="der_core" data-sortable="true" data-value-type="float2">DER<small class="hidden"> (Core set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="jer_core" data-sortable="true" data-value-type="float2">JER<small class="hidden"> (Core set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="der_full" data-sortable="true" data-value-type="float2">DER<small class="hidden"> (Full set)</small></th>
      <th class="sep-left-cell text-center" data-chartable="true" data-field="jer_full" data-sortable="true" data-value-type="float2">JER<small class="hidden"> (Full set)</small></th>
    </tr>
  </thead>
  <tbody>
    {% for row in site.data.track1 %}
    {% if row["team"] == "Team_00115" %}
    <tr class="info" data-hline="true">
    {% else %}
    <tr>
    {% endif %}
      <td></td>
      <td>{{ row["team"] }}</td>
      <td>{{ row["num_entries"] }}</td>
      <td>{{ row["submission_id"] }}</td>
      <td>{{ row["datetime"] }}</td>
      <td>{{ row["description_url"] }}</td>
      <td>{{ row["der_core"] }}</td>
      <td>{{ row["jer_core"] }}</td>
      <td>{{ row["der_full"] }}</td>
      <td>{{ row["jer_full"] }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>



## Track 2