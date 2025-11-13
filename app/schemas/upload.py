from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class DetectedObject(BaseModel):
    type: str  # power_line, transformer, pole, etc.
    confidence: float
    bbox: List[int]  # [x1, y1, x2, y2]

class AnalysisResult(BaseModel):
    detected_objects: List[DetectedObject]
    overall_condition: str  # good, warning, critical
    issues_found: List[str]
    recommendations: List[str]

class UploadResponse(BaseModel):
    message: str
    file_id: str
    filename: str
    file_url: str
    analysis_result: AnalysisResult
    status: str

class ProcessingHistoryEntry(BaseModel):
    id: str
    user_id: str
    filename: str
    file_url: str
    uploaded_at: datetime
    analysis_result: AnalysisResult
    status: str  # processing, completed, failed