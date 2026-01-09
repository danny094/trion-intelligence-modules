"""
Example: How TRION uses Intelligence Modules

This shows the integration between protocols and execution.
"""

from typing import Dict, List, Any
import json

# ============================================================================
# MOCK CLASSES (Simplified for illustration)
# ============================================================================

class Task:
    def __init__(self, description: str):
        self.description = description
        self.keywords = description.lower().split()

class Protocol:
    def __init__(self, data: Dict):
        self.name = data['protocol']['name']
        self.steps = data['protocol']['steps']
        self.when_to_use = data['protocol']['when_to_use']
        self.typical_complexity = data['protocol']['typical_complexity']
        self.needs_expert = data['protocol']['needs_expert']
        self.expert_excerpt = data['protocol']['expert_excerpt']

class IntelligenceModuleLibrary:
    def __init__(self, protocols_dir: str = './intelligence-modules/protocols/'):
        self.protocols = self.load_protocols(protocols_dir)
    
    def load_protocols(self, directory: str) -> List[Protocol]:
        """Load all protocol JSON files"""
        # In real implementation, scan directory for *.json
        # For demo, load example protocol
        with open('./examples/example-protocol.json') as f:
            data = json.load(f)
        return [Protocol(data)]
    
    def select_protocol(self, task: Task) -> Protocol:
        """
        Select protocol based on task patterns
        """
        for protocol in self.protocols:
            task_patterns = protocol.when_to_use['task_patterns']
            
            # Check if any pattern matches task keywords
            matches = sum(1 for pattern in task_patterns 
                         if any(word in task.keywords for word in pattern.split('-')))
            
            if matches >= 2:  # Threshold for match
                print(f"✅ Selected protocol: {protocol.name}")
                return protocol
        
        print("⚠️  No protocol matched, using fallback")
        return None

# ============================================================================
# INTEGRATION POINT 1: Idea Generator
# ============================================================================

class IdeaGenerator:
    def __init__(self):
        self.intelligence_modules = IntelligenceModuleLibrary()
    
    def generate(self, task: Task) -> Dict[str, Any]:
        """
        Generate execution plan using Intelligence Module
        """
        print(f"\n📋 Generating ideas for: '{task.description}'")
        
        # ⭐ Try to find matching protocol
        protocol = self.intelligence_modules.select_protocol(task)
        
        if protocol:
            # Use protocol as template
            plan = self.create_from_protocol(task, protocol)
            print(f"✅ Created structured plan from {protocol.name}")
            return plan
        else:
            # Fallback to heuristic brainstorming
            print("⚠️  Using fallback brainstorming")
            return self.brainstorm(task)
    
    def create_from_protocol(self, task: Task, protocol: Protocol) -> Dict:
        """Create execution plan from protocol"""
        return {
            'approach': f"Follow {protocol.name} protocol",
            'steps': [
                {
                    'phase': step['phase'],
                    'description': step['description'],
                    'outputs': step['outputs'],
                    'validation': step['validation']
                }
                for step in protocol.steps
            ],
            'complexity': protocol.typical_complexity,
            'needs_expert': protocol.needs_expert,
            'confidence': 0.9  # High because structured
        }
    
    def brainstorm(self, task: Task) -> Dict:
        """Fallback brainstorming"""
        return {
            'approach': 'Heuristic approach',
            'steps': ['Analyze', 'Execute', 'Verify'],
            'complexity': 5,
            'confidence': 0.6
        }

# ============================================================================
# INTEGRATION POINT 2: Complexity Estimator
# ============================================================================

class ComplexityEstimator:
    def __init__(self):
        self.intelligence_modules = IntelligenceModuleLibrary()
    
    def estimate(self, task: Task) -> Dict[str, Any]:
        """
        Estimate complexity with protocol awareness
        """
        print(f"\n📊 Estimating complexity for: '{task.description}'")
        
        # Check if protocol available
        protocol = self.intelligence_modules.select_protocol(task)
        
        if protocol:
            # ⭐ Use protocol's complexity rating
            print(f"✅ Using protocol complexity: {protocol.typical_complexity}/10")
            return {
                'complexity': protocol.typical_complexity,
                'expert_recommended': protocol.needs_expert,
                'protocol_available': True,
                'protocol_name': protocol.name
            }
        else:
            # Fallback heuristic
            print("⚠️  Using heuristic estimation")
            return {
                'complexity': 5,
                'expert_recommended': False,
                'protocol_available': False
            }

