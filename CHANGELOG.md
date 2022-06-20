# v0.10.0

- dropped support for Python 3.7
- increase minimum version of `httpx` to avoid [Improper Input Validation in httpx](https://github.com/advisories/GHSA-h8pj-cxx2-jfg2)
- updated to the latest API at 2022-06-20

# v0.9.1

- updated to the latest API at 2022-06-13

# v0.9.0

- updated to the latest API at 2022-06-06

# v0.8.0

- updated to the latest API at 2022-05-28
- added command to donwload the Swagger 2.x specs from the API endpoint

# v0.7.0

- updated to the latest API at 2022-05-26

# v0.6.0

- updated to the latest API at 2022-05-05
- added a new `mode` field in the incidend model, the field's content is the same as the `type` field; the `type` field is now considered deprecated

# v0.5.0

- updated to the latest API at 2022-04-29
- patch to add back `reporter` in the `IncidentRoleResponseBody` schema; this is for incidents created before the latest API update which removed the `reporter` item