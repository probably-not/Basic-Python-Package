import os
import sys
# Set up a path adjustment so that the package we are testing is in our path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Any imports of our modules that need to be tested
from {{project_name}} import core
