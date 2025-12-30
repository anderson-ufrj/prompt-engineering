# Test Suite for Prompt Engineering Lab

Author: Anderson Henrique da Silva  
Location: Minas Gerais, Brazil

## Overview

This test suite provides comprehensive testing for the Prompt Engineering Lab infrastructure, including:

- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end workflows with real data simulation
- **Performance Tests**: Metrics validation and analysis

## Test Structure

```
tests/
├── __init__.py
├── test_interaction_analyzer.py      # Metrics collection tests
├── test_experiment_runner.py         # A/B testing framework tests
├── test_version_manager.py           # Version management tests
└── test_integration_real_data.py     # Real data integration tests
```

## Running Tests

### Prerequisites

Install test dependencies:
```bash
pip install -r requirements.txt
```

### Run All Tests

```bash
# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=evidence --cov=experiments --cov=anderson_skill --cov-report=html

# Run specific test file
pytest tests/test_interaction_analyzer.py -v
```

### Run Integration Tests

```bash
# Run integration tests with real data simulation
python tests/test_integration_real_data.py

# Run specific components
pytest tests/test_integration_real_data.py::test_real_interactions -v
```

## Test Categories

### 1. Unit Tests (`test_*.py`)

**test_interaction_analyzer.py**:
- ✅ InteractionMetrics dataclass validation
- ✅ MetricsCollector data persistence
- ✅ Quality score distribution calculation
- ✅ Recommendation generation logic
- ✅ Data filtering by time periods

**test_experiment_runner.py**:
- ✅ ExperimentVariant creation
- ✅ Experiment lifecycle management
- ✅ Statistical analysis (A/B testing)
- ✅ Report generation
- ✅ Multiple variant comparison

**test_version_manager.py**:
- ✅ Semantic version bumping logic
- ✅ Change impact analysis
- ✅ File-based change detection
- ✅ Version history tracking
- ✅ Next change suggestions

### 2. Integration Tests (`test_integration_real_data.py`)

Real-world simulation including:
- 📊 Simulated interaction collection (20+ interactions)
- 🧪 A/B testing with realistic experiment design
- 🤖 Machine learning model training
- 📈 Performance dashboard generation
- 🔮 Calibration prediction testing

## Test Data

### Mock Interactions

The integration tests create realistic mock data:

```python
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
    # ... more interaction types
]
```

### Success Indicators

Based on quality scores:
- **High Quality (>0.8)**: task_completed, no_followup_needed, user_satisfied
- **Medium Quality (0.6-0.8)**: task_completed, minor_followup_needed
- **Low Quality (<0.6)**: task_incomplete, major_revisions_needed

## Coverage Goals

Target coverage: **76%+** (matching your DMMF profile)

Current coverage areas:
- ✅ Core functionality (90%+)
- ✅ Edge cases (80%+)
- ✅ Error handling (85%+)
- ⚠️ Integration scenarios (70%+)

## Continuous Integration

### Pre-commit Hooks

```bash
# Install pre-commit
pip install pre-commit
pre-commit install

# Run manually
pre-commit run --all-files
```

### GitHub Actions (suggested `.github/workflows/tests.yml`)

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest tests/ --cov=./ --cov-report=xml
    - name: Upload coverage
      uses: codecov/codecov-action@v1
```

## Performance Benchmarks

Expected performance:
- **Unit Tests**: < 5 seconds total
- **Integration Tests**: < 30 seconds
- **Coverage Report**: < 10 seconds
- **Real Data Simulation**: < 60 seconds

## Debugging Failed Tests

### Common Issues

1. **Import Errors**
   ```bash
   # Add parent directory to PYTHONPATH
   export PYTHONPATH=$PYTHONPATH:$(pwd)
   ```

2. **Missing Dependencies**
   ```bash
   # Install missing packages
   pip install -r requirements.txt
   ```

3. **File Permission Errors**
   ```bash
   # Fix permissions
   chmod +x tests/*.py
   ```

### Debug Mode

```bash
# Run with debug output
pytest tests/ --log-cli-level=DEBUG -s

# Run specific test with debugging
pytest tests/test_interaction_analyzer.py::TestMetricsCollector::test_capture_interaction -v -s
```

## Extending Tests

### Adding New Test Cases

1. Follow naming convention: `test_<component>_<feature>.py`
2. Use descriptive test method names
3. Include docstrings explaining test purpose
4. Use fixtures for setup/teardown
5. Assert specific conditions, not general states

### Example Test Structure

```python
def test_new_feature_specific_behavior(self):
    """Test that new feature handles specific input correctly"""
    # Arrange
    component = Component()
    test_input = "specific_input"
    expected_output = "expected_output"
    
    # Act
    result = component.process(test_input)
    
    # Assert
    assert result == expected_output
    assert component.state == "expected_state"
```

## Validation Checklist

Before committing:

- [ ] All unit tests pass
- [ ] Integration tests pass
- [ ] Code coverage > 76%
- [ ] No test warnings
- [ ] Tests are deterministic
- [ ] Mock data is realistic
- [ ] Documentation updated

## Future Enhancements

- [ ] Property-based testing with Hypothesis
- [ ] Performance benchmarking suite
- [ ] Load testing for metrics collection
- [ ] Chaos engineering tests
- [ ] Mutation testing
- [ ] Visual regression testing for dashboards

## Questions and Issues

Report issues: andersonhs27@gmail.com  
Include: test file, error message, expected vs actual behavior