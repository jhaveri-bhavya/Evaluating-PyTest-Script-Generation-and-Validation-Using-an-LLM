## Here is the pytest test file:

import pytest
from solutions.square_perimeter import square_perimeter

def test_square_perimeter():
    assert square_perimeter(10) == 40
    assert square_perimeter(5) == 20
    assert square_perimeter(4) == 16
```

# To run the test, you can use the command `pytest -v` in the terminal.

# Please note that the `solutions` directory should be in the same directory as your `square_perimeter.py` file. If it's not, you'll need to specify the full path to the `solutions` directory.