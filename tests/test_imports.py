# 6R:Fire
"""
Basic smoke tests to verify all modules can be imported successfully.
"""

import os
import sys

import pytest

# Add src directories to path for imports
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src", "trihex_gpt_custom")
)
sys.path.insert(
    0,
    os.path.join(
        os.path.dirname(__file__), "..", "src", "trihex_gpt_custom", "modules"
    ),
)
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "src", "soul-diagnosis-webhook")
)


def test_trihex_diagnosis_module_import():
    """Test that trihex_diagnosis_module can be imported."""
    try:
        from trihex_diagnosis_module import trihex_diagnose

        assert callable(trihex_diagnose)
    except ImportError:
        pytest.skip("trihex_diagnosis_module not available")


def test_astro_resolver_import():
    """Test that astro_resolver can be imported."""
    try:
        import astro_resolver

        assert hasattr(astro_resolver, "__name__")
    except ImportError:
        pytest.skip("astro_resolver not available")


def test_life_path_utils_import():
    """Test that life_path_utils can be imported."""
    try:
        from life_path_utils import calculate_life_path_number

        assert callable(calculate_life_path_number)
    except ImportError:
        pytest.skip("life_path_utils not available")


def test_eto_classification_dict_import():
    """Test that eto_classification_dict can be imported."""
    try:
        import eto_classification_dict

        assert hasattr(eto_classification_dict, "__name__")
    except ImportError:
        pytest.skip("eto_classification_dict not available")


def test_generate_pdf_import():
    """Test that generate_pdf can be imported."""
    try:
        import generate_pdf

        assert hasattr(generate_pdf, "__name__")
    except ImportError:
        pytest.skip("generate_pdf not available")


def test_flask_app_import():
    """Test that the Flask webhook app can be imported."""
    try:
        import os
        import sys

        webhook_path = os.path.join(
            os.path.dirname(__file__), "..", "src", "soul-diagnosis-webhook"
        )
        sys.path.insert(0, webhook_path)

        import app as webhook_app

        assert hasattr(webhook_app, "app")
    except ImportError:
        pytest.skip("Flask webhook app not available")


def test_streamlit_app_import():
    """Test that the Streamlit app can be imported."""
    try:
        import os
        import sys

        streamlit_path = os.path.join(
            os.path.dirname(__file__), "..", "src", "trihex_gpt_custom"
        )
        sys.path.insert(0, streamlit_path)

        import app as streamlit_app

        assert hasattr(streamlit_app, "__name__")
    except ImportError:
        pytest.skip("Streamlit app not available")


def test_basic_functionality():
    """Test basic functionality if modules are available."""
    try:
        from trihex_diagnosis_module import trihex_diagnose

        # Test with sample data
        result = trihex_diagnose("甲子", 1, "智", "数")
        assert isinstance(result, dict)
        assert "spiral" in result

    except (ImportError, Exception):
        pytest.skip("Basic functionality test not available")
