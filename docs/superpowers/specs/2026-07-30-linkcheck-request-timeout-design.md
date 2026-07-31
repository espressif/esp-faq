# Linkcheck Request Timeout Design

## Context

The `doc_linkcheck` CI matrix checks all external links for the English and
Chinese documentation. The English job has exceeded the one-hour GitLab job
limit and has been terminated with `SIGTERM` (`errcode: -15`). The repository
does not currently set Sphinx's per-request `linkcheck_timeout`.

## Design

Add the following setting to `docs/conf_common.py` next to the existing
linkcheck configuration:

```python
linkcheck_timeout = 15
```

This bounds each external HTTP request to 15 seconds while preserving the
existing URL coverage. No URLs will be ignored, and the retry count,
rate-limit policy, worker count, and GitLab job timeout will remain unchanged.

## Verification

1. Before the configuration change, verify that loading `docs/conf_common.py`
   does not produce `linkcheck_timeout == 15`.
2. After the change, verify that Sphinx loads `linkcheck_timeout == 15`.
3. Run `git diff --check` and inspect the final diff.

The full external linkcheck remains network-dependent and may still report
genuine link failures or server-side blocking. The success criterion for this
change is that an individual unresponsive request cannot wait indefinitely.

## Scope

Only `docs/conf_common.py` is changed in the implementation. There are no URL
exceptions and no CI timeout changes.
