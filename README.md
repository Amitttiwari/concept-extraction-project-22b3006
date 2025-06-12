# concept-extraction-project-22b3006
# 🧠 Concept Extraction from Competitive Exam Questions

**Roll Number:** 22b3006  
**Submitted to:** `edme-tutor`  
**Subject:** AI/Data Tools for Education – UPSC/NTA Concept Mapping

---

## 📌 Objective

This project aims to analyze competitive exam questions (e.g., UPSC, CUET) and extract the **core conceptual topics** being tested in each question (like "Harappan Civilization", "Temple Education", or "Cyclic Geometry").

This helps:
- Understand topic distribution in past papers
- Enable curriculum gap analysis
- Aid in personalized learning and revision

---

## 📁 Repository Structure

.
├── main.py # Entry point: CLI and core pipeline
├── llm_api.py # Simulated concept extractor (LLM-ready)
├── csv_reader.py # Reads input CSVs from resources/
├── resources/ # Contains CSVs for ancient_history, math, etc.
│ ├── ancient_history.csv
│ ├── economics.csv
│ ├── math.csv
│ └── physics.csv
├── output_concepts.csv # Output with extracted concepts
├── requirements.txt # Required Python packages
├── Makefile # Shortcuts to run the code
└── README.md # This file


---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run the extractor for a subject
```
python main.py --subject=ancient_history
You can replace ancient_history with economics, math, or physics.
```
3. Output
```
A CSV file output_concepts.csv will be created in the root folder containing extracted concepts.
```
🧪 Simulated LLM Prompts & Output
Though actual LLM API calls are disabled (to avoid cost), we simulated results using a manual prompt format:

## 📋 Prompt Format:
Given the question: "<question text>", identify the historical concept(s) this question is based on.

## ✅ Example Questions & Concepts
Question	Extracted Concepts
Which of the following was a feature of the Harappan civilization?	Harappan Civilization; Urban Planning
Ghatikas were institutions associated with...?	Temple Education; Ancient Learning
Ganeshwar is known for...?	Chalcolithic Sites; Copper Artifacts
Sine of angle known in 5th century?	History of Indian Mathematics; Trigonometry
Money Multiplier is influenced by...?	Monetary Policy; Fractional Reserve Banking

## 🤖 Future Integration with LLMs
You can easily integrate a real LLM (e.g., OpenAI or Claude) by modifying the extract_concepts function in llm_api.py:

### llm_api.py
```
def extract_concepts(question):
    # Future API integration
    response = openai.ChatCompletion.create(
        model="gpt-4",
        prompt=f"Identify the concepts from this question: {question}",
        ...
    )
    return parse(response)

You can store your API key in .env as:
OPENAI_API_KEY=your-key-here



