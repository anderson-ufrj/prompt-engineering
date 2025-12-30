#!/usr/bin/env python3
"""
Integration Tests with Real Data Collection
Author: Anderson Henrique da Silva
Location: Minas Gerais, Brazil

This script demonstrates how to integrate the metrics collection
with actual AI interactions and run experiments with real data.
"""

import json
import time
from pathlib import Path
from datetime import datetime
import sys
import os

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from src.metrics.interaction_analyzer import MetricsCollector, InteractionMetrics
from src.experiments.experiment_runner import ExperimentRunner, Experiment, ExperimentVariant
from src.calibration.auto_calibration import AutoCalibrationEngine

def simulate_real_interaction():
    """Simulate a real AI interaction for testing purposes"""
    
    # Simulate different types of interactions that might occur
    interaction_types = [
        {
            "context": ["anderson-skill", "debugging", "urgent"],
            "pattern": "chain",
            "prompt_tokens": 120,
            "response_tokens": 250,
            "response_time": 1100,
            "quality": 0.85,
            "iterations": 1,
            "type": "debugging_urgent"
        },
        {
            "context": ["anderson-skill", "brainstorming", "exploratory"],
            "pattern": "parallel",
            "prompt_tokens": 200,
            "response_tokens": 400,
            "response_time": 1800,
            "quality": 0.92,
            "iterations": 2,
            "type": "brainstorming_deep"
        },
        {
            "context": ["anderson-skill", "code-review", "technical"],
            "pattern": "evaluator",
            "prompt_tokens": 180,
            "response_tokens": 320,
            "response_time": 1500,
            "quality": 0.78,
            "iterations": 1,
            "type": "code_review"
        },
        {
            "context": ["anderson-skill", "interview-prep", "professional"],
            "pattern": "route",
            "prompt_tokens": 160,
            "response_tokens": 280,
            "response_time": 1300,
            "quality": 0.88,
            "iterations": 1,
            "type": "interview_prep"
        }
    ]
    
    import random
    interaction = random.choice(interaction_types)
    
    # Add some realistic variation
    interaction['response_time'] += random.randint(-200, 200)
    interaction['quality'] += random.uniform(-0.1, 0.1)
    interaction['quality'] = max(0.1, min(1.0, interaction['quality']))
    
    return interaction

def collect_real_interactions(num_interactions=10):
    """Collect a batch of simulated real interactions"""
    
    print(f"🔄 Collecting {num_interactions} real interactions...")
    
    collector = MetricsCollector()
    interactions_data = []
    
    for i in range(num_interactions):
        interaction = simulate_real_interaction()
        
        # Determine success indicators based on quality
        success_indicators = []
        if interaction['quality'] > 0.8:
            success_indicators.extend(["task_completed", "no_followup_needed", "user_satisfied"])
        elif interaction['quality'] > 0.6:
            success_indicators.extend(["task_completed", "minor_followup_needed"])
        else:
            success_indicators.extend(["task_incomplete", "major_revisions_needed"])
        
        metrics = InteractionMetrics(
            timestamp=datetime.now().isoformat(),
            prompt_tokens=interaction['prompt_tokens'],
            response_tokens=interaction['response_tokens'],
            response_time_ms=interaction['response_time'],
            quality_score=interaction['quality'],
            iteration_count=interaction['iterations'],
            context_used=interaction['context'],
            pattern_applied=interaction['pattern'],
            success_indicators=success_indicators
        )
        
        interaction_id = collector.capture_interaction(metrics)
        interactions_data.append({
            "id": interaction_id,
            "type": interaction['type'],
            "metrics": interaction
        })
        
        print(f"  ✅ Interaction {i+1}: {interaction['type']} (quality: {interaction['quality']:.2f})")
        time.sleep(0.1)  # Small delay to simulate real timing
    
    print(f"📊 Completed collection of {num_interactions} interactions")
    return interactions_data

