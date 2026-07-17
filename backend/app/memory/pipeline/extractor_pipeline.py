"""
Memory Extraction Pipeline
==========================

Coordinates every registered Memory Extractor.

Responsibilities
----------------

• Execute extractors
• Maintain extraction order
• Keep MemoryManager independent from extraction logic

The pipeline owns orchestration.

Extractors own business logic.
"""

from app.memory.extractor.architecture_extractor import ArchitectureExtractor
from app.memory.extractor.business_extractor import BusinessExtractor
from app.memory.extractor.decision_extractor import DecisionExtractor
from app.memory.extractor.review_extractor import ReviewExtractor
from app.memory.extractor.workflow_extractor import WorkflowExtractor
from app.memory.extractor.artifact_extractor import ArtifactExtractor

class ExtractionPipeline:

    def __init__(self):

        self.extractors = [

            
        BusinessExtractor(),
    
        ArchitectureExtractor(),
    
        DecisionExtractor(),
    
        ReviewExtractor(),
    
        ArtifactExtractor(),
    
        WorkflowExtractor(),

        ]

    def execute(
        self,
        session,
        artifact,
        manager,
    ):
        """
        Execute every registered extractor.
        """

        for extractor in self.extractors:

            extractor.extract(
                session=session,
                artifact=artifact,
                manager=manager,
            )