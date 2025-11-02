from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

# Response Models
class CheckResult(BaseModel):
    """Result from a single forensic check"""
    risk_score: int = Field(ge=0, le=100, description="Risk score from 0 (safe) to 100 (high risk)")
    applicable: bool = Field(default=True, description="Whether this check applies to the document")
    issues: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of issues found")
    flags: Optional[List[str]] = Field(default=None, description="Warning flags")
    details: Optional[Dict[str, Any]] = Field(default=None, description="Additional details")
    error: Optional[str] = Field(default=None, description="Error message if check failed")

class ForensicAnalysisResponse(BaseModel):
    """Complete forensic analysis results"""
    overall_score: float = Field(ge=0, le=100, description="Overall risk score")
    risk_level: str = Field(description="Risk level: LOW, MEDIUM, or HIGH")
    
    # Individual check results
    alignment: CheckResult = Field(description="Text alignment analysis")
    fonts: CheckResult = Field(description="Font consistency analysis")
    metadata: CheckResult = Field(description="PDF metadata analysis")
    numbers: CheckResult = Field(description="Number pattern analysis")
    image: CheckResult = Field(description="Image quality analysis")
    page_numbers: Optional[CheckResult] = Field(default=None, description="Page numbering check (NOA only)")
    noa_id_check: Optional[CheckResult] = Field(default=None, description="ID duplicate detection (NOA only)")
    
    # Metadata
    processing_time: float = Field(description="Analysis time in seconds")
    timestamp: datetime = Field(default_factory=datetime.now, description="Analysis timestamp")
    file_name: str = Field(description="Original file name")
    doc_type: str = Field(description="Document type analyzed")

class ForensicRecordResponse(BaseModel):
    """Forensic database record"""
    id: int
    identification_number: str
    sin_last_4: Optional[str] = None
    full_name: Optional[str] = None
    date_issued: Optional[str] = None
    uploaded_timestamp: str
    file_name: str

class DuplicateDetectionResponse(BaseModel):
    """Duplicate ID detection record"""
    id: int
    identification_number: str
    original_file_name: str
    duplicate_file_name: str
    detected_timestamp: str

class ErrorResponse(BaseModel):
    """Error response model"""
    error: str
    detail: str
    type: Optional[str] = None

