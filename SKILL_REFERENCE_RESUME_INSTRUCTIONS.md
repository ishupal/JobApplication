# Instructions for Resume-Tailoring Skill: Reference Resume Selection

## ADD THIS AS PHASE 0.5 (After Library Init, Before Research)

---

## Phase 0.5: Reference Resume Selection

**Goal:** Select the best matching reference resume from the user's library to use as the base for tailoring

**When:** After Phase 0 (Library Initialization) and before Phase 1 (Research)

**Process:**

### 1. Scan Reference Resume Library

```
Use Glob tool to find all reference resumes:
pattern="*.md"
path="resumes/refrence_resume/"

Example output:
- Data Engineer.md
- Data Analyst.md
- Data Lead.md
- AI Engineer.md
```

**If no reference resumes found:**
```
"No reference resumes found in resumes/refrence_resume/ folder.

I'll proceed with building from your general resume library instead.

Recommendation: Create reference resumes for common role types you apply to (Data Engineer, Data Lead, etc.) to improve tailoring speed and quality."

→ Continue with normal workflow
```

### 2. Analyze Job Description for Matching

**Extract from JD:**
- **Job title keywords:** Senior, Lead, Manager, Engineer, Analyst, Scientist, etc.
- **Domain:** Data Engineering, Analytics, AI/ML, BI, Governance, etc.
- **Key technical skills:** Python, SQL, Cloud platforms, specific tools
- **Seniority level:** Junior, Mid, Senior, Lead, Principal, Manager
- **Primary focus:** Technical implementation, Leadership, Strategy, Analysis, etc.

**Example analysis:**
```
Job Description Analysis:
- Title: "Senior Data Engineer"
- Domain: Data Engineering
- Seniority: Senior
- Key Skills: Python, Airflow, GCP, BigQuery, ETL pipelines
- Focus: Technical implementation (pipeline building, data architecture)
```

### 3. Score Each Reference Resume

**For each reference resume found:**

**Read the file** (first 100 lines sufficient for scoring):
```
Use Read tool:
file_path="resumes/refrence_resume/{filename}"
limit=100
```

**Score on 4 dimensions (total 100%):**

#### A. Filename Match (40 points)
Match job title keywords with filename:
- Exact role match: 40 points ("Data Engineer.md" for Data Engineer role)
- Partial match: 25 points ("Data Lead.md" for Senior Data Engineer)
- Domain match: 15 points ("AI Engineer.md" for ML Engineer)
- No match: 0 points

#### B. Skills Match (30 points)
Count matching skills between JD and reference resume:
- >80% skill overlap: 30 points
- 60-80% overlap: 20 points
- 40-60% overlap: 10 points
- <40% overlap: 5 points

#### C. Seniority Match (20 points)
Match seniority level:
- Exact match: 20 points (Senior in both)
- One level off: 10 points (Mid vs Senior)
- Two+ levels off: 0 points

#### D. Domain/Focus Match (10 points)
Match primary job domain:
- Same domain: 10 points (both Data Engineering)
- Adjacent domain: 5 points (Data Engineering vs Analytics)
- Different domain: 0 points

**Example Scoring:**
```
Reference Resume: "Data Engineer.md"
- Filename match: 40/40 (exact "Data Engineer")
- Skills match: 25/30 (75% overlap: Python, SQL, GCP, pipelines)
- Seniority match: 20/20 (both Senior)
- Domain match: 10/10 (both Data Engineering)
Total Score: 95/100
```

### 4. Select Best Match

**Choose highest scoring reference resume**

**Present to user:**
```
"📋 REFERENCE RESUME SELECTION

Analyzing job description:
- Target Role: Senior Data Engineer
- Domain: Data Engineering
- Key Skills: Python, Airflow, GCP, BigQuery, ETL
- Seniority: Senior

Evaluated {N} reference resumes:

1. Data Engineer.md - 95/100 ⭐ SELECTED
   ✓ Exact role match
   ✓ 75% skill overlap
   ✓ Senior level match
   ✓ Data Engineering domain

2. Data Lead.md - 65/100
   ~ Leadership focus (job needs technical)
   ✓ Senior level
   ~ 50% skill overlap

3. Data Analyst.md - 45/100
   ✗ Different focus (analysis vs engineering)
   ✗ Mid-level seniority

Using 'Data Engineer.md' as base for tailoring.

This resume emphasizes:
- Pipeline building and data architecture
- Cloud platform engineering (GCP)
- ETL/ELT development
- Technical implementation

Perfect match for this role! 🎯"
```

