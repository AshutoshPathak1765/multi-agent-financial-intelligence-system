from enum import Enum


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    
class ToolStrategy(str, Enum):
    RAG = "rag"
    SEARCH = "search"
    BOTH = "both"
    NONE = "none"
    
class CriticDecision(str, Enum):
    APPROVED = "approved"
    RETRY = "retry"