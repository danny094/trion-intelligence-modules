# TRION Architecture Overview

**Simplified overview for Intelligence Module collaboration**

## 🎯 Core Philosophy

**TRION** = **TRI**-layer **O**perating **N**etwork

AI should be:
- **OWNED** not rented
- **LOCAL** not cloud  
- **ACCESSIBLE** not exclusive
- **TRANSPARENT** not black-box
- **RELIABLE** not unpredictable

## 🏗️ Three-Layer Architecture

```
┌─────────────────────────────────────────────────────────┐
│ USER INPUT                                              │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 1: THINKING (DeepSeek-R1:8b)                     │
│                                                         │
│ Purpose: Recognize, Plan, Structure                    │
│                                                         │
│ Responsibilities:                                       │
│ ├─ Intent Classification                               │
│ ├─ ⭐ Protocol Selection (Intelligence Modules)        │
│ ├─ Sequential Plan Generation                          │
│ ├─ Memory Needs Detection                             │
│ └─ Confidence Signals                                  │
│                                                         │
│ Output: Structured execution plan with protocol        │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 2: CONTROL (Qwen3:4b)                            │
│                                                         │
│ Purpose: Validate, Execute, Supervise                  │
│                                                         │
│ Responsibilities:                                       │
│ ├─ Safety Validation                                   │
│ ├─ Policy Compliance                                   │
│ ├─ Sequential Execution (15-component engine)          │
│ ├─ Budget Management (tokens, time, experts)           │
│ ├─ Checkpoint Evaluation (prevent runaway)             │
│ ├─ Error Handling & Recovery                          │
│ └─ Expert Spawning Decisions                          │
│                                                         │
│ Note: Control ALWAYS decides, never the agent          │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│ LAYER 3: OUTPUT (Llama3.1:8b or similar)               │
│                                                         │
│ Purpose: Format, Style, Deliver                        │
│                                                         │
│ Responsibilities:                                       │
│ ├─ Result Integration                                  │
│ ├─ Persona Style Application                          │
│ ├─ Natural Language Generation                        │
│ └─ User-Friendly Formatting                           │
└─────────────────────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────┐
│ USER OUTPUT                                             │
└─────────────────────────────────────────────────────────┘
```

## 💡 Why Three Layers?

**Separation of Concerns:**
- **Thinking** ≠ **Control** ≠ **Style**
- Different roles, different models
- Clean interfaces between layers

**Benefits:**
- Modularity (swap models independently)
- Testability (test each layer separately)
- Reliability (failures contained)
- Transparency (clear decision boundaries)

## 🧠 Sequential Thinking Engine

**15-component execution framework** that provides:

### Core Components (11)

**Planning Group:**
1. Memory Manager - Context preservation
2. Idea Generator - Solution approaches ⭐ Uses Intelligence Modules
3. Complexity Estimator - Resource prediction ⭐ Protocol-aware
4. Prioritizer - Importance ranking

**Execution Group:**
5. Todo Tracker - Queue management
6. Dependency Manager - Ordering & parallelism
7. Error Handler - Recovery strategies
8. Validator - Quality control ⭐ Protocol compliance

**Optimization Group:**
9. Time Estimator - Duration prediction
10. Resource Manager - Budget control
11. Documentation Logger - Audit trail

### Meta-Layers (4)

**Safety & Control layers:**
- **Checkpoint Manager** - Prevents runaway execution
- **Cognitive Budget** - Prevents cost explosion  
- **Partial Success** - Graceful degradation
- **Reflection Logger** - Continuous improvement

## 🎯 Skill-Agent System

**Ephemeral task experts** for complex steps:

**Key Properties:**
- **Lifetime:** Single task only
- **Autonomy:** Zero (tools provided, no discovery)
- **Memory:** None (stateless)
- **Scope:** Narrow (one step)
- **Control:** Layer 2 always decides

**Integration with Intelligence Modules:**
When expert spawned, receives:
- Task description
- **Protocol excerpt** ⭐ (simplified from full protocol)
- Context data
- Expected outputs

→ Expert follows protocol structure → consistent quality!

## 🔗 Where Intelligence Modules Fit

