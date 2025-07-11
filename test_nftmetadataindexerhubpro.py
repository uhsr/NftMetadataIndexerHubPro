# test_nftmetadataindexerhubpro.py
"""
Tests for NftMetadataIndexerHubPro module.
"""

import unittest
from nftmetadataindexerhubpro import NftMetadataIndexerHubPro

class TestNftMetadataIndexerHubPro(unittest.TestCase):
    """Test cases for NftMetadataIndexerHubPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerHubPro()
        self.assertIsInstance(instance, NftMetadataIndexerHubPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerHubPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
