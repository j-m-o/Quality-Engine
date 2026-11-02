# Fictional ticket: APP-1427

**Project:** Sample Customer Portal  
**Work item type:** Story  
**Summary:** Let signed-in users update email notification preferences  
**Product:** Customer Portal  
**Priority:** Medium

## Description
A signed-in user can enable or disable email notifications from a preference screen. The selected preference should be saved for that user and remain in place after a page refresh.

## Acceptance criteria
1. A signed-in user can view their current notification preference.
2. The user can change the email notification setting and save it.
3. The interface confirms that the change was saved.
4. A page reload reflects the saved preference.
5. A user cannot change another user's preferences.

## Synthetic test inventory for demo only
- `TEST-011`: Authenticated user can sign in, recently passed.
- `TEST-044`: Preferences page displays the current setting for a signed-in user, recently passed.
- No recorded test in this **fictional supplied inventory** directly verifies saving, persistence or cross-user authorization.

## Known unknowns
- API contract and error response behavior
- Rollout and data migration requirements
- Test data provisioning and team execution baseline

All names, tickets, tests, results and scores in this example are synthetic. Nothing was retrieved from a connected tracker or test platform.