```
User: "Complex task"
      ↓
Layer 1: 
  - Recognizes task type
  - ⭐ Retrieves Intelligence Module (your protocol)
  - Creates plan following protocol steps
      ↓
Sequential Thinking:
  - Uses protocol as template (Idea Generator)
  - Knows protocol complexity (Complexity Estimator)
  - Validates protocol compliance (Validator)
      ↓
Layer 2:
  - Executes steps sequentially
  - For complex step: spawns expert with protocol excerpt
      ↓
Skill-Agent:
  - Receives protocol guidance
  - Executes following structure
  - Returns validated result
      ↓
Layer 3:
  - Integrates all results
  - Formats for user
```

## 💾 Memory System

**Three types of memory:**

**Short-Term Memory (STM)**
- Current conversation facts
- Recent context
- Active task state

**Long-Term Memory (LTM)**  
- Important persistent facts
- User preferences
- Historical patterns

**Knowledge Graph**
- Semantic relationships (concept connections)
- Temporal edges (time-based)
- Co-occurrence (patterns)

**Storage:**
- PostgreSQL + pgvector (semantic search)
- NetworkX (graph operations)
- Importance scoring + time decay

## 🔧 System Specifications

**Hardware:**
- GPU: RTX 2060 SUPER (5GB VRAM)
- CPU: Decent multi-core
- RAM: 16GB+

**Models:**
- Layer 1: DeepSeek-R1:8b (7GB model)
- Layer 2: Qwen3:4b (2.5GB model)  
- Layer 3: Llama3.1:8b (4.7GB model)

**Execution:**
- Sequential (one model at a time)
- No model parallelism (VRAM constraint)
- Efficient model swapping

**Performance:**
- End-to-end: 18-30 seconds
- Layer 1: 5-8s
- Layer 2: 8-15s
- Layer 3: 5-7s

**Cost:**
- Zero API costs (fully local)
- Zero per-token fees
- Zero rate limits

## 🎯 Design Principles

### 1. Control Supremacy
**Layer 2 always decides**
- Layer 1 provides signals, not commands
- Experts provide data, not decisions
- Control evaluates and chooses

### 2. Transparency
**Everything is logged**
- All decisions documented
- Full audit trail
- No black boxes

### 3. Fail-Safe
**Graceful degradation**
- Partial results > complete failure
- Clear error messages
- Recovery strategies

### 4. Local-First
**No cloud dependency**
- Runs entirely on-premise
- No API keys needed
- Complete data privacy

### 5. Modularity
**Components are swappable**
- Different models per layer
- Protocol-based interfaces
- Easy testing & iteration

## 📊 Current Status

**Production-Ready:**
- ✅ 3-layer pipeline operational
- ✅ Memory system (25 STM, 65 nodes, 923 edges)
- ✅ WebUI for persona management
- ✅ Admin API (13 endpoints)
- ✅ Sequential Thinking designed
- ✅ Skill-Agent architecture designed

**In Development:**
- 🔄 Intelligence Modules integration (your work!)
- 🔄 Sequential Thinking implementation
- 🔄 Skill-Agent foundation
- 🔄 Dynamic protocol selection

**Success Metrics:**
- Test coverage: 83.3% (10/12 passing)
- Memory ops: 100% functional
- Pipeline: 100% operational
- Documentation: Comprehensive

## 🚀 Where We're Going

**Phase 1: Intelligence Modules (Current)**
- Integrate procedural reasoning protocols
- Enable protocol-guided execution
- Improve task breakdown quality

**Phase 2: Sequential Thinking**
- Full 15-component implementation
- Cognitive budget enforcement
- Checkpoint system

**Phase 3: Skill-Agents**
- Expert library
- Protocol-guided agents
- Multi-expert coordination

**Phase 4: Optimization**
- Reflection-based improvements
- Performance tuning
- Scale testing

## 📚 Further Reading

- `SEQUENTIAL_THINKING.md` - 15-component engine details
- `SKILL_AGENTS.md` - Ephemeral expert system
- `INTEGRATION_GUIDE.md` - How modules integrate

## 💬 Questions?

Open an issue or refer to main documentation.

---

**Last Updated:** 2026-01-08  
**Status:** Production System with Active Development
