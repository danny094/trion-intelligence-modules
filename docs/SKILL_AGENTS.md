# Skill-Agent System (Simplified)

**Ephemeral Task Experts with Protocol Guidance**

## 🎯 Core Concept

**Skill-Agents** are temporary, specialized experts that execute single complex steps following Intelligence Module protocols.

**Key Properties:**
- **Ephemeral:** Lifetime = 1 task, then destroyed
- **Specialized:** Narrow domain expertise
- **Protocol-Guided:** Follow Intelligence Module excerpts
- **Supervised:** Control Layer always decides
- **Isolated:** MCP-based, no core access

## 🚫 What Skill-Agents Are NOT

```
❌ Autonomous agents (they don't decide)
❌ Permanent systems (destroyed after use)
❌ Tool discoverers (tools provided, not searched)
❌ Memory keepers (stateless, no persistence)
❌ Chain creators (can't spawn other agents)
```

## ✅ What Skill-Agents ARE

```
✅ Specialized executors (do ONE thing well)
✅ Protocol followers (use Intelligence Module guidance)
✅ Data providers (return structured results)
✅ Supervised workers (Control decides everything)
✅ Temporary tools (exist only for task)
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│ Control Layer (Layer 2)                         │
│                                                 │
│ Decides:                                        │
│ - Does this step need expert?                  │
│ - Which expert domain?                         │
│ - What protocol excerpt to provide?            │
│ - Budget acceptable?                           │
└─────────────────────────────────────────────────┘
                    │
                    ↓
        ┌───────────────────────┐
        │ Spawn Expert (MCP)    │
        └───────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────┐
│ Skill-Agent (Ephemeral)                        │
│                                                 │
│ Receives:                                       │
│ ├─ Task description                            │
│ ├─ ⭐ Protocol excerpt (from Intelligence Mod.)│
│ ├─ Context data                                │
│ └─ Expected outputs                            │
│                                                 │
│ Executes:                                       │
│ ├─ Follows protocol key_points                │
│ ├─ Uses protocol checklist                    │
│ ├─ Applies to context                         │
│ └─ Returns structured result                  │
│                                                 │
│ TTL: Task complete OR timeout OR error         │
└─────────────────────────────────────────────────┘
                    │
                    ↓
┌─────────────────────────────────────────────────┐
│ Control Layer                                   │
│                                                 │
│ Validates:                                      │
│ - Protocol compliance?                         │
│ - All outputs present?                         │
│ - Quality acceptable?                          │
│ - Confidence sufficient?                       │
└─────────────────────────────────────────────────┘
```

## ⭐ Intelligence Module Integration

**Critical Feature:** Experts receive protocol guidance!

### Without Protocol

```
Control: "Perform causal analysis"
Expert: "Uh... how exactly? What checks?"
Result: Inconsistent, might miss confounders
```

### With Protocol (Intelligence Module)

```
Control: "Perform causal analysis using this protocol"

Expert receives:
{
  "task": "Check for confounders",
  "protocol_excerpt": {
    "description": "Variables affecting both X and Y",
    "key_points": [
      "Check temporal order",
      "Test independence",
      "Consider domain knowledge"
    ],
    "checklist": [
      "Variable affects cause",
      "Variable affects effect",
      "Temporal precedence OK"
    ]
  }
}

Expert: "Clear! Following checklist..."
Result: Consistent, complete, validated
```

## 🎯 Expert Types (Examples)

**Data Analysis Expert:**
- Domain: Statistical analysis
- Protocol: Causal-Reasoning, Bayesian-Update
- Outputs: Insights, patterns, confidence

**Code Review Expert:**
- Domain: Software quality
- Protocol: Constraint-First
- Outputs: Issues, recommendations, severity

**Verification Expert:**
- Domain: Quality assurance
- Protocol: Plan-Act-Verify
- Outputs: Validation report, test results

## 🔄 Complete Flow Example

**Task:** "Analyze survey data for causal relationships"

### Step 1: Control Decision

```
Layer 2 receives step: "Check for confounders"

Evaluation:
- Complexity: HIGH
- Available expertise: Internal insufficient
- Protocol available: Causal-Reasoning
- Budget: 1/3 experts used ✅

Decision: SPAWN EXPERT
```

### Step 2: Expert Spawn

