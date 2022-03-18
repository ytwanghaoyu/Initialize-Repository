# -*- coding: utf-8 -*-

import pytest
import my_repo


def test_read_version():
    assert hasattr(my_repo, "__version__")


if __name__ == "__main__":
    pytest.main(["-s", __file__])
