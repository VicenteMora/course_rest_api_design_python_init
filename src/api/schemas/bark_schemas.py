from ninja import Schema

Class BarkSchemaOut(Schema):
    """Schema for Bark response."""
    id: int
    message: str