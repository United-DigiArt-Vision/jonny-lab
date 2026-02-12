---
name: dragon-dev-loop
description: >
  Standard development process with TDD and multi-agent QA loop.
  Use when: building features, fixing bugs, writing code, any development task that will be delivered to Dino.
  Don't use when: editing docs/config/data files only, updating MEMORY.md, changing cron jobs.
  Ensures: Requirements → Tests first (Vermithrax) → Implementation (Caraxes) → QA (Vermithrax) → Loop until PASS → Delivery with full protocol.
---

# Dragon Dev Loop

Standard development process. **No exceptions for any code change delivered to Dino.**

## The Loop

```
1. REQUIREMENTS (Balerion)     → PRD / REQUIREMENTS.md
2. TESTS FIRST (Vermithrax 🛡️) → Test spec + acceptance criteria
3. IMPLEMENT (Caraxes 🔴)      → Code against tests
4. QA (Vermithrax 🛡️)          → Test, report, PASS/FAIL
5. FAIL? → Back to 3           → Loop until PASS
6. PASS → Deliver to Dino      → With FULL protocol in chat
```

## Roles

| Dragon | Role | When |
|--------|------|------|
| **Balerion** | Requirements, orchestration, final validation, delivery | Start + End |
| **Vermithrax** 🛡️ | Define tests, QA report, PASS/FAIL | Before + After implementation |
| **Caraxes** 🔴 | Implement, fix findings | Middle |

## Delivery Protocol (MANDATORY)

Every delivery to Dino includes IN THE CHAT:
1. Requirements document (path + key requirements)
2. Test specification (path + what/how tested)
3. Traceability matrix (requirement → test → result)
4. All file paths
5. Pass/fail decision with numbers

**No "it's done, check it out"!** Always full protocol.

## Escalation

- Loop > 3x without PASS → Report to Dino with analysis
- Unclear requirements → Ask Dino BEFORE starting
- Technically impossible → Report with alternatives

## Rules

1. No code without requirements
2. No code without tests (Vermithrax defines tests BEFORE implementation)
3. No FAIL delivered to Dino — loop until PASS
4. Always full protocol on delivery
5. Vermithrax has final say on quality
6. Loop is mandatory — Balerion starts it automatically
