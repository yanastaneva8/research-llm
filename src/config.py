import ssl
from pathlib import Path                                                                                                                                                                                            

import yaml                                                                                                                                                                                                         
                
PROJECT_ROOT = Path(__file__).parent.parent                                                                                                                                                                         
CONFIG_PATH = PROJECT_ROOT / "config.yaml"
                                                                                                                                                                                                                    
# Fix SSL for arXiv on macOS                                                                                                                                                                                        
ssl._create_default_https_context = ssl._create_unverified_context                                                                                                                                                  
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
def load_config():                                                                                                                                                                                                  
    with open(CONFIG_PATH) as f:                                                                                                                                                                                    
        return yaml.safe_load(f)                                                                                                                                                                                    
                                                                                                                                                                                                                    
                                                                                                                                                                                                                    
# Paths                                                                                                                                                                                                             
DATA_DIR = PROJECT_ROOT / "data"                                                                                                                                                                                    
RAW_DIR = DATA_DIR / "arxiv_raw"                                                                                                                                                                                    
METADATA_DIR = DATA_DIR / "metadata"                                                                                                                                                                                
CHUNKS_DIR = DATA_DIR / "chunks"                                                                                                                                                                                    
CHROMADB_DIR = DATA_DIR / "chromadb"                                                                                                                                                                                
OUTPUT_DIR = PROJECT_ROOT / "output"                                                                                                                                                                                
STYLE_DIR = PROJECT_ROOT / "style_papers"                                                                                                                                                                           
                                                                                                                                                                                                                    
# Ollama                                                                                                                                                                                                            
OLLAMA_URL = "http://localhost:11434"                                                                                                                                                                               
LLM_MODEL = "mistral"                                                                                                                                                                                               
EMBED_MODEL = "nomic-embed-text"                                                                                                                                                                                    
                                                                                                                                                                                                                    
