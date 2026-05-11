import math
from collections import Counter

# Define the skill aliases
SKILL_ALIASES = {
    "python": "python",
    "pyhton": "python",
    "java": "java",
    "javascript": "javascript",
    "javascrpit": "javascript",
    "js": "javascript",
    "typescript": "typescript",
    "typescrpit": "typescript",
    "c++": "cpp",
    "cpp": "cpp",
    "r": "r",
    "kotlin": "kotlin",

    "machinelearning": "machine_learning",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "sklearn": "machine_learning",

    "deeplearning": "deep_learning",
    "deep learning": "deep_learning",
    "deep-learning": "deep_learning",

    "tensorflow": "tensorflow",
    "pytorch": "pytorch",
    "keras": "keras",
    "nlp": "nlp",
    "bert": "bert",
    "xgboost": "xgboost",

    "feature engineering": "feature_engineering",

    "statistics": "statistics",
    "stats": "statistics",

    "regression": "regression",
    "clustering": "clustering",

    "data-viz": "data_visualization",
    "data visualization": "data_visualization",
    "data viz": "data_visualization",
    "matplotlib": "data_visualization",
    "tableau": "data_visualization",
    "power-bi": "data_visualization",
    "power bi": "data_visualization",
    "powerbi": "data_visualization",

    "pandas": "pandas",
    "numpy": "numpy",

    "react": "react",
    "reacts": "react",
    "reactjs": "react",

    "vue": "vue",
    "vue.js": "vue",
    "vuejs": "vue",

    "redux": "redux",
    "tailwind": "tailwind",

    "html/css": "html_css",
    "html css": "html_css",
    "html": "html_css",
    "css": "html_css",

    "jest": "jest",
    "graphql": "graphql",

    "node.js": "nodejs",
    "nodejs": "nodejs",
    "node js": "nodejs",

    "flask": "flask",

    "spring boot": "spring_boot",
    "springboot": "spring_boot",

    "rest api": "rest_api",
    "rest": "rest_api",
    "restapi": "rest_api",

    "microservices": "microservices",

    "sql": "sql",
    "mysql": "mysql",
    "mysq": "mysql",

    "postgresql": "postgresql",
    "postgres": "postgresql",

    "mongodb": "mongodb",
    "redis": "redis",

    "docker": "docker",

    "kubernetes": "kubernetes",
    "kubernates": "kubernetes",
    "k8s": "kubernetes",

    "ci/cd": "ci_cd",
    "cicd": "ci_cd",
    "ci cd": "ci_cd",

    "aws": "aws",

    "android": "android",
    "firebase": "firebase",

    "algorithms": "algorithms",
    "algoritms": "algorithms",

    "data structure": "data_structures",
    "data structures": "data_structures",

    "competitive programming": "competitive_programming",

    "ui/ux": "ui_ux",
    "ui ux": "ui_ux",
    "figma": "figma"
}

# Define the resumes
RESUMES = {
    "Arjun Sharma": ["Pyhton", "MachineLearning", "SQL", "pandas", "numpy", "Deep-learning"],
    "Priya Nair": ["JavaScrpit", "Reacts", "Node.JS", "MongoDb", "REST api", "HTML/CSS"],
    "Rahul Gupta": ["Java", "Spring Boot", "MySql", "Microservices", "Docker", "kubernates"],
    "Sneha Patel": ["Python", "TensorFlow", "Keras", "NLP", "BERT", "data-viz", "matplotlib"],
    "Vikram Singh": ["C++", "Algoritms", "Data Structure", "competitive programming", "python"],
    "Ananya Krishnan": ["javascript", "vue.js", "python", "flask", "PostgreSQL", "AWS", "CI/CD"],
    "Karan Mehta": ["Python", "Sklearn", "XGboost", "feature engineering", "SQL", "tableau"],
    "Deepika Rao": ["Java", "Android", "Kotlin", "Firebase", "REST", "UI/UX", "figma"],
    "Aditya Kumar": ["Reactjs", "TypeScrpit", "GraphQL", "redux", "tailwind", "nodejs", "jest"],
    "Meera Iyer": ["python", "R", "statistics", "ML", "regression", "clustering", "Power-BI"]
}

# Define the job descriptions
JOB_DESCRIPTIONS = {
    "JD-1": {
        "company": "Kakao",
        "role": "ML Engineer",
        "required_skills": [
            "Python",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "SQL",
            "Data Visualization"
        ],
        "preferred_skills": [
            "NLP",
            "BERT",
            "Feature Engineering",
            "Statistics"
        ]
    },

    "JD-2": {
        "company": "Naver",
        "role": "Backend Engineer",
        "required_skills": [
            "Java",
            "Spring Boot",
            "MySQL",
            "PostgreSQL",
            "Microservices",
            "Docker",
            "Kubernetes"
        ],
        "preferred_skills": [
            "REST API",
            "CI/CD",
            "Redis"
        ]
    },

    "JD-3": {
        "company": "Line",
        "role": "Frontend Engineer",
        "required_skills": [
            "JavaScript",
            "React",
            "Vue",
            "TypeScript",
            "REST API",
            "HTML/CSS"
        ],
        "preferred_skills": [
            "Node.js",
            "GraphQL",
            "Redux",
            "Jest",
            "AWS"
        ]
    }
}

