# Contributing to TRION Intelligence Modules

Thank you for contributing to TRION! This guide explains how to create and submit Intelligence Modules.

## 🎯 What is an Intelligence Module?

An Intelligence Module is a **structured reasoning protocol** that tells TRION "how to think" about specific types of problems.

**Not code** - They're JSON data files that get retrieved and followed.  
**Not prompts** - They're structured templates with explicit steps and validation criteria.  
**Not rules** - They're reasoning procedures that guide execution.

## 📋 Module Requirements

### Essential Components

Every module must include:

1. **Metadata**
   - Name (unique identifier)
   - Version (semantic versioning)
   - Description (what problem it solves)

2. **When to Use**
   - Task patterns that trigger this protocol
   - Complexity range (1-10)
   - Uncertainty tolerance level

3. **Steps**
   - Structured phases of reasoning
   - Expected outputs per phase
   - Validation criteria

4. **Expert Excerpt**
   - Simplified version for Skill-Agents
   - Key points and checklists
   - Single-step execution guidance

5. **Metadata**
   - Typical complexity
   - Whether expert needed
   - Advantages and limitations

### Quality Standards

Modules should be:

✅ **Clear** - Each step explicitly defined  
✅ **Testable** - Outputs can be validated  
✅ **Modular** - Steps are atomic and independent  
✅ **Practical** - Applicable to real tasks  
✅ **Deterministic** - Same inputs → same structure  

## 📝 Module Format

### JSON Schema

Complete schema: `/intelligence-modules/schemas/protocol-schema.json`

### Template

```json
{
  "protocol": {
    "name": "Your-Protocol-Name",
    "version": "1.0.0",
    "description": "What this protocol does and when to use it",
    
    "when_to_use": {
      "task_patterns": [
        "pattern1",
        "pattern2"
      ],
      "complexity_range": [5, 8],
      "uncertainty_tolerance": "medium",
      "domain": "general"
    },
    
    "steps": [
      {
        "phase": "Phase Name",
        "description": "What happens in this phase",
        "procedure": [
          "Specific action 1",
          "Specific action 2"
        ],
        "outputs": [
          "expected_output_1",
          "expected_output_2"
        ],
        "validation": "How to verify this phase succeeded",
        "failure_modes": [
          "What could go wrong",
          "How to detect it"
        ]
      }
    ],
    
    "expert_excerpt": {
      "description": "Simplified for single-step agent execution",
      "key_points": [
        "Most important principle 1",
        "Most important principle 2"
      ],
      "checklist": [
        "Check item 1",
        "Check item 2"
      ],
      "common_mistakes": [
        "Mistake to avoid 1",
        "Mistake to avoid 2"
      ]
    },
    
    "typical_complexity": 6,
    "needs_expert": false,
    "compute_requirements": "low",
    
    "advantages": [
      "Advantage 1",
      "Advantage 2"
    ],
    
    "limitations": [
      "Limitation 1",
      "Limitation 2"
    ],
    
    "examples": [
      {
        "task": "Example task description",
        "expected_approach": "How protocol guides the task"
      }
    ],
    
    "references": [
      {
        "title": "Source or inspiration",
        "url": "https://example.com"
      }
    ]
  }
}
```

## 🔧 Integration Points

Your module will integrate with:

### 1. Idea Generator (Component #2)

**Purpose:** Uses your protocol as a template for task breakdown

**What it does:**
- Detects task matches `when_to_use` patterns
- Retrieves your protocol
- Creates execution plan following your `steps`
- Estimates resources based on your `typical_complexity`

**What you need to provide:**
- Clear task patterns
- Well-defined steps
- Accurate complexity estimate

### 2. Complexity Estimator (Component #3)

**Purpose:** Assesses if task needs expert based on protocol

**What it does:**
- Checks your `typical_complexity`
- Reads your `needs_expert` flag
- Factors protocol availability into estimates

**What you need to provide:**
- Honest complexity rating (1-10)
- Accurate expert requirement assessment

### 3. Validator (Component #8)

**Purpose:** Verifies execution followed protocol

**What it does:**
- Checks if all `outputs` present
- Runs `validation` checks
- Confirms protocol compliance

**What you need to provide:**
- Explicit output expectations
- Testable validation criteria
- Clear success/failure indicators

### 4. Skill-Agents (When Spawned)

**Purpose:** Execute complex steps following protocol

**What they receive:**
- Your `expert_excerpt` (not full protocol)
- Task context
- Expected outputs

**What you need to provide:**
- Simplified excerpt (agent-friendly)
- Clear key points
- Actionable checklist

## 📤 Submission Process

### Step 1: Create Module

1. Copy `/examples/example-protocol.json`
2. Customize for your protocol
3. Validate against schema
4. Test locally (if possible)

### Step 2: Submit Pull Request

1. Fork this repository
2. Add your module to `/intelligence-modules/protocols/your-protocol-name.json`
3. Create PR with:
   - **Title:** `Add [Protocol Name] module`
   - **Description:** 
     - What problem it solves
     - When to use it
     - Example applications
4. Tag with `intelligence-module` label

### Step 3: Review & Iteration