def run_real_experiment():
    """Run an experiment with real collected data"""
    
    print("🧪 Running real experiment: 'Context Length vs Performance'...")
    
    runner = ExperimentRunner()
    
    # Create experiment comparing different context approaches
    experiment = Experiment(
        id="ctx-performance-001",
        name="Context Length vs Performance",
        hypothesis="Optimized context length improves response time by 20% without quality loss",
        variants=[
            ExperimentVariant(
                id="full-context",
                name="Full Context",
                prompt_template="Complete personal context + technical skills + situational mode",
                context_modifiers=["complete_context", "all_skills", "full_background"],
                expected_outcome="Highest quality but slower response",
                success_criteria=["quality_score > 0.85", "response_time < 2000"]
            ),
            ExperimentVariant(
                id="essential-context",
                name="Essential Context",
                prompt_template="Core identity + relevant skills only",
                context_modifiers=["core_identity", "relevant_skills", "minimal_background"],
                expected_outcome="Good quality with faster response",
                success_criteria=["quality_score > 0.80", "response_time < 1500"]
            ),
            ExperimentVariant(
                id="adaptive-context",
                name="Adaptive Context",
                prompt_template="Context adapted to task complexity and urgency",
                context_modifiers=["adaptive_load", "complexity_based", "urgency_aware"],
                expected_outcome="Optimal balance of quality and speed",
                success_criteria=["quality_score > 0.82", "response_time < 1700"]
            )
        ],
        control_variant="full-context",
        metrics_to_track=["quality_score", "response_time", "iteration_count", "user_satisfaction"],
        sample_size=50  # Use less data to simulate realistic constraints
    )
    
    experiment_id = runner.create_experiment(experiment)
    print(f"  ✅ Created experiment: {experiment_id}")
    
    # Run the experiment
    results = runner.run_experiment(experiment_id)
    
    if 'error' in results:
        print(f"  ❌ Experiment failed: {results['error']}")
        return None
    
    print(f"  🎯 Experiment completed!")
    print(f"     Winner: {results['winner']}")
    print(f"     Confidence: {results['confidence_level']:.1%}")
    print(f"     Statistical significance: {'Yes' if results['statistical_significance'] else 'No'}")
    
    # Print detailed results
    print("\n  📈 Detailed Results:")
    for variant_id, variant_data in results['variant_results'].items():
        print(f"     {variant_id}:")
        print(f"       Success Rate: {variant_data['success_rate']:.1%}")
        print(f"       Quality Score: {variant_data['avg_quality_score']:.2f}")
        print(f"       Response Time: {variant_data['avg_response_time']:.0f}ms")
    
    return results

def train_calibration_model():
    """Train the auto-calibration model with collected data"""
    
    print("🤖 Training auto-calibration model...")
    
    engine = AutoCalibrationEngine()
    
    # Collect sufficient data for training
    print("  📊 Collecting training data...")
    collector = MetricsCollector()
    
    # Check if we have enough existing data
    existing_report = collector.generate_report(days=30)
    
    if 'error' not in existing_report and existing_report['total_interactions'] >= 50:
        print(f"  ✅ Found {existing_report['total_interactions']} existing interactions")
        
        # Load existing interaction data for training
        import pandas as pd
        
        # Get all interaction files
        interaction_files = list(Path("evidence/metrics/data").glob("*.json"))
        interactions = []
        
        for file in interaction_files:
            try:
                with open(file) as f:
                    data = json.load(f)
                    interactions.append(data)
            except (json.JSONDecodeError, KeyError):
                continue
        
        print(f"  📋 Loaded {len(interactions)} interactions for training")
        
    else:
        print(f"  ⚠️  Insufficient data ({existing_report.get('total_interactions', 0)} interactions)")
        print("  🔄 Collecting additional training data...")
        
        # Collect more data
        collect_real_interactions(50)
        
        # Try again
        interaction_files = list(Path("evidence/metrics/data").glob("*.json"))
        interactions = []
        
        for file in interaction_files[:50]:  # Limit to 50 for training
            try:
                with open(file) as f:
                    data = json.load(f)
                    interactions.append(data)
            except (json.JSONDecodeError, KeyError):
                continue
    
    if len(interactions) < 10:
        print("  ❌ Insufficient data for training (need at least 10 interactions)")
        return False
    
    # Train the model
    print(f"  🎯 Training model with {len(interactions)} interactions...")
    training_result = engine.train_models(interactions)
    
    if 'error' in training_result:
        print(f"  ❌ Training failed: {training_result['error']}")
        return False
    
    print(f"  ✅ Model trained successfully!")
    print(f"     Accuracy: {training_result['model_accuracy']:.2%}")
    print(f"     Clusters found: {training_result['clusters_found']}")
    print(f"     Samples used: {training_result['samples_used']}")
    
    return True

