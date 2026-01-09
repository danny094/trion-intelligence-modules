# Intelligence Module Integration Guide

**How Intelligence Modules integrate into TRION**

## 🎯 Overview

Intelligence Modules are **procedural RAG** - structured reasoning protocols that guide TRION's cognitive processes. This guide explains exactly how your modules integrate with the system.

## 🔗 Three Integration Points

Your modules integrate into **3 core components** of the Sequential Thinking Engine:

### 1. Idea Generator (Component #2)

**Purpose:** Uses your protocol as a template for task breakdown

**Integration Flow:**

```python
class IdeaGenerator:
    def generate(self, task: Task) -> List[Idea]:
        """Generate solution approaches"""
        
        # ⭐ Check if task matches a protocol
        protocol = self.intelligence_modules.select_protocol(task)
        
        if protocol:
            # Use protocol as structured template
            idea = Idea(
                description=f"Follow {protocol.name}",
                steps=protocol.steps,  # ⭐ Your steps become execution steps
                complexity=protocol.typical_complexity,
                needs_expert=protocol.needs_expert,
                confidence=0.9  # High because structured
            )
            ideas.append(idea)
        
        # Also generate fallback ideas
        ideas.extend(self.brainstorm(task))
        
        return ideas
```

**What happens:**
1. User task analyzed
2. Task patterns matched against your `when_to_use.task_patterns`
3. If match → your protocol retrieved
4. Your `steps` become the execution plan template
5. Sequential Thinking executes following your structure

**Example:**

```
User: "Analyze this data for cause-effect relationships"

Your Protocol: Causal-Reasoning
  task_patterns: ["causal-analysis", "cause-effect", "confounders"]
  steps: [
    {phase: "Identify Variables", ...},
    {phase: "Check Confounders", ...},
    {phase: "Test Counterfactuals", ...},
    {phase: "Validate Causality", ...}
  ]

Result: Plan with 6 steps (Load, Identify, Check, Test, Validate, Report)
        Following YOUR causal reasoning structure!
```

---

### 2. Complexity Estimator (Component #3)

**Purpose:** Assesses task difficulty with protocol awareness

**Integration Flow:**

```python
class ComplexityEstimator:
    def estimate(self, task: Task) -> ComplexityScore:
        """Estimate with protocol knowledge"""
        
        # Check if protocol available
        protocol = self.intelligence_modules.select_protocol(task)
        
        if protocol:
            # ⭐ Use your complexity rating
            return ComplexityScore(
                overall=protocol.typical_complexity,
                expert_recommended=protocol.needs_expert,
                protocol_available=True,
                protocol_name=protocol.name,
                compute_requirements=protocol.compute_requirements
            )
        
        # Fallback to heuristic estimation
        return self.heuristic_estimate(task)
```

**What happens:**
1. When protocol available, your `typical_complexity` used
2. Your `needs_expert` flag guides expert spawning
3. Your `compute_requirements` inform resource allocation
4. More accurate estimates → better planning

**Example:**

```
Task: "Perform Bayesian update on hypothesis"

Your Protocol: Bayesian-Update
  typical_complexity: 7
  needs_expert: false
  compute_requirements: "low"

Result: 
  - Complexity set to 7 (medium-high)
  - Expert not spawned (can do internally)
  - Low compute budget allocated
  - Realistic time estimate
```

---

### 3. Validator (Component #8)

**Purpose:** Verifies execution followed protocol

**Integration Flow:**

```python
class Validator:
    def check_result(self, step: Step, result: Any) -> ValidationResult:
        """Validate with protocol compliance"""
        
        if step.protocol:
            # ⭐ Validate against your requirements
            required_outputs = step.protocol.outputs
            
            issues = []
            for output in required_outputs:
                if output not in result:
                    issues.append(f"Missing: {output}")
            
            # ⭐ Check your validation criteria
            validation_check = step.protocol.validation
            if not self.evaluate(validation_check, result):
                issues.append(f"Validation failed: {validation_check}")
            
            return ValidationResult(
                valid=len(issues) == 0,
                protocol_compliant=True,
                issues=issues,
                confidence=1.0 - (len(issues) * 0.2)
            )
```

**What happens:**
1. After each step execution
2. Check if all your `outputs` present
3. Run your `validation` criteria
4. Report compliance or issues
5. Ensures quality

**Example:**

```
Your Protocol Step:
  phase: "Plan"
  outputs: ["step_list", "success_criteria"]
  validation: "All steps have clear outcomes"

Execution Result:
  {
    "step_list": ["Step 1", "Step 2"],
    "success_criteria": ["Criterion A"]
  }

Validation:
  ✅ step_list present
  ✅ success_criteria present
  ✅ All steps have clear outcomes
  → VALID, confidence: 1.0
```

---

## 🤖 Skill-Agent Integration

When Control Layer spawns an expert for a complex step:

**What Expert Receives:**

```python
{
  "task": "Check for confounders in causal analysis",
  
  # ⭐ Your expert excerpt (not full protocol)
  "protocol_excerpt": {
    "description": "Confounders are variables affecting both X and Y",
    "key_points": [
      "Check temporal order",
      "Test independence",
      "Consider domain knowledge"
    ],
    "checklist": [
      "Variable affects both cause and effect",
      "Temporal precedence maintained",
      "Independence test performed"
    ]
  },
  
  "context": {
    "data": <dataframe>,
    "variables": ["X", "Y", "Z"]
  },
  
  "expected_outputs": ["confounders_list", "confidence"]
}
```

