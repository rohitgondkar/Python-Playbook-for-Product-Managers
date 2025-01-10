
def prioritize_roadmap(features):
    # Scoring model: Impact * Confidence / Effort
    for feature in features:
        feature['score'] = feature['impact'] * feature['confidence'] / feature['effort']
    return sorted(features, key=lambda x: x['score'], reverse=True)

# Example usage
if __name__ == "__main__":
    roadmap = [
        {'name': 'Feature A', 'impact': 8, 'confidence': 7, 'effort': 4},
        {'name': 'Feature B', 'impact': 6, 'confidence': 8, 'effort': 5},
        {'name': 'Feature C', 'impact': 9, 'confidence': 6, 'effort': 6}
    ]
    prioritized_roadmap = prioritize_roadmap(roadmap)
    for feature in prioritized_roadmap:
        print(f"{feature['name']} - Score: {feature['score']:.2f}")
