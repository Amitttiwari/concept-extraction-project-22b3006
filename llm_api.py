# Placeholder for concept extraction
def extract_concepts(question):
    # Simulate using keyword-based mapping (replace with LLM later)
    mappings = {
        "harappan": "Harappan Civilization",
        "ashoka": "Ashokan Edicts",
        "guild": "Ancient Trade & Economy",
        "edicts": "Mauryan Empire",
        "temple": "Temple-based Education",
        "quadrilateral": "Indian Geometry",
        "sine": "Ancient Trigonometry",
        "land revenue": "Revenue System",
        "brahmin": "Brahmadeya Grants",
        "science": "Indian Science History",
        "flux": "Electromagnetism",
        "proton": "Atomic Theory",
        "price": "Cost Price & Selling Price",
        "income": "Microeconomics",
        "demand": "Market Dynamics"
    }

    concepts = set()
    lowered = question.lower()
    for keyword, concept in mappings.items():
        if keyword in lowered:
            concepts.add(concept)
    
    return list(concepts) if concepts else ["General Concept"]
