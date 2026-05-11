# redrob-ai-# Resume Matching Engine using TF-IDF & Cosine Similarity

A Python-based Resume Matching Engine developed for the Redrob AI Campus Hackathon.

This project normalizes noisy resume skill data, computes TF-IDF vectors manually (without external ML libraries), builds Job Description vectors, and ranks the best candidates using cosine similarity.

---

# Features

- Skill normalization using alias mapping
- Handles noisy and misspelled skills
- Resume skill deduplication
- Shared vocabulary generation
- Manual TF-IDF implementation
- Binary vector generation for Job Descriptions
- Cosine similarity matching
- Top-3 candidate ranking per Job Description
- Tie-breaking using alphabetical order
- Fully implemented using Python standard libraries only

---

# Problem Statement

Given:
- 10 resumes from university students
- 3 Job Descriptions from Korean tech companies

The system:
1. Normalizes skills
2. Builds TF-IDF vectors for resumes
3. Builds binary vectors for JDs
4. Computes cosine similarity
5. Returns Top-3 matching candidates for each role

---

# Tech Stack

- Python 3
- Standard Libraries Only
  - `math`
  - `collections`
  - `re`

No external libraries were used.

---

# Project Structure

```text
resume-matching-engine/
│
├── main.py
├── README.md
└── output.txt
```

---

# Core Concepts Used

## 1. Skill Normalization

Noisy skill names are converted into canonical forms using an alias dictionary.

Example:

```text
Pyhton → python
Deep-learning → deep_learning
Reacts → react
```

Unknown skills are discarded.

---

## 2. TF-IDF Vectorization

TF-IDF is computed manually for resumes.

### Term Frequency (TF)

```math
TF = 1 / N
```

Where:
- `N` = total unique skills in a resume

### Inverse Document Frequency (IDF)

```math
IDF(skill) = ln(10 / df(skill))
```

Where:
- `df(skill)` = number of resumes containing the skill

### TF-IDF

```math
TFIDF = TF × IDF
```

---

## 3. Cosine Similarity

Used to measure similarity between:
- Resume TF-IDF vectors
- JD binary vectors

```math
Cosine(A, B) = (A · B) / (|A| × |B|)
```

Higher cosine similarity indicates better candidate-job matching.

---

# Workflow

## Step 1 — Normalize Skills
- Convert to lowercase
- Split using commas
- Apply alias mapping
- Remove unknown tokens
- Deduplicate skills

## Step 2 — Build Vocabulary
- Create shared vocabulary from resumes
- Sort alphabetically

## Step 3 — Compute TF-IDF
- Calculate TF
- Calculate IDF
- Generate resume vectors

## Step 4 — Build JD Vectors
- Convert JD skills into binary vectors

## Step 5 — Compute Similarity
- Use cosine similarity

## Step 6 — Rank Candidates
- Sort by similarity score
- Break ties alphabetically

---

# Output Format

```text
JD-1 — Kakao (ML Engineer)
Sneha Patel(0.91), Karan Mehta(0.82), Meera Iyer(0.74)

JD-2 — Naver (Backend Engineer)
Rahul Gupta(0.93), Ananya Krishnan(0.71), Priya Nair(0.52)

JD-3 — Line (Frontend Engineer)
Aditya Kumar(0.94), Priya Nair(0.86), Ananya Krishnan(0.79)
```

---

# Constraints Followed

- No external libraries
- No sklearn
- No pandas
- Manual TF-IDF implementation
- Manual cosine similarity implementation
- Natural logarithm used
- No IDF smoothing
- Shared vocabulary consistency maintained

---

# Functions Implemented

```python
normalize_skills()
build_vocabulary()
compute_document_frequency()
compute_tfidf_vectors()
build_jd_vectors()
cosine_similarity()
rank_candidates()
pretty_print_results()
```

---

# Edge Cases Handled

- Misspelled skills
- Duplicate skills
- Unknown skills
- Empty vectors
- Tie-breaking
- Vocabulary consistency
- Multi-word aliases

---

# Time Complexity

| Operation | Complexity |
|---|---|
| Skill Normalization | O(N × S) |
| Vocabulary Creation | O(V log V) |
| TF-IDF Computation | O(N × V) |
| Cosine Similarity | O(N × V × J) |

Where:
- `N` = number of resumes
- `S` = skills per resume
- `V` = vocabulary size
- `J` = number of job descriptions

---

# Why TF-IDF?

TF-IDF helps identify:
- Important skills in a resume
- Rare but valuable skills
- Skills that distinguish candidates

Common skills receive lower weight, while specialized skills receive higher importance.

---

# Why Cosine Similarity?

Cosine similarity:
- Works well with sparse vectors
- Measures directional similarity
- Ignores vector magnitude differences
- Is widely used in information retrieval systems

---

# Sample Debug Outputs

The program also prints:
- Normalized skills
- Vocabulary
- Document frequencies
- TF-IDF vectors
- JD vectors
- Similarity scores

This helps validate intermediate computations.

---

# How to Run

## Clone Repository

```bash
git clone https://github.com/yourusername/resume-matching-engine.git
cd resume-matching-engine
```

## Run Program

```bash
python main.py
```

---

# Learning Outcomes

This project demonstrates:
- Information Retrieval concepts
- Vector Space Models
- TF-IDF computation
- Cosine similarity
- Text normalization
- Data preprocessing
- Search & ranking systems

---

# Future Improvements

Possible future enhancements:
- Weighted required/preferred skills
- Semantic skill matching
- Resume parsing from PDFs
- Web interface
- Real-time ranking dashboard
- ML-based recommendation system

---

# Author

Dhruv Sharma

Built for the Redrob AI Campus Hackathon.