We'll review for:
- Schema compliance
- Clarity and completeness
- Integration feasibility
- Practical applicability

**Expected timeline:** 3-5 days for initial review

### Step 4: Integration Testing

Once approved, we'll:
1. Integrate into TRION test environment
2. Run on sample tasks
3. Measure effectiveness
4. Report results back

### Step 5: Merge & Deploy

After successful testing:
1. Merge to main branch
2. Deploy to production
3. Monitor effectiveness
4. Iterate based on reflection data

## 🧪 Testing Guidelines

### Self-Testing Checklist

Before submitting, verify:

- [ ] Valid JSON (no syntax errors)
- [ ] Follows schema structure
- [ ] All required fields present
- [ ] Task patterns are clear
- [ ] Steps are well-defined
- [ ] Outputs are explicit
- [ ] Validation is testable
- [ ] Expert excerpt is simplified
- [ ] Complexity rating is realistic
- [ ] Examples are provided

### Manual Testing (Optional)

If you have access to LLMs, test by:

1. **Prompting with protocol:**
   ```
   Task: [Your example task]
   Protocol: [Your protocol steps]
   Follow the protocol strictly.
   ```

2. **Checking output:**
   - Does it follow steps?
   - Are outputs produced?
   - Is validation possible?

3. **Iterating:**
   - Refine unclear steps
   - Add missing validation
   - Simplify complex phases

## 📊 Success Metrics

Your module's effectiveness will be measured:

**Adoption Rate:**
- How often selected for tasks
- Task success rate with protocol
- User satisfaction ratings

**Quality Metrics:**
- Protocol compliance rate
- Validation pass rate
- Error reduction vs. baseline

**Performance:**
- Execution time impact
- Token efficiency
- Expert spawn accuracy

We'll share these metrics with you for continuous improvement.

## 💡 Module Ideas

### High Priority

**Plan-Act-Verify** ⭐
- Multi-step tasks with validation
- Most universally applicable
- Fixes current failure mode #2

**Bayesian Update**
- Uncertainty quantification
- Confidence calibration
- Fixes current failure mode #1

**Causal Reasoning**
- Cause-effect analysis
- Confounder checking
- Systematic counterfactuals

**Constraint-First**
- Problem-solving with hard limits
- Boundary condition identification
- Invariant enforcement

### Medium Priority

**Systems Thinking**
- Feedback loops
- Second-order effects
- Emergent behaviors

**Decomposition Strategy**
- Breaking complex into simple
- Dependency identification
- Parallelization opportunities

**Ask-Clarify Policy**
- High uncertainty handling
- Missing context detection
- User interaction protocols

### Domain-Specific

**Data Analysis**
- Statistical reasoning
- Pattern detection
- Validation procedures

**Code Review**
- Security checking
- Performance analysis
- Best practice validation

**Decision Making**
- Option generation
- Criteria weighting
- Risk assessment

## ❓ FAQ

### Q: Can I submit partial modules?

**A:** Yes! Submit work-in-progress with `[WIP]` tag. We can collaborate on completion.

### Q: How many modules can I submit?

**A:** As many as you want! Start with one, iterate, then expand.

### Q: What if my module doesn't fit the schema?

**A:** Open an issue to discuss schema extensions. We're flexible for good ideas.

### Q: Can I update submitted modules?

**A:** Absolutely! Submit PR with version bump and changelog.

### Q: How do I know if my module is being used?

**A:** We'll share telemetry data showing usage frequency and effectiveness.

### Q: Can modules call other modules?

**A:** Not yet, but we're considering "meta-protocols" that combine modules.

### Q: What about domain-specific knowledge?

**A:** Modules should be procedural, not factual. Domain knowledge goes elsewhere.

### Q: How do I get credit?

**A:** Your name in module metadata, README acknowledgments, and commit history.

## 📞 Getting Help

**Questions about format?** See `/examples/example-protocol.json`  
**Questions about integration?** See `/docs/INTEGRATION_GUIDE.md`  
**Questions about architecture?** See `/docs/ARCHITECTURE_OVERVIEW.md`  
**Other questions?** Open an issue with `question` label

## 🎓 Best Practices

### DO:
✅ Keep steps atomic and testable  
✅ Provide clear validation criteria  
✅ Include failure modes  
✅ Simplify expert excerpts  
✅ Give concrete examples  
✅ Be explicit about complexity  
✅ Iterate based on feedback  

### DON'T:
❌ Make steps too high-level  
❌ Assume implicit knowledge  
❌ Skip validation criteria  
❌ Overload expert excerpts  
❌ Inflate complexity ratings  
❌ Mix multiple protocols  
❌ Include implementation code  

## 🏆 Recognition

Top contributors will be:
- Listed in README acknowledgments
- Mentioned in release notes
- Invited to architecture discussions
- Given early access to new features

## 📄 License

By contributing, you agree your modules are licensed under MIT License (same as project).

---

**Thank you for contributing to TRION!** 🚀

Your reasoning structures will help build more reliable, transparent, and capable AI systems.

**Questions?** Open an issue or reach out directly.

---

**Last Updated:** 2026-01-08  
**Version:** 1.0.0