def test_calibration_predictions():
    """Test the calibration model with sample contexts"""
    
    print("🔮 Testing calibration predictions...")
    
    engine = AutoCalibrationEngine()
    
    # Test different context scenarios
    test_contexts = [
        {
            "type": "debugging",
            "context_elements": ["anderson-skill", "debugging", "urgent"],
            "pattern": "chain",
            "prompt_tokens": 120,
            "urgency": 3
        },
        {
            "type": "brainstorming",
            "context_elements": ["anderson-skill", "brainstorming", "exploratory"],
            "pattern": "parallel",
            "prompt_tokens": 200,
            "urgency": 1
        },
        {
            "type": "interview",
            "context_elements": ["anderson-skill", "interview-prep", "professional"],
            "pattern": "route",
            "prompt_tokens": 160,
            "urgency": 2
        }
    ]
    
    for i, context in enumerate(test_contexts):
        try:
            prediction = engine.predict_optimal_config(context)
            
            print(f"\n  Context {i+1} ({context['type']}):")
            print(f"     Predicted success: {prediction.confidence:.1%}")
            print(f"     Recommendations: {len(prediction.recommended_adjustments)}")
            for rec in prediction.recommended_adjustments[:2]:  # Show top 2
                print(f"       - {rec}")
                
        except Exception as e:
            print(f"  ⚠️  Context {i+1} prediction failed: {e}")

def generate_comprehensive_report():
    """Generate a comprehensive performance report"""
    
    print("📊 Generating comprehensive performance report...")
    
    try:
        from evidence.dashboard import PerformanceDashboard
        
        dashboard = PerformanceDashboard()
        report = dashboard.generate_comprehensive_report(days=30)
        
        if 'error' in report:
            print(f"  ❌ Report generation failed: {report['error']}")
            return None
        
        print(f"  ✅ Report generated successfully!")
        print(f"     Total interactions: {report['total_interactions']}")
        print(f"     Average quality: {report['avg_quality_score']:.2f}")
        print(f"     Success rate: {report['success_rate']:.1%}")
        print(f"     Recommendations: {len(report['recommendations'])}")
        
        # Show trend analysis if available
        if 'trend_analysis' in report and 'quality_trend' in report['trend_analysis']:
            trend = report['trend_analysis']['quality_trend']
            print(f"     Quality trend: {trend['direction']} (R²: {trend['r_squared']:.3f})")
        
        return report
        
    except ImportError as e:
        print(f"  ⚠️  Dashboard dependencies not available: {e}")
        print("  💡 Install dependencies: pip install -r requirements.txt")
        return None

def main():
    """Main integration test function"""
    
    print("🚀 Starting Real Data Integration Tests")
    print("=" * 50)
    
    # Test 1: Collect real interactions
    print("\n1️⃣  Collecting Real Interactions")
    print("-" * 40)
    interactions = collect_real_interactions(20)
    
    # Test 2: Run real experiment
    print("\n2️⃣  Running Real Experiment")
    print("-" * 40)
    experiment_results = run_real_experiment()
    
    # Test 3: Train calibration model
    print("\n3️⃣  Training Calibration Model")
    print("-" * 40)
    training_success = train_calibration_model()
    
    # Test 4: Test calibration predictions
    if training_success:
        print("\n4️⃣  Testing Calibration Predictions")
        print("-" * 40)
        test_calibration_predictions()
    
    # Test 5: Generate comprehensive report
    print("\n5️⃣  Generating Performance Report")
    print("-" * 40)
    report = generate_comprehensive_report()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 INTEGRATION TEST SUMMARY")
    print("=" * 50)
    
    results = {
        "Interactions Collected": len(interactions) if interactions else 0,
        "Experiment Run": "✅ Success" if experiment_results else "❌ Failed",
        "Model Trained": "✅ Success" if training_success else "❌ Failed",
        "Report Generated": "✅ Success" if report else "❌ Failed"
    }
    
    for test, result in results.items():
        print(f"  {test}: {result}")
    
    print(f"\n🎯 Next Steps:")
    print(f"  1. Review generated reports in evidence/metrics/reports/")
    print(f"  2. Check experiment results in experiments/results/")
    print(f"  3. Use calibration model for future interactions")
    print(f"  4. Run pytest tests/test_*.py for unit test validation")
    
    print(f"\n✨ Integration tests completed!")

if __name__ == "__main__":
    main()