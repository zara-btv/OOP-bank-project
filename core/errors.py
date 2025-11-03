class NegativeAmountError(Exception):
    """Raised when a negative amount is used in deposit or withdraw."""
    pass

class InsufficientAmountError(Exception):
    """Raised when withdrawal exceeds available balance."""
    pass
