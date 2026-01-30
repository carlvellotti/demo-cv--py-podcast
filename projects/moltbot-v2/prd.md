# PRD: Moltbot v2 - Smart Notifications

## Overview

**Problem:** Users receive too many notifications and can't distinguish important ones from noise. 45% report feeling "overwhelmed" by notifications.

**Solution:** ML-powered notification priority scoring that learns from user behavior and surfaces what matters.

**Owner:** Carl
**Status:** In Review
**Target Release:** Feb 28, 2026

---

## Goals & Success Metrics

| Metric | Current | Target | How We Measure |
|--------|---------|--------|----------------|
| Notification Click Rate | 12% | 25% | Clicks / Total notifications shown |
| User "overwhelm" score | 45% | <20% | Weekly survey |
| Digest Open Rate | 34% | 50% | Email analytics |
| DAU | 2,000 | 5,000 | Product analytics |

**Non-goals:**
- We are NOT building a notification center UI (that's v3)
- We are NOT supporting third-party app integrations yet
- We are NOT doing real-time ML inference (batch processing only)

---

## User Stories

**As a** busy professional
**I want to** see my most important notifications first
**So that** I don't miss critical messages while ignoring noise

**As a** user who gets too many notifications
**I want to** have a "quiet mode" that only shows urgent items
**So that** I can focus without missing emergencies

**As a** new user
**I want to** have reasonable defaults before the system learns my preferences
**So that** the product is useful from day one

---

## Requirements

### Must Have (P0)
- [ ] ML model scores notifications 1-100 based on predicted importance
- [ ] Settings UI with notification preferences (by app, by type)
- [ ] "Quiet hours" toggle on main settings screen
- [ ] Digest email shows high-priority items first
- [ ] 7-day learning period before personalized scoring activates

### Should Have (P1)
- [ ] User can manually mark notifications as "always important" or "never show"
- [ ] Weekly summary of notification patterns
- [ ] Tooltip explaining why a notification was ranked high/low

### Nice to Have (P2)
- [ ] Export notification history
- [ ] Team-level notification bundles

---

## Design

Settings UI: Tabbed layout with three tabs:
1. **Notifications** - Per-app and per-type toggles
2. **Quiet Hours** - Schedule and exceptions
3. **Learning** - View/reset ML preferences

[PLACEHOLDER FOR FIGMA LINK]

---

## Technical Considerations

- **ML Model:** Gradient boosted trees, trained on click/dismiss/snooze signals
- **Latency:** Scoring happens in batch (every 5 min), not real-time
- **Data:** 6 months of anonymized behavior data for training
- **Privacy:** All scoring happens server-side, no raw behavior sent to third parties

---

## Rollout Plan

| Phase | Audience | Timeline | Success Criteria |
|-------|----------|----------|------------------|
| Alpha | Internal team (50) | Feb 1-7 | No critical bugs |
| Beta | 10% of users | Feb 8-21 | Click rate >18% |
| GA | 100% of users | Feb 28 | Click rate >22% |

---

## Open Questions

- [ ] GDPR: Do we need explicit consent for behavior-based scoring?
- [ ] What's the fallback if ML model confidence is low?
- [ ] How do we handle users who opt out of personalization?

---

## Appendix

### Competitive Analysis

| Product | Approach | Strength | Weakness |
|---------|----------|----------|----------|
| Slack Focus | Manual DND | Simple | No learning |
| Apple Focus | App-based rules | System-level | No cross-app priority |
| Gmail Priority | ML inbox sorting | Good ML | Email only |