```
MCP spawns: causal-analysis-expert

Provided to expert:
{
  "task": "Check for confounders in survey data",
  
  "protocol_excerpt": {
    "description": "Confounders affect both cause and effect",
    "key_points": [
      "Check temporal precedence",
      "Test statistical independence",
      "Validate with domain knowledge"
    ],
    "checklist": [
      "Variable precedes cause",
      "Variable correlates with cause",
      "Variable correlates with effect",
      "Independence test performed"
    ],
    "common_mistakes": [
      "Ignoring temporal order",
      "Skipping independence tests"
    ]
  },
  
  "context": {
    "data": <survey_dataframe>,
    "cause_variable": "engagement",
    "effect_variable": "retention",
    "candidate_confounders": ["age", "tenure", "department"]
  },
  
  "expected_outputs": [
    "confounders_list",
    "confidence",
    "reasoning"
  ]
}
```

### Step 3: Expert Execution

```
Expert follows protocol:

1. Read key_points ✓
2. Apply checklist to each candidate:
   
   "age":
   ✓ Precedes engagement
   ✓ Correlates with engagement (p<0.01)
   ✓ Correlates with retention (p<0.01)
   ✓ Independence test: FAILS
   → CONFOUNDER
   
   "tenure": 
   ✓ Precedes engagement
   ✓ Correlates with engagement (p<0.05)
   ✓ Correlates with retention (p<0.01)
   ✓ Independence test: FAILS
   → CONFOUNDER
   
   "department":
   ✓ Precedes engagement
   ✗ No significant correlation
   → NOT A CONFOUNDER

3. Compile results following structure
```

### Step 4: Expert Returns

```
{
  "confounders_list": ["age", "tenure"],
  "confidence": 0.85,
  "reasoning": "Both age and tenure show strong correlation 
                with engagement and retention, and fail 
                independence tests. Department shows no 
                significant effect.",
  "details": {
    "age": {
      "correlation_with_cause": 0.42,
      "correlation_with_effect": 0.38,
      "p_value": 0.001
    },
    "tenure": {
      "correlation_with_cause": 0.35,
      "correlation_with_effect": 0.41,
      "p_value": 0.003
    }
  }
}
```

### Step 5: Control Validation

```
Layer 2 validates:

Protocol compliance:
✓ confounders_list present
✓ confidence present
✓ reasoning present
✓ Checklist followed (temporal, correlation, independence)

Quality check:
✓ Confidence adequate (0.85 > 0.7)
✓ Reasoning clear
✓ Details provided

Decision: ACCEPT
```

### Step 6: Expert Destroyed

```
✅ Task complete
🗑️  Expert process terminated
📝 No residual state
💾 No memory kept
```

## 🎯 Key Benefits

### For Quality

✅ **Consistency:** Same protocol every time
✅ **Completeness:** Checklist ensures nothing missed
✅ **Validation:** Structured outputs verified
✅ **Traceability:** Protocol followed is logged

### For System

✅ **No Drift:** Ephemeral = no accumulated errors
✅ **Isolation:** MCP = core protected
✅ **Control:** Layer 2 always supervises
✅ **Scalability:** Spawn as needed, destroy after

### For Development

✅ **Testable:** Protocol excerpts easily tested
✅ **Debuggable:** Clear inputs/outputs
✅ **Improvable:** Protocol updates improve all experts
✅ **Modular:** Add new experts without changing core

## 🔧 Implementation Status

**Current:** Fully designed (16KB doc)
**Integration:** Protocol excerpt passing ready
**Timeline:** Phase 2 (Weeks 3-4 after Intelligence Modules)

## 🔗 Synergy with Intelligence Modules

```
Intelligence Module provides:
├─ When to use expert (needs_expert flag)
├─ What expert should do (expert_excerpt)
├─ How to validate (required outputs, validation)
└─ Quality standards (checklist, common_mistakes)

Skill-Agent receives:
├─ Clear guidance (protocol excerpt)
├─ Actionable steps (checklist)
├─ Expected structure (outputs)
└─ Validation criteria (for self-check)

Control Layer enforces:
├─ Protocol compliance
├─ Output validation
├─ Quality standards
└─ Budget limits
```

## 📚 Full Documentation

Complete spec: `/documentation/features/SKILL_AGENT_ARCHITECTURE.md` (690 lines)

---

**Last Updated:** 2026-01-08
