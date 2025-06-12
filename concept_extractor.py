import re

KEYWORD_CONCEPT_MAP = {
    'harappan': 'Harappan Civilization',
    'ashoka': 'Ashokan Edicts',
    'edict': 'Ashokan Edicts',
    'vedic': 'Vedic Culture',
    'tank': 'Water Management',
    'brahmin': 'Brahmadeya System',
    'college': 'Temple-based Education',
    'sin': 'Indian Mathematics',
    'quadrilateral': 'Indian Geometry',
    'surgery': 'Ancient Indian Science',
    'transplant': 'Ancient Medicine',
    'planning': 'Urban Planning',
    'kautilya': 'Mauryan Empire',
    'terracotta': 'Material Culture',
}

def extract_concepts(text):
    concepts = set()
    text = text.lower()
    for keyword, concept in KEYWORD_CONCEPT_MAP.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', text):
            concepts.add(concept)
    return list(concepts)