### 5. Load Selected Reference Resume as Base

**Load the entire reference resume:**
```
Use Read tool:
file_path="resumes/refrence_resume/{selected_file}"
Read all lines
```

**This becomes your BASE CONTENT:**
- Use its structure
- Use its content sections
- Use its Career Profile style
- Use its Areas of Expertise
- Use its Work Experience descriptions

**BUT** still tailor it:
- Emphasize matching skills more
- Reframe bullets to match JD language
- Add/highlight relevant achievements
- Adjust Career Profile to mention specific company/role if helpful

### 6. Proceed with Tailoring

**Continue with normal workflow BUT:**
- Use reference resume content as the base (not building from scratch)
- Research phase still happens (Phase 1)
- Template generation uses reference resume structure (Phase 2)
- Content matching prioritizes reference resume bullets (Phase 3)
- Generation phase outputs in NEW format (Phase 4)

**Key difference:**
- OLD: Build resume from general library pieces
- NEW: Start with proven reference resume, tailor to specific job

---

## Fallback Behavior

**If no reference resumes exist:**
```
Proceed with original workflow (build from general library)
```

**If reference resume is poor match (<50% score):**
```
"⚠️ Best reference resume match: {filename} ({score}/100)

This is a relatively low match. Would you like to:
1. Proceed with this reference resume anyway
2. Build from general library instead (original workflow)

Recommendation: {1 or 2 based on score}"

[Wait for user input]
```

---

## Benefits of Reference Resume Approach

1. **Faster:** Start with complete resume instead of building from scratch
2. **Better quality:** Reference resumes are pre-optimized and tested
3. **Consistent:** Each role type has consistent framing
4. **Flexible:** Easy to add new role variations
5. **Controlled:** User maintains the reference library

---

## Integration with Existing Phases

**Updated Phase Flow:**

```
Phase 0: Library Initialization
  ↓
Phase 0.5: Reference Resume Selection ← NEW
  ↓
Phase 1: Research Phase
  ↓
Phase 2: Template Generation
  ↓
Phase 2.5: Experience Discovery (optional)
  ↓
Phase 3: Assembly Phase
  ↓
Phase 4: Generation Phase
  ↓
Phase 5: Library Update (optional)
```

---

## Example: Complete Flow

**User provides JD for "Senior Data Engineer at Google"**

**Phase 0.5 runs:**
1. Finds 4 reference resumes in library
2. Scores each against JD
3. Selects "Data Engineer.md" (92% match)
4. Loads entire reference resume
5. Informs user of selection and rationale

**Phases 1-4 run:**
- Research Google and role
- Use Data Engineer.md structure as template
- Match/tailor content to Google's JD
- Generate .md file with tailored content

**Output:**
"Ishupal Singh - Google Senior Data Engineer Resume.md"
- Based on Data Engineer.md reference
- Tailored to Google's specific requirements
- Emphasizes matching skills and experience
- Uses proven structure and framing

---

## Technical Implementation Notes

**Glob tool usage:**
```python
pattern="*.md"
path="resumes/refrence_resume/"
```

**Read tool usage for scoring:**
```python
file_path="resumes/refrence_resume/Data Engineer.md"
limit=100  # Sufficient for scoring
```

**Read tool usage for loading:**
```python
file_path="resumes/refrence_resume/Data Engineer.md"
# Read all lines (no limit)
```

**Matching logic:**
Use keyword matching and similarity scoring:
- Job title keywords: ["data", "engineer", "senior", "lead", "analyst", "ml", "ai"]
- Skill extraction from JD and resume
- Calculate overlap percentage

---

## Summary

This phase adds intelligent reference resume selection BEFORE the main tailoring workflow, giving users:
- Control over how different role types are framed
- Speed (starting with complete resume)
- Quality (using tested, optimized content)
- Flexibility (easy to add new role types)

When I use the resume-tailoring skill, I will:
1. Check for reference resumes
2. Score and select best match
3. Load and use as base
4. Tailor to specific job
5. Generate .md output
