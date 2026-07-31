# Linkcheck Request Timeout Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bound every Sphinx external-link request to 15 seconds so an unresponsive server cannot hold a linkcheck worker indefinitely.

**Architecture:** Add one shared Sphinx configuration value in `docs/conf_common.py`, which is loaded by both the English and Chinese documentation builds. Preserve URL coverage and all other retry, rate-limit, worker, and GitLab timeout settings.

**Tech Stack:** Python configuration, Sphinx 4.5 linkcheck builder, GitLab CI

## Global Constraints

- Set `linkcheck_timeout` to exactly `15` seconds.
- Do not add `linkcheck_ignore` entries.
- Do not change retries, rate-limit policy, worker count, or GitLab job timeout.

---

### Task 1: Configure the per-request timeout

**Files:**
- Modify: `docs/conf_common.py:47`
- Test: one-off Python configuration assertion executed from the repository root

**Interfaces:**
- Consumes: Sphinx configuration globals imported from `esp_docs.conf_docs`.
- Produces: integer Sphinx configuration value `linkcheck_timeout = 15` for both language builds.

- [x] **Step 1: Run the failing configuration assertion**

```bash
python3 -c "import runpy; c=runpy.run_path('docs/conf_common.py'); assert c.get('linkcheck_timeout') == 15, c.get('linkcheck_timeout')"
```

Expected: FAIL because `linkcheck_timeout` is not set to `15` by the repository configuration.

- [x] **Step 2: Add the minimal configuration**

Add immediately after `linkcheck_anchors = False`:

```python
linkcheck_timeout = 15
```

- [x] **Step 3: Run the configuration assertion again**

```bash
python3 -c "import runpy; c=runpy.run_path('docs/conf_common.py'); assert c.get('linkcheck_timeout') == 15, c.get('linkcheck_timeout')"
```

Expected: PASS with exit code 0.

- [x] **Step 4: Verify scope and formatting**

```bash
git diff --check
git diff -- docs/conf_common.py
```

Expected: no formatting errors and exactly one runtime configuration line added.

- [ ] **Step 5: Commit and push**

```bash
git add docs/conf_common.py docs/superpowers/plans/2026-07-30-linkcheck-request-timeout.md
git commit -m "ci: bound linkcheck request timeout"
git push origin maintain/2026h2_i2c_link
```

Expected: the MR source branch advances to the new commit.