**What Expert Does:**

```
Expert (following your excerpt):
1. Reads your key_points
2. Follows your checklist
3. Applies to context data
4. Returns structured output

Result:
{
  "confounders_list": ["Z"],
  "confidence": 0.85,
  "reasoning": "Z affects both X and Y, temporal order OK"
}
```

**Why This Works:**
- ✅ Expert has clear guidance (your excerpt)
- ✅ Consistent execution (same protocol every time)
- ✅ Validated output (against your checklist)
- ✅ High quality (structured approach)

---

## 📊 Complete Flow Example

**User Task:** "Analyze survey data to identify causal factors"

### Step 1: Protocol Selection (Layer 1)

```
Task Analysis:
  - Keywords: "causal factors"
  - Type: "data analysis"
  - Complexity: Unknown

Protocol Matching:
  Causal-Reasoning protocol:
    task_patterns: ["causal-analysis", "causal-factors"]
    ✅ MATCH!

Selected: Causal-Reasoning protocol
```

### Step 2: Plan Generation (Idea Generator)

```
Protocol Steps → Execution Plan:

1. Load Data (internal)
2. Identify Variables (internal)
3. Check Confounders (expert - from your protocol)
4. Test Counterfactuals (expert - from your protocol)
5. Validate Causality (internal)
6. Report Findings (internal)

Complexity: 7 (from your protocol.typical_complexity)
Expert needed: Yes (from your protocol.needs_expert)
```

### Step 3: Execution (Layer 2 + Sequential Thinking)

```
Step 1: Load Data
  ✅ Internal execution
  Result: DataFrame(500 rows, 8 cols)

Step 2: Identify Variables
  ✅ Internal execution  
  Result: variables = ["satisfaction", "engagement", "retention"]

Step 3: Check Confounders
  ⚠️ Complex → Spawn Expert
  
  Expert receives:
    - Your expert_excerpt for "Check Confounders"
    - Data context
    - Expected outputs: ["confounders_list", "confidence"]
  
  Expert executes following your checklist:
    ✓ Check temporal order
    ✓ Test independence
    ✓ Domain knowledge
  
  Expert returns:
    {
      "confounders_list": ["age", "tenure"],
      "confidence": 0.8
    }
  
  Validation (your criteria):
    ✅ confounders_list present
    ✅ confidence present
    ✅ Validation passed

Step 4: Test Counterfactuals
  ⚠️ Complex → Spawn Expert
  (Similar flow with your expert_excerpt)

Steps 5-6: Continue following protocol...
```

### Step 4: Output (Layer 3)

```
Layer 3 receives:
  - All step results
  - Protocol followed: Causal-Reasoning
  - Confidence: 0.85

Formats for user:
  "I analyzed your survey data using causal reasoning methodology.
   
   Key findings:
   - Engagement causally influences retention (p<0.05)
   - Confounders: age, tenure
   - Counterfactual test: Removing engagement → 30% retention drop
   
   Analysis followed Causal Reasoning Protocol with 85% confidence.
   
   [Complete report attached]"
```

---

## 🎯 Key Takeaways for Module Creators

### Your `when_to_use` determines selection:
- Be specific with task_patterns
- Accurate complexity_range
- Realistic uncertainty_tolerance

### Your `steps` become the execution:
- Clear, atomic phases
- Explicit outputs
- Testable validation

### Your `expert_excerpt` guides agents:
- Simplified for single step
- Actionable checklist
- Key principles only

### Your metadata informs planning:
- `typical_complexity` → resource allocation
- `needs_expert` → spawning decisions
- `compute_requirements` → budget

---

## 🔧 Testing Your Integration

### Unit Test (Simulated)

```python
# Test protocol selection
task = Task("Perform causal analysis of user behavior")
protocol = intelligence_modules.select_protocol(task)
assert protocol.name == "Causal-Reasoning"

# Test plan generation
idea = idea_generator.create_from_protocol(task, protocol)
assert len(idea.steps) == len(protocol.steps)
assert idea.complexity == protocol.typical_complexity

# Test validation
step_result = {
  "confounders_list": ["age"],
  "confidence": 0.8
}
validation = validator.check_protocol_compliance(
  step_result, 
  protocol.steps[2]  # "Check Confounders" step
)
assert validation.valid == True
```

### Integration Test (Real Execution)

```
1. Submit test task matching your protocol
2. Observe Layer 1 selects your protocol
3. Verify plan follows your steps
4. Check expert receives your excerpt
5. Validate outputs match your requirements
6. Confirm validation passes
```

---

## 📚 Advanced Topics

### Multiple Protocol Selection

If task matches multiple protocols:
- Highest confidence protocol selected
- Or user prompted to choose
- Or protocols combined (future feature)

### Protocol Chaining

Protocols can reference others:
```json
{
  "steps": [
    {
      "phase": "Decompose",
      "sub_protocol": "Plan-Act-Verify"
    }
  ]
}
```

### Dynamic Protocol Adjustment

Based on reflection data:
- Selection thresholds tuned
- Complexity estimates refined
- Expert needs updated

---

## 💬 Questions?

**Selection not working?** Check `when_to_use.task_patterns`  
**Steps not followed?** Verify `steps` structure  
**Validation failing?** Review `validation` criteria  
**Expert not getting excerpt?** Check `expert_excerpt` format

Refer to schema: `/intelligence-modules/schemas/protocol-schema.json`

---

**Last Updated:** 2026-01-08