# Normalize the resumes
normalized_resumes = {}
for name, skills in RESUMES.items():
    normalized_skills = []
    for skill in skills:
        skill = skill.lower()
        for alias, normalized_skill in SKILL_ALIASES.items():
            if alias in skill:
                normalized_skills.append(normalized_skill)
                break
        else:
            if skill in SKILL_ALIASES:
                normalized_skills.append(SKILL_ALIASES[skill])
    normalized_resumes[name] = list(set(normalized_skills))

print("Normalized Resume Skills:")
for name, skills in normalized_resumes.items():
    print(f"{name}: {skills}")

# Build the shared vocabulary
vocabulary = set()
for skills in normalized_resumes.values():
    vocabulary.update(skills)
vocabulary = sorted(list(vocabulary))

print("\nShared Vocabulary:")
print(vocabulary)

# Calculate the document frequency table
document_frequency = {}
for skill in vocabulary:
    document_frequency[skill] = sum(1 for skills in normalized_resumes.values() if skill in skills)

print("\nDocument Frequency Table:")
for skill, frequency in document_frequency.items():
    print(f"{skill}: {frequency}")

# Calculate TF-IDF for each resume
def calculate_tf_idf(resume, skill):
    tf = 1 / len(resume)
    idf = math.log(10 / document_frequency[skill])
    return tf * idf

tf_idf_resumes = {}
for name, skills in normalized_resumes.items():
    tf_idf_skills = {}
    for skill in skills:
        tf_idf_skills[skill] = calculate_tf_idf(skills, skill)
    tf_idf_resumes[name] = tf_idf_skills

print("\nTF-IDF Vectors:")
for name, skills in tf_idf_resumes.items():
    print(f"{name}: {skills}")

# Calculate the JD binary vectors
jd_binary_vectors = {}
for jd_id, jd in JOB_DESCRIPTIONS.items():
    binary_vector = {}
    for skill in vocabulary:
        if skill in [SKILL_ALIASES.get(s.lower(), s.lower()) for s in jd["required_skills"]] or skill in [SKILL_ALIASES.get(s.lower(), s.lower()) for s in jd["preferred_skills"]]:
            binary_vector[skill] = 1
        else:
            binary_vector[skill] = 0
    jd_binary_vectors[jd_id] = binary_vector

print("\nJD Binary Vectors:")
for jd_id, vector in jd_binary_vectors.items():
    print(f"{jd_id}: {vector}")

# Calculate the cosine similarity between resumes and job descriptions
def calculate_cosine_similarity(resume, jd_vector):
    resume_vector = [tf_idf_resumes[resume].get(skill, 0) for skill in vocabulary]
    jd_vector = [jd_vector[skill] for skill in vocabulary]
    dot_product = sum(a * b for a, b in zip(resume_vector, jd_vector))
    magnitude_resume = math.sqrt(sum(a ** 2 for a in resume_vector))
    magnitude_jd = math.sqrt(sum(a ** 2 for a in jd_vector))
    return dot_product / (magnitude_resume * magnitude_jd)

cosine_similarities = {}
for jd_id, jd_vector in jd_binary_vectors.items():
    similarities = {}
    for name in RESUMES.keys():
        similarities[name] = calculate_cosine_similarity(name, jd_vector)
    cosine_similarities[jd_id] = similarities

print("\nCosine Similarity Scores:")
for jd_id, similarities in cosine_similarities.items():
    for name, similarity in similarities.items():
        print(f"{jd_id} - {name}: {similarity:.2f}")

# Print the top 3 matching candidates for each job description
for jd_id, similarities in cosine_similarities.items():
    sorted_similarities = sorted(similarities.items(), key=lambda x: (-x[1], x[0]))
    print(f"\nJob Description: {jd_id}")
    for name, similarity in sorted_similarities[:3]:
        print(f"{name}: {similarity:.2f}")

# Output the results in the required format
for jd_id, similarities in cosine_similarities.items():
    sorted_similarities = sorted(similarities.items(), key=lambda x: (-x[1], x[0]))
    print(f"\n{jd_id} — {JOB_DESCRIPTIONS[jd_id]['company']} ({JOB_DESCRIPTIONS[jd_id]['role']})")
    result = ", ".join(f"{name}({similarity:.2f})" for name, similarity in sorted_similarities[:3])
    print(result)


