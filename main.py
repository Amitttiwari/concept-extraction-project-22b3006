import argparse
import csv
from csv_reader import read_csv
from llm_api import extract_concepts

def main(subject):
    df = read_csv(subject)
    if df is None:
        return

    output_rows = [("Question Number", "Question", "Concepts")]

    for _, row in df.iterrows():
        q_num = row.get("question number", "N/A")
        question = row.get("question", "")
        concepts = extract_concepts(question)
        output_rows.append((q_num, question, "; ".join(concepts)))

    # Save to output file
    with open("output_concepts4.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(output_rows)
    
    print(f"✅ Concepts written to output_concepts.csv for subject: {subject}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--subject', required=True, help="Subject file name without .csv")
    args = parser.parse_args()
    main(args.subject)


