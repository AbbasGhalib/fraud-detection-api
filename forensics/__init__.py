"""
Document Forensics Module
Independent forensic analysis for any PDF document
"""

from .forensic_analyzer import analyze_document_forensics
from .visualizer import create_forensic_visualizations
from .checks import (
    check_text_alignment,
    check_font_consistency,
    check_metadata,
    check_number_patterns,
    check_image_quality
)

__all__ = [
    'analyze_document_forensics',
    'create_forensic_visualizations',
    'check_text_alignment',
    'check_font_consistency',
    'check_metadata',
    'check_number_patterns',
    'check_image_quality'
]

