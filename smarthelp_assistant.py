# Clinical Symptom Risk Triage Assistant
# ======================================
# - We are building a probabiitic decision support tool for symptom-based triage using a Naive Bayes style classifier
# - Using: Python, Probability, uncertainty modeling, naive Bayes, lightwieght clinical decision support, interpretable scoring
# - Program learns probability patterns from labeled symptoms data.
# - Important Note: This is a teaching demo project, and not a valid system

from collections import Counter, defaultdict
from math import log

def train_naive_bayes(training_data, feature_names, label_name):
    label_counts = Counter(row[label_name] for row in training_data)
    total_rows = len(training_data)

    labels = sorted(label_counts.keys())
    priors = {}
    for label in labels:
        priors[label] = label_counts[label] / total_rows
    
    possible_feature_values = {feature: set() for feature in feature_names}
    for row in training_data:
        for feature in feature_names:
            possible_feature_values[feature].add(row[feature])
    
    likelihoods = {feature: defaultdict(dict) for feature in feature_names}
    for feature in feature_names:
        values = possible_feature_values[feature]

        for label in labels:
            subset = [row for row in training_data if row[label_name] == label]
            subset_count = len(subset)

            value_counts = Counter(row[feature] for row in subset)

            for value in values:
                
                likelihoods[feature][label][value] = (
                    value_counts[value] + 1
                ) / (subset_count + len(values))

    return priors, likelihoods, labels, possible_feature_values

def predict_naive_bayes(case, priors, likelihoods, labels):
    scores = {}
    for label in labels:
        score = log(priors[label])

        for feature, value in case.items(): 
            if feature in likelihoods and value in likelihoods[feature][label]:
                score += log(likelihoods[feature][label][value])

        scores[label] = score 
    
    predicted_label = max(scores, key=scores.get)
    return predicted_label, scores

def main():
    print("=" * 40) 
    print("Clinical Symptom Risk Triage Assistant")
    print("=" * 40)

    
    training_data = [
        {"fever": "yes", "cough": "yes", "sneezing": "no", "body_aches": "yes", "condition": "flu"},
        {"fever": "yes", "cough": "no", "sneezing": "no", "body_aches": "yes", "condition": "flu"},
        {"fever": "no", "cough": "no", "sneezing": "yes", "body_aches": "no", "condition": "allergy"},
        {"fever": "no", "cough": "no", "sneezing": "yes", "body_aches": "no", "condition": "allergy"},
        {"fever": "no", "cough": "yes", "sneezing": "yes", "body_aches": "no", "condition": "allergy"},
    ]

    feature_names = ["fever", "cough", "sneezing", "body_aches"]
    label_name = "condition"

    priors, likelihoods, labels, possible_feature_values = train_naive_bayes(
        training_data,
        feature_names,
        label_name
    )

    print("\nClass Priors:")
    for label, value in priors.items():
        print(f" P({label}) = {value:.3f}")

    test_cases = [
        {"fever": "yes", "cough": "yes", "sneezing": "no", "body_aches": "yes"},
        {"fever": "no", "cough": "yes", "sneezing": "yes", "body_aches": "no"},
        {"fever": "yes", "cough": "no", "sneezing": "yes", "body_aches": "no"},
    ]

    
    for i, case in enumerate(test_cases, start=1):
        prediction, scores = predict_naive_bayes(case, priors, likelihoods, labels)

        print(f"\nPatient Case {i}")
        print("-" * 20) 
        print(f"Symptoms: {case}")
        print(f"Predicted Condition: {prediction}")
        print("Log Scores:")
        for label, score in scores.items():
            print(f" {label}: {score:.4f}")

if __name__ == "__main__":
    main()
