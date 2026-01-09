# Intelligence Modules Directory

This directory contains structured reasoning protocols for TRION.

## 📁 Structure

```
intelligence-modules/
├── README.md (this file)
├── schemas/
│   └── protocol-schema.json    # JSON schema for validation
└── protocols/
    └── (your protocols here)   # Submitted modules
```

## 📝 Module Format

Modules are JSON files following the schema in `/schemas/protocol-schema.json`.

**Required fields:**
- `name` - Protocol identifier
- `version` - Semantic versioning
- `description` - What it does
- `when_to_use` - Task patterns, complexity, uncertainty
- `steps` - Structured reasoning phases
- `expert_excerpt` - Simplified for agents
- `typical_complexity` - 1-10 scale

**Optional but recommended:**
- `advantages` - Benefits
- `limitations` - When not to use
- `examples` - Concrete applications
- `references` - Sources/inspirations

## ✅ Validation

Before submitting, validate against schema:

```bash
# Using Python jsonschema
python -c "
import json, jsonschema
schema = json.load(open('schemas/protocol-schema.json'))
protocol = json.load(open('your-protocol.json'))
jsonschema.validate(protocol, schema)
print('✅ Valid!')
"
```

## 📤 Submission

1. Create protocol JSON in this directory
2. Name it: `protocol-name.json` (kebab-case)
3. Validate against schema
4. Submit PR
5. We review and integrate

## 🎯 Priority Modules

We currently need:

1. **Plan-Act-Verify** (example provided)
   - Multi-step validation
   - Structured execution

2. **Bayesian-Update**
   - Confidence calibration
   - Uncertainty quantification

3. **Causal-Reasoning**
   - Confounder checking
   - Counterfactual testing

4. **Constraint-First**
   - Boundary conditions
   - Invariant identification

## 📖 Documentation

- Format details: `/CONTRIBUTING.md`
- Integration: `/docs/INTEGRATION_GUIDE.md`
- Example: `/examples/example-protocol.json`
- Schema: `/schemas/protocol-schema.json`

## 💬 Questions?

Open an issue with `intelligence-module` label.

---

**Last Updated:** 2026-01-08
