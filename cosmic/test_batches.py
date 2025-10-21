from datetime import date
from batches import Batch, OrderLine

def test_allocating_to_a_batch_reduces_the_availability_quantity():
    # Given
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    # When    
    batch.allocate(line)
    # Then
    assert batch.available_quantity == 18