# ============================================================================
# INTEGRATION POINT 3: Validator
# ============================================================================

class Validator:
    def check_protocol_compliance(self, result: Dict, protocol_step: Dict) -> Dict:
        """
        Validate result against protocol requirements
        """
        print(f"\n✅ Validating against protocol step: {protocol_step['phase']}")
        
        required_outputs = protocol_step['outputs']
        issues = []
        
        # Check if all required outputs present
        for output in required_outputs:
            if output not in result:
                issues.append(f"Missing output: {output}")
        
        # Check validation criteria
        validation_text = protocol_step['validation']
        # In real implementation, would evaluate validation programmatically
        
        valid = len(issues) == 0
        
        print(f"{'✅ Valid' if valid else '❌ Invalid'}: {len(issues)} issues")
        
        return {
            'valid': valid,
            'issues': issues,
            'confidence': 1.0 - (len(issues) * 0.2)
        }

# ============================================================================
# DEMO: Complete Flow
# ============================================================================

def demo_complete_flow():
    """
    Demonstrate complete integration flow
    """
    print("=" * 70)
    print("TRION Intelligence Module Integration Demo")
    print("=" * 70)
    
    # User task
    task = Task("Create a multi-step data analysis with validation at each phase")
    
    # ──────────────────────────────────────────────────────────
    # Step 1: Idea Generation with Protocol
    # ──────────────────────────────────────────────────────────
    idea_generator = IdeaGenerator()
    plan = idea_generator.generate(task)
    
    print("\n📝 Generated Plan:")
    print(f"  Approach: {plan['approach']}")
    print(f"  Complexity: {plan['complexity']}/10")
    print(f"  Steps: {len(plan['steps'])}")
    for i, step in enumerate(plan['steps'], 1):
        print(f"    {i}. {step['phase']}: {step['description'][:50]}...")
    
    # ──────────────────────────────────────────────────────────
    # Step 2: Complexity Estimation with Protocol
    # ──────────────────────────────────────────────────────────
    complexity_estimator = ComplexityEstimator()
    complexity = complexity_estimator.estimate(task)
    
    print(f"\n📊 Complexity Assessment:")
    print(f"  Complexity: {complexity['complexity']}/10")
    print(f"  Expert Recommended: {complexity['expert_recommended']}")
    print(f"  Protocol Available: {complexity['protocol_available']}")
    
    # ──────────────────────────────────────────────────────────
    # Step 3: Execution (Simulated)
    # ──────────────────────────────────────────────────────────
    print(f"\n▶️  Executing Plan (Simulated)...")
    
    # Simulate first step execution
    step = plan['steps'][0]
    print(f"\n  Executing: {step['phase']}")
    
    # Simulated result
    result = {
        'step_list': ['Load data', 'Validate', 'Analyze'],
        'success_criteria': ['Data loaded', 'No errors'],
        'dependencies': [],
        'resource_estimates': {'time': 30, 'tokens': 1000}
    }
    
    # ──────────────────────────────────────────────────────────
    # Step 4: Validation with Protocol
    # ──────────────────────────────────────────────────────────
    validator = Validator()
    validation = validator.check_protocol_compliance(result, step)
    
    print(f"\n✅ Validation Result:")
    print(f"  Valid: {validation['valid']}")
    print(f"  Confidence: {validation['confidence']:.2f}")
    if validation['issues']:
        print(f"  Issues: {validation['issues']}")
    
    print("\n" + "=" * 70)
    print("✅ Demo Complete - Intelligence Module Integration Working!")
    print("=" * 70)

if __name__ == '__main__':
    demo_complete_flow()